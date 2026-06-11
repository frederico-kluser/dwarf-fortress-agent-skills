#!/usr/bin/env python3
"""Fase 2 (V3) — Constrói as skills a partir do HTML renderizado (pages.jsonl).

Mudanças-chave vs V2:
  - Fonte é HTML JÁ RENDERIZADO da API (htmlmd.to_markdown), não wikitext bruto →
    infoboxes, tabelas de token e /raw preservados (sem "[TABLE]", sem stubs vazios).
  - assign_skill: páginas /raw roteadas por ASSUNTO (creature raw → df-criaturas),
    categorias filtradas (qualidade/manutenção/versão fora), first-match por
    PRIORIDADE declarada (ordem do dict), sem fallback de substring perigoso.
  - Artigos longos são DIVIDIDOS em partes navegáveis (part-k), não truncados.
  - Índice do SKILL.md ordenado por RELEVÂNCIA (nº de links internos recebidos).
  - SKILL.md bilíngue, com metadata, bloco "Como buscar" (search.py) e mapa de tópicos.
"""
import os, sys, re, json, collections, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from taxonomy import SKILL_CATEGORIES, DROP_CATS, TITLE_RESCUE
import htmlmd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.environ.get("SKILLS_OUT", os.path.join(ROOT, ".agents", "skills"))
PAGES_JSONL = os.environ.get("PAGES_JSONL", os.path.join(HERE, "pages.jsonl"))

MAX_INDEX_ENTRIES = 30
MAX_REF_BYTES = 48_000          # acima disto → dividir em partes navegáveis

VERSION_CAT = re.compile(r"^(DF2014|V0\.\d+|40d|23a|Masterwork|Modification|2010|3\.x)\b", re.I)
QUALITY_CAT = re.compile(r"(Quality Articles$|needing review|^New in|script error|broken file|"
                         r"deprecated source|omitted template|using deprecated)", re.I)

# map categoria(lower) → lista de skills (preserva ordem de prioridade do dict)
rawcat_to_skill = collections.OrderedDict()
for skill, cfg in SKILL_CATEGORIES.items():
    for rc in cfg["raw_cats"]:
        rawcat_to_skill.setdefault(rc.lower(), []).append(skill)


def useful_cats(categories):
    out = []
    for c in categories:
        if c in DROP_CATS or VERSION_CAT.search(c) or QUALITY_CAT.search(c):
            continue
        out.append(c)
    return out


def assign_skill(title, categories):
    cats = set(c.lower() for c in useful_cats(categories))
    # first-match por PRIORIDADE (ordem do dict de skills)
    for skill, cfg in SKILL_CATEGORIES.items():
        for rc in cfg["raw_cats"]:
            if rc.lower() in cats:
                return skill
    # fallback de keyword SEGURO (termos específicos, sem substrings ambíguos)
    tl = " " + re.sub(r"[^a-z0-9]+", " ", title.lower()) + " "
    for skill, cfg in SKILL_CATEGORIES.items():
        for kw in cfg["kw"]:
            if f" {kw.replace('-', ' ')} " in tl or f" {kw} " in tl:
                return skill
    # resgate por título (páginas v50 sem categoria útil)
    base = re.split(r"/", title.lower())[0].strip()
    return TITLE_RESCUE.get(base)


def slugify(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:80] or "page"


def split_article(md, title, url):
    """>MAX_REF_BYTES → divide em partes navegáveis com nota de continuação."""
    if len(md.encode("utf-8")) <= MAX_REF_BYTES:
        return [(title, md)]
    lines = md.split("\n")
    parts, cur, size = [], [], 0
    for ln in lines:
        b = len(ln.encode("utf-8")) + 1
        if size + b > MAX_REF_BYTES and cur:
            parts.append("\n".join(cur)); cur, size = [], 0
        cur.append(ln); size += b
    if cur:
        parts.append("\n".join(cur))
    n = len(parts)
    out = []
    for i, body in enumerate(parts, 1):
        note = (f"\n\n---\n*Parte {i} de {n} de «{title}». "
                f"Demais partes em arquivos `...-part-{{1..{n}}}.md` na mesma pasta. "
                f"Fonte: {url}*\n")
        head = "" if i == 1 else f"# {title} (parte {i}/{n})\n\n"
        out.append((f"{title} (parte {i}/{n})" if i > 1 else title, head + body + note))
    return out


