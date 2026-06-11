# Tetrahedrite

> Fonte: [Tetrahedrite](https://dwarffortresswiki.org/index.php/Tetrahedrite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Ore of copper (100%) Ore of silver (20%) Masonry Stone crafting Construction**
- **Location**
- **Found in stone layers as veins**
- **Properties**
- **Material value 3☼ Fire-safe Not magma-safe Melting point 11111 °U ( x ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 4900 kg/m³ Specific heat 800 J/kg·K Color silver**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Tetrahedrite** is an incredibly common ore of both copper and silver. Smelting tetrahedrite will produce 4 copper bars and 0-4 silver bars\*. On average, each nugget of tetrahedrite will produce less than one bar of silver when smelted.

\* There is a separate 20% chance for each of the 4 silver bars being produced. This works out to be an average of 0.8 silver bars each time a unit of tetrahedrite is smelted, with "no bars" or "1 bar" being equally common (40.96% of the time), 2 bars not uncommon (15.36% of the time), and 3 or 4 uncommon but not impossible (2.56% and 0.16%, respectively).

Tetrahedrite can also be used in alloy reactions requiring either a copper-bearing ore or a silver-bearing ore, but will only be used as a *silver* ore if no other silver ores are available. Two tetrahedrite nuggets can be smelted together as a copper-bearing ore and a silver-bearing ore to make eight billon bars for a roughly 70% increase in value compared to smelting the nuggets independently.

When using tetrahedrite as a copper-bearing ore, it's often best to smelt it into bars first and then use those copper bars to create the alloy. This allows you to produce some silver bars in addition to the bars of alloy, but does require additional fuel and time. A clear exception to this is when producing billon from two tetrahedrite nuggets, when the benefits of using tetrahedrite as a silver-bearing ore outweigh the drawbacks of using tetrahedrite as a copper-bearing ore.

Tetrahedrite crystals with chalcopyrite and sphalerite crystals (size: 8.2 × 6.4 × 4.7 cm)

## Understanding the value chain

A single tetrahedrite boulder (seen in-game as simply "tetrahedrite", laying on the floor as a byproduct of mining) has a value of 9 (3 for being a stone boulder, times 3 for it being tetrahedrite).

This boulder can be smelted into 4 bars of copper, each having a value of 10 (5 for being bars, times 2 for them being made of copper), for a total of 40, and a random amount of 0 to 4 bars of silver (mean being 0.8), each having a value of 50 (5 for being bars, times 10 for them being made of silver). So each single tetrahedrite boulder gives you a (mean) value of 80 in copper and silver bars. If you smelt two of them into billon instead, this yields 8 billon bars worth 30 each (5 for being bars, 6 for being made of billon), for a total of 240 value, i.e. 120 per boulder.

Each bar can be then forged into items, like a battle axe. A copper battle axe will have a value of 20 (10 for being a battle axe, times 2 for being made of copper), thus the original tetrahedrite boulder will yield a total value of 160 (80 from the 4 copper battle axes, plus 80 as a mean of the possible silver battle axes, each worth 100). This can be multiplied up to 2× since battle axes have quality levels.

    [INORGANIC:TETRAHEDRITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:tetrahedrite][DISPLAY_COLOR:0:7:1][TILE:156]
    [ENVIRONMENT:ALL_STONE:VEIN:100]
    [ITEM_SYMBOL:'*']
    [METAL_ORE:COPPER:100]
    [METAL_ORE:SILVER:20]
    [MATERIAL_VALUE:3]
    [IS_STONE]
    [MELTING_POINT:11111]
    [SOLID_DENSITY:4900]
    [STATE_COLOR:ALL_SOLID:SILVER]
