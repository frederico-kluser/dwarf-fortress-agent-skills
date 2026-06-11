---
name: df-dwarves
description: >-
  Gestão de dwarves no Dwarf Fortress: labores, habilidades, atributos, humores (strange mood), necessidades, pensamentos, nobres, profissões, justiça e psicologia. Use quando o usuário perguntar (inclusive em português) sobre gerenciar anões, trabalho, labor, humor estranho, nobres, mandatos ou felicidade. Termos EN: labor, skill, attribute, strange mood, noble, profession, happiness, thought, need, justice. Exclusivo do Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: fortress
---

# DF Dwarves (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-dwarves "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 177 artigos — use o search.py para o resto)
- Preferences → `references/preferences.md`
- Animal trainer → `references/animal-trainer.md`
- Skill → `references/skill.md`
- Mechanic → `references/mechanic.md`
- Critical thinker → `references/critical-thinker.md`
- Mathematician → `references/mathematician.md`
- Record keeper → `references/record-keeper.md`
- Cook → `references/cook.md`
- Fisherdwarf → `references/fisherdwarf.md`
- Miner → `references/miner.md`
- Ambusher → `references/ambusher.md`
- Trapper → `references/trapper.md`
- Chemist → `references/chemist.md`
- Carpenter → `references/carpenter.md`
- Geographer → `references/geographer.md`
- Bone carver → `references/bone-carver.md`
- Logician → `references/logician.md`
- Observer → `references/observer.md`
- Astronomer → `references/astronomer.md`
- Peasant → `references/peasant.md`
- Thought → `references/thought.md`
- Optics engineer → `references/optics-engineer.md`
- Weaponsmith → `references/weaponsmith.md`
- Mason → `references/mason.md`
- Swimmer → `references/swimmer.md`
- Thresher → `references/thresher.md`
- Social skill → `references/social-skill.md`
- Furnace operator → `references/furnace-operator.md`
- Druid → `references/druid.md`
- Herbalist → `references/herbalist.md`

*…e mais 147 artigos (use o search.py).*
