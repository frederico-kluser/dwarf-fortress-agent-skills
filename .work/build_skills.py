#!/usr/bin/env python3
"""Fase 2-5 V2 — Flat skill structure, YAML-safe, index capped, files truncated.

Architecture changes from V1:
  - NO duplication between modes (flat unique names)
  - SKILL.md index: max 30 entries + reference to search.sh
  - Reference files capped at ~12KB (truncated with source link)
  - Giant files (e.g. string-dump-raw 923KB) split into alphabetical chunks
  - All descriptions YAML-safe (no unquoted ":") — taxonomy.py guarantees this
  - No router hierarchy — each skill is a flat peer discovered by its description
"""
import os, sys, re, subprocess, collections, unicodedata, json, html as _html
import mwparserfromhell
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from taxonomy import SKILL_CATEGORIES, DROP_CATS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, ".agents", "skills")

# ── config ──
MAX_INDEX_ENTRIES = 30          # max articles listed in SKILL.md index
MAX_REF_BYTES = 48_000       # max reference file size before truncation (~12K tokens)
SPLIT_THRESHOLD = 200_000    # split giant token dumps into letter-chunks

cat_tpl_re = re.compile(r"\{\{\s*[Cc]ategory\s*\|\s*([^}|]+)")
cat_link_re = re.compile(r"\[\[Category:([^\]\|]+)")

