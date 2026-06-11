# Nightwing

> Fonte: [Nightwing](https://dwarffortresswiki.org/index.php/Nightwing) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes nightwings for their needle-like horns.**
- **Biome**
- **Any Desert**
- **Attributes**
- **Alignment:** Evil
- **Flying · Genderless · No Pain · No Exert · Learns · Fanciful · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 120,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A flying monster with stretched skin over its emaciated body. It has the head of a jackal with needle-like horns protruding through its mane.*

**Nightwings** are fanciful, intelligent creatures who are only found in evil deserts, where they spawn one at a time. Resembling a humanoid jackal with wings, they are twice the size of the average dwarf and will attack them on sight, using their wings to fly away from attacks and mauling civilians with their fangs and nails. If under attack by a nightwing, it is recommended to fight it with crossbows to take it out of the air before moving in with a melee squad, as they will make short work of it provided they can reach it.

Nightwings possess a great number of unusual characteristics. They need no sustenance to survive, don't need to breathe, are immune to pain and exertion, don't feel fear or emotion, cannot be stunned and nauseated, and are unaffected by dizziness or fevers. They will suck the blood out of those hit by their bite attacks, are born adults and are also genderless, meaning they are incapable of breeding. They are sapient (though they can't speak) and are able to equip items and open unforbidden doors.

Nightwings possess a pet value of 1,000, but lack the necessary tokens to be trainable (and even if modded to be trainable, the fact they are intelligent creatures will lead to strange behavior). Due to the aforementioned intelligence, dwarves will not butcher, eat or use products made from nightwings, limiting their use to occupying space in your refuse stockpile, live training or putting them somewhere of your liking if you capture one in a cage trap.

Some dwarves like nightwings for their *jackal heads*, their *bat wings*, their *long tails*, their *manes*, their *fangs*, their *ability to suck blood*, their *tightly-stretched skin* and their *needle-like horns*.

A nightwing ambushing a fluffy wambler, drawn in crayon by Bay 12 Games.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

On maps containing bat men, nightwings have been found to feel bitter at being constantly overshadowed.

|  |
|----|
| "Nightwing" in other / Languages / Dwarven / : / anan-fesh / Elven / : / lithéme-nine / Goblin / : / anu-bustusm / Human / : / kulur-emtha |

    [CREATURE:NIGHTWING]
        [DESCRIPTION:A flying monster with stretched skin over its emaciated body.  It has the head of a jackal with needle-like horns protruding through its mane.]
        [NAME:nightwing:nightwings:nightwing]
        [CASTE_NAME:nightwing:nightwings:nightwing]
        [CREATURE_TILE:'N'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [LARGE_PREDATOR][EVIL]
        [FANCIFUL]
        [LARGE_ROAMING][FREQUENCY:5]
        [BIOME:ANY_DESERT]
        [PETVALUE:1000]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [GRASSTRAMPLE:0]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [PREFSTRING:jackal heads]
        [PREFSTRING:bat wings]
        [PREFSTRING:long tails]
        [PREFSTRING:manes]
        [PREFSTRING:fangs]
        [PREFSTRING:ability to suck blood]
        [PREFSTRING:tightly-stretched skin]
        [PREFSTRING:needle-like horns]
        [EQUIPS]
        [CANOPENDOORS]
        [CAN_LEARN]
        [FLIER]
        [NOPAIN][NOBREATHE][NONAUSEA][NOEMOTION][NOEXERT][NOFEAR]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [BODY:HUMANOID_NECK:2WINGS:TAIL:2EYES:2EARS:NOSE:2LUNGS:NECK:SPINE:BRAIN:SKULL:4FINGERS:4TOES:2HEAD_HORN:HUMANOID_JOINTS:MOUTH:TONGUE:EYELIDS:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [BODY_SIZE:0:0:120000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_SUCK_BLOOD:50:100]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_LEARNED]
        [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
            [TL_COLOR_MODIFIER:DARK_BROWN:1]
                [TLCM_NOUN:hair:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:TAUPE_PALE:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
            [TL_COLOR_MODIFIER:IRIS_EYE_RED:1]
                [TLCM_NOUN:eyes:PLURAL]
