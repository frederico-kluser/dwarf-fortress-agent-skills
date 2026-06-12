# DFHack adventure tools catalog (with safety labels)

> Fonte: docs.dfhack.org adventure-tag (53.14-r2), descrições oficiais — artigo manual
> desta skill. License: MIT. Snapshot: 2026-06.

Every DFHack tool tagged `adventure`, grouped by what the copilot may do with it.
Run any of them through the bridge: `df_bridge.py run <tool> [args]`.

## Level 1 — information (safe, use freely)

| Tool | What it does |
|---|---|
| `advtools` | A collection of useful adventure mode tools (conversation/log helpers) |
| `gui/sitemap` | List and zoom to people, locations, or artifacts in the site |
| `gui/adv-finder` | Find and track historical figures and artifacts |
| `gui/unit-info-viewer` | Display detailed information about a unit |
| `cprobe` | Display low-level properties of the selected unit |
| `probe` / `bprobe` | Low-level properties of the selected tile / building |
| `position` | Report cursor and mouse position, along with other info |
| `markdown` | Export displayed text to a Markdown file |

Note: `gui/*` tools open windows on the PLAYER's screen — useful to point the user at
something, not for headless reading (use `df_bridge.py state` for that).

## Level 2 — quality of life (ok when it helps the user)

| Tool | What it does |
|---|---|
| `gui/journal` | Journal with a multi-line text editor (notes/quest log) |
| `gui/notify` | Show notifications for important events |
| `hide-tutorials` | Hide new-game tutorial popups |
| `toggle-kbd-cursor` | Toggles the keyboard cursor (needed by cursor-based tools) |
| `resize-armor` | Resize armor and clothing to fit the wearer |
| `set-timeskip-duration` | Modify the duration of the pre-game world update |
| `fix/sleepers` | Fixes sleeping units belonging to a camp that never wake up (bugfix) |

## Level 3 — world-changing / armok (ONLY on explicit user request)

| Tool | What it does |
|---|---|
| `flashstep` | Teleport your adventurer to the mouse cursor |
| `bodyswap` | Take direct control of any visible unit |
| `createitem` / `gui/create-item` / `gui/sandbox` | Create arbitrary items/units/trees |
| `forceequip` | Move items into a unit's inventory |
| `launch` | "Thrash your enemies with a flying suplex" |
| `add-spatter` | Add poisons and magical effects to weapons |
| `firestarter` / `extinguish` | Light fires / put out fires |
| `liquids` / `liquids-here` | Place magma, water or obsidian |
| `tiletypes` (+`-command`, `-here`, `-here-point`) | Paint map tiles |
| `plant` / `regrass` | Grow/remove shrubs and trees / regrow grass |
| `clean` / `cleaners` / `spotclean` / `clear-webs` | Remove contaminants/webs from the map |
| `reveal` / `unreveal` / `revtoggle` / `revflood` / `revforget` | Reveal or re-hide the local map |
| `reveal-adv-map` / `reveal-hidden-sites` / `reveal-hidden-units` | Reveal world map / all sites / sneaking units |
| `gui/reveal` | Reveal map tiles (UI) |
| `resurrect-adv` | Bring a dead adventurer back to life |
| `ghostly` | Toggle an adventurer's ghost status |
| `unretire-anyone` | Adventure as any living historical figure |
| `gui/family-affairs` | Manage romantic relationships and generate pregnancies |
| `changeitem` | Change item material, quality, and subtype |
| `add-recipe` | Add crafting recipes to a civ |
| `colonies` | Manipulate vermin colonies and hives |
| `putontable` | Make an item appear on a table |
| `gui/rename` | Edit in-game language-based names |

Reveal tools in particular are save-altering and spoil exploration — confirm intent,
and prefer `revforget`-aware workflows if the user wants to undo.

## Visualization

| Tool | What it does |
|---|---|
| `stonesense` (alias `ssense`) | A 3D isometric visualizer window of the local map |

## Pairing with the wiki skills

Mechanics questions raised by these tools (how conversation works, sneaking, fast
travel, sites) belong to the `df-adventure` wiki skill — search there:
`search.py --skill df-adventure "fast travel"`.
