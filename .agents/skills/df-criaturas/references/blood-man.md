# Blood man

> Fonte: [Blood man](https://dwarffortresswiki.org/index.php/Blood_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blood men for their gruesomeness.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Alignment:** Evil
- **Genderless · No Stun · No Pain · No Exert · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **Puddle of corrupted blood**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A man-shaped abomination made entirely of blood. These cursed creatures are only found very near the underworld.*

**Blood men** are exceptionally rare, evil-aligned construct creatures composed of blood found only in the third cavern layer. They stand the height of a human, feel no emotion or exertion, are immune to pain and cannot be stunned. While this sounds terrifying on paper, being made out of a liquid means you're going to lose limbs very easily. They are among the weakest, most harmless creatures you will encounter in the caverns, as even civilian dwarves and children can quickly punch their limbs off. Additionally, their punches are soft enough to not do real damage to even naked dwarves.

When they die, they leave a tile of "corrupted blood", but there's nothing dangerous about it, and it doesn't carry any sort of syndrome. Despite being made of a liquid, dunking blood men in water won't cause them to fall apart. Blood men are biologically immortal and only die from violence. They can't be spawned in the object testing arena.

Some dwarves like blood men for their *gruesomeness*.

|  |
|----|
| "Blood man" in other / Languages / Dwarven / : / nazush udos / Elven / : / cameda onino / Goblin / : / ogom ngorûg / Human / : / cadem abo |

## Gallery

-

  Very easy to get a blood sample from.\
  *Art by Fault*

-

  Dwells near the underworld.\
  *Concept art by Bay 12 Games.*

    [CREATURE:BLOOD_MAN]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A man-shaped abomination made entirely of blood.  These cursed creatures are only found very near the underworld.]
        [NAME:blood man:blood men:blood man]
        [CASTE_NAME:blood man:blood men:blood man]
        [EVIL]
        [CREATURE_TILE:'M'][COLOR:4:0:0]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [FREQUENCY:1]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:2:5]
        [NOBONES]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [NOFEAR]
        [ODOR_STRING:blood]
        [ODOR_LEVEL:50]
        [SMELL_TRIGGER:10000] cannot smell
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [PREFSTRING:gruesomeness]
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen corrupted blood]
            [STATE_ADJ:ALL_SOLID:frozen corrupted blood]
            [STATE_NAME:LIQUID:corrupted blood]
            [STATE_ADJ:LIQUID:corrupted blood]
            [STATE_NAME:GAS:boiling corrupted blood]
            [STATE_ADJ:GAS:boiling corrupted blood]
            [PREFIX:NONE]
        [TISSUE:BLOOD]
            [TISSUE_NAME:blood:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:BLOOD]
            [TISSUE_MAT_STATE:LIQUID]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:BLOOD]
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
        [ITEMCORPSE:LIQUID_MISC:NO_SUBTYPE:LOCAL_CREATURE_MAT:BLOOD]
        [ALL_ACTIVE]
