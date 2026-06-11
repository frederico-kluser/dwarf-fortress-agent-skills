#!/usr/bin/env python3
"""Fase 2.2-5 — Clean wikitext, convert to markdown, assign categories,
write the full .agents/df-skills/ tree for fortress-mode and adventure-mode."""
import os, sys, json, re, subprocess, collections, unicodedata
import mwparserfromhell
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from taxonomy import SKILL_CATEGORIES, DROP_CATS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, ".agents", "df-skills")

cat_tpl_re = re.compile(r"\{\{\s*[Cc]ategory\s*\|\s*([^}|]+)")
cat_link_re = re.compile(r"\[\[Category:([^\]\|]+)")

# ---- load pages, dedupe (prefer larger of Main vs DF2014) ----
raw = {}
for line in open(os.path.join(HERE, "pages.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    raw[r["title"]] = r

canonical = {}  # base_title -> record
for title, rec in raw.items():
    base = title[7:] if title.startswith("DF2014:") else title
    prev = canonical.get(base)
    if prev is None or rec["bytes"] > prev["bytes"]:
        canonical[base] = rec

print(f"Canonical pages: {len(canonical)}", file=sys.stderr)

# ---- assign skill categories ----
# build raw_cat -> skill_cat lookup
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

def assign_skills(title, text):
    # /raw subpages are token data -> modding only
    if title.endswith("/raw") or title.endswith(" raw"):
        return {"modding"}, set()
    cats = page_raw_cats(text)
    skills = set()
    for c in cats:
        for s in rawcat_to_skill.get(c.lower(), []):
            skills.add(s)
    if skills:
        return skills, cats
    # keyword fallback on title (only — avoid over-broad body matches)
    tl = title.lower()
    for skill, cfg in SKILL_CATEGORIES.items():
        for kw in cfg["kw"]:
            if kw in tl:
                skills.add(skill)
                break
    return skills, cats

# ---- slug + clean + convert ----
def slugify(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:80] or "page"

NAV_PREFIXES = ("av", "articleversion", "navbox", "quality", "migrated",
                "old", "new in v", "stub", "translation", "d for dwarf",
                "disambig", "tocright", "clear")

def clean_wikitext(text):
    code = mwparserfromhell.parse(text)
    for tpl in list(code.filter_templates()):
        name = str(tpl.name).strip().lower()
        if any(name.startswith(p) for p in NAV_PREFIXES):
            try: code.remove(tpl)
            except ValueError: pass
    out = str(code)
    # strip [[File:...]] / [[Image:...]] including deeply nested [[...]] captions
    def strip_file_links(s):
        i = 0
        res = []
        while i < len(s):
            m = re.match(r"\[\[(?:File|Image):", s[i:], re.I)
            if m:
                depth = 0
                j = i
                while j < len(s):
                    if s[j:j+2] == "[[":
                        depth += 1; j += 2
                    elif s[j:j+2] == "]]":
                        depth -= 1; j += 2
                        if depth == 0:
                            break
                    else:
                        j += 1
                i = j
            else:
                res.append(s[i]); i += 1
        return "".join(res)
    out = strip_file_links(out)
    # strip category templates/links and interwiki links from body
    out = cat_tpl_re.sub("", out)
    out = re.sub(r"\{\{\s*[Cc]ategory\s*\|[^}]*\}\}", "", out)
    out = cat_link_re.sub("", out)
    out = re.sub(r"\[\[Category:[^\]]*\]\]", "", out)
    out = re.sub(r"\[\[[a-z]{2}:[^\]]*\]\]", "", out)  # interwiki
    return out.strip()

def to_markdown(wikitext, title):
    try:
        p = subprocess.run(
            ["pandoc", "-f", "mediawiki", "-t", "gfm-raw_html", "--wrap=none"],
            input=wikitext, capture_output=True, text=True, timeout=60)
        md = p.stdout
    except Exception:
        md = wikitext
    # decode common HTML entities that pandoc passes through
    import html as _html
    md = md.replace("&nbsp;", " ")
    md = _html.unescape(md)
    # strip raw HTML blocks/tags that survived (figure, img, a, table, etc.)
    md = re.sub(r"<figure>.*?</figure>", "", md, flags=re.S)
    md = re.sub(r"<figcaption>.*?</figcaption>", "", md, flags=re.S)
    md = re.sub(r"<[^>]+>", "", md)
    # drop images first (markdown ![alt](src)), incl. multiline alt text
    md = re.sub(r"!\[.*?\]\([^)]*\)", "", md, flags=re.S)
    # drop leftover image-link tails like  ](Foo.jpg "caption")
    md = re.sub(r"\]\([^)]*\.(?:jpg|jpeg|png|gif|svg)[^)]*\)", "", md, flags=re.I)
    # turn wiki links [text](broken-target "title") into plain text
    for _ in range(3):
        md = re.sub(r"\[([^\[\]]+)\]\([^)]*\)", r"\1", md)
    # remove any remaining template residue and stray braces
    md = re.sub(r"\{\{[^{}]*\}\}", "", md)
    md = re.sub(r"[{}]{2,}", "", md)
    md = re.sub(r"^\s*\\?\|.*}}\s*$", "", md, flags=re.M)
    # tidy: collapse leftover lines that are only punctuation/pipes
    md = re.sub(r"^[ \t]*[\\|*]+[ \t]*$", "", md, flags=re.M)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    url = "https://dwarffortresswiki.org/index.php/" + title.replace(" ", "_")
    header = (f"# {title}\n\n"
              f"> Fonte: [{title}]({url}) — Dwarf Fortress Wiki (GFDL/MIT)\n\n")
    return header + md + "\n"

# ---- build per-mode category -> pages ----
modes = {"fortress-mode": collections.defaultdict(dict),
         "adventure-mode": collections.defaultdict(dict)}
page_count = collections.Counter()
unassigned = 0

for base, rec in canonical.items():
    title = base
    skills, cats = assign_skills(title, rec["text"])
    if not skills:
        unassigned += 1
        continue
    for skill in skills:
        cfg = SKILL_CATEGORIES[skill]
        target_modes = (["fortress-mode", "adventure-mode"] if cfg["modes"] == "both"
                        else ["fortress-mode"] if cfg["modes"] == "fortress"
                        else ["adventure-mode"])
        for m in target_modes:
            modes[m][skill][title] = rec

print(f"Unassigned pages: {unassigned}", file=sys.stderr)

# ---- write tree ----
def write_category(mode, skill, pages_map):
    cfg = SKILL_CATEGORIES[skill]
    cat_dir = os.path.join(OUT, mode, "skills", skill)
    ref_dir = os.path.join(cat_dir, "references")
    os.makedirs(ref_dir, exist_ok=True)
    index_lines = []
    written = 0
    for title, rec in sorted(pages_map.items()):
        slug = slugify(title)
        wt = clean_wikitext(rec["text"])
        if len(wt.strip()) < 30:
            continue
        md = to_markdown(wt, title)
        with open(os.path.join(ref_dir, slug + ".md"), "w", encoding="utf-8") as f:
            f.write(md)
        index_lines.append(f"- {title} → `references/{slug}.md`")
        written += 1
        page_count[(mode, skill)] += 1
    # SKILL.md for the category
    idx = "\n".join(index_lines)
    skill_md = f"""---
name: {skill}
description: {cfg['desc']}
---

# {skill.replace('-', ' ').title()} (Dwarf Fortress — {mode})

Localize e leia **apenas** o artigo relevante em `references/` (progressive disclosure — não leia tudo).

## Como buscar
Se não souber o arquivo exato, rode a busca local (a partir da raiz `df-skills/`):
`bash scripts/search.sh {mode}/{skill} "termo de busca"`
e leia o arquivo retornado.

## Índice de artigos ({written})
{idx}
"""
    with open(os.path.join(cat_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skill_md)
    return written

for mode, cats in modes.items():
    for skill, pages_map in cats.items():
        n = write_category(mode, skill, pages_map)
        print(f"  {mode}/{skill}: {n} articles", file=sys.stderr)

# save summary for the dispatcher generator
summary = {m: {s: page_count[(m, s)] for s in cats} for m, cats in modes.items()}
json.dump(summary, open(os.path.join(HERE, "build_summary.json"), "w"), indent=1)
print("\nDONE. Summary saved.", file=sys.stderr)
