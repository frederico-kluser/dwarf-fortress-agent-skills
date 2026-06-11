#!/usr/bin/env python3
"""Fase 3 — Extract real taxonomy from {{category|X}} templates AND [[Category:X]]
tags, build per-page category sets, dump full category->pages map."""
import os, json, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
pages = [json.loads(l) for l in open(os.path.join(HERE, "pages.jsonl"), encoding="utf-8")]

cat_tpl_re = re.compile(r"\{\{\s*[Cc]ategory\s*\|\s*([^}|]+)")
cat_link_re = re.compile(r"\[\[Category:([^\]\|]+)")

cat_counts = collections.Counter()
cat_to_pages = collections.defaultdict(list)
page_cats = {}

for p in pages:
    title = p["title"]
    cats = set()
    for m in cat_tpl_re.findall(p["text"]):
        cats.add(m.strip())
    for m in cat_link_re.findall(p["text"]):
        c = m.strip()
        # normalize DF2014: prefix
        c = re.sub(r"^DF2014:", "", c)
        cats.add(c)
    page_cats[title] = sorted(cats)
    for c in cats:
        cat_counts[c] += 1
        cat_to_pages[c].append(title)

# write outputs
json.dump(cat_counts.most_common(),
          open(os.path.join(HERE, "cat_counts.json"), "w"), indent=1)
json.dump({c: sorted(v) for c, v in cat_to_pages.items()},
          open(os.path.join(HERE, "cat_to_pages.json"), "w"), indent=1)
json.dump(page_cats,
          open(os.path.join(HERE, "page_cats.json"), "w"), indent=1)

print(f"Pages: {len(pages)}")
print(f"Distinct categories: {len(cat_counts)}")
uncategorized = sum(1 for p in pages if not page_cats[p["title"]])
print(f"Uncategorized pages: {uncategorized}")
print(f"\nAll categories by frequency:")
for c, n in cat_counts.most_common():
    print(f"  {n:>4}  {c}")
