# Inorganic material definition token

> Fonte: [Inorganic material definition token](https://dwarffortresswiki.org/index.php/Inorganic_material_definition_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

The following tokens can be used in inorganic material definitions, generally for stones, gems, and metals, but *not* with materials attached to plants or creatures.

Inorganic material raw files are named `inorganic_.txt`, and start with their filename, then the `[OBJECT:INORGANIC]` token. Following the header, each new inorganic material definition begins with the `[INORGANIC:]` token, where is a unique identifier for the material; and that material's properties are then defined using the tokens listed below, in addition to the tokens listed under Material definition token.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  WAFERS |  | Used on metals, causes the metal to be made into wafers instead of bars. |
|  DEEP_SPECIAL |  | Causes the stone to form hollow tubes leading to the Underworld. Used for raw adamantine. When mined, stone has a 100% yield. If no material with this token exists, hollow veins will instead be made of the first available inorganic, usually iron. Implies [`[SPECIAL]`](/index.php/Inorganic_material_definition_token#SPECIAL "Inorganic material definition token"). |
|  METAL_ORE | metal:chance | Allows the ore to be smelted into metal in the smelter. Each token with a non-zero chance causes the game to roll d100 four times, each time creating one bar of the type requested on success. |
|  THREAD_METAL | metal:chance | Allows strands to be extracted from the metal at a craftsdwarf's workshop. |
|  DEEP_SURFACE |  | Causes the stone to line the landscape of the Underworld. Used for slade. When mined (if it's mineable), stone has a 100% yield. If no material with this token exists, other materials will be used in place of slade. Underworld spires will still be referred to as a "spire of slade" in the world's history. |
|  AQUIFER |  | Allows the stone to support an aquifer. |
|  METAMORPHIC |  | Causes the material to form metamorphic layers. |
|  SEDIMENTARY |  | Causes the material to form sedimentary layers. |
|  SOIL |  | Causes the material to form soil layers, allowing it to appear in (almost) any biome. Mining is faster and produces no stones. |
|  SOIL_OCEAN |  | Causes the material to form pelagic sediment layers beneath deep oceans. Mining is faster and produces no stones. |
|  SOIL_SAND |  | Causes the material to form sand layers, allowing it to appear in sand deserts and shallow oceans. Mining is faster and produces no stones. Sand layers can also be used for making glass. Can be combined with \[SOIL\]. |
|  SEDIMENTARY_OCEAN_SHALLOW |  | Permits an already \[SEDIMENTARY\] stone layer to appear underneath shallow ocean regions. |
|  SEDIMENTARY_OCEAN_DEEP |  | Permits an already \[SEDIMENTARY\] stone layer to appear underneath deep ocean regions. |
|  IGNEOUS_INTRUSIVE |  | Causes the material to form igneous intrusive layers. |
|  IGNEOUS_EXTRUSIVE |  | Causes the material to form igneous extrusive layers. |
|  ENVIRONMENT | class:type:freq | Specifies what types of layers will contain this mineral. Multiple instances of the same token segment will cause the rock type to occur more frequently, but won't increase its abundance in the specified environment. See below. |
|  ENVIRONMENT_SPEC | stone:type:freq | Specifies which specific minerals will contain this mineral. See below. |
|  LAVA |  | Specifies that the stone is created when combining water and magma, also causing it to line the edges of magma pools and volcanoes. If multiple minerals are marked as lava stones, a different one will be used in each biome or geological region. |
|  SPECIAL |  | Prevents the material from showing up in certain places. AI-controlled entities won't use the material to make items and don't bring it in caravans, though the player can use it as normal. Also, inorganic generated creatures (forgotten beasts, titans, demons) will never be composed of this material. Explicitly set by all evil weather materials and implied by [`[DEEP_SURFACE]`](/index.php/Inorganic_material_definition_token#DEEP_SURFACE "Inorganic material definition token") and [`[DEEP_SPECIAL]`](/index.php/Inorganic_material_definition_token#DEEP_SPECIAL "Inorganic material definition token"). |
|  GENERATED |  | Indicates that this is a generated material. Cannot be specified in user-defined raws. |
|  DIVINE |  | Found on random-generated metals and cloth. Marks this material as usable by Deity-created generated entities. |
|  SPHERE | sphere | Found on divine materials. Presumably links the material to a god of the same sphere. |
|  MYTHICALv51.01-beta26 |  | Implied by [`[MYTHICAL_REMNANT]`](/index.php/Inorganic_material_definition_token#MYTHICAL_REMNANT "Inorganic material definition token") and [`[MYTHICAL_SUBSTANCE]`](/index.php/Inorganic_material_definition_token#MYTHICAL_SUBSTANCE "Inorganic material definition token"), all usable in written raws. |
|  MYTHICAL_REMNANTv51.01-beta26 |  | Found on primordial remnants. |
|  MYTHICAL_SUBSTANCEv51.01-beta26 |  | Found on mythical substances. If a creature has a liquid or a glob of this in their inventory, they will consume it in the `COMBAT` (aka `DEFEND`) and `FLEEING`contexts after suffering a major injury. |

## ENVIRONMENT and ENVIRONMENT_SPEC

Format:

- \[ENVIRONMENT:::\]

Possible values for class:

|  |  |
|----|----|
| Environment class token | Description |
|  ALL_STONE | Will appear in every stone. |
|  IGNEOUS_ALL,  IGNEOUS_INTRUSIVE,  IGNEOUS_EXTRUSIVE | Will appear in igneous layers, either igneous intrusive, igneous extrusive, or both. |
|  SOIL,  SOIL_OCEAN,  SOIL_SAND | Will appear in soil. SOIL_OCEAN is oceans specifically and SOIL_SAND is sand specifically. |
|  METAMORPHIC | Will appear in metamorphic layers. |
|  SEDIMENTARY | Will appear in sedimentary layers. |
|  ALLUVIAL | Will appear in alluvial layers. |

Possible values for inclusion type:

|  |  |
|----|----|
| Inclusion type token | Description |
|  CLUSTER | Large ovoids that occupy their entire 48x48 embark tile. Microcline is an example. When mined, stone has a 25% yield (as with layer stones). |
|  CLUSTER_SMALL | Blobs of 3-9 tiles. Will always be successfully mined. Red pyropes are an example. When mined, stone has a 100% yield. |
|  CLUSTER_ONE | Single tiles. Will always be successfully mined. Clear diamonds are an example. When mined, stone has a 100% yield. |
|  VEIN | Large streaks of stone. Native gold is an example. When mined, stone has a 33% yield instead of the usual 25%. |

An inclusion may be contained within a larger inclusion. For example, diamond small clusters are found within kimberlite veins.

The frequency number varies from 1 to 100 and determines the relative frequency at which the stone will be chosen to appear - if all frequency values are the same, then all stones will be equally likely to appear.

\
ENVIRONMENT_SPEC follows much the same format, but takes a specific stone material ID where ENVIRONMENT would take a class token. What you can use will depend on what inorganic raws are around.

## See also

- Material definition token
