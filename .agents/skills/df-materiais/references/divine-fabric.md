# Divine fabric

> Fonte: [Divine fabric](https://dwarffortresswiki.org/index.php/Divine_fabric) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Properties**
- **Material value 300 Not fire-safe Not magma-safe Melting point None Boiling point None Ignition point None Heat damage point 10250 °U Cold damage point 9900 °U Solid density 1 Specific heat 420**
- **Not fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|  |  |
|:--:|----|
|  | This article contains **massive spoilers**. If you do not wish to have your game experience spoiled, **do not scroll down**! |

**Divine fabrics** are special, procedurally generated fabrics that can be found in vaults. Divine fabrics are used as material for items and clothing used by angels, who ruthlessly protect the vault's priceless treasures. Unlike divine metals, divine fabrics cannot be modified into other items, nor are they appreciably better than their mundane counterparts.

As a quirk, human and elven caravans may bring instruments and instrument parts made out of divine fabric for trade.Bug:9275

## Traits

Divine fabrics appear to have identical material properties to standard silk cloth except a lack of ignition point. Although they cannot catch fire, they still suffer damage from high temperatures and are not fire-safe. The only differences between types of divine fabric are their name and their color\[Verify\], both decided by a selected sphere of the deity involved in their creation.

Its texture can cure depression. Its color can remove pain. Its sheen can spawn happiness.

## Types

|            |                    |              |
|------------|--------------------|--------------|
| Sphere     | Name               | Color\*      |
| Beauty     | dancing wisps      | Yellow       |
| Blight     | rotted fabric      | Black        |
| Chaos      | never-still cloth  | Red          |
| Darkness   | liquid darkness    | Black        |
| Dawn       | shining cloth      | Orange       |
| Day        | bright cloth       | White        |
| Death      | pale fabric        | Pale blue    |
| Deformity  | twisted fabric     | Black        |
| Disease    | patchy cloth       | Gray         |
| Dreams     | wispy cloth        | Blue         |
| Dusk       | translucent cloth  | Clear        |
| Fire       | flickering cloth   | Yellow       |
| Jewels     | faceted cloth      | Green        |
| Lakes      | still blue fabric  | Blue         |
| Lies       | heavy cloth        | Black        |
| Light      | glowing cloth      | White        |
| Lightning  | flashing sparks    | Yellow       |
| Mist       | misty cloth        | Clear        |
| Moon       | white cloth        | White        |
| Muck       | dirty fabric       | Brown        |
| Music      | sonorous lines     | Black        |
| Night      | pitch-black fabric | Black        |
| Nightmares | screaming mouths   | Medium taupe |
| Oceans     | undulating cloth   | Sea green    |
| Rain       | moist fabric       | Clear        |
| Rainbows   | multicolored cloth | Clear        |
| Rivers     | flowing fabric     | Blue         |
| Sky        | clear blue cloth   | Sky blue     |
| Stars      | motes of light     | White        |
| Storms     | flowing cloth      | Gray         |
| Sun        | blazing cloth      | White        |
| Thunder    | shining cloth      | White        |
| Trickery   | shimmering cloth   | Clear        |
| Twilight   | shadow stuff       | Black        |
| Volcanos   | molten liquid      | Red          |
| Water      | liquid cloth       | Blue         |
| Wind       | rustling fabric    | Gray         |

- The color name represents their arbitrary color token, while the background is their ASCII color. See color.

    Example raws (as extracted from world.dat in version 0.47.05)

    [INORGANIC:DIVINE_2]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:7:0:1]
        [BUILD_COLOR:7:0:1]
        [STATE_COLOR:ALL_SOLID:WHITE]
        [USE_MATERIAL_TEMPLATE:SILK_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:motes of light]
        [IGNITE_POINT:NONE]
        [MATERIAL_VALUE:300]
        [SOLID_DENSITY:1]
        [MOLAR_MASS:1]
        [SPHERE:STARS]

    [INORGANIC:DIVINE_4]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:1:0:1]
        [BUILD_COLOR:1:0:1]
        [STATE_COLOR:ALL_SOLID:BLUE]
        [USE_MATERIAL_TEMPLATE:SILK_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:liquid cloth]
        [IGNITE_POINT:NONE]
        [MATERIAL_VALUE:300]
        [SOLID_DENSITY:1]
        [MOLAR_MASS:1]
        [SPHERE:WATER]

    [INORGANIC:DIVINE_6]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:0:0:1]
        [BUILD_COLOR:0:0:1]
        [STATE_COLOR:ALL_SOLID:BLACK]
        [USE_MATERIAL_TEMPLATE:SILK_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:sonorous lines]
        [IGNITE_POINT:NONE]
        [MATERIAL_VALUE:300]
        [SOLID_DENSITY:1]
        [MOLAR_MASS:1]
        [SPHERE:MUSIC]

    [INORGANIC:DIVINE_8]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:3:0:1]
        [BUILD_COLOR:3:0:1]
        [STATE_COLOR:ALL_SOLID:CLEAR]
        [USE_MATERIAL_TEMPLATE:SILK_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:moist fabric]
        [IGNITE_POINT:NONE]
        [MATERIAL_VALUE:300]
        [SOLID_DENSITY:1]
        [MOLAR_MASS:1]
        [SPHERE:RAIN]
