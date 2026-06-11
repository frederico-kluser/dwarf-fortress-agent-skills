#!/usr/bin/env python3
"""Generate scripts/search.sh, per-mode dispatcher SKILL.md, and master SKILL.md."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from taxonomy import SKILL_CATEGORIES

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, ".agents", "df-skills")
summary = json.load(open(os.path.join(HERE, "build_summary.json")))

# short routing hint per category (situation -> skill)
ROUTE_HINT = {
    "combate": "lutar, armas, armaduras, ferimentos, sangramento, partes do corpo, síndromes/venenos",
    "criaturas": "um bicho específico, monstros, inimigos, megabestas, animais, raças, montarias",
    "materiais": "metais, pedras, minérios, gemas, do que algo é feito, magma-safe, valor de material",
    "geologia-mundo": "biomas, camadas de pedra, oceanos, florestas, worldgen, lugares, lore do mundo",
    "saude-alimentacao": "comer, beber, hospital, doenças, cura, fome, sede, cansaço",
    "modding": "tokens, arquivos raw, init, tilesets, criaturas custom, editar definições",
    "interface-controles": "teclas, menus, designações, como fazer algo na tela (v50)",
    "industria": "forja, fundição, agricultura, cerveja, artesanato, produção",
    "construcao": "oficinas, móveis, mecanismos, traps, stockpiles, salas, máquinas",
    "dwarves-gestao": "labores, habilidades, humores, nobres, profissões, justiça, felicidade",
    "comercio-economia": "comércio, caravanas, depot, riqueza, mandatos",
    "fortress-geral": "defesa, siege, eventos, visão geral do modo fortaleza",
    "adventure-geral": "criação de personagem, viagem, fast travel, conversas, acampamento, sítios, retire/reclaim",
}

# ---------- scripts/search.sh ----------
os.makedirs(os.path.join(OUT, "scripts"), exist_ok=True)
search_sh = r'''#!/usr/bin/env bash
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

case "$SCOPE" in
  all) DIRS="$ROOT/adventure-mode $ROOT/fortress-mode" ;;
  *)   DIRS="$ROOT/$SCOPE" ;;
esac

# ranqueia por nº de ocorrências (mais relevante primeiro), top 20
rg -c -i --no-messages --type md "$QUERY" $DIRS 2>/dev/null \
  | sort -t: -k2 -rn | head -20 \
  || echo "Nenhum resultado para: $QUERY"
'''
p = os.path.join(OUT, "scripts", "search.sh")
open(p, "w").write(search_sh)
os.chmod(p, 0o755)

# ---------- per-mode dispatcher ----------
def mode_dispatcher(mode, label, focus):
    cats = summary[mode]
    rows = []
    for skill, n in sorted(cats.items(), key=lambda x: -x[1]):
        hint = ROUTE_HINT.get(skill, SKILL_CATEGORIES[skill]["desc"][:60])
        rows.append(f"| {hint} | `skills/{skill}` ({n} artigos) |")
    table = "\n".join(rows)
    md = f"""---
name: df-{mode}
description: Guia de conhecimento do Dwarf Fortress para o {label}. {focus} Roteia a pergunta do jogador para a skill de categoria certa (combate, criaturas, materiais, etc.), carrega o SKILL.md dela e lê o artigo específico em references/.
---

# Dwarf Fortress — {label} (Roteador)

Você está no **{label}**. **Não responda de memória** sobre mecânicas — roteie para a categoria certa, carregue o `SKILL.md` dela e leia o arquivo de referência específico (progressive disclosure).

## Roteamento (situação do jogador → skill de categoria)
| Se o jogador fala sobre... | Carregue a skill |
|---|---|
{table}

## Procedimento
1. Identifique a categoria pela tabela acima.
2. Leia o `SKILL.md` da categoria (Nível 2).
3. Use o índice dela (ou `scripts/search.sh`) para achar o artigo.
4. Leia **apenas** o(s) arquivo(s) de `references/` necessário(s) (Nível 3).
5. Responda citando a mecânica exata e a página-fonte.

