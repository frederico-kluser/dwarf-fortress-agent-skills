---
name: df-saude
description: >-
  Saúde, comida e agricultura no Dwarf Fortress: comer, beber, hospital, doenças, cura, plantio, cervejaria e necessidades fisiológicas. Use quando o usuário perguntar (inclusive em português) sobre comida, bebida, lavoura, tratar ferimentos, infecção, fome, sede ou cansaço. Termos EN: food, drink, hospital, disease, heal, farming, crops, brewing, agriculture, hunger, thirst. Funciona para Adventure Mode e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Saude (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-saude "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 131 artigos — use o search.py para o resto)
- Food → `references/food.md`
- Crop → `references/crop.md`
- Kitchen → `references/kitchen.md`
- Surgeon → `references/surgeon.md`
- Diagnostician → `references/diagnostician.md`
- Plump helmet → `references/plump-helmet.md`
- Quarry bush → `references/quarry-bush.md`
- Pig tail → `references/pig-tail.md`
- Sweet pod → `references/sweet-pod.md`
- Rope reed → `references/rope-reed.md`
- Cave wheat → `references/cave-wheat.md`
- Whip vine → `references/whip-vine.md`
- Sliver barb → `references/sliver-barb.md`
- Dimple cup → `references/dimple-cup.md`
- Hide root → `references/hide-root.md`
- Hemp → `references/hemp.md`
- Longland grass → `references/longland-grass.md`
- Blade weed → `references/blade-weed.md`
- Sun berry → `references/sun-berry.md`
- Flax → `references/flax.md`
- Shrub → `references/shrub.md`
- Cotton → `references/cotton.md`
- Kenaf → `references/kenaf.md`
- Strawberry → `references/strawberry.md`
- Prickle berry → `references/prickle-berry.md`
- Jute → `references/jute.md`
- Rat weed → `references/rat-weed.md`
- Fisher berry → `references/fisher-berry.md`
- Ramie → `references/ramie.md`
- Banana → `references/banana.md`

*…e mais 101 artigos (use o search.py).*
