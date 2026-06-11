# Flesh ball

> Fonte: [Flesh ball](https://dwarffortresswiki.org/index.php/Flesh_ball) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes flesh balls for their calming roundness.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Genderless · No Stun**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 100-200
- **Butchering returns**
- **Food items**
- **Meat:** 2
- **Raw materials**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large ball of skin found moving around the debris near underground ponds. It is there that it absorbs dead matter for food.*

The **flesh ball** is an amphibious creature, made entirely out of muscle and blood, that is quite slow on the ground. They appear in clusters of 2–5 in the third layer of the caverns and are as heavy as a human, but they are harmless to dwarves, possessing no means of attacking but a weak push which will glance away from just about anything.

Flesh balls are featureless, skinless and boneless. As simple balls of muscle, they do not need to breathe or sleep, have no thought, cannot vomit, become dizzy, or be stunned, but are still easily killable anyway. They produce two pieces of meat when butchered. Flesh balls possess a pet value of 10, but lack the necessary tokens to be trainable. They can't be spawned in the object testing arena.

Some dwarves like flesh balls for their *warmth* and their *calming roundness*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

- A !!Flesh Ball!! is a famous delicacy in the fabled dwarven barbecue!
- Not to be confused with Cacodemons.
- Also a famous topping on pizzas with a certain absence of bones.
- Known to like voodoo dolls.
- Have been found living with a talking bin of thinly cut potatoes and a goblet of freezing mixed milk and sugar, the latter of which was referred to as a master.

|  |
|----|
| "Flesh ball" in other / Languages / Dwarven / : / ar biban / Elven / : / leci èle / Goblin / : / etkûk enu / Human / : / ammen ohe |

## Gallery

-

  *Art by Arne*.

-

  "Slowly-moving flesh ball that absorbs debris near water."\
  *Concept art by Bay 12 Games.*

    [CREATURE:FLESH_BALL]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A large ball of skin found moving around the debris near underground ponds.  It is there that it absorbs dead matter for food.]
        [NAME:flesh ball:flesh balls:flesh ball]
        [CASTE_NAME:flesh ball:flesh balls:flesh ball]
        [CREATURE_TILE:'o'][COLOR:6:0:0]
        [PETVALUE:10]
        [FREQUENCY:10]
        [BIOME:SUBTERRANEAN_WATER]
        [LARGE_ROAMING]
        [UNDERGROUND_DEPTH:3:3]
        [NOBONES]
        [NATURAL]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:2:5]
        [PREFSTRING:calming roundness]
        [PREFSTRING:warmth]
        [BODY:BASIC_1PARTBODY]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [USE_MATERIAL_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE] not skin -- it is eaten rather than tanned
            [STATE_NAME:ALL_SOLID:flesh]
            [STATE_ADJ:ALL_SOLID:flesh]
        [USE_TISSUE_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE]
            [TISSUE_NAME:flesh:NP]
        [TISSUE_LAYER:BY_CATEGORY:ALL:MUSCLE]
        [GAIT:WALK:Creep:6900:NO_BUILD_UP:0:LAYERS_SLOW:STRENGTH:AGILITY]
        [GAIT:CRAWL:Creep:6900:NO_BUILD_UP:0:LAYERS_SLOW:STRENGTH:AGILITY]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [BODY_SIZE:0:0:70000]
        [MAXAGE:100:200]
        [ALL_ACTIVE]
        [NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
        [CANNOT_JUMP]
        [NOTHOUGHT]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:MUSCLE]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                [TLCM_NOUN:flesh:SINGULAR]