## Busca local
Não sabe o arquivo? Rode:
`bash scripts/search.sh {mode} "termo de busca"`
ou restrinja a uma categoria:
`bash scripts/search.sh {mode}/combate "termo"`

## Regras
- Carregue uma categoria por vez (orçamento de contexto).
- Se a pergunta cruzar categorias (ex.: "armadura de aço"), carregue `materiais` E `combate`.
- O conteúdo cobre v50/v0.47; se houver ambiguidade de versão, assuma **v50** e avise.
"""
    open(os.path.join(OUT, mode, "SKILL.md"), "w").write(md)

mode_dispatcher("adventure-mode", "Adventure Mode",
    "Foco em jogar como um aventureiro: criação de personagem, viagem, exploração de sítios, conversas e combate em primeira pessoa.")
mode_dispatcher("fortress-mode", "Fortress Mode",
    "Foco em gerenciar uma fortaleza: dwarves, indústria, construção, comércio e defesa.")

# ---------- master dispatcher ----------
adv_n = sum(summary["adventure-mode"].values())
for_n = sum(summary["fortress-mode"].values())
master = f"""---
name: dwarf-fortress-guide
description: Assistente-mestre de conhecimento do Dwarf Fortress. Use SEMPRE que o usuário fizer QUALQUER pergunta sobre jogar Dwarf Fortress — fortaleza, aventureiro, dwarves, combate, criaturas, indústria, construção, geologia, comércio, interface ou modding. Esta é a skill roteadora de topo: primeiro confirma se o jogador está no Adventure Mode ou no Fortress Mode, depois carrega o roteador daquele modo.
---

# Guia-Mestre do Dwarf Fortress (Roteador de Topo)

Há dois modos de jogo, cada um com sua própria árvore de skills. **Antes de responder, determine o modo do jogador.**

## Passo 1 — Escolha do modo
Pergunte (ou infira da conversa):

> **Você está jogando Adventure Mode (aventureiro) ou Fortress Mode (fortaleza)?**

| Modo | Carregue | Cobre |
|---|---|---|
| 🗺️ **Adventure Mode** (aventureiro, exploração, roguelike em 1ª pessoa) | `adventure-mode/SKILL.md` | {adv_n} artigos |
| 🏰 **Fortress Mode** (gerenciar fortaleza, dwarves, indústria) | `fortress-mode/SKILL.md` | {for_n} artigos |

- Se o jogador disser "aventureiro", "viagem", "explorar", "minha personagem" → **Adventure Mode**.
- Se disser "meu forte", "meus dwarves", "construir oficina", "caravana" → **Fortress Mode**.
- Na dúvida, **pergunte** explicitamente antes de prosseguir.

## Passo 2 — Roteamento dentro do modo
Depois de carregar o `SKILL.md` do modo, use a tabela de roteamento dele para
achar a categoria (combate, criaturas, materiais, etc.), carregue o `SKILL.md`
da categoria e leia **apenas** o artigo relevante em `references/`.

## Regras
- **Não responda de memória** sobre mecânicas — baseie-se nos arquivos de referência.
- Carregue uma categoria por vez (orçamento de contexto).
- Conteúdo compartilhado (criaturas, armas, materiais, geologia, saúde, modding)
  existe em **ambos** os modos — use a árvore do modo atual.
- Conteúdo é v50/v0.47; em caso de ambiguidade de versão, assuma **v50** e avise.

## Busca local (ripgrep, sem embeddings)
`bash scripts/search.sh all "termo"`            # nos dois modos
`bash scripts/search.sh adventure-mode "termo"`  # só aventura
`bash scripts/search.sh fortress-mode/industria "termo"`  # categoria específica
"""
open(os.path.join(OUT, "SKILL.md"), "w").write(master)

print("Dispatchers + search.sh written.")
print(f"  adventure-mode: {adv_n} articles across {len(summary['adventure-mode'])} skills")
print(f"  fortress-mode:  {for_n} articles across {len(summary['fortress-mode'])} skills")
