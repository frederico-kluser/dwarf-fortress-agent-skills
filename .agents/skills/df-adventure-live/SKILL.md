---
name: df-adventure-live
description: >-
  Copiloto ao vivo de Adventure Mode no Dwarf Fortress (via DFHack): observa o que o
  jogador está fazendo agora (estado do aventureiro, saúde, fome/sede/sono,
  inventário, quem está por perto, ameaças, data do mundo), explica o mundo e os
  eventos, aconselha o próximo passo e ajuda a jogar efetivamente, com leituras JSON
  do save em tempo real. Use quando o usuário estiver jogando Adventure Mode e pedir
  (inclusive em português) "o que está acontecendo", "quem está perto", "como estou",
  "o que faço agora", narração da aventura, ou ajuda prática com as ferramentas
  DFHack de aventura. Termos EN: adventure mode copilot, live state, adventurer
  status, health, nearby units, threats, inventory, journal, sitemap, advtools,
  real-time assistant. Requer o jogo aberto no Linux; complementa a df-live-bridge
  (canalização) e a df-adventure (mecânicas da wiki).
metadata:
  source: DFHack 53.x + sondagem ao vivo da API — artigos manuais, não-wiki
  snapshot: "2026-06"
  license: MIT
  mode: adventure
---

# DF Adventure Live (copiloto de Adventure Mode)

Esta skill define **como ser o copiloto** de uma sessão ao vivo: ler o estado real do
save, narrar/explicar no idioma do usuário e aconselhar a próxima ação. A canalização
(status/log/run/state) é a skill `df-live-bridge`; as mecânicas de jogo (viagem,
conversa, combate) são a skill `df-adventure` (wiki).

## O ciclo do copiloto (faça nesta ordem)

1. A sessão está de pé?

       python3 .agents/skills/scripts/df_bridge.py status --json

2. Foto do momento (aventureiro + ameaças + data, JSON):

       python3 .agents/skills/scripts/df_bridge.py state all
       python3 .agents/skills/scripts/df_bridge.py state units --radius 12     # quem está por perto
       python3 .agents/skills/scripts/df_bridge.py state inventory             # equipamento e mochila

3. O que aconteceu desde a última checagem (anúncios em inglês — traduza ao narrar):

       python3 .agents/skills/scripts/df_bridge.py log --new --json

4. Narre em 2-4 frases: onde está, como está (saúde/necessidades), quem importa por
   perto, o que mudou. Depois **um** conselho concreto de próximo passo.
   Interpretação dos campos: `references/adventure-copilot-playbook.md`.

## Níveis de ação (segurança)

- **Nível 1 — sempre ok**: todas as leituras acima; tools de informação
  (`gui/sitemap`, `gui/adv-finder`, `gui/unit-info-viewer`, `probe`, `position`).
- **Nível 2 — qualidade de vida, ok se ajudar**: `gui/journal`, `gui/notify`,
  `hide-tutorials`, `toggle-kbd-cursor`, `markdown` (exportar texto).
- **Nível 3 — muda o mundo: só com pedido explícito do usuário**: `advtools` de
  efeito, `flashstep`, `createitem`/`gui/sandbox`, `forceequip`, `liquids`,
  `tiletypes`, `reveal*`, `bodyswap`, `resurrect-adv`, `unretire-anyone` e tudo
  rotulado *armok* — são cheats/edição de save. Catálogo completo com rótulos:
  `references/adventure-tools.md`.
- O campo `hidden: true` em `state units/threats` é informação que o jogo esconde
  (emboscadas, furtivos). Avise que existe presença oculta **sem detalhar** — a menos
  que o usuário peça espoiler.

## Como buscar (referências desta skill)

    python3 .agents/skills/scripts/search.py --skill df-adventure-live "sitemap"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (2 artigos)
- Adventure copilot playbook (field-by-field state reading) → `references/adventure-copilot-playbook.md`
- DFHack adventure tools catalog (with safety labels) → `references/adventure-tools.md`
