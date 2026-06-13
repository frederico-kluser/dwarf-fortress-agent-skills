# Action catalog — verbs, verified keys, safety tier, batch recipes

> Fonte: sondagem ao vivo do enum `df.interface_key` (DF 53.14 + DFHack 53.14-r2,
> 151 teclas `A_*`). Artigo manual desta skill (não-wiki). License: MIT. Snapshot 2026-06.

Este é o vocabulário de AÇÃO do copiloto. Toda ação é uma tecla simulada
(`gui.simulateInput`) ou um clique sintético — **o que um jogador faria**. Os RPCs de
movimento do RemoteFortressReader estão desativados no v50, então este é o caminho.

## Como executar (a ponte df_bridge.py)

Ação única:               `df_bridge.py act key A_TALK` · `act click X Y` · `act move n`
**Array de ações (batch):** `df_bridge.py act [flags] batch "<DSL>"`  ← flags ANTES de `batch`

DSL (uma ação por linha ou `;`; `#` comenta):

    goto X,Y [maxsteps=N]     # rota BFS até o tile do mapa (verifica por passo)
    move DIR [times=N]        # n s e w ne nw se sw up down wait
    key NOME [NOME...]        # nomes de df.interface_key (ex.: A_TALK SELECT CUSTOM_A)
    click X,Y [right]         # clique sintético em coords de TELA (as de `read screen`)
    wait short|long|N         # A_SHORT_WAIT | A_WAIT | N esperas curtas
    read screen|state|threats # captura no relatório (não muda nada)
    expect focus|text SUBSTR  # afirma; aborta o batch se não bater
    sleep MS                  # pausa real (assenta o frame), não é turno do jogo

JSON equivale: `'[{"op":"key","keys":["A_TALK"]},{"op":"move","dir":"n","times":3}]'`.
`--dry-run` valida e ecoa o plano sem pressionar nada. `--file`/`--stdin` para planos grandes.

## Segurança do batch (decisão do usuário: AUTONOMIA TOTAL)

O batch **não barra** verbos destrutivos nem auto-aborta em ameaça — ele **sempre reporta**
ameaças por passo (`threats`) e para **só em erro real**: jogo caiu (`game_lost`), sem
progresso, `expect` falhou, ou **barreira de viagem** (após `A_TRAVEL` as coords do mapa
ficam inválidas → passos de coordenada abortam, salvo `--allow-travel-barrier`).
Cautela opcional: `--stop-on-threat`, `--stop-on-focus-change`.
As regras TÉCNICAS continuam imutáveis: só input simulado/leituras (nunca mutar UI via Lua),
verificação por passo, salvar após marcos. O agente narra antes de agir; o usuário pré-autorizou
encadear ações.

Tiers (informativos): **T1** ler/observar · **T2** qualidade de vida · **T3** muda o mundo.

## Movimento & viagem
| Verbo | Tecla(s) | Tier | Batch |
|---|---|---|---|
| andar 1 | `A_MOVE_N/S/E/W/NE/NW/SE/SW` | T1 | `move n times=3` |
| andar cuidadoso | `A_CARE_MOVE_*` | T1 | `key A_CARE_MOVE_N` |
| subir/descer z | `A_MOVE_UP` / `A_MOVE_DOWN` / `A_MOVE_N_UP`… | T1 | `key A_MOVE_UP` |
| ir até tile (rota) | (BFS dfb-nav) | T1 | `goto 88,72` |
| ficar parado | `A_MOVE_SAME_SQUARE` | T1 | `key A_MOVE_SAME_SQUARE` |
| furtividade/postura | `A_SNEAK` `A_STANCE` `A_MOVEMENT` `A_MOVEMENT_SWIM` | T1 | `key A_SNEAK` |
| **viajar (BARREIRA)** | `A_TRAVEL` `A_TRAVEL_MAP` `A_END_TRAVEL` `A_TRAVEL_SLEEP` | T2 | `key A_TRAVEL` — coords resetam! use 2 batches |

