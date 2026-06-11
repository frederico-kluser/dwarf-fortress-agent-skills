# Hydra

> Fonte: [Hydra](https://dwarffortresswiki.org/index.php/Hydra) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hydras for their seven heads.**
- **Biome**
- **Any Land**
- **Attributes**
- **Building destroyer : Level 2**
- **Megabeast · No Stun · No Pain · No Exert · Fanciful**
- **Tamed Attributes**
- **Pet value:** 10,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 200,000 cm 3
- **Max:** 8,000,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Butchering returns ( Value multiplier ×10)**
- **Food items**
- **Meat:** 130-474
- **Fat:** 49-104
- **Brain:** 28-35
- **Heart:** 2-4
- **Lungs:** 8-10
- **Intestines:** 12-16
- **Liver:** 4-5
- **Kidneys:** 4
- **Tripe:** 4-5
- **Sweetbread:** 1-2
- **Eyes:** 14
- **Spleen:** 2
- **Raw materials**
- **Bones:** 61-67
- **Skull:** 7
- **Teeth:** 21

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant dragon-like monster with seven biting heads.*

The **hydra** (plural: **hydras** from the raws) is a species of reptilian megabeasts with seven heads, each of them filled with sharpened teeth to rip your dwarves apart in quick succession. They are the smallest of the megabeasts, being under half the size of an adult roc or bronze colossus. All hydras are born with Talented skill in fighting, biting, striking and dodging, as well as Grandmaster skill in observing. Like all megabeasts, they are building destroyers.

Decapitation: the least efficient way to fight a hydra, but excellent training for weapon skills.

While they're about the size of what would be considered semi-megabeasts, hydras are **very** dangerous opponents for one simple reason – or rather, seven: not only do they possess significant combat skill while being much larger than your dwarves, they can attack with all seven of their heads at once. This means that engaging a hydra in melee can be ~~a bad idea~~ Fun, as your hammerdwarves may suffer up to seven bite attacks per turn, quickly overwhelming them. Additionally, hydras are immune to pain, cannot be stunned and feel no exertion, so little will stop them from continuing to shred your dwarves with their many toothy maws. Hydras are also the only creatures in the game with a healing factor, and their tissues will heal damage 100 times faster than other normal beings – a heavily battered hydra who escapes combat will have fully healed its wounds (save infections) in a few in-game weeks, though they are not able to regrow lost limbs (or extra heads, for that matter). A fallen hydra will provide the fortress with a fantastic amount of food and bones which will likely last several months. An undead hydra will still retain its healing properties.

In adventure mode, the best thing to do is to set your combat preferences to "dodge" and attempt to break any bite the hydra manages to get into you. Keep your back to a wall or tree so that a charging hydra will get knocked down when you dodge out of the way. Rather than trying to dispatch the 7 heads one after another, stabbing the hydra's upper body with a pike will bring about its demise much faster. The small contact area and high penetration depth of a pike will easily generate mortal wounds to the lungs, and with luck, can also damage the heart and spine too. Once its breathing is hindered by perforated lungs, the hydra will suffocate to death in short order.

Despite their huge size and destructive nature, hydras are as vulnerable to cage traps as any other creature. In the event the player succeeds in capturing one, they can be trained into one of the most valuable pets in the game (tied only with other megabeasts in value). A trained hydra serves as a perfect defense force for a fortress (though they can't be further trained into war/hunting beasts) and will probably turn any goblin or troll intruder into mince meat unless overwhelmed, and in the event another hydra of the opposite gender shows up, the player will get the chance to breed them for even more hydras. The offspring are born adults and take 20 years to reach their full size. Being megabeasts, hydras are perpetually hostile to your military squads and must be kept separated from your soldiers, otherwise they will kill each other on sight.Bug:10731

Despite being reptiles, hydras don't lay eggs and give live birth (meaning they don't need a nest box). Because they're born adults, it isn't possible for their offspring to become fully tame without modding.

Some dwarves like hydras for their *seven heads*.

A hydra would look approximately this formidable if you managed to remove one of its heads.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

It is inadvisable to fight a hydra while outside in the cold northern or southern regions, where it could unexpectedly begin to hail on said hydra. If this occurs, your best bet is to jump onto the hydra's back.

Estimated size comparison between a hydra and a dwarf.

    [CREATURE:HYDRA]
        [DESCRIPTION:A giant dragon-like monster with seven biting heads.]
        [NAME:hydra:hydras:hydra]
        [CASTE_NAME:hydra:hydras:hydra]
        [CREATURE_TILE:'H'][COLOR:4:0:1]
        [PETVALUE:10000]
        [PET_EXOTIC]
        [BIOME:ANY_LAND]
        [FREQUENCY:5]
        [FANCIFUL]
        [LARGE_PREDATOR]
        [MEGABEAST][DIFFICULTY:10]
            [ATTACK_TRIGGER:3:3:3]
        [SPHERE:MUCK]
        [SPHERE:REBIRTH]
        [SPHERE:STRENGTH]
        [NOFEAR][NOEXERT]
        [NOSTUN]
        [NOPAIN]
        [BUILDINGDESTROYER:2]
        [GRASSTRAMPLE:50]
        [BONECARN]
        [PREFSTRING:seven heads]
        [BODY:BASIC_2PARTBODY:7HEADNECKS:BASIC_FRONTLEGS:BASIC_REARLEGS:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:SPINE:BRAIN:SKULL:3TOES_FQ_REG:3TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:1]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:1]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:200000]
        [BODY_SIZE:20:0:8000000]
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
            [ATTACK_FLAG_INDEPENDENT_MULTIATTACK]
        [ATTACK:CLAW:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:CLAW]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:claw:claws]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ALL_ACTIVE]
        [LAIR:SIMPLE_BURROW:100]
        [LAIR_HUNTER]
        [MULTIPART_FULL_VISION]
        [NATURAL_SKILL:BITE:6]
        [NATURAL_SKILL:GRASP_STRIKE:6]
        [NATURAL_SKILL:MELEE_COMBAT:6]
        [NATURAL_SKILL:DODGING:6]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:14]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GOLD:1:RED:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:10]
        [SELECT_TISSUE_LAYER:ALL]
            [TL_HEALING_RATE:1]
