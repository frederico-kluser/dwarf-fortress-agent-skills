---
name: df-fortress-construcao
description: >-
  Construção da fortaleza no Dwarf Fortress: oficinas, móveis, mecanismos, pontes, alavancas, stockpiles, salas, zonas, construções e componentes de máquina. Use quando o usuário perguntar (inclusive em português) sobre construir, design de fortaleza, armazenamento ou engenharia. Termos EN: building, workshop, furniture, mechanism, stockpile, bridge, lever, pump. Exclusivo do Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: fortress
---

# DF Fortress Construcao (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-fortress-construcao "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 100 artigos — use o search.py para o resto)
- Cage → `references/cage.md`
- Zone → `references/zone.md`
- Workshop → `references/workshop.md`
- Construction → `references/construction.md`
- Stockpile → `references/stockpile.md`
- Furniture → `references/furniture.md`
- Door → `references/door.md`
- Bridge → `references/bridge.md`
- Lever → `references/lever.md`
- Trade depot → `references/trade-depot.md`
- Screw pump → `references/screw-pump.md`
- Statue → `references/statue.md`
- Smelter → `references/smelter.md`
- Bed → `references/bed.md`
- Mechanism → `references/mechanism.md`
- Pressure plate → `references/pressure-plate.md`
- Wall → `references/wall.md`
- Floodgate → `references/floodgate.md`
- Floor → `references/floor.md`
- Well → `references/well.md`
- Grate → `references/grate.md`
- Glass furnace → `references/glass-furnace.md`
- Table → `references/table.md`
- Water wheel → `references/water-wheel.md`
- Anvil → `references/anvil.md`
- Slab → `references/slab.md`
- Coffin → `references/coffin.md`
- Cabinet → `references/cabinet.md`
- Hatch cover → `references/hatch-cover.md`
- Kiln → `references/kiln.md`

*…e mais 70 artigos (use o search.py).*
