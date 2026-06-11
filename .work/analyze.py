#!/usr/bin/env python3
"""Analyze the DF wiki dump: for each page take the LAST revision,
classify by namespace, count redirects vs real content."""
import sys, collections, re
import mwxml

import os
DUMP = os.path.join(os.path.dirname(__file__), "df-history.xml")
dump = mwxml.Dump.from_file(open(DUMP, encoding="utf-8"))

ns_pages = collections.Counter()          # unique pages per ns
ns_real  = collections.Counter()          # pages w/ non-redirect, non-stub content
ns_bytes = collections.Counter()
redirect_re = re.compile(r"^\s*#REDIRECT", re.I)

main_real = 0
main_stub = 0
df2014_real = 0

n = 0
for page in dump:
    n += 1
    last_text = None
    for rev in page:                      # iterate to last revision
        last_text = rev.text or ""
    ns = page.namespace
    ns_pages[ns] += 1
    if last_text is None:
        continue
    is_redirect = bool(redirect_re.match(last_text))
    is_stub = "{{migrated_article}}" in last_text.lower() and len(last_text) < 400
    if not is_redirect and len(last_text.strip()) > 50 and not is_stub:
        ns_real[ns] += 1
        ns_bytes[ns] += len(last_text)
    if ns == 0:
        if is_redirect: pass
        elif is_stub: main_stub += 1
        elif len(last_text.strip()) > 50: main_real += 1
    if ns == 116 and not is_redirect and len(last_text.strip()) > 50 and not is_stub:
        df2014_real += 1
    if n % 20000 == 0:
        print(f"  ...{n} pages processed", file=sys.stderr)

NS_NAMES = {0:"Main(v50)",116:"DF2014(v0.47)",114:"v0.34",112:"v0.31",
            110:"23a",106:"40d",14:"Category",10:"Template",6:"File",
            2:"User",1:"Talk",104:"Modification",102:"Utility",100:"Bloodline"}
print(f"\nTotal unique pages: {n}\n")
print(f"{'ns':>4} {'name':<16} {'pages':>7} {'real_content':>12}")
for ns,_ in ns_pages.most_common():
    print(f"{ns:>4} {NS_NAMES.get(ns,'?'):<16} {ns_pages[ns]:>7} {ns_real.get(ns,0):>12}")
print(f"\nMain ns(0): real={main_real}  migrated_stub={main_stub}")
print(f"DF2014 ns(116): real content pages={df2014_real}")
