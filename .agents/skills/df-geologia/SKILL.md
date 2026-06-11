---
name: df-geologia
description: >-
  Geologia e mundo do Dwarf Fortress: biomas, camadas de pedra e solo, oceanos, florestas, plantas, árvores, geração de mundo (worldgen), lugares e lore. Use quando o usuário perguntar (inclusive em português) sobre terreno, onde achar recursos, bioma, caverna, planta, árvore, worldgen ou história do mundo. Termos EN: biome, world, geology, layer, cavern, tree, plant, worldgen, ocean, forest, river. Adventure e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Geologia (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-geologia "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 412 artigos — use o search.py para o resto)
- Temperate → `references/temperate.md`
- Tropical → `references/tropical.md`
- Biome → `references/biome.md`
- Forest → `references/forest.md`
- Civilization → `references/civilization.md`
- Tree → `references/tree.md`
- Ocean → `references/ocean.md`
- Grassland → `references/grassland.md`
- Shrubland → `references/shrubland.md`
- Savanna → `references/savanna.md`
- River → `references/river.md`
- Grass → `references/grass.md`
- Mountain → `references/mountain.md`
- Lake → `references/lake.md`
- Tundra → `references/tundra.md`
- Advanced world generation → `references/advanced-world-generation.md`
- Staring eyeball → `references/staring-eyeball.md`
- Wormy tendril → `references/wormy-tendril.md`
- Bubble bulb → `references/bubble-bulb.md`
- Valley herb → `references/valley-herb.md`
- Cave moss → `references/cave-moss.md`
- Kobold bulb → `references/kobold-bulb.md`
- Downy grass → `references/downy-grass.md`
- Abaca → `references/abaca.md`
- Arrow bamboo → `references/arrow-bamboo.md`
- Golden bamboo → `references/golden-bamboo.md`
- Hedge bamboo → `references/hedge-bamboo.md`
- Floor fungus → `references/floor-fungus.md`
- Bentgrass → `references/bentgrass.md`
- Cloudberry → `references/cloudberry.md`

*…e mais 382 artigos (use o search.py).*
