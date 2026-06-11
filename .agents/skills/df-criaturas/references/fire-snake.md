# Fire snake

> Fonte: [Fire snake](https://dwarffortresswiki.org/index.php/Fire_snake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fire snakes for their mystery.**
- **Biome**
- **Underground Depth: 2-4**
- **Attributes**
- **Exotic pet · Extract · Hateable**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A serpent made of pure fire which can inject liquid fire as venom.*

**Fire snakes** are fire-proof vermin made entirely out of fire. They spawn only around magma sites, which are defined as the original biomes, and don't include any channels that carry magma away from magma pipes or magma pools. They may start fires, so locating fuel or graphite stockpiles near magma (or passages leading to magma) is risky. They will also inspire an unhappy thought if a dwarf that hates them encounters one.

With a body temperature of 14000 °U , a fire snake is hotter than magma and hotter than the melting point of nearly all magma-safe materials. It can melt or burn its way out of nearly any animal trap (even nether-cap, though the trap remains unharmed), with the exception of adamantine. Fortunately, like most other vermin, a cat will handily kill them, especially if pastured in the area of the infestation.

Although fire snakes spawn near magma, a dwarf on trapping duty can unwittingly transport a fire snake to an animal stockpile elsewhere in your fortress. Once set down by the trapper, a fire snake's high temperature can destroy the animal trap that holds it. Once free, a fire snake can cause all sorts of fun with your loose objects, including the destruction of masterworks, leading to unhappy thoughts in their creators, and cages, releasing any creatures held therein.

As vermin, fire snakes don't "spit" any sort of fire - the only thing they do is destroy wooden items that they 'step' on.

An artifact made from a fire snake's vermin remains, which can be produced only during a macabre strange mood, will inherit the static temperature property of the fire snake. This will result in high levels of !\!fun!! for any thieving kea or kobolds who attempt to make off with a fort's spicy new treasure. Similarly, this same !\!fun!! will also apply to any dwarves who attempt to wear it.

Liquid fire is a valuable extract derived from captured fire snakes.

Some dwarves like fire snakes for their *mystery*.

|  |
|----|
| "Fire snake" in other / Languages / Dwarven / : / ziril therleth / Elven / : / inira imaza / Goblin / : / zedan slorust / Human / : / usmok rosha |

Who needs venom?

    [CREATURE:SNAKE_FIRE]
        [DESCRIPTION:A serpent made of pure fire which can inject liquid fire as venom.]
        [NAME:fire snake:fire snakes:fire snake]
        [CASTE_NAME:fire snake:fire snakes:fire snake]
        [CREATURE_TILE:249][COLOR:6:0:1]
        [PETVALUE:10]
        [PET_EXOTIC]
        [NATURAL]
        [VERMIN_GROUNDER][FREQUENCY:100][VERMIN_HATEABLE]
        [FIREIMMUNE][WEBIMMUNE][IMMOLATE][MAGMA_VISION]
        [SMALL_REMAINS]
        [NOT_BUTCHERABLE]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [BIOME:SUBTERRANEAN_LAVA]
        [UNDERGROUND_DEPTH:2:4]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:mystery]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION][NOTHOUGHT]
        [NOBONES]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:2EYES:NOSE:MOUTH:FORKED_TONGUE:GENERIC_TEETH_WITH_FANGS]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [USE_MATERIAL_TEMPLATE:FLAME:FLAME_TEMPLATE]
        [USE_TISSUE_TEMPLATE:FLAME:FLAME_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:ALL:FLAME]
        [USE_MATERIAL_TEMPLATE:VENOM:FLAME_TEMPLATE]
            [STATE_NAME:ALL:liquid fire]
            [STATE_ADJ:ALL:liquid fire]
            [PREFIX:NONE]
        [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
        [VERMIN_BITE:10:bitten:LOCAL_CREATURE_MAT:VENOM:LIQUID]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [BODY_SIZE:0:0:1000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [ALL_ACTIVE]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [FIXED_TEMP:14000]
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [ODOR_STRING:smoke]
        [ODOR_LEVEL:50]
        [SMELL_TRIGGER:10000]
