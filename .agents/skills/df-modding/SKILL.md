---
name: df-modding
description: >-
  Modding do Dwarf Fortress: tokens, arquivos raw, init, tilesets, gráficos e edição de definições do jogo. Use quando o usuário quiser modificar o jogo, entender referência de tokens (creature token, weapon token), criar raças custom ou editar raws. Termos EN: token, raw, modding, tileset, init, graphics, reaction, mod. Funciona para Adventure Mode e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Modding (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-modding "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 108 artigos — use o search.py para o resto)
- Creature token → `references/creature-token.md`
- Size → `references/size.md`
- Butcher → `references/butcher.md`
- Entity token → `references/entity-token.md`
- Interaction token → `references/interaction-token.md`
- Material definition token → `references/material-definition-token.md`
- Body token → `references/body-token.md`
- Modding → `references/modding.md`
- Language token → `references/language-token.md`
- Personality facet → `references/personality-facet.md`
- Material token → `references/material-token.md`
- Building token → `references/building-token.md`
- Plant token → `references/plant-token.md`
- Position token → `references/position-token.md`
- Reaction → `references/reaction.md`
- Graphics token → `references/graphics-token.md`
- Trading → `references/trading.md`
- Personality value → `references/personality-value.md`
- Unit type token → `references/unit-type-token.md`
- Graphics → `references/graphics.md`
- Item token → `references/item-token.md`
- Tilesets → `references/tilesets.md`
- Creature variation token → `references/creature-variation-token.md`
- Ethic → `references/ethic.md`
- Tissue definition token → `references/tissue-definition-token.md`
- Armor token → `references/armor-token.md`
- Inorganic material definition token → `references/inorganic-material-definition-token.md`
- Speech file → `references/speech-file.md`
- Token → `references/token.md`
- Biome token → `references/biome-token.md`

*…e mais 78 artigos (use o search.py).*
