#!/usr/bin/env bash
# Busca lexical local nos artigos markdown (alternativa a embeddings).
# Uso:
#   scripts/search.sh "<modo>" "<termo>"     # busca dentro de um modo
#   scripts/search.sh "<modo>/<skill>" "<termo>"  # busca dentro de uma categoria
#   scripts/search.sh all "<termo>"          # busca nos dois modos
#
# Exemplos:
#   scripts/search.sh adventure-mode "steel armor"
#   scripts/search.sh adventure-mode/combate "bleeding"
#   scripts/search.sh fortress-mode/industria "magma forge"
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCOPE="${1:?uso: search.sh <modo[/skill]|all> \"termo\"}"; shift
QUERY="$*"
if [ -z "$QUERY" ]; then echo "informe um termo de busca"; exit 1; fi

# Normaliza o escopo. Aceita:
#   all
#   <modo>              -> <modo>/skills
#   <modo>/<skill>      -> <modo>/skills/<skill>
resolve_scope() {
  case "$1" in
    */*) echo "$ROOT/${1%%/*}/skills/${1#*/}" ;;
    *)   echo "$ROOT/$1/skills" ;;
  esac
}
case "$SCOPE" in
  all) DIRS="$ROOT/adventure-mode/skills $ROOT/fortress-mode/skills" ;;
  *)   DIRS="$(resolve_scope "$SCOPE")" ;;
esac

# 1) ranqueia por nº de ocorrências no conteúdo (mais relevante primeiro)
hits=$(rg -c -i --no-messages --type md "$QUERY" $DIRS 2>/dev/null | sort -t: -k2 -rn | head -20)

# 2) também casa por nome de arquivo (slug do título)
slug=$(echo "$QUERY" | tr 'A-Z ' 'a-z-')
files=$(rg --files $DIRS 2>/dev/null | rg -i --no-messages "$slug" | head -10 || true)

if [ -n "$hits" ]; then
  echo "$hits"
elif [ -n "$files" ]; then
  echo "$files"
else
  echo "Nenhum resultado para: $QUERY"
fi
