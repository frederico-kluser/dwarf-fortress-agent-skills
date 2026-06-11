# Native platinum

> Fonte: [Native platinum](https://dwarffortresswiki.org/index.php/Native_platinum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of platinum (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in alluvial layers as small clusters Found within olivine as veins Found within magnetite as veins Found within chromite as small clusters**
- **Properties**
- **Material value 40☼ Fire-safe Magma-safe Melting point 13182 °U ( m ) Boiling point 16885 °U ( m ) Ignition point none ( m ) Solid density 21400 kg/m³ Specific heat 130 J/kg·K Color silver**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Native platinum** is the only ore of platinum, one of the most valuable metals available (equal in value to aluminum). Its high material value makes both the ore and the smelted metal a convenient material for high-value furniture for nobles. If the deposits are not mined out, smoothed and engraved platinum walls can add a lot of value to rooms, too.

Native platinum can occur in veins inside bodies of magnetite and olivine and as small clusters within chromite. The veins from magnetite specifically can extend far outside the magnetite they originate from and the vein may even be interrupted at the magnetite cluster border.

When mined, chunks of native platinum are called *platinum nuggets*.

### In Real Life

Native platinum is technically not an ore; it's simply chunks of mostly pure metallic platinum. As platinum is an extremely unreactive metal, even less reactive than gold, this is by far the most common form in which platinum is found in nature.

A 112g (3.6 oz) platinum nugget.

    [INORGANIC:NATIVE_PLATINUM]
    [STONE_NAME:platinum nuggets]
    [ENVIRONMENT:ALLUVIAL:CLUSTER_SMALL:100]
    [ENVIRONMENT_SPEC:OLIVINE:VEIN:100]
    [ENVIRONMENT_SPEC:MAGNETITE:VEIN:100]
    [ENVIRONMENT_SPEC:CHROMITE:CLUSTER_SMALL:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:PLATINUM:100]
    [STATE_NAME_ADJ:ALL_SOLID:native platinum]
    [STATE_NAME_ADJ:LIQUID:molten native platinum]
    [STATE_NAME_ADJ:GAS:boiling native platinum]
    [DISPLAY_COLOR:7:7:1]
    [TILE:156]
    [MATERIAL_VALUE:40]
    [SPEC_HEAT:130]
    [MELTING_POINT:13182]
    [BOILING_POINT:16885]
    [SOLID_DENSITY:21400]
    [LIQUID_DENSITY:19770]
    [MOLAR_MASS:195084]
    used stone template values for mining speed until there's more information about how native metal is mined
        [IMPACT_YIELD:120000]
        [IMPACT_FRACTURE:120000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:120000]
        [COMPRESSIVE_FRACTURE:120000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:15000]
        [TENSILE_FRACTURE:15000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:15000]
        [TORSION_FRACTURE:15000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:15000] used marble
        [SHEAR_FRACTURE:15000]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:15000]
        [BENDING_FRACTURE:15000]
        [BENDING_STRAIN_AT_YIELD:100]
    [MAX_EDGE:1000] no swords until you can pick mats
    [ITEMS_HARD]
    [IS_STONE]
    [STATE_COLOR:ALL_SOLID:SILVER]
