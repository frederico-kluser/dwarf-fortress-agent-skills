---
name: df-central
description: >-
  Central de comando do ecossistema Dwarf Fortress deste repositório: explica todas
  as possibilidades (13 skills de conhecimento da wiki + ponte DFHack ao vivo +
  copiloto de Adventure Mode), indica qual skill usar em cada cenário, como combinar
  várias simultaneamente, e carrega a missão permanente do copiloto — jogar,
  aprender e criar novas skills com segurança. Use quando o usuário perguntar
  (inclusive em português) o que dá para fazer, qual skill serve para quê, pedir
  para continuar a missão/projeto do copiloto, retomar uma sessão anterior, ou
  fizer um pedido amplo que cruza conhecimento de wiki com o jogo rodando. Termos
  EN: mission control, skill router, capabilities overview, which skill when,
  combine skills, copilot hub, resume session. Vale para Fortress e Adventure Mode.
metadata:
  source: manual (mission control do repo) — não-wiki
  snapshot: "2026-06"
  license: MIT
  mode: both
---

# DF Central (mission control do ecossistema)

Esta é a skill-mapa: diz **o que existe, quando usar o quê, e como combinar**.
O detalhe de cada área mora na skill correspondente — leia o SKILL.md dela depois daqui.

## O ecossistema em uma olhada

**Conhecimento (wiki v50, 13 skills — perguntas de "como funciona"):**
`df-fortress-geral` (visão geral/embark/física/FAQ) · `df-criaturas` · `df-combate` ·
`df-materiais` · `df-saude` · `df-geologia` · `df-modding` · `df-interface` (teclas/menus) ·
`df-adventure` (mecânicas de aventura) · `df-fortress-industria` · `df-fortress-construcao` ·
`df-dwarves` · `df-comercio`.

**Jogo AO VIVO (DFHack, 2 skills — observar e operar a sessão rodando):**
- `df-live-bridge` — a canalização: `df_bridge.py status|log|watch|state|act|run|pause`,
  instalação do DFHack no Linux, protocolo RPC. É o COMO técnico.
- `df-adventure-live` — o copiloto de Adventure Mode: narração, conselhos, níveis de
  segurança de ação, playbook de leitura de estado e as regras pós-crash. É o COMO se comportar.

**Scripts** (em `.agents/skills/scripts/`): `search.py` (busca FTS5 em tudo),
`df_bridge.py` (ponte), `dfb-state.lua`/`dfb-act.lua`/`dfb-nav.lua` (instalados no jogo
automaticamente), `install_dfhack_linux.sh`.

## Cenário → skill (e combinações)

| Cenário | Use | Combine com |
|---|---|---|
| "Como funciona X?" (mecânica, criatura, material…) | a skill de wiki do assunto | `df-live-bridge` se a pergunta for sobre a sessão atual ("o aço da MINHA forja") |
| "O que está acontecendo no meu jogo?" / narração | `df-adventure-live` (ciclo do copiloto) | a skill de wiki do que aparecer (ex.: viu um Forgotten Beast → `df-criaturas`) |
| "Pausa/roda comando/lê eventos" | `df-live-bridge` | — |
| Instalar/consertar DFHack | `df-live-bridge` (setup ref) | — |
| Jogar por mim / me ajuda a agir | `df-adventure-live` (níveis de ação!) + `act goto/key/screen` da `df-live-bridge` | `df-adventure` para a mecânica da ação |
| "Continue a missão do copiloto" / retomar projeto | **esta skill** → seção "Missão permanente" + `PROMPT.md` na raiz do repo | `df-adventure-live` + `df-live-bridge` |
| Pergunta ampla/iniciante sem jogo aberto | `df-fortress-geral` | — |

Padrões de combinação simultânea:
1. **Copiloto completo** = `df-adventure-live` (comportamento) + `df-live-bridge` (comandos)
   + wiki skill do assunto do momento. É o trio padrão durante uma sessão ao vivo.
2. **Explicar evento ao vivo** = `log --new` (bridge) → categoria do evento → wiki skill
   correspondente (combat→`df-combate`, mood→`df-dwarves`, caravan→`df-comercio`).
3. **Aprender + agir** = wiki primeiro (o que é e os riscos), live depois (fazer).

## A missão permanente (do usuário, 2026-06)

> Jogar de verdade pela ponte, descobrir necessidades vivendo o jogo, e a cada fricção
> **criar/atualizar uma skill** — testar no save real, refinar, commitar — até o domínio
> completo do jogo. As skills são as AÇÕES que o agente oferece quando o usuário pede ajuda.

Ciclo de trabalho: observar (`state`/`log`) → tentar (`act`) → registrar o aprendido
(references/ da skill da área) → codificar a capacidade (script/subcomando) → testar ao
vivo → commit+push → próximo item do backlog (no `references/mission-and-roadmap.md`).

Regras inegociáveis (resumo; íntegra no playbook da `df-adventure-live`):
- Só **input simulado** (teclas/mouse) e leituras — NUNCA mutação de estrutura de UI
  via Lua (`screen.dismiss` etc.: já custou um mundo inteiro).
- Ações que mudam o jogo só com pedido explícito; narrar antes de agir.
- Sugerir save após cada marco; nunca experimentar em sessão não-salva.

## Como retomar uma sessão (faça nesta ordem)

    python3 .agents/skills/scripts/df_bridge.py status --json   # jogo aberto? DFHack ok?
    python3 .agents/skills/scripts/df_bridge.py state all       # foto do momento
    python3 .agents/skills/scripts/df_bridge.py log --new       # o que aconteceu desde a última vez

Estado do projeto, histórico de ciclos e backlog: `references/mission-and-roadmap.md`.
Prompt completo de continuação (formato XML, para colar numa sessão nova): `PROMPT.md`
na raiz do repositório.

## Como buscar (referências desta skill)

    python3 .agents/skills/scripts/search.py --skill df-central "backlog"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (1 artigo)
- Mission, cycle history, capability inventory & roadmap → `references/mission-and-roadmap.md`
