#!/usr/bin/env python3
"""Generate scripts/search.sh (V2) and optional dispatcher in .agents/skills/.

V2 — flat structure. No mode routers. search.sh works directly on skill dirs.
The "dispatcher" is the description of each skill in the system prompt.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from taxonomy import SKILL_CATEGORIES

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, ".agents", "skills")

os.makedirs(os.path.join(OUT, "scripts"), exist_ok=True)

# ── search.sh ──
search_sh = r'''#!/usr/bin/env bash
# Busca lexical local nos artigos markdown (ripgrep, sem embeddings).
#
# Uso:
#   scripts/search.sh <skill> "termo"    busca dentro de uma skill
#   scripts/search.sh all "termo"        busca em TODAS as skills
#
# Exemplos:
#   scripts/search.sh df-combate "steel armor"
#   scripts/search.sh df-criaturas "goblin"
#   scripts/search.sh all "magma forge"
#
# A skill pode ser qualquer subdiretório em .agents/skills/ que tenha
# um diretório references/.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCOPE="${1:?uso: search.sh <skill|all> termo}"; shift
QUERY="$*"
if [ -z "$QUERY" ]; then echo "informe um termo de busca"; exit 1; fi

if [ "$SCOPE" = "all" ]; then
  DIRS=$(find "$ROOT" -mindepth 2 -maxdepth 2 -name references -type d | tr '\n' ' ')
else
  DIRS="$ROOT/$SCOPE/references"
fi

# busca por conteúdo, ranqueado por nº de ocorrências
hits=$(rg -c -i --no-messages --type md "$QUERY" $DIRS 2>/dev/null \
  | sort -t: -k2 -rn | head -20 || true)

if [ -n "$hits" ]; then
  echo "$hits" | sed "s|$ROOT/||"
else
  echo "Nenhum resultado para: $QUERY"
fi
'''
p = os.path.join(OUT, "scripts", "search.sh")
with open(p, "w") as f:
    f.write(search_sh)
os.chmod(p, 0o755)

# ── optional dispatcher SKILL.md (only if you want it) ──
skills = sorted(SKILL_CATEGORIES.items())
table = "\n".join(
    f"| {cfg['desc'][:100]}... | `{name}` | {cfg['modes']} |"
    for name, cfg in skills
)

dispatcher = f"""---
name: dwarf-fortress
description: Conhecimento enciclopédico do Dwarf Fortress v50/v0.47 extraído da wiki oficial. Use SEMPRE que o jogador perguntar qualquer coisa sobre Dwarf Fortress — mecânicas, criaturas, combate, materiais, construção, modding, controles, adventure mode ou fortress mode. Skills especializadas por categoria estão disponíveis.
---

# Dwarf Fortress Guide

Skills especializadas. Escolha a mais relevante pela description.

| Descrição | Skill | Modo |
|---|---|---|
{table}

## Como usar
1. Veja qual skill cobre o tópico da pergunta.
2. Carregue o `SKILL.md` dela.
3. Leia o artigo em `references/` — ou use `scripts/search.sh`.

## Busca local
`bash scripts/search.sh all "termo"`
"""
with open(os.path.join(OUT, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(dispatcher)

print("search.sh created")
print(f"optional dispatcher: {len(SKILL_CATEGORIES)} skills listed")
print(f"\nSkill directories to discover (flat, no collisions):")
for name in sorted(SKILL_CATEGORIES):
    print(f"  {name}")