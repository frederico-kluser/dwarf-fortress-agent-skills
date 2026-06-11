#!/usr/bin/env bash
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
