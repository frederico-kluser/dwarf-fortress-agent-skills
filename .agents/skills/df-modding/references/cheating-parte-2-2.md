# Cheating (parte 2/2)

    [REACTION:SEED_STEW]
    [NAME:The Stew of Seeds]
    [BUILDING:STILL:NONE]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:MUSHROOM_HELMET_PLUMP:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:GRASS_TAIL_PIG:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:GRASS_WHEAT_CAVE:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:POD_SWEET:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:BUSH_QUARRY:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:TUBER_BLOATED:SEED]
    [FUEL]
    [SKILL:BREWING]

The entity_default tags:

    [PERMITTED_REACTION:HEMATITE_SONATA]
    [PERMITTED_REACTION:CALCITE_CACOPHONY]
    [PERMITTED_REACTION:MICROCLINE_MELODY]
    [PERMITTED_REACTION:SEED_STEW]
    [PERMITTED_REACTION:MALACHITE_MUSE]
    [PERMITTED_REACTION:CASSITERITE_CAROL]

**Free leather reaction:**

    [REACTION:MAKE_LEATHER]
    [NAME:create leather]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:20:SKIN_TANNED:NO_SUBTYPE:CREATURE_MAT:FISH_CAVE:LEATHER]
    [SKILL:SMELT]

### Free Soap from the practice workshop

This reaction changes the "practice_bonecarving" reaction into a create soap reaction which creates elf soap. And it uses the crossbow skill for some reason.

    [REACTION:PRACTICE_BONECARVING]
    [NAME:create soap]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [PRODUCT:100:1:BAR:NONE:CREATURE_MAT:ELF:SOAP][PRODUCT_DIMENSION:150]
    [SKILL:CROSSBOW]

# Memory Hacking

DFHack console, one of the easiest ways to cheat and/or run scripts.

Memory hacking is much harder than raw editing, and requires special tools. The most prevalent tool today is DFHack, which provides complete access to most of *Dwarf Fortress* internal memory through C++ plugins as well as Lua scripts. The `gui/gm-editor` command allows direct data editing of the selected creature, item, or job, while `gui/gm-editor world` does the same for global variables.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
For When Losing Is Too Fun


---
*Parte 2 de 2 de «Cheating». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Cheating*
