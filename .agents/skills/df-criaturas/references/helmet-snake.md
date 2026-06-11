# Helmet snake

> Fonte: [Helmet snake](https://dwarffortresswiki.org/index.php/Helmet_snake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes helmet snakes for their impressive heads.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40 cm 3
- **Mid:** 2,000 cm 3
- **Max:** 50,000 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 40-60
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 4
- **Fat:** 4
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A snake-like creature living deep underground. Its head is covered in armor so that is resembles the head of a dragon.*

**Helmet snakes** are creatures who inhabit the first and second layers of the caverns. They spawn individually and slither through the underground, attacking anything smaller than themselves; they continuously grow throughout their entire lives, with the oldest snakes being nearly as heavy as a fully grown dwarf, and they may attempt to take a bite out of one if provoked. Helmet snakes are distinctive for their extremely potent venom, which causes nausea, bruising, bleeding, fever, dizziness, swelling, oozing and even necrosis on those it bites[\[1\]](/index.php/v0.34_Talk:Helmet_snake#Bite_symptoms "v0.34 Talk:Helmet snake"). Without proper protection, a helmet snake can very easily kill a dwarf.

Helmet snakes can be captured in cage traps and trained into pets. They are born adults and can't be rendered fully tame. A female trained snake can be placed in a nest box, where she'll lay a large amount of eggs, or either gender can be butchered for a significant amount of returns (note the returns noted to the right represent a fully grown snake, younger ones will yield less). Products made from helmet snake parts are worth twice more than those made from common domestic animals. You may also try and use them for fortress defense - you can very easily cripple a goblin if your snake hits a bite attack, though the invader's armor and dodging skills may help them shrug it off, in addition to putting your pet in mortal danger.

You can sometimes get helmet snakes by raiding sites occupied by kobolds.

Unlike most creatures, helmet snakes can't be spawned in the object testing arena.

Some dwarves like helmet snakes for their *impressive heads*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some immature male humans have jokingly used the creature's name to describe a part of their own anatomy.

## Gallery

-

  Note: May hiss and roar at the same time.

-

  "Cobra-sized, armored-headed snake." Notably, they can grow much larger...\
  *Concept art by Bay 12 Games.*

    [CREATURE:HELMET_SNAKE]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A snake-like creature living deep underground.  Its head is covered in armor so that is resembles the head of a dragon.]
        [NAME:helmet snake:helmet snakes:helmet snake]
        [CASTE_NAME:helmet snake:helmet snakes:helmet snake]
        [CREATURE_TILE:'s'][COLOR:7:0:1]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:30]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [LARGE_PREDATOR]
        [LOW_LIGHT_VISION:10000]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:2]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:impressive heads]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:FORKED_TONGUE:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
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
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
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
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen helmet snake venom]
            [STATE_ADJ:ALL_SOLID:frozen helmet snake venom]
            [STATE_NAME:LIQUID:helmet snake venom]
            [STATE_ADJ:LIQUID:helmet snake venom]
            [STATE_NAME:GAS:boiling helmet snake venom]
            [STATE_ADJ:GAS:boiling helmet snake venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:helmet snake bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:HELMET_SNAKE:ALL]
                [SYN_INJECTED]
                [CE_FEVER:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_NAUSEA:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_DIZZINESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_SWELLING:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_OOZING:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_BRUISING:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_BLEEDING:SEV:10:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:75:END:100]
                [CE_NECROSIS:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:800:END:3000]
        [BODY_SIZE:0:0:40]
        [BODY_SIZE:2:0:2000]
        [BODY_SIZE:60:0:50000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:40:60]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:50]
                [CLUTCH_SIZE:10:30]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
