---
name: df-combate
description: >-
  Combate no Dwarf Fortress: armas, armaduras, escudos, ferimentos, partes do corpo, síndromes, venenos, mecânica de luta e militar (squads, treino, defesa). Use quando o usuário perguntar (inclusive em português) sobre lutar, equipar arma ou armadura, sangramento, dor, treinar soldados, montar esquadrão, ou defender a fortaleza. Termos EN: weapon, armor, shield, wound, syndrome, poison, military, squad, training, siege defense. Funciona para Adventure Mode e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Combate (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`.agents/skills/scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-combate "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 128 artigos — use o search.py para o resto)
- Skin → `references/skin.md`
- Trap → `references/trap.md`
- Skull → `references/skull.md`
- Military → `references/military.md`
- Climber → `references/climber.md`
- Weapon → `references/weapon.md`
- Armor → `references/armor.md`
- Bone → `references/bone.md`
- Siege → `references/siege.md`
- Archery → `references/archery.md`
- Crossbowman → `references/crossbowman.md`
- Military tactics → `references/military-tactics.md`
- Feather → `references/feather.md`
- Squad → `references/squad.md`
- Crossbow → `references/crossbow.md`
- Horn → `references/horn.md`
- Hair → `references/hair.md`
- Wool → `references/wool.md`
- Thief → `references/thief.md`
- Cartilage → `references/cartilage.md`
- Bolt → `references/bolt.md`
- Prepared organs → `references/prepared-organs.md`
- Siege engine → `references/siege-engine.md`
- Nail → `references/nail.md`
- Nervous tissue → `references/nervous-tissue.md`
- Ambush → `references/ambush.md`
- Drowning chamber → `references/drowning-chamber.md`
- Pick → `references/pick.md`
- Trap design → `references/trap-design.md`
- Short sword → `references/short-sword.md`

*…e mais 98 artigos (use o search.py).*
