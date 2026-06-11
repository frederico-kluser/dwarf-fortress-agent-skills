# Iron man

> Fonte: [Iron man](https://dwarffortresswiki.org/index.php/Iron_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes iron men for their stern appearance.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Building destroyer : Level 2**
- **Genderless · No Stun · No Pain · No Exert · Syndrome · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **☼ iron statue ☼ (worth 530☼)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A man-shaped creature made of iron.*

**Iron men** are dangerous and exceptionally rare inorganic construct creatures made out of iron, who inhabit the third layer of the caverns. Like other inorganic construct creatures, they are non-sentient, feel no pain, fear or exertion, cannot be stunned and don't need to breathe. They are as large as humans and are level 2 building destroyers. Iron men are immortal and only die to violence.

Iron men are not as tough as you'd expect, the reason being the fact they are actually hollow: they have an iron exterior layer and an interior gas layer, making them far more fragile than a fully metallic creature such as the bronze colossus, and even dwarf nails can damage the iron. Iron men are unharmed by fire and magma, but can be damaged by dragonfire just like regular iron items. Additionally, iron men will, when damaged, leak a poisonous gas which causes a syndrome called "iron man cough", consisting of coughing up blood. Dwarves with standard disease resistance will experience a peak in coughing shortly (100 time units) after infection, and will recover in less than a game day (1000 time units out of a full day's 1200 time units). These periods will vary according to the disease resistance of the infected dwarf, but the disease is not life-threatening. (Unless, of course, being sick is the straw that breaks the camel's back of your dwarf's sanity.)

Upon death, iron men become a masterwork iron statue of themselves. Parts like thumbs and noses removed from the creature during combat may be melted at a smelter in order to produce a small amount of iron.

Some dwarves like iron men for their *stern appearance*.

\

Admired for its *stern appearance*.

### Creature behavior and origin

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Surprisingly, the Iron Man does not deplete your fortress' booze supplies, nor does it woo nearly all of your female dwarves or hold a grudge against your Hammerer.

On rare occasions, humans who exhibit strange moods may sometimes turn into one of these. However, dwarves have been unable to duplicate this process, even given the finest workshops and crafting materials, leading most dwarven scholars to declare it impossible for a human to do so in a cave, with a box of scraps. !!EDIT!! The scholars are now running around naked, on account of losing a bet.

Iron men are also known to frequently make use of automated machinery in order to try and artificially gain divine goodwill.

It's unknown if the creature's metallic nature is a result of travelling through a magnetic field, or if it is capable of time travel. However, it's certain that it's made completely of iron, with no components of other metals or alloys like lead or steel. It will, however, still seek to fill your dwarves full of dread.

|  |
|----|
| "Iron man" in other / Languages / Dwarven / : / datan udos / Elven / : / icori onino / Goblin / : / dusna ngorûg / Human / : / uzin abo |

    [CREATURE:ELEMENTMAN_IRON]
        [DESCRIPTION:A man-shaped creature made of iron.]
        [NAME:iron man:iron men:iron man]
        [CASTE_NAME:iron man:iron men:iron man]
        [CREATURE_TILE:'M'][COLOR:0:0:1]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [FREQUENCY:1][DIFFICULTY:2]
        [POPULATION_NUMBER:15:30]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [NOFEAR]
        [PREFSTRING:stern appearance]
        [ODOR_LEVEL:0]
        [SMELL_TRIGGER:10000] cannot smell
        [NOBONES]
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [USE_MATERIAL_TEMPLATE:GAS:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen iron man gas]
            [STATE_NAME_ADJ:ALL_SOLID:frozen iron man gas]
            [STATE_NAME:LIQUID:condensed iron man gas]
            [STATE_NAME_ADJ:LIQUID:condensed iron man gas]
            [STATE_NAME:GAS:iron man gas]
            [STATE_NAME_ADJ:GAS:iron man gas]
            [STATE_COLOR:ALL:YELLOW]
            [MELTING_POINT:9870]
            [BOILING_POINT:9930]
            [PREFIX:NONE]
            [SYNDROME]
                [SYN_NAME:iron man cough]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_INHALED]
                [CE_COUGH_BLOOD:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:START:5:PEAK:100:END:1000]
        [TISSUE:IRON]
            [TISSUE_NAME:iron:NP]
            [TISSUE_MATERIAL:INORGANIC:IRON]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE:GAS]
            [TISSUE_NAME:gas:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:GAS]
            [TISSUE_MAT_STATE:GAS]
            [RELATIVE_THICKNESS:50]
            [TISSUE_LEAKS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:IRON]
        [TISSUE_LAYER_UNDER:BY_CATEGORY:ALL:GAS]
        [BODY_SIZE:0:0:70000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ITEMCORPSE:STATUE:NO_SUBTYPE:INORGANIC:IRON]
        [ITEMCORPSE_QUALITY:5]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_LEARNED]
