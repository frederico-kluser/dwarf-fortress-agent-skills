---
name: df-fortress-industria
description: >-
  Indústria da fortaleza no Dwarf Fortress: forja, fundição, oficinas de produção, artesanato, têxtil e cadeias de produção. Use quando o usuário perguntar (inclusive em português) sobre produzir bens, fundir metal, forjar, ou economia de produção. Termos EN: smelt, forge, craft, industry, production, smith, workshop, magma forge. Exclusivo do Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: fortress
---

# DF Fortress Industria (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-fortress-industria "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 29 de 29 artigos — use o search.py para o resto)
- Meat industry → `references/meat-industry.md`
- Nest box → `references/nest-box.md`
- Millstone → `references/millstone.md`
- Hive → `references/hive.md`
- Fishery → `references/fishery.md`
- Quern → `references/quern.md`
- Furniture industry → `references/furniture-industry.md`
- Still → `references/still.md`
- Glass industry → `references/glass-industry.md`
- Hauling → `references/hauling.md`
- Metal industry → `references/metal-industry.md`
- Beekeeping industry → `references/beekeeping-industry.md`
- Industry → `references/industry.md`
- Melt item → `references/melt-item.md`
- Ceramic industry → `references/ceramic-industry.md`
- Fishing industry → `references/fishing-industry.md`
- Paper industry → `references/paper-industry.md`
- Guild → `references/guild.md`
- Stone industry → `references/stone-industry.md`
- Arms industry → `references/arms-industry.md`
- Fuel industry → `references/fuel-industry.md`
- Gem industry → `references/gem-industry.md`
- Smelting → `references/smelting.md`
- Rest → `references/rest.md`
- Clean self → `references/clean-self.md`
- Butcher's shop → `references/butcher-s-shop.md`
- Farmer's workshop → `references/farmer-s-workshop.md`
- Tanner's shop → `references/tanner-s-shop.md`
- Vermin catcher's shop → `references/vermin-catcher-s-shop.md`
