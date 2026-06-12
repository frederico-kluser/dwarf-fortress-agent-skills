# Adventure copilot playbook — reading live state, field by field

> Fonte: sondagem ao vivo da API DFHack 53.14 (probes Lua neste repo) + docs.dfhack.org —
> artigo manual desta skill (não é extrato da wiki). License: MIT. Snapshot: 2026-06.

This is the interpretation guide for the JSON returned by `df_bridge.py state …`
(produced in-game by the bundled `dfb-state.lua` script, auto-installed into
`dfhack-config/scripts/`). All facts below were verified against a live 53.14 save.

## `state adventurer`

| Field | Meaning | Copilot guidance |
|---|---|---|
| `name`, `race`, `profession` | readable identity ("Uram Ormamones \"Martyrbanded\", Spearman") | use the short name when narrating |
| `pos {x,y,z}` | local map coordinates (site/wilderness block) | only meaningful relative to other units' `pos` |
| `health.blood / blood_max` | current/total blood | < ~75% = bleeding seriously; advise bandaging/rest |
| `health.wounds` | count of wound entries | > 0: inspect with `gui/unit-info-viewer` before fights |
| `health.pain, nausea, dizziness` | rising counters, 0 = fine | pain ≫ 0 explains slow/failed actions |
| `health.winded, stunned, unconscious` | incapacitation counters | any > 0 mid-combat = emergency, advise retreat/wait |
| `health.webbed, paralysis, fever, exhaustion` | conditions | webbed > 0 in combat = cannot act; exhaustion from sprinting |
| `needs.hunger_timer` | counts UP; `hungry` ≥ 75000, `starving` ≥ 150000 | suggest eating from backpack before "starving" |
| `needs.thirst_timer` | `thirsty` ≥ 25000, `dehydrated` ≥ 50000 | drinking from waterskin/river resets it |
| `needs.sleepiness_timer` | `drowsy` ≥ 57600 | drowsy fighters miss; suggest sleeping somewhere safe |
| `kills` | notable kills of this unit | flavor for narration |
| `stress_category` | DFHack stress bucket (3 ≈ neutral; lower = better mood) | mention only when it shifts |

Thresholds are the classic announcement cutoffs; treat them as labels, not exact science —
the booleans (`hungry`, `thirsty`, `drowsy`…) are computed in-game for you.

## `state units` / `state threats`

`units` lists everyone nearby; `threats` pre-filters to `danger == true`.
Both are sorted by distance, capped at 20 entries, scanned within `--radius` tiles
(default 25) and ±5 z-levels.

| Field | Meaning | Copilot guidance |
|---|---|---|
| `name`, `race` | readable identity + race ("law-giver", "Elf Beast Hunter") | civilians with court titles = you are in a keep/town hall |
| `dist` | Chebyshev distance in tiles | < 5 = conversation range; < 2 = melee range |
| `dir` | compass from the adventurer (`NW`, `S +2z`…) | "+2z" = above you (stairs/upper floor) |
| `danger` | DFHack `isDanger` — would attack you | the threat list; mention these first |
| `great_danger` | megabeast/semimegabeast/titan-class | drop everything, advise flee or prepare |
| `invader`, `undead`, `agitated`, `crazed` | why it is dangerous | shapes the advice (undead: aim for limbs…) |
| `wildlife`, `tame` | context | tame animals in town are scenery |
| `hidden` | the GAME hides this unit (sneaking/ambush) | armok-level info: hint "something is lurking" without details unless asked |

Empty `threats` + many titled civilians = safe social area: advise quests, trade, talk.

## `state inventory`

List of `{mode, item}`. `mode` values seen live: `Weapon` (wielded — includes shields),
`Worn` (armor/clothing/backpack), `Flask` (waterskin/pouch slot). No food listed =
nothing carried to eat — flag it before travel.

## `state date`

`year`, `month` (Granite…Obsidian), `day` (1–28), `season`. Months map to seasons
(Granite–Felsite = spring, … Moonstone–Obsidian = winter). Night/bogeymen and frozen
rivers are season/time concerns when advising travel.

## `log --new` (events since last check)

gamelog lines are English announcements, category-tagged by the bridge (`combat`,
`death`, `siege`, `mood`…). In adventure mode expect conversation lines, combat
blow-by-blow and travel notices. Narrate the 2–3 most relevant, translated.

## Narration template

> **Onde**: keep da cidade, 15 de Granite (primavera), ano 100.
> **Como**: ileso (sangue 100%), sem fome/sede; lança de ferro + escudo de cobre.
> **Quem**: barão, law-giver e um Profeta a 2–7 tiles; nenhuma ameaça num raio de 40.
> **Mudou**: a deusa Gili te deu a missão da cosmic mudstone (Scaly Temple).
> **Próximo passo**: fale com o law-giver sobre a localização do templo antes de viajar.

Four lines of situation + one concrete suggestion beats a data dump. Always answer in
the user's language; the JSON is English.

## When something fails

- exit 12 = game closed / DFHack not loaded → run `status`, tell the user to launch via `./dfhack`.
- `qerror: sem aventureiro` = not in adventure mode (menu/fort mode) → say so, offer fort-mode reads instead.
- Lua error mentioning a field → the DF version changed structures; re-probe with
  `df_bridge.py run lua "…pairs(...)…"` and update `dfb-state.lua` (this is a living tool).
