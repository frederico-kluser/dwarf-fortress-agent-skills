---
name: df-comercio
description: >-
  Comércio e economia da fortaleza no Dwarf Fortress: negociação, caravanas, trade depot, riqueza, mercadorias, mandatos e moeda. Use quando o usuário perguntar (inclusive em português) sobre negociar, caravana, depot, valor do forte ou economia. Termos EN: trade, caravan, depot, merchant, wealth, economy, coin, item. Exclusivo do Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: fortress
---

# DF Comercio (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`.agents/skills/scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-comercio "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 33 artigos — use o search.py para o resto)
- Block → `references/block.md`
- Caravan → `references/caravan.md`
- Animal trap → `references/animal-trap.md`
- Bucket → `references/bucket.md`
- Tool → `references/tool.md`
- Barrel → `references/barrel.md`
- Finished goods → `references/finished-goods.md`
- Currency → `references/currency.md`
- Bag → `references/bag.md`
- Bin → `references/bin.md`
- Decoration → `references/decoration.md`
- Item quality → `references/item-quality.md`
- Storage → `references/storage.md`
- Jug → `references/jug.md`
- Instrument → `references/instrument.md`
- Wealth → `references/wealth.md`
- Large pot → `references/large-pot.md`
- Wheelbarrow → `references/wheelbarrow.md`
- Flask → `references/flask.md`
- Weight → `references/weight.md`
- Jewelry → `references/jewelry.md`
- Item → `references/item.md`
- Honeycomb → `references/honeycomb.md`
- Stepladder → `references/stepladder.md`
- Their wagons have bypassed your inaccessible site → `references/their-wagons-have-bypassed-your-inaccessible-site.md`
- Stack → `references/stack.md`
- Figurine → `references/figurine.md`
- Item designations → `references/item-designations.md`
- Dwarven economy → `references/dwarven-economy.md`
- Trade agreement → `references/trade-agreement.md`

*…e mais 3 artigos (use o search.py).*