## Conversa & comércio  (a "skill de conversa" que faltava)
Fluxo v50: `A_TALK` → **clicar na criatura** no mapa → opções por letra (`CUSTOM_A`..`Z`) →
menu de tópicos (comércio é um tópico). Conversas persistem ao fechar a tela.
| Verbo | Tecla(s) | Tier | Batch |
|---|---|---|---|
| iniciar conversa | `A_TALK` + clique | T2 | `key A_TALK; click 26,9; read screen` |
| escolher opção | `CUSTOM_A`..`CUSTOM_Z` / clique | T2 | `key CUSTOM_A; read screen` |
| comerciar (tópico) | (tópico da conversa) | T2 | `…read screen; key CUSTOM_?` |
| performar/interagir | `A_PERFORM` `A_INTERACT` `A_COMPANIONS` | T2 | `key A_PERFORM` |
| barganha (tela própria) | `A_BARTER_VIEW` `A_BARTER_CURRENCY_1/2` `A_BARTER_TRADE` `A_BARTER_SHOW` | T2 | `key A_BARTER_TRADE` |

## Necessidades (comer/beber/dormir — a "skill de necessidades")
| Verbo | Tecla(s) | Tier | Batch |
|---|---|---|---|
| comer/beber | `A_INV_EATDRINK` | T2 | `key A_INV_EATDRINK; read screen; key SELECT` |
| dormir | `A_SLEEP` `A_SLEEP_SLEEP` `A_SLEEP_WAIT` `A_SLEEP_DAWN` | T2 | `key A_SLEEP; read screen; key A_SLEEP_DAWN` |
| esperar | `A_SHORT_WAIT` `A_WAIT` | T1 | `wait short` |

## Combate (a "skill de combate" — T3, avançar só a pedido)
| Verbo | Tecla(s) | Tier | Batch |
|---|---|---|---|
| atacar | `A_ATTACK` `A_COMBAT_ATTACK` `A_ATTACK_CONFIRM` | T3 | `key A_ATTACK; read screen` |
| esquivar/agarrar | `A_COMBAT_DODGE` `A_WRESTLE` | T3 | `key A_WRESTLE` |
| arremessar/atirar | `A_THROW` `A_SHOOT` `A_NOCK` | T3 | `key A_THROW; read screen` |
| render/táticas | `A_YIELD` `A_TACTICAL_SETTINGS` | T2 | `key A_YIELD` |

## Inventário (a "skill de inventário")
`A_INV_LOOK` `A_INV_WEAR` `A_INV_REMOVE` `A_INV_PUTIN` `A_INV_DROP` `A_INV_DRAW_WEAPON`
`A_GROUND` `A_HOLD` `A_JUMP` — ex.: `key A_INV_LOOK; read screen`.

## Olhar / status / log
Olhar: `A_LOOK` `A_SEARCH` `A_CENTER` `A_ODOR` `A_DISPLAY_TRACKS` `A_FRESHEST_TRACK`.
Status: `A_STATUS` (`_HEALTH` `_KILLS` `_WRESTLE` `_ATT_SKILL` `_DESC`).
Log do mundo (quests/pessoas/intriga): `A_LOG` + `A_LOG_PEOPLE/EVENTS/AGREEMENTS/SITES/`
`SUBREGIONS/FEATURE_LAYERS/BESTIARY/ARTIFACTS/INTRIGUE`. Ex.: `key A_LOG; key A_LOG_AGREEMENTS; read screen`.

## Navegação de menu (primitivos)
`SELECT` · `LEAVESCREEN` (fecha menu, NUNCA use Lua p/ fechar) · `STANDARDSCROLL_UP/DOWN/LEFT/RIGHT`
· `CUSTOM_A`..`CUSTOM_Z` · cliques (`click X Y`). O overlay de Help (1ª vez) come teclado mas
deixa cliques passarem — opere por clique quando o foco tiver `Help`.

## Receita completa: sair, achar alguém na rua e perguntar de comércio
    # 1) sair do prédio até um tile de rua (coords do mapa via state/probe)
    goto 77,80
    # 2) abrir conversa e clicar na pessoa (coords de TELA via read screen)
    key A_TALK
    read screen
    click 26,9
    read screen
    # 3) escolher a opção de conversa/comércio (letra lida na tela)
    key CUSTOM_A
    read screen
