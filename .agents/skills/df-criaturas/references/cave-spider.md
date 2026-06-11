# Cave spider

> Fonte: [Cave spider](https://dwarffortresswiki.org/index.php/Cave_spider) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave spiders for their mystery.**
- **Biome**
- **Underground Depth: 1-2**
- **Variations**
- **Cave spider - Giant cave spider**
- **Attributes**
- **Exotic pet · Extract · Hateable · Syndrome · Webs**
- **Pet value:** 0
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny underground bug, sought after for its thread.*

A **cave spider** is a type of subterranean vermin. It produces webs that can be collected and woven into cave spider silk thread.

Cave spiders can be annoying and beneficial at the same time. They will usually hang out around underground areas like caverns or underground water sources. They will leave webs around these areas or even in your fortress that can be collected via the 'collect webs' job at the loom, which is created automatically when webs are around. They can be annoying because they will bite the occasional pet or dwarf, though they're only mildly venomous. However, their bite induces a permanent syndrome, which, although not severe (very mild chronic dizziness), can prove crippling to a dwarf whose job needs immediate reaction (e.g. soldiering or lever-pulling). Dizziness also reduces the potential quality of items made by the dwarf, and probably applies other penalties yet to be discovered. Cave spiders are hateable vermin and will produce an unhappy thought for dwarves who detest them.

A cave spider caught in an animal trap, along with a glass vial, can be used to create cave spider venom. This has no use other than as a trade good. See extracts and animal dissector for more information.

Some dwarves like cave spiders for their *mystery*.

Admired for its *mystery*.

## Pest control

**Cave Spider webs**\
The white gem-like items.

If you have cats around your fortress, they will hunt cave spiders down without mercy just like any other vermin, and this can be a bit annoying if you want those webs. You can attempt to solve this problem by confining all unattached cats using cages or restraints and eliminating cats that have adopted a dwarf, but this approach can cause happiness issues, and migrants will continue to introduce pet cats to your fortress.

Assigning pet cats to a small, out-of-the-way room designated as a pasture can effectively restrain them without causing the dwarf-happiness issues killing them would. Be aware that assigning many cats to too small a pasture will result in catfights.

## Industrial use

Unfortunately, taming a cave spider does not provide a source of controlled silk production, as cave spiders in cages will not spin webs. Because of this, a silk farm requires an area (potentially cleared and sealed, for dwarven safety) in which the vermin can run wild. Since cave spiders do not reproduce like creatures, any such farm will need to be in a biome that generates cave spiders. You can also dig out a room in an upper level (near your loom) and attach a lever to a placed cage q-a-j (much the same as you would with caged goblins, though be sure to tame the spiders), once the cage has been filled with tame cave spiders, q-a-P pull the lever, releasing the spiders (that have been caught in an animal trap baited with meat), they will be released and begin filling the area with webs without your dwarves and pets having to deal with bites.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

|  |
|----|
| "Cave spider" in other / Languages / Dwarven / : / äs sethal / Elven / : / garetho thepani / Goblin / : / omo utes / Human / : / ngethac azoc |

Despite popular belief, cave spiders do not appear solely in abandoned mineshafts, and are not constantly spawned by square devices known as "monster spawners". The poison received from a cave spider cannot be negated by simply drinking milk. Despite further rumors by humans, cave spiders are not dark blue.

    [CREATURE:SPIDER_CAVE]
        [DESCRIPTION:A tiny underground bug, sought after for its thread.]
        [NAME:cave spider:cave spiders:cave spider]
        [CASTE_NAME:cave spider:cave spiders:cave spider]
        [CREATURE_TILE:249][COLOR:7:0:0]
        [CREATURE_CLASS:POISONOUS]
        [CARNIVORE]
        [PET_EXOTIC]
        [PARALYZEIMMUNE]
        [WEBIMMUNE]
        [NATURAL]
        [BIOME:SUBTERRANEAN_WATER]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:2]
        [VERMIN_GROUNDER][VERMIN_HATEABLE]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [PREFSTRING:mystery]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [HOMEOTHERM:10040]
        [LOW_LIGHT_VISION:10000]
        [NOT_BUTCHERABLE]
        [NOPAIN][EXTRAVISION][NOSTUN][NOFEAR]
        [NOBONES]
        [BODY:SPIDER:2EYES:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen cave spider venom]
            [STATE_ADJ:ALL_SOLID:frozen cave spider venom]
            [STATE_NAME:LIQUID:cave spider venom]
            [STATE_ADJ:LIQUID:cave spider venom]
            [STATE_NAME:GAS:boiling cave spider venom]
            [STATE_ADJ:GAS:boiling cave spider venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:cave spider bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:SPIDER_CAVE:ALL]
                [SYN_INJECTED]
                [CE_DIZZINESS:SEV:10:PROB:100:RESISTABLE:START:5:PEAK:100]  never ends!
        [USE_MATERIAL_TEMPLATE:SILK:SILK_TEMPLATE]
        [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
        [VERMIN_BITE:10:bitten:LOCAL_CREATURE_MAT:VENOM:LIQUID]
        [WEBBER:LOCAL_CREATURE_MAT:SILK]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:50]
        [MAXAGE:1:1]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
