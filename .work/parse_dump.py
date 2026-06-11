#!/usr/bin/env python3
"""Fase 2.1 — Parse the allrevisions XML dump correctly.

The dump uses API:Allrevisions chunking: one logical wiki page may appear in
MANY <page arvcontinue="..."> blocks, each holding a slice of its revisions.
So we must merge by (ns, title) and keep the globally-latest revision text.

Outputs a JSONL of current-revision pages for the target namespace(s).
"""
import os, sys, json, re, collections
import mwxml

HERE = os.path.dirname(os.path.abspath(__file__))
DUMP = os.path.join(HERE, "df-history.xml")

# Which namespaces hold real content we care about.
# 0 = Main (v50 target, post-migration). 116 = DF2014 (v0.47 fallback).
TARGET_NS = {0, 116}

redirect_re = re.compile(r"^\s*#REDIRECT", re.I)

# (ns,title) -> (latest_ts, text)
latest = {}
seen_pages = 0

dump = mwxml.Dump.from_file(open(DUMP, encoding="utf-8"))
for page in dump:
    if page.namespace not in TARGET_NS:
        # still consume revisions to advance iterator
        for _ in page:
            pass
        continue
    key = (page.namespace, page.title)
    for rev in page:
        ts = rev.timestamp
        ts_key = ts.unix() if ts is not None else 0
        cur = latest.get(key)
        if cur is None or ts_key >= cur[0]:
            latest[key] = (ts_key, rev.text or "")
    seen_pages += 1
    if seen_pages % 20000 == 0:
        print(f"  ...{seen_pages} target page-blocks scanned, "
              f"{len(latest)} unique titles", file=sys.stderr)

# Now classify and write
out_path = os.path.join(HERE, "pages.jsonl")
stats = collections.Counter()
cat_counts = collections.Counter()
written = 0
with open(out_path, "w", encoding="utf-8") as out:
    for (ns, title), (ts, text) in latest.items():
        is_redirect = bool(redirect_re.match(text))
        if is_redirect:
            stats["redirect"] += 1
            continue
        stub = "{{migrated_article}}" in text.lower() and len(text) < 400
        if stub:
            stats["migrated_stub"] += 1
        if len(text.strip()) < 30:
            stats["tiny"] += 1
            continue
        cats = re.findall(r"\[\[Category:([^\]\|]+)", text)
        for c in cats:
            cat_counts[c.strip()] += 1
        rec = {
            "ns": ns,
            "title": title,
            "is_stub": stub,
            "categories": [c.strip() for c in cats],
            "bytes": len(text),
            "text": text,
        }
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        written += 1
        stats[f"ns{ns}_written"] += 1

print(f"\nUnique titles in target ns: {len(latest)}")
print(f"Written content pages: {written}")
for k, v in stats.most_common():
    print(f"  {k}: {v}")
print(f"\nTop 40 categories:")
for c, n in cat_counts.most_common(40):
    print(f"  {n:>4}  {c}")
print(f"\nTotal distinct categories: {len(cat_counts)}")

# save category counts for taxonomy work
with open(os.path.join(HERE, "categories.json"), "w", encoding="utf-8") as f:
    json.dump(cat_counts.most_common(), f, ensure_ascii=False, indent=1)
