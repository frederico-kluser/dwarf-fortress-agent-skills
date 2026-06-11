---
name: df-criaturas
description: >-
  Criaturas, animais e bestiário do Dwarf Fortress: bichos, monstros, inimigos, montarias, animais domésticos, megabestas, humanoides, vermes e raças jogáveis, incluindo os dados de raw (tokens) de cada criatura. Use quando o usuário perguntar (em qualquer idioma, inclusive português) sobre uma criatura, bicho, animal, monstro, dragão, goblin, troll, gato, cão, ou sobre stats de criatura como tamanho, pet value, ataques. Termos EN: creature, animal, beast, monster, megabeast, vermin, mount, pet, dragon, goblin, titan, forgotten beast. Adventure e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Criaturas (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`.agents/skills/scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-criaturas "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 1642 artigos — use o search.py para o resto)
- Dwarf → `references/dwarf.md`
- Giant earthworm → `references/giant-earthworm.md`
- Creature → `references/creature.md`
- Elf → `references/elf.md`
- Goblin → `references/goblin.md`
- Human → `references/human.md`
- Megabeast → `references/megabeast.md`
- Forgotten beast → `references/forgotten-beast.md`
- Fly → `references/fly.md`
- Rat → `references/rat.md`
- Pond turtle → `references/pond-turtle.md`
- Mosquito → `references/mosquito.md`
- Bark scorpion → `references/bark-scorpion.md`
- Crow → `references/crow.md`
- Hamster → `references/hamster.md`
- Lizard → `references/lizard.md`
- Jumping spider → `references/jumping-spider.md`
- Nautilus → `references/nautilus.md`
- Snail → `references/snail.md`
- Brown recluse spider → `references/brown-recluse-spider.md`
- Slug → `references/slug.md`
- Wren → `references/wren.md`
- Firefly → `references/firefly.md`
- Monarch butterfly → `references/monarch-butterfly.md`
- Skink → `references/skink.md`
- Sparrow → `references/sparrow.md`
- Tick → `references/tick.md`
- Worm → `references/worm.md`
- Grasshopper → `references/grasshopper.md`
- Green tree frog → `references/green-tree-frog.md`

*…e mais 1612 artigos (use o search.py).*
