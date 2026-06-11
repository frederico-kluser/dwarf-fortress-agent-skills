# Iron

> Fonte: [Iron](https://dwarffortresswiki.org/index.php/Iron) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Make pig iron at smelter Make steel at smelter Melee Weapons Crossbows Bolts Picks Armor Anvils Metal crafting Construction**
- **Ore**
- **Hematite Limonite Magnetite**
- **Properties**
- **Material value 10☼ Impact strength 1085 MPa Shear strength 310 MPa Fire-safe Magma-safe Melting point 12768 °U Boiling point 15150 °U Ignition point none Solid density 7850 kg/m³ Liquid density 6980 kg/m³ Specific heat 450 J/kg·K Color gray**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Iron** is an important resource, needed for steel, the best mundane metal for weapons and armor, and if steel availability is limited, iron is next best, though only slightly better than bronze. Iron is also a fire and magma-safe material that can be used to make most anything.

Three ores contain iron: hematite, magnetite, and limonite.

Iron does not rust in game, so there's no harm in leaving iron objects out in the rain or submerging them in water.

## Uses

- Melee weapons. Mostly useful for edged weapons; good for bolts as well. You can also make crossbows out of iron, but there are better metals.
- Armor. It's pretty good, though not the best.
- Construction, if you are so inclined.
- Good-quality furniture. It is quite heavy, however.
- Magma-safe mechanisms, though there are plenty of magma-safe stones that would work just as well, if you can get your hands on them.
- Anvils, which can only be made from iron or steel.

## Production

Iron comes from three ores: hematite (veins in sedimentary, small clusters in all other stone layers), magnetite (large clusters in sedimentary, small clusters in all other stone layers), and limonite (veins in sedimentary only). Any of these iron ores can be smelted at a smelter to produce four iron bars. If you have a standard smelter, a bar of fuel will be necessary; magma smelters require no fuel to operate (though steel still needs it as a carbon source).

Iron will also be available through goblinite, as well as the dwarven and human caravans.

## Alloys

Iron may be combined with other materials at a smelter, mostly for the production of steel

- Iron + Flux + Fuel = Pig iron
- Iron + Pig iron + Flux + Fuel = 2 × Steel

Note that fuel is used as a reactant: even magma smelters need fuel for these reactions. A standard smelter will require two bars of fuel, one as a reactant and one to operate the furnace. This conforms with the process of carbonization of iron and pig iron in ferrous metallurgy in real life.

Pieces of iron.

|  |
|----|
| "Iron" in other / Languages / Dwarven / : / datan / Elven / : / icori / Goblin / : / dusna / Human / : / uzin |

    Dwarfoloid picked out a lot of the material numbers here to replace my placeholders.
    Colors added by Bohandas.

    [INORGANIC:IRON]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:iron]
        [STATE_NAME_ADJ:LIQUID:molten iron]
        [STATE_NAME_ADJ:GAS:boiling iron]
        [DISPLAY_COLOR:0:7:1]
        [BUILD_COLOR:0:7:1]
        [MATERIAL_VALUE:10]
        [SPEC_HEAT:450]
        [MELTING_POINT:12768]
        [BOILING_POINT:15150]
        [ITEMS_WEAPON][ITEMS_WEAPON_RANGED][ITEMS_AMMO][ITEMS_DIGGER][ITEMS_ARMOR][ITEMS_ANVIL]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [SOLID_DENSITY:7850]
        [LIQUID_DENSITY:6980]
        [MOLAR_MASS:55845]
        [IMPACT_YIELD:542500] Was 1080000, but just using 3.5x tensile multiples for everything until better numbers are available, which might not be likely
        [IMPACT_FRACTURE:1085000]
        [IMPACT_STRAIN_AT_YIELD:319]
        [COMPRESSIVE_YIELD:542500]
        [COMPRESSIVE_FRACTURE:1085000]
        [COMPRESSIVE_STRAIN_AT_YIELD:319] bulk modulus 170 GPa
        [TENSILE_YIELD:155000]
        [TENSILE_FRACTURE:310000]
        [TENSILE_STRAIN_AT_YIELD:73] young's modulus 211 GPa
        [TORSION_YIELD:155000]
        [TORSION_FRACTURE:310000]
        [TORSION_STRAIN_AT_YIELD:189]
        [SHEAR_YIELD:155000]
        [SHEAR_FRACTURE:310000]
        [SHEAR_STRAIN_AT_YIELD:189] shear modulus 82 GPa
        [BENDING_YIELD:155000]
        [BENDING_FRACTURE:310000]
        [BENDING_STRAIN_AT_YIELD:73]
        [MAX_EDGE:10000]
        [STATE_COLOR:ALL_SOLID:GRAY]