# ── load pages, dedupe ──
raw = {}
for line in open(os.path.join(HERE, "pages.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    raw[r["title"]] = r

canonical = {}
for title, rec in raw.items():
    base = title[7:] if title.startswith("DF2014:") else title
    prev = canonical.get(base)
    if prev is None or rec["bytes"] > prev["bytes"]:
        canonical[base] = rec

print(f"Canonical pages: {len(canonical)}", file=sys.stderr)

# ── assign skills (flat, no duplication) ──
rawcat_to_skill = {}
for skill, cfg in SKILL_CATEGORIES.items():
    for rc in cfg["raw_cats"]:
        rawcat_to_skill.setdefault(rc.lower(), []).append(skill)

def page_raw_cats(text):
    cats = set()
    for m in cat_tpl_re.findall(text):
        cats.add(m.strip())
    for m in cat_link_re.findall(text):
        cats.add(re.sub(r"^DF2014:", "", m.strip()))
    return cats

def assign_skill(title, text):
    if title.endswith("/raw") or title.endswith(" raw"):
        return "df-modding"  # raw subpages → modding only
    cats = page_raw_cats(text)
    for c in cats:
        for s in rawcat_to_skill.get(c.lower(), []):
            return s  # first match wins (flat, one skill per page)
    # keyword fallback on title
    tl = title.lower()
    for skill, cfg in SKILL_CATEGORIES.items():
        for kw in cfg["kw"]:
            if kw in tl:
                return skill
    return None

# collect: skill -> list of (title, rec)
skill_pages = collections.defaultdict(list)
unassigned = 0
for base, rec in canonical.items():
    sk = assign_skill(base, rec["text"])
    if sk:
        skill_pages[sk].append((base, rec))
    else:
        unassigned += 1

print(f"Unassigned pages: {unassigned}", file=sys.stderr)

# ── slug + clean + convert ──
def slugify(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:80] or "page"

NAV_PREFIXES = ("av", "articleversion", "navbox", "quality", "migrated",
                "old", "new in v", "stub", "translation", "d for dwarf",
                "disambig", "tocright", "clear")

def strip_file_links(s):
    """Remove [[File:X]] and [[Image:X]] with arbitrarily nested brackets."""
    i = 0; res = []
    while i < len(s):
        m = re.match(r"\[\[(?:File|Image):", s[i:], re.I)
        if m:
            depth = 0; j = i
            while j < len(s):
                if s[j:j+2] == "[[":
                    depth += 1; j += 2
                elif s[j:j+2] == "]]":
                    depth -= 1; j += 2
                    if depth == 0: break
                else: j += 1
            i = j
        else:
            res.append(s[i]); i += 1
    return "".join(res)

def clean_wikitext(text):
    code = mwparserfromhell.parse(text)
    for tpl in list(code.filter_templates()):
        name = str(tpl.name).strip().lower()
        if any(name.startswith(p) for p in NAV_PREFIXES):
            try: code.remove(tpl)
            except ValueError: pass
    out = str(code)
    out = strip_file_links(out)
    out = cat_tpl_re.sub("", out)
    out = re.sub(r"\{\{\s*[Cc]ategory\s*\|[^}]*\}\}", "", out)
    out = cat_link_re.sub("", out)
    out = re.sub(r"\[\[Category:[^\]]*\]\]", "", out)
    out = re.sub(r"\[\[[a-z]{2}:[^\]]*\]\]", "", out)  # interwiki
    return out.strip()

def to_markdown(wikitext, title, url):
    try:
        p = subprocess.run(
            ["pandoc", "-f", "mediawiki", "-t", "gfm-raw_html", "--wrap=none"],
            input=wikitext, capture_output=True, text=True, timeout=60)
        md = p.stdout
    except Exception:
        md = wikitext
    # decode HTML entities
    md = md.replace("&nbsp;", " ")
    md = _html.unescape(md)
    # strip HTML blocks/tags
    md = re.sub(r"<figure>.*?</figure>", "", md, flags=re.S)
    md = re.sub(r"<figcaption>.*?</figcaption>", "", md, flags=re.S)
    md = re.sub(r"<[^>]+>", "", md)
    # drop images
    md = re.sub(r"!\[.*?\]\([^)]*\)", "", md, flags=re.S)
    md = re.sub(r"\]\([^)]*\.(?:jpg|jpeg|png|gif|svg)[^)]*\)", "", md, flags=re.I)
    # flatten links to plain text
    for _ in range(3):
        md = re.sub(r"\[([^\[\]]+)\]\([^)]*\)", r"\1", md)
    # strip template residue
    md = re.sub(r"\{\{[^{}]*\}\}", "", md)
    md = re.sub(r"[{}]{2,}", "", md)
    md = re.sub(r"^\s*\\?\|.*\}\}\s*$", "", md, flags=re.M)
    md = re.sub(r"^[ \t]*[\\\|*]+[ \t]*$", "", md, flags=re.M)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    # build header
    header = (f"# {title}\n\n"
              f"> Fonte: [{title}]({url}) — Dwarf Fortress Wiki (GFDL/MIT)\n\n")
    return header + md + "\n"

def maybe_truncate(text, title, url, max_bytes=MAX_REF_BYTES):
    """If text exceeds max_bytes, truncate with note."""
    b = text.encode("utf-8")
    if len(b) <= max_bytes:
        return text
    # truncate to max_bytes at paragraph boundary
    truncated = b[:max_bytes].decode("utf-8", errors="replace")
    truncated = truncated.rsplit("\n\n", 1)[0]
    note = (f"\n\n---\n⚠️ Conteúdo truncado ({len(b)} bytes = ~{len(b)//4} tokens). "
            f"Para o artigo completo, visite [{title}]({url}).")
    return truncated + note

def split_large_article(title, text, url, threshold=SPLIT_THRESHOLD):
    """For huge token-dump articles, split by letter ranges."""
    b = text.encode("utf-8")
    if len(b) < threshold:
        return [(title, text, url)]
    # Split into letter-chunks by finding `\n[A-Z]` section markers
    chunks = []
    lines = text.split("\n")
    current = [lines[0]]
    last_marker = ""
    for line in lines[1:]:
        marker_m = re.match(r"^[A-Z]$", line.strip())
        if marker_m and len("\n".join(current).encode()) > 100_000:
            ctitle = f"{title} ({last_marker or 'intro'})"
            chunks.append((ctitle, "\n".join(current), url))
            current = [line]
            last_marker = line.strip()
        else:
            if marker_m:
                last_marker = line.strip()
            current.append(line)
    if current:
        ctitle = f"{title} ({last_marker or 'end'})"
        chunks.append((ctitle, "\n".join(current), url))
    if len(chunks) <= 1:
        return [(title, text, url)]
    return chunks

# ── write tree ──
os.makedirs(OUT, exist_ok=True)
page_count = collections.Counter()

for skill, pages in sorted(skill_pages.items()):
    cfg = SKILL_CATEGORIES[skill]
    skill_dir = os.path.join(OUT, skill)
    ref_dir = os.path.join(skill_dir, "references")
    os.makedirs(ref_dir, exist_ok=True)

    # write all reference pages
    written = 0
    ref_entries = []  # (title, slug, bytes) for index
    for title, rec in sorted(pages, key=lambda x: x[0].lower()):
        url = "https://dwarffortresswiki.org/index.php/" + title.replace(" ", "_")
        wt = clean_wikitext(rec["text"])
        if len(wt.strip()) < 30:
            continue
        md = to_markdown(wt, title, url)

        # handle giant articles
        b = md.encode("utf-8")
        if len(b) > SPLIT_THRESHOLD:
            # split monster into chunks
            chunks = split_large_article(title, md, url)
            for i, (ctitle, ctext, curl) in enumerate(chunks):
                cslug = slugify(ctitle)
                ctext = maybe_truncate(ctext, ctitle, curl)
                with open(os.path.join(ref_dir, cslug + ".md"), "w", encoding="utf-8") as f:
                    f.write(ctext)
                if i == 0:
                    ref_entries.append((ctitle, cslug, len(ctext.encode())))
                else:
                    ref_entries.append(("  " + ctitle, cslug, len(ctext.encode())))
                written += 1
        else:
            md = maybe_truncate(md, title, url)
            slug = slugify(title)
            with open(os.path.join(ref_dir, slug + ".md"), "w", encoding="utf-8") as f:
                f.write(md)
            ref_entries.append((title, slug, len(b)))
            written += 1

        page_count[skill] = written

    # build SKILL.md index (top N by size → most substantial articles first)
    ref_entries.sort(key=lambda x: -x[2])
    top = ref_entries[:MAX_INDEX_ENTRIES]
    remaining = len(ref_entries) - len(top)
    idx_lines = [f"- {t} → `references/{s}.md`" for t, s, _ in top]
    if remaining > 0:
        idx_lines.append(f"\n*...e mais {remaining} artigos (use o search.sh para encontrá-los)*")

    idx = "\n".join(idx_lines)
    skill_md = f"""---
name: {skill}
description: {cfg['desc']}
---

# {skill.replace('-', ' ').title()} (Dwarf Fortress)

{cfg['desc']}

Leia **apenas** o artigo relevante em `references/`. Não pré-carregue tudo.

## Como buscar
Se não souber o arquivo exato, rode a busca local:
`bash scripts/search.sh "{skill}" "termo de busca"`
Ela varre todos os artigos desta categoria e retorna os mais relevantes.

## Índice de artigos (principais {len(top)} de {len(ref_entries)})
{idx}
"""
    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skill_md)

    print(f"  {skill}: {written} articles ({len(ref_entries)} total)", file=sys.stderr)

print("\nDONE.", file=sys.stderr)