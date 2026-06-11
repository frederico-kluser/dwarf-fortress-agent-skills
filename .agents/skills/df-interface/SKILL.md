---
name: df-interface
description: >-
  Interface do Dwarf Fortress v50/Premium: teclas, menus, designações, ícones e atalhos. Use quando o usuário perguntar (inclusive em português) como fazer algo na tela, qual tecla apertar, ou como navegar os menus. Termos EN: interface, control, keybinding, menu, designation, hotkey, UI shortcut. Funciona para Adventure Mode e Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: both
---

# DF Interface (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`.agents/skills/scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-interface "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 56 artigos — use o search.py para o resto)
- Labor → `references/labor.md`
- Adventurer mode → `references/adventurer-mode.md`
- Noble → `references/noble.md`
- Justice → `references/justice.md`
- Building → `references/building.md`
- Fortification → `references/fortification.md`
- Embark → `references/embark.md`
- Minecart → `references/minecart.md`
- Ramp → `references/ramp.md`
- Unit list → `references/unit-list.md`
- Manager → `references/manager.md`
- Object testing arena → `references/object-testing-arena.md`
- Stocks → `references/stocks.md`
- Standing orders → `references/standing-orders.md`
- Channel → `references/channel.md`
- Location → `references/location.md`
- Work orders → `references/work-orders.md`
- Dwarf fortress mode → `references/dwarf-fortress-mode.md`
- Forbid → `references/forbid.md`
- Status icon → `references/status-icon.md`
- Announcement → `references/announcement.md`
- Status → `references/status.md`
- Smoothing → `references/smoothing.md`
- Civilization and World Info → `references/civilization-and-world-info.md`
- Digging designation canceled → `references/digging-designation-canceled.md`
- Menu → `references/menu.md`
- Traffic → `references/traffic.md`
- Designations menu → `references/designations-menu.md`
- Named objects → `references/named-objects.md`
- Objects → `references/objects.md`

*…e mais 26 artigos (use o search.py).*
