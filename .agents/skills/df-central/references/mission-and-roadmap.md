# Mission, cycle history, capability inventory & roadmap

> Fonte: manual (mission control deste repo) — não é extrato da wiki. License: MIT.
> Última atualização: 2026-06-12.

## The mission (set by the user, June 2026)

The project pivoted from a passive knowledge base to a **live game copilot**: the agent
plays the game through the bridge, discovers needs by actually living a campaign,
and converts every friction into a skill — create/update → use → test on the real
save → refine → commit — "until complete mastery of the game". Skills are the ACTIONS
the agent offers when the user asks for help. All skills are routed by `df-central`.

## Cycle history (all commits on main, pushed)

| Cycle | Commit | What it delivered |
|---|---|---|
| 0 | `29a0d83`..`ea6e6a2` | df-live-bridge skill, df_bridge.py (status/log/watch/run/pause, gamelog tail with bookmark, dfhack-run + raw RPC TCP client), install_dfhack_linux.sh, DFHack 53.14-r2 actually installed, ANSI fix |
| 1 | `f6a222d` | `state` subcommand + dfb-state.lua (adventurer/threats/units/inventory/date/all as JSON), df-adventure-live skill (copilot playbook + tools catalog), glossary +12 |
| 2 | `ecd1dc3` | ACTION layer: dfb-act.lua + `act focus|screen|key|move` (read visible screen text, simulate keys, walk with focus guard); played for real (closed a menu, read quest sidebar, walked) |
| 3 | `f6d59a9` | dfb-nav.lua (BFS router) + `act goto x y` (per-step verification, route recomputation); synthetic mouse recipe; v50 conversation flow mapped; **crash post-mortem + safety rules** |
| 4 | `e2f20ad` | df-central mission control skill + PROMPT.md continuation prompt (XML) |
| 5 | (this) | **act batch** (array de ações, DSL+JSON, autonomia total) + primitivo `click` + `dfb-common.lua` (version guard / safe field) + `test_bridge.py` (1º teste offline, servidor RPC falso) + `action-catalog.md` (151 teclas verificadas) + journal JSONL. df-central orquestra ações. |

## Capability inventory (all live-tested on DF 53.14 + DFHack 53.14-r2)

- **Read**: `status` (paths/RPC health) · `log --new` (bookmark, category tags) ·
  `watch` (bounded follow) · `state adventurer|threats|units|inventory|date|all`
  (JSON from in-game Lua; field semantics in the df-adventure-live playbook) ·
  `act screen` (visible UI text) · `act focus` (which screen is open).
- **Act**: `run <any DFHack command>` · `pause/unpause` · `act key <interface_key>` ·
  `act click <x> <y>` (synthetic mouse, screen-tile coords, bounds-checked) ·
  `act move <dir>` (guarded) · `act goto <x> <y>` (BFS route + verification) ·
  **`act batch "<DSL>"`** = array of actions (goto/move/key/click/wait/read/expect/sleep;
  flags before `batch`; `--dry-run`; per-step verify; threats always reported; stops only
  on real error / travel-barrier; JSONL journal in `$XDG_STATE_HOME/df-bridge/journal/`).
- **Verbs verified** (151 `A_*` keys live): see `action-catalog.md` — talk/trade
  (`A_TALK`+click+`CUSTOM_*`, `A_BARTER_*`), travel (`A_TRAVEL*`), needs (`A_INV_EATDRINK`,
  `A_SLEEP*`), combat (`A_ATTACK`/`A_THROW`/`A_SHOOT`/`A_YIELD`), inventory (`A_INV_*`), log (`A_LOG_*`).
- **Quality**: `dfb-common.lua` (shared via reqscript: json/utf/focus/`safe` pcall field/
  `version_guard` substring-match/adventurer) — refactored into state/act/nav, fixes the
  counters2 crash. `test_bridge.py` = first offline test (fake RPC server; 17 cases).
- **Conversation (v50 flow, mapped live)**: `A_TALK` → click a creature on the map →
  lettered options (`CUSTOM_A`..`Z`): continue conversation / shout / talk to deity /
  assume identity → topic menu (trade lives here — "the ability to trade in shops").
  Conversations persist across screen closes. First-time Help overlay eats KEYBOARD
  but passes CLICKS through.
- **In-game scripts**: any `dfb-*.lua` next to df_bridge.py auto-installs into
  `<DF>/dfhack-config/scripts/` on first state/act call.

## Hard rules (cost: one unsaved world, 2026-06-12)

1. Input simulation and reads ONLY. Never mutate UI structure from Lua
   (`dfhack.screen.dismiss` on a vanilla screen = instant crash).
2. World-changing actions only on explicit user request; narrate before acting.
3. Suggest a save after every milestone; never experiment on an unsaved session.
4. `dfhack-run`: "Could not read handshake header" = the game died mid-call.
5. Route execution must verify position per step (blind step replay desyncs).

## Roadmap (ordered backlog — each item becomes/extends a skill)

1. **Conversation navigator** (finish): trade topic selection + reply reading; the
   greeting already worked ("Hello Uram. Long live the cause!"). Extends
   df-adventure-live + maybe `act talk <name>` sugar in the bridge.
2. **Travel assistant**: `A_TRAVEL` world-map reading + route narration.
3. **Needs macros**: eat/drink/sleep menu sequences (and "carry food!" advice).
4. **Combat copilot**: attack menu reading, target advice, retreat triggers on
   `state threats`.
5. **Character sheet reader**: skills/attributes via Lua → build advice.
6. **Fortress-mode state**: citizens/moods/stocks for `dfb-state` → universal copilot.
7. **df-dfhack-tools**: full 337-tool reference crawled from docs.dfhack.org
   (license check first; tag taxonomy: fort 229 · armok 98 · adventure 43 · auto 24).
8. **Rich events**: `eventful.onReport` Lua mirror → JSONL the bridge tails
   (strictly richer than gamelog).
9. CP437 decode for gamelog names (Al� → Alé).

## Machine facts (this dev machine)

DF 53.14 native Linux at `~/.steam/steam/steamapps/common/Dwarf Fortress`, DFHack
53.14-r2 installed (manual tarball). Launch WITH DFHack: `cd <DF> && ./dfhack`
(Steam direct launch = no DFHack = bridge blind). RPC localhost:5000. The world
"Asmurjal"/adventurer Uram was lost to the cycle-3 crash; a new world is being made.