def count_inbound_links(pages):
    """Conta links internos recebidos por título (proxy de relevância p/ o índice)."""
    cnt = collections.Counter()
    href_re = re.compile(r'href="/index\.php/([^"#?]+)')
    for rec in pages:
        for m in href_re.findall(rec.get("html", "")):
            t = m.replace("_", " ")
            try:
                t = bytes(t, "utf-8").decode("unicode_escape")
            except Exception:
                pass
            cnt[t] += 1
    return cnt


SKILL_MD_TEMPLATE = """---
name: {name}
description: >-
{desc}
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: {modes}
---

# {pretty} (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill {name} "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais {topn} de {total} artigos — use o search.py para o resto)
{index}
"""


def indent_desc(desc, spaces=2):
    pad = " " * spaces
    return "\n".join(pad + line for line in re.sub(r"\s+", " ", desc).strip().split("\n"))


def main():
    pages = []
    with open(PAGES_JSONL, encoding="utf-8") as f:
        for line in f:
            pages.append(json.loads(line))
    print(f"Páginas carregadas: {len(pages)}", file=sys.stderr)

    inbound = count_inbound_links(pages)

    skill_pages = collections.defaultdict(list)
    unassigned = 0
    for rec in pages:
        sk = assign_skill(rec["title"], rec.get("categories", []))
        if sk:
            skill_pages[sk].append(rec)
        else:
            unassigned += 1
    print(f"Não atribuídas: {unassigned}", file=sys.stderr)

    os.makedirs(OUT, exist_ok=True)
    for skill in sorted(skill_pages):
        cfg = SKILL_CATEGORIES[skill]
        skill_dir = os.path.join(OUT, skill)
        ref_dir = os.path.join(skill_dir, "references")
        os.makedirs(ref_dir, exist_ok=True)

        ref_entries = []   # (title, slug, inbound_score)
        written = 0
        for rec in sorted(skill_pages[skill], key=lambda r: r["title"].lower()):
            title, url = rec["title"], rec["url"]
            md = htmlmd.to_markdown(rec["html"], title, url, rec.get("categories"))
            if len(re.sub(r"\s+", "", md)) < 60:          # vazio de verdade
                continue
            score = inbound.get(title, 0)
            for ptitle, pbody in split_article(md, title, url):
                slug = slugify(ptitle)
                with open(os.path.join(ref_dir, slug + ".md"), "w", encoding="utf-8") as f:
                    f.write(pbody)
                ref_entries.append((ptitle, slug, score if "(parte" not in ptitle else -1))
                written += 1

        # índice por RELEVÂNCIA (links internos recebidos), partes>1 ao fim
        ref_entries.sort(key=lambda x: (-x[2], x[0].lower()))
        top = ref_entries[:MAX_INDEX_ENTRIES]
        idx_lines = [f"- {t} → `references/{s}.md`" for t, s, _ in top]
        remaining = len(ref_entries) - len(top)
        if remaining > 0:
            idx_lines.append(f"\n*…e mais {remaining} artigos (use o search.py).*")

        skill_md = SKILL_MD_TEMPLATE.format(
            name=skill, desc=indent_desc(cfg["desc"]), modes=cfg["modes"],
            pretty="DF " + skill[3:].replace("-", " ").title(),
            topn=len(top), total=len(ref_entries), index="\n".join(idx_lines))
        with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(skill_md)
        print(f"  {skill}: {written} arquivos ({len(ref_entries)} entradas de índice)",
              file=sys.stderr)

    print("DONE.", file=sys.stderr)


if __name__ == "__main__":
    main()
