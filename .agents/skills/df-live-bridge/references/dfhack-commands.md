# DFHack command cheatsheet for live control

> Fonte: docs.dfhack.org (DFHack 53.x) — artigo manual desta skill (não é extrato da
> wiki). License: MIT. Snapshot: 2026-06.

How commands travel: everything below is a **DFHack console command**. From outside the
game they are delivered through the RunCommand RPC — that is what `dfhack-run` does, and
what `df_bridge.py run <command…>` (in the bundled `scripts/` directory) wraps with
detection, fallback and clear errors. Anything you could type in the DFHack console
works the same way here.

## Pause control

| Command | Effect |
|---|---|
| `lua "dfhack.world.SetPauseState(true)"` | pause the game (official Lua API; needs a loaded world) |
| `lua "dfhack.world.SetPauseState(false)"` | unpause the game |
| `fpause` | **force**-pause everything, including UI rendering — FPS emergencies only; there is no `funpause` |

`df_bridge.py pause` / `unpause` are shortcuts for the two Lua calls. Pass the whole Lua
statement as a single quoted argument.

## Digging & designations

| Command | Effect |
|---|---|
| `quickfort run <blueprint>` | apply a dig/build/place blueprint (e.g. `quickfort run library/dreamfort.csv -n /surface1`) |
| `quickfort list` | list available blueprints |
| `dig-now` | instantly complete all current dig designations |
| `digv` | designate the whole mineral vein at the keyboard cursor |
| `digtype` | designate all tiles of the same type as the one under the cursor |

User blueprints live in `dfhack-config/blueprints/`; the stock library ships in
`hack/data/blueprints/` (reference it with the `library/` prefix). Cursor-based tools
(`digv`, `digtype`) need an in-game keyboard cursor and are less useful remotely —
prefer `quickfort` blueprints for remote mining designation.

## Map & stock information (read-only, safe)

| Command | Effect |
|---|---|
| `prospect` | summarize visible ores/layers of the current embark |
| `prospect all` | include not-yet-revealed materials (spoiler-ish but safe) |
| `getplants` | list/designate gatherable plants |
| `ls` | list all available commands |
| `help <command>` | usage of a specific command |

## Cleanup & items (these mutate the game — ask the user first)

| Command | Effect |
|---|---|
| `cleanowned` | confiscate scattered/worn items owned by dwarves |
| `autodump` | teleport items marked for dumping to the cursor |
| `unforbid all` | unforbid every item on the map |

## Lua one-liners

`lua "<statement>"` runs a statement in the DFHack Lua interpreter, e.g.:

    lua "print(df.global.cur_year)"
    lua "print(dfhack.df2utf(dfhack.TranslateName(df.global.world.world_data.name)))"

## gamelog event categories (what `df_bridge.py --json` tags)

| Category | Typical English announcements | PT hint |
|---|---|---|
| `death` | "…has been struck down", "…has died", "…found dead" | morte de anão/criatura |
| `siege` | "A vile force of darkness…", "…is under siege", "Snatcher!" | cerco/emboscada/raptor |
| `mood` | "…has been possessed!", "…withdraws from society", "fey mood" | humor estranho (artefato) |
| `birth` | "…has given birth", "…has hatched" | nascimento |
| `trade` | "A caravan…has arrived", "merchants", "liaison" | caravana/comércio |
| `migrants` | "Some migrants have arrived." | migrantes |
| `combat` | "…strikes…", "…attacks…", "The flying ☼ lodges firmly…" | combate |
| `job_cancel` | "…cancels Construct Building: Needs…", "Interrupted by…" | trabalho cancelado |
| `season` | "It is now summer.", "Spring has arrived…" | estação do ano |
| `other` | everything else | — |

The tag is a triage aid; translate the announcement text itself when reporting.

## Safety notes

- Commands act on a **live, unpaused** game unless you pause first — pause before bulk
  operations (`quickfort`, `autodump`, `cleanowned`).
- Read-only commands (`prospect`, `getplants`, `ls`, `help`, the pause toggles) are
  safe to run without asking.
- Quote Lua statements as one argument; the shell must deliver them to `run` intact.
- A failed command returns the console's error text plus a `CR_*` code
  (`CR_NOT_FOUND` = no such command in this DFHack version — check with `ls`).
