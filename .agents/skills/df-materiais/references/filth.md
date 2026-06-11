# Filth

> Fonte: [Filth](https://dwarffortresswiki.org/index.php/Filth) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Filth** is one of the more obscure materials present within the game code, as well as a smell. It comes in two varieties: solid brown and liquid yellow filth. Randomly generated creatures such as forgotten beasts may occasionally be composed of grime and filth, and it is currently unknown where filth can be encountered otherwise.

## Brown filth

This type of filth is a brown-colored solid. It does not melt, but gradually decomposes in temperatures above 10180 °U . It has a density of 1200, slightly higher than water.

    [MATERIAL:FILTH_B] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL:BROWN]
        [STATE_NAME_ADJ:ALL_SOLID:filth]
        [STATE_NAME_ADJ:SOLID_PRESSED:pressed filth]
        [BASIC_COLOR:6:0]
        [BUILD_COLOR:6:0:0]
        [TILE_COLOR:7:7:1]
        [SPEC_HEAT:4181]
        [HEATDAM_POINT:10180]
        [SOLID_DENSITY:1200]

## Yellow filth

Yellow-colored filth is a liquid that freezes at 10000 °U and boils at 10180 °U . It has a density of 920 when frozen and 1000 when liquid, exactly the same as water.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

### Dwarven poop

It is true that dwarves do not poop, but they do have other means of... er... removing their waste. A famous dwarven doctor, Urist McIliedHeIsNotFamous, discovered that the average dwarf has an extremely efficient digestive system. Any tiny amount of waste that passes digestion will then be turned into - you guessed it - beard hair.

    [MATERIAL:FILTH_Y] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL:YELLOW]
        [STATE_NAME_ADJ:ALL_SOLID:frozen filth]
        [STATE_NAME_ADJ:LIQUID:filth]
        [STATE_NAME_ADJ:GAS:boiling filth]
        [STATE_NAME_ADJ:SOLID_POWDER:frozen filth powder]
        [STATE_NAME_ADJ:SOLID_PASTE:filth slush]
        [BASIC_COLOR:6:1]
        [BUILD_COLOR:6:0:1]
        [TILE_COLOR:7:7:1]
        [SPEC_HEAT:4181]
        [HEATDAM_POINT:10180]
        [MELTING_POINT:10000]
        [BOILING_POINT:10180]
        [SOLID_DENSITY:920]
        [LIQUID_DENSITY:1000]
