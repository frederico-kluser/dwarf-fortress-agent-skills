# Primordial remnant

> Fonte: [Primordial remnant](https://dwarffortresswiki.org/index.php/Primordial_remnant) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Properties**
- **Material value 200☼ Impact strength 2 GPa Shear strength 2 GPa ×1.2 Fire-safe Magma-safe Melting point None Boiling point None Ignition point None Solid density 1000 kg/m³ Specific heat 7500 J/kg·K**
- **Fire-safe:** Magma-safe

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

*"In the beginning, there was an endless expanse of salt..."* - Toady One, Future of the Fortress

**Primordial remnants**, alternatively known as **remnants of creation** and **mythical remnants**, are a type of procedurally-generated material that can be found as artifacts.

## Properties

The name and appearance of a remnant is generated based on its associated sphere. This linkage is consistent between all remnants and mysterious dungeons - "cosmic wood" might be guarded by "adepts of the forest," while a "primal crystal" might generate "gem worshippers". Currently, only one type of remnant can exist in a world.

Remnants have identical mechanical properties to divine metal - their yield is 1,000,000 KPa in all dimensions, and fractures at 2,000,000 KPa - superior to steel. They are perfectly inelastic and can be extremely sharp, with a strain-at-yield of 0 and a max edge of 12,000. Their density is 1,000 kg/m³, about as much as wood. Remnants are completely fireproof.

(A remnant associated with the sphere of metals gains the [`[ITEMS_METAL]`](/index.php/Material_definition_token#ITEMS_METAL "Material definition token") token, and is thus recognized as being metal.)

Because remnants are hidden in mysterious dungeons without any historical interactions, they can't be viewed in legends mode until they're encountered in play.

## Raw material

Primordial remnants originate from mysterious lairs, though historical figures can steal them like other artifacts, and bring them into the wider world.

They have, as of yet, no known powers or uses. Religions seek to gather them, and therefore offer a quest to retrieve one. They are categorized as a "small rock," like those used for knapping.

## List of remnants

There are unique sprites and different colors for primordial remnants, depending on the sphere they are attached to. Similar materials can have ambiguous spheres, and thus the powers a sphere grants are sometimes indeterminate on the remnant name alone.

|  |  |  |  |  |
|----|----|----|----|----|
| Icon | Possible Sphere(s) | Name | Color | Possible Powers (based on sphere) |
|  | Default / None | glitchstuff | Black | — |
|  | Mountains, Minerals, Caverns | stone | Gray | Mountains / – Ice Bolt, Suffocate, Cause Dizziness / Minerals / – Propel / Caverns / – Blind |
|  | Jewels | crystal | White | **Jewels** – Propel |
|  | Chaos | chaos | Red | **Chaos** – Cause Pain, Blister, Bleeding, Nausea, Cause Dizziness |
|  | Darkness, Death, Nightmares | darkness | Black | Darkness / – Blind / Death / – Cause Pain, Paralysis, Blind, Suffocate / Nightmares / – Propel, Cause Pain, Blister, Paralysis, Bleeding, Sicken (Cough Blood), Sicken (Vomit Blood), Nausea, Rot, Blind, Suffocate, Cause Dizziness |
|  | Dreams | dreamstuff | Green | **Dreams** – Propel |
|  | Fire | fire | Red | **Fire** – Blister, Blind |
|  | Light | light | Yellow | **Light** – Blind |
|  | Lightning | lightning | Yellow | **Lightning** – Blind |
|  | Metals | metal | Silver | **Metals** – Propel |
|  | Moon | moonstone | White | **Moon** – Blind |
|  | Muck | mudstone | Brown | **Muck** – Nausea, Rot, Blind, Suffocate |
|  | Oceans, Water | ice | Blue | Oceans / – Ice Bolt / Water / – Ice Bolt, Suffocate |
|  | Plants | leaf | Green | **Plants** – Propel |
|  | Salt | salt | White | **Salt** – Paralysis, Nausea |
|  | Mist, Sky, Storms, Wind | cloudstuff | White | Mist / – Blind / Sky / – Propel / Storms / – Ice Bolt, Propel / Wind / – Propel |
|  | Stars | stardust | Yellow | **Stars** – Blind |
|  | Sun | sunstone | Yellow | **Sun** – Blister, Blind |
|  | Trees | wood | Brown | **Trees** – Propel |
|  | Volcanoes | obsidian | Red | **Volcanoes** – Propel |

## Equipment

Jewelry and weapons made from primordial remnants are found in mysterious dungeons and palaces, respectively. These items are also magical, granting the wielder use of an X interaction. Weapons made from these materials are as strong as divine metal, and use the same set of special graphics. The powers are based on the sphere of the primordial remnant, see the above table. For more information on magic powers and their effects, see intelligent undead.

## List of powers

|  |  |  |
|----|----|----|
| Icon | Power | Flavor text |
|  | **Ice Bolt** | *This item shimmers with frost.* |
|  | **Propel Away** | *Air swirls around this item.* |
|  | **Pain** | *This item feels sinister.* |
|  | **Paralysis** | *This item feels strangely still.* |
|  | **Blisters** | *This item feels prickly.* |
|  | **Sicken** | *This item is unsettling.* |
|  | **Bleeding** | N/A |
|  | **Blind** | *This item is difficult to look at.* |
|  | **Rot** | *This item smells foul.* |
|  | **Dizziness** | *This item seems to spin in place.* |
|  | **Suffocate** | *This item whistles quietly.* |

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

A world can generate where sweet dreams are made of these. Adventurers might have to travel the world and several seas, as everybody (or at least the clergy) is looking for something.

A Chosen undead can gather fire-based remnants to prevent the Age of Death.

    Script

    mythical_remnant_adjectives
    =
    {

    "primordial"
    ,

    "elder"
    ,

    "cosmic"
    ,

    "primal"
    ,

    "elemental"
    ,

    "primeval"

    }

    mythical_remnant_spheres
    =
    {}

    mythical_remnant_spheres
    .
    MOUNTAINS
    =
    {

    name
    =
    "stone"
    ,

    color
    =
    "4:0:1"
    ,

    state_color
    =
    "GRAY"

    }

    mythical_remnant_spheres
    .
    MINERALS
    =
    mythical_remnant_spheres
    .
    MOUNTAINS

    mythical_remnant_spheres
    .
    CAVERNS
    =
    mythical_remnant_spheres
    .
    MOUNTAINS

    mythical_remnant_spheres
    .
    EARTH
    =
    mythical_remnant_spheres
    .
    MOUNTAINS

    mythical_remnant_spheres
    .
    JEWELS
    =
    {

    name
    =
    "crystal"
    ,

    color
    =
    "7:0:1"
    ,

    state_color
    =
    "WHITE"

    }

    mythical_remnant_spheres
    .
    CHAOS
    =
    {

    name
    =
    "chaos"
    ,

    color
    =
    "4:0:1"
    ,

    state_color
    =
    "RED"

    }

    mythical_remnant_spheres
    .
    DARKNESS
    =
    {

    name
    =
    "darkness"
    ,

    color
    =
    "0:0:1"
    ,

    state_color
    =
    "BLACK"

    }

    mythical_remnant_spheres
    .
    DEATH
    =
    mythical_remnant_spheres
    .
    DARKNESS

    mythical_remnant_spheres
    .
    NIGHTMARES
    =
    mythical_remnant_spheres
    .
    DARKNESS

    mythical_remnant_spheres
    .
    DREAMS
    =
    {

    name
    =
    "dreamstuff"
    ,

    color
    =
    "2:0:1"
    ,

    state_color
    =
    "GREEN"

    }

    mythical_remnant_spheres
    .
    FIRE
    =
    {

    name
    =
    "fire"
    ,

    color
    =
    "4:0:1"
    ,

    state_color
    =
    "RED"

    }

    mythical_remnant_spheres
    .
    LIGHT
    =
    {

    name
    =
    "light"
    ,

    color
    =
    "6:0:1"
    ,

    state_color
    =
    "YELLOW"

    }

    mythical_remnant_spheres
    .
    LIGHTNING
    =
    {

    name
    =
    "lightning"
    ,

    color
    =
    "6:0:1"
    ,

    state_color
    =
    "YELLOW"

    }

    mythical_remnant_spheres
    .
    METALS
    =
    {

    name
    =
    "metal"
    ,

    color
    =
    "7:0:1"
    ,

    state_color
    =
    "SILVER"

    }

    mythical_remnant_spheres
    .
    MOON
    =
    {

    name
    =
    "moonstone"
    ,

    color
    =
    "7:0:1"
    ,

    state_color
    =
    "WHITE"

    }

    mythical_remnant_spheres
    .
    DARKNESS
    =
    {

    name
    =
    "mudstone"
    ,

    color
    =
    "6:0:0"
    ,

    state_color
    =
    "BROWN"

    }

    mythical_remnant_spheres
    .
    OCEANS
    =
    {

    name
    =
    "ice"
    ,

    color
    =
    "1:0:1"
    ,

    state_color
    =
    "BLUE"

    }

    mythical_remnant_spheres
    .
    WATER
    =
    mythical_remnant_spheres
    .
    OCEANS

    mythical_remnant_spheres
    .
    PLANTS
    =
    {

    name
    =
    "leaf"
    ,

    color
    =
    "2:0:1"
    ,

    state_color
    =
    "GREEN"

    }

    mythical_remnant_spheres
    .
    SALT
    =
    {

    name
    =
    "salt"
    ,

    color
    =
    "7:0:1"
    ,

    state_color
    =
    "WHITE"

    }

    mythical_remnant_spheres
    .
    MIST
    =
    {

    name
    =
    "cloudstuff"
    ,

    color
    =
    "7:0:1"
    ,

    state_color
    =
    "WHITE"

    }

    mythical_remnant_spheres
    .
    SKY
    =
    mythical_remnant_spheres
    .
    MIST

    mythical_remnant_spheres
    .
    STORMS
    =
    mythical_remnant_spheres
    .
    MIST

    mythical_remnant_spheres
    .
    WIND
    =
    mythical_remnant_spheres
    .
    MIST

    mythical_remnant_spheres
    .
    STARS
    =
    {

    name
    =
    "stardust"
    ,

    color
    =
    "6:0:1"
    ,

    state_color
    =
    "YELLOW"

    }

    mythical_remnant_spheres
    .
    SUN
    =
    {

    name
    =
    "sunstone"
    ,

    color
    =
    "6:0:1"
    ,

    state_color
    =
    "YELLOW"

    }

    mythical_remnant_spheres
    .
    TREES
    =
    {

    name
    =
    "wood"
    ,

    color
    =
    "6:0:0"
    ,

    state_color
    =
    "BROWN"

    }

    mythical_remnant_spheres
    .
    VOLCANOS
    =
    {

    name
    =
    "obsidian"
    ,

    color
    =
    "4:0:1"
    ,

    state_color
    =
    "RED"

    }

    materials
    .
    mythical_remnant
    .
    default
    =
    function
    (
    sph
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"

    local

    sph_info

    =

    mythical_remnant_spheres
    [
    sph
    ]

    or

    {
    name
    =
    "glitchstuff"
    ,

    color
    =
    "0:0:1"
    ,

    state_color
    =
    "BLACK"
    }

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DISPLAY_COLOR:"
    ..
    sph_info
    .
    color
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BUILD_COLOR:"
    ..
    sph_info
    .
    color
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_COLOR:ALL:"
    ..
    sph_info
    .
    state_color
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME_ADJ:ALL_SOLID:"
    ..
    pick_random
    (
    mythical_remnant_adjectives
    )
    ..
    " "
    ..
    sph_info
    .
    name
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_VALUE:200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SPEC_HEAT:7500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MELTING_POINT:NONE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BOILING_POINT:NONE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEMS_HARD]"

    if
    (
    sph
    ==
    "METALS"
    )

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEMS_METAL]"

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SOLID_DENSITY:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[LIQUID_DENSITY:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MOLAR_MASS:20000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[IMPACT_YIELD:1000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[IMPACT_FRACTURE:2000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[IMPACT_STRAIN_AT_YIELD:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[COMPRESSIVE_YIELD:1000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[COMPRESSIVE_FRACTURE:2000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[COMPRESSIVE_STRAIN_AT_YIELD:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TENSILE_YIELD:1000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TENSILE_FRACTURE:2000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TENSILE_STRAIN_AT_YIELD:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TORSION_YIELD:1000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TORSION_FRACTURE:2000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TORSION_STRAIN_AT_YIELD:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SHEAR_YIELD:1000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SHEAR_FRACTURE:2000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SHEAR_STRAIN_AT_YIELD:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BENDING_YIELD:1000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BENDING_FRACTURE:2000000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BENDING_STRAIN_AT_YIELD:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MAX_EDGE:12000]"

    return

    {
    mat
    =
    lines
    ,
    weight
    =
    1
    }

    end
