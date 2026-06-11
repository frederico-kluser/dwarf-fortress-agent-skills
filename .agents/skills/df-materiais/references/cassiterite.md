# Cassiterite

> Fonte: [Cassiterite](https://dwarffortresswiki.org/index.php/Cassiterite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of tin (100%) Masonry Stone crafting Construction**
- **Location**
- **Found in alluvial layers as small clusters Found within granite as veins**
- **Properties**
- **Material value 2☼ Fire-safe Magma-safe Melting point 12025 °U ( m ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 6900 kg/m³ Specific heat 800 J/kg·K Color gray**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cassiterite** is the only ore of tin. This ore can also be smelted into the alloys bronze, trifle pewter, and fine pewter.

Cassiterite is also the main component of tin glaze.

It is found in alluvial layers as small clusters and in granite as veins.

## Smelting

Cassiterite is a required ingredient to make several types of metal alloy bars from ore at a smelter:

- Tin bars
- Bronze bars - with native copper, malachite, or tetrahedrite
- Trifle pewter bars - with native copper, malachite or tetrahedrite *(takes 2 cassiterite)*
- Fine pewter bars - with native copper, malachite or tetrahedrite *(takes 3 cassiterite)*

The above can also be made from bars of tin combined with bars of the appropriate metals. Note that bismuth bronze and lay pewter, both of which require tin, cannot be made directly from cassiterite, but must be made using tin bars.

See metal for a full discussion of formulae and options.

-

  Cassiterite, 3-4 cm

-

  Cassiterite on quartz

-

  Cassiterite on a rock

    [INORGANIC:CASSITERITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:cassiterite][DISPLAY_COLOR:6:7:0][TILE:156]
    [ENVIRONMENT:ALLUVIAL:CLUSTER_SMALL:100]
    [ENVIRONMENT_SPEC:GRANITE:VEIN:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:TIN:100]
    [MATERIAL_VALUE:2]
    [IS_STONE]
    [MELTING_POINT:12025]
    [SOLID_DENSITY:6900]
    [MATERIAL_REACTION_PRODUCT:GLAZE_MAT:INORGANIC:TIN_GLAZE]
    [STATE_COLOR:ALL_SOLID:GRAY]
