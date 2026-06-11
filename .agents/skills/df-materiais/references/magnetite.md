# Magnetite

> Fonte: [Magnetite](https://dwarffortresswiki.org/index.php/Magnetite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of iron (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in sedimentary layers as large clusters Found in metamorphic layers as small clusters Found in igneous intrusive layers as small clusters Found in igneous extrusive layers as small clusters**
- **Properties**
- **Material value 8☼ Fire-safe Magma-safe Melting point 12768 °U ( m ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 5046 kg/m³ Specific heat 800 J/kg·K Color gray**
- **Fire-safe:** Magma-safe
- **Contains**
- **Native platinum (veins)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Magnetite** is an ore of iron a mid-value metal useful for weapons and armor. , It appears as large, oval-shaped clusters inside sedimentary layers and small clusters in metamorphic layers and igneous layers. A magnetite cluster may sometimes contain veins of native platinum, which can continue outside of the cluster itself.

In terms of metalsmithing, magnetite is identical to hematite and limonite, producing four iron bars when smelted at a smelter. However, magnetite is distinguished by the extreme size of each deposit compared to the other iron ores, for sedimentary clusters anyway. While a vein might hold 100 tiles of ore, a cluster can contain around 750 -- this is offset somewhat by the 25% lower chance for a mined tile to drop an ore boulder, compared to vein stone, but the typical yield of the entire large cluster is still much higher.

## In the real world

Magnetite is the most magnetic of all the naturally occurring minerals. It is often found in the form of black sand.

Magnetite.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Magnetite is silvery in color, not red with black specks. It also does not generate more frequently in glaciers or the fourth layer of the caverns.

    [INORGANIC:MAGNETITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:magnetite][DISPLAY_COLOR:0:7:1][TILE:'~']
    [ENVIRONMENT:SEDIMENTARY:CLUSTER:100]
    [ENVIRONMENT:METAMORPHIC:CLUSTER_SMALL:100]
    [ENVIRONMENT:IGNEOUS_INTRUSIVE:CLUSTER_SMALL:100]
    [ENVIRONMENT:IGNEOUS_EXTRUSIVE:CLUSTER_SMALL:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:IRON:100]
    [SOLID_DENSITY:5046]
    [MATERIAL_VALUE:8]
    [IS_STONE]
    [MELTING_POINT:12768]
    [STATE_COLOR:ALL_SOLID:GRAY]
