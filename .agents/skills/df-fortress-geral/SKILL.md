---
name: df-fortress-geral
description: >-
  Mecânicas gerais do Fortress Mode no Dwarf Fortress: defesa, eventos, embarks, física (água, magma, pressão, desabamento), guias de iniciante, FAQs, quickstart e visão geral. Use para perguntas amplas (inclusive em português) sobre tocar uma fortaleza, embark, cerco, magma, água, ou que não caiam numa categoria específica. Termos EN: fortress, embark, siege, magma, water, pressure, cave-in, guide, FAQ, getting started. Exclusivo do Fortress Mode.
metadata:
  source: dwarffortresswiki.org namespace 0 (v50 / Premium)
  snapshot: "2026-06"
  license: GFDL & MIT
  mode: fortress
---

# DF Fortress Geral (Dwarf Fortress)

Os artigos em `references/` estão em **inglês** (fonte: wiki oficial). O usuário pode
perguntar em português: traduza a pergunta para os termos de jogo em inglês (veja
`.agents/skills/scripts/glossary-pt-en.tsv`), busque em inglês e **responda no idioma do usuário**.
Leia **apenas** o artigo relevante — não pré-carregue tudo.

## Como buscar (faça isto primeiro)
Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-fortress-geral "steel smelting"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (principais 30 de 133 artigos — use o search.py para o resto)
- Pasture → `references/pasture.md`
- Fire → `references/fire.md`
- Cave-in → `references/cave-in.md`
- Bedroom design → `references/bedroom-design.md`
- Wear → `references/wear.md`
- Audio → `references/audio.md`
- Burrow → `references/burrow.md`
- Design strategies → `references/design-strategies.md`
- Combat → `references/combat.md`
- War → `references/war.md`
- Dwarven atom smasher → `references/dwarven-atom-smasher.md`
- Engraving → `references/engraving.md`
- Grazer → `references/grazer.md`
- Time → `references/time.md`
- Experience → `references/experience.md`
- Dwarf Fortress → `references/dwarf-fortress.md`
- Frequently Asked Questions → `references/frequently-asked-questions.md`
- Contaminant → `references/contaminant.md`
- Stupid dwarf trick → `references/stupid-dwarf-trick.md`
- Citizenship → `references/citizenship.md`
- Exploit → `references/exploit.md`
- Mass pitting → `references/mass-pitting.md`
- Quickstart guide → `references/quickstart-guide.md`
- Path → `references/path.md`
- Silk farming → `references/silk-farming.md`
- Dam → `references/dam.md`
- Magic → `references/magic.md`
- Obsidian farming → `references/obsidian-farming.md`
- Reservoir → `references/reservoir.md`
- Catsplosion → `references/catsplosion.md`

*…e mais 103 artigos (use o search.py).*
