---
name: df-adventure
description: >-
  Adventure Mode do Dwarf Fortress: criação de personagem, viagem, fast travel, conversas com NPCs, acampamento, exploração de sítios e masmorras, retire/reclaim. Use quando o usuário estiver no modo Aventureiro ou perguntar (inclusive em português) sobre aventura, exploração, quests, diálogos ou viagem. Termos EN: adventurer, travel, camp, quest, conversation, retire, site, dungeon. Exclusivo do Adventure Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: adventure
---

# DF Adventure (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`../scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 ../scripts/search.py --skill df-adventure "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 30 artigos — use o search.py para o resto)
- Historical figure → `references/historical-figure.md`
- Performer → `references/performer.md`
- Scholar → `references/scholar.md`
- Knapper → `references/knapper.md`
- Clothing → `references/clothing.md`
- Legends → `references/legends.md`
- Messenger → `references/messenger.md`
- Wrestling → `references/wrestling.md`
- Claim → `references/claim.md`
- Tavern keeper → `references/tavern-keeper.md`
- Scribe → `references/scribe.md`
- Quest → `references/quest.md`
- Intrigue → `references/intrigue.md`
- Adventurer mode gameplay → `references/adventurer-mode-gameplay.md`
- Reputation → `references/reputation.md`
- Rumor → `references/rumor.md`
- Level of conflict → `references/level-of-conflict.md`
- Adventure mode quick start → `references/adventure-mode-quick-start.md`
- Talking → `references/talking.md`
- Die → `references/die.md`
- Occupation → `references/occupation.md`
- Adventurer mode character creation → `references/adventurer-mode-character-creation.md`
- Campfire → `references/campfire.md`
- Adventure mode quick reference → `references/adventure-mode-quick-reference.md`
- Adventurer mode F.A.Q. → `references/adventurer-mode-f-a-q.md`
- Bestiary → `references/bestiary.md`
- Guide to intelligent wilderness creatures in adventurer mode → `references/guide-to-intelligent-wilderness-creatures-in-adventurer-mode.md`
- History of Adventure Mode → `references/history-of-adventure-mode.md`
- Surrender → `references/surrender.md`
- Kisat Dur → `references/kisat-dur.md`
