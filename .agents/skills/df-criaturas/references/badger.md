# Badger

> Fonte: [Badger](https://dwarffortresswiki.org/index.php/Badger) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes badgers for their underground communities.**
- **Biome**
- **Taiga Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Badger - Badger man - Giant badger**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,500 cm 3
- **Mid:** 7,500 cm 3
- **Max:** 15,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 11
- **Fat:** 11
- **Brain:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Tripe:** 1
- **Raw materials**
- **Bones:** 10
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mammal with a striped face. It lives in groups and is ferocious in combat.*

**Badgers** are small creatures found in a variety of biomes, from temperate forests to taigas, where they appear in clusters of 4-12 individuals. While carnivorous, they are benign and timid by default, but differ from most other creatures due to being prone to rage; a badger has a small chance of randomly flipping out in a furious fit, attacking anything unfortunate enough to be at its vicinity (such as a dwarf) until it calms down. A peasant attacked by an enraged badger may suffer from nasty bruises and scratches, but they'll often cripple the animal back with a single kick; while infamous in previous versions of the game, badgers today are not life-threatening unless the dwarf in question is a child, since they're only half the size of a dog. A male badger is called a *boar*, while females are called *sows* and newborns are named *pups*.

Badgers can be captured in cage traps and trained into cheap exotic pets. They give equivalent returns to dogs when butchered, and are fairly easy to hunt or trap due to appearing in large numbers. An enraged badger can serve as a distraction against intruders, but don't expect it to survive a fight against anything bigger than itself.

They're not to be confused with the honey badger, which is a different animal.

Some dwarves like badgers for their *underground communities* and their *striped faces*.

Admired for their *striped faces*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Here is a lovely quote from Untelligent of the Bay12 forums.

"For ages, the crown of the King of Beasts has rested upon no head, the title long being vacant. Elephants became docile long ago, Carp have shrunk even smaller than they once were and dwarves made less fearful of their terrifying stare, and Giant Cave Spiders had the razor-tips of their fangs filed off.

But now, a new beast, freshly wrought from the blood-forges of Armok himself, has begun its reign of terror over the land. He made it ubiquitous, such that all would know its name. He filled it with fury, such that none would think it harmless. And He granted several of them tremendous size and insatiable anger far beyond that of their normal kin, such that even those who had thought they had mastered them had still more treacherous foes to be slain by.

There is a new King of Beasts, and its name is Badger. Tremble before it."

This may seem to contradict earlier claims of the badger being harmless. This is true, for a single badger or for small groups. Unfortunately, they tend to enter the map in huge "badger storms", swirling masses of highly irritable, lightning quick, sharp-clawed monsters. Any dwarf unlucky enough to be caught alone in a badger storm will soon find themselves being torn to shreds, reduced to a mangled pile of flesh.

*..Hands and feet will be severed.*

    Badgers were sponsored by the generous contributions of the Bay 12 community.

        Skadan
        Arcturis
        canccu

    [CREATURE:BADGER]
        [DESCRIPTION:A small mammal with a striped face.  It lives in groups and is ferocious in combat.]
        [NAME:badger:badgers:badger]
        [CHILD:1][GENERAL_CHILD_NAME:badger cub:badger cubs]
        [CREATURE_TILE:'b'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:25]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:4:12]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:GRASSLAND_TEMPERATE]
        [BONECARN]
        [BENIGN][PRONE_TO_RAGE:1]
        [GRASSTRAMPLE:0]
        [PREFSTRING:underground communities]
        [PREFSTRING:striped faces]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1500]
        [BODY_SIZE:1:0:7500]
        [BODY_SIZE:2:0:15000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:15]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [NOCTURNAL]
        [CREPUSCULAR]
        [NO_WINTER]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [CASTE_NAME:badger sow:badger sows:badger sow]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [CASTE_NAME:badger boar:badger boars:badger boar]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:EAR:HAIR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TOE:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:legs:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
                [TL_COLOR_MODIFIER:STRIPES_BLACK_WHITE:1]
                    [TLCM_NOUN:head:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
