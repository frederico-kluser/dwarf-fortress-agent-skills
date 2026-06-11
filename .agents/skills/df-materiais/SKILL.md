---
name: df-materiais
description: >-
  Materiais do Dwarf Fortress: metais, pedras, minérios, gemas, ligas, aço, adamantine, madeira, couro, conchas, extratos e propriedades físicas (magma-safe, valor, peso, densidade). Use quando o usuário perguntar (inclusive em português) sobre material, metal, pedra, minério, gema, aço, liga, do que algo é feito, ou "how to make steel". Termos EN: metal, stone, ore, gem, alloy, steel, iron, bronze, adamantine, leather, magma safe. Funciona para Adventure Mode e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Materiais (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`.agents/skills/scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-materiais "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 759 artigos — use o search.py para o resto)
- Stone → `references/stone.md`
- Meat → `references/meat.md`
- Item value → `references/item-value.md`
- Fat → `references/fat.md`
- Wood → `references/wood.md`
- Gem → `references/gem.md`
- Alcohol → `references/alcohol.md`
- Color → `references/color.md`
- Metal → `references/metal.md`
- Magma → `references/magma.md`
- Glass → `references/glass.md`
- Water → `references/water.md`
- Plant → `references/plant.md`
- Mangrove → `references/mangrove.md`
- Opal → `references/opal.md`
- Feather tree → `references/feather-tree.md`
- Glumprong → `references/glumprong.md`
- Nether-cap → `references/nether-cap.md`
- Blood thorn → `references/blood-thorn.md`
- Olive → `references/olive.md`
- Highwood → `references/highwood.md`
- Oak → `references/oak.md`
- Papaya → `references/papaya.md`
- Persimmon → `references/persimmon.md`
- Willow → `references/willow.md`
- Apricot → `references/apricot.md`
- Tower-cap → `references/tower-cap.md`
- Apple → `references/apple.md`
- Cherry → `references/cherry.md`
- Custard-apple → `references/custard-apple.md`

*…e mais 729 artigos (use o search.py).*
