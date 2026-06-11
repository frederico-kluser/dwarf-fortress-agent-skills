# Glass

> Fonte: [Glass](https://dwarffortresswiki.org/index.php/Glass) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Glass** is produced at the glass furnace using fuel with either sand (green glass), sand and pearlash (clear glass), or rock crystal and pearlash (crystal glass). A magma glass furnace can also be used, in which case no fuel is required. Raw glass (of all three types) can also be acquired from some trade caravans and be purchased in the embark screen. You have to buy or collect sand to get the raw materials to make glass.

Glass value corresponds to the difficulty of its production, with green glass having the lowest material value (2), clear glass, intermediate (5), and crystal glass, the highest (10).

## Uses

Glass can be used for most things that can be produced at a Stoneworker's workshop, except slabs, querns and millstones. Glass can also be used to make tubes. Note that the names for some glass products are different from the same products made from different materials. For example, a glass tube has the same uses as a wooden pipe. It can also be used to produce goods normally made at a craftsdwarf's workshop by a stone crafter, except obsidian short swords and generic crafts. In addition, it may be made as raw glass, which can then be cut as a gem at a jeweler's workshop by a gem cutter, similarly to cutting generic stones. Note that raw glass ***cannot*** be made into glass items (excluding strange moods), but can only be cut into gem-like items which can be used for decorating items.

Raw glass, especially raw green glass, is excellent practice for aspiring jewelers (and its production provides experience for glassmakers). The value of glass is on par with low-to-mid value gemstones, meaning that a source of sand on your map used in tandem with a magma glass furnace makes decoration with cut raw green glass an essentially free, and very lucrative, way to increase the value of your goods, while training legendary glassmakers and jewelers – particularly when those goods are themselves made of glass.

Glass can also be made into blocks which can be used to build workshops and constructions, even glass trap components. Creatures cannot see through floors or walls made from glass blocks, even though the graphics are transparent. Unique goods made from glass include glass windows and vials, as well as renamed versions of common furniture.

- A glass chest is called a box.
- A glass door is called a portal.
- A glass pipe is called a tube.
- A glass cage is called a terrarium.
- A glass flask is called a vial.

For more information on the use of glass, see the Glass industry page.

Raw and cut glass storage options can be found under the Gem stockpile sub-menu. Glass blocks are stored in Bar/Block stockpiles.

## Glass Block Floors, AKA The Dwarven X-Ray

In DF Premium's graphical mode, floors made out of glass blocks reveal the z-level directly beneath them and everything on those tiles in real time, even if built on top of a solid cave floor. This exploit can be useful when you want to avoid digging into Hidden Fun Stuff, because even though players can see through glass floors no matter what, entities in the game itself never can.[1]

## Glass and magma

Glass behaves somewhat oddly with magma, despite being strictly magma-safe (with a melting point of 13600 °U ) – **built** glass furniture will survive indefinitely when covered with magma, but **unbuilt** glass items tend to disappear instantly when submerged in magma.Bug:10314

## Physical properties

Through memory hacking, the material properties of each type of glass have been determined; for reference, they have been reconstructed below as material definitions:

    Green glass

    [MATERIAL:GLASS_GREEN] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL_SOLID:DARK_GREEN]
        [STATE_NAME_ADJ:SOLID:green glass]
        [STATE_COLOR:LIQUID:RED]
        [STATE_NAME_ADJ:LIQUID:molten green glass]
        [STATE_COLOR:GAS:RED]
        [STATE_NAME_ADJ:GAS:boiling green glass]
        [STATE_NAME_ADJ:SOLID_POWDER:ground green glass]
        [STATE_NAME_ADJ:SOLID_PASTE:green glass paste]
        [STATE_NAME_ADJ:SOLID_PRESSED:pressed green glass]
        [BASIC_COLOR:2:0]
        [BUILD_COLOR:2:0:0]
        [TILE_COLOR:7:7:1]
        [MATERIAL_VALUE:2]
        [SPEC_HEAT:700]
        [MELTING_POINT:13600]
        [BOILING_POINT:16000]
        [SOLID_DENSITY:2600]
        [LIQUID_DENSITY:2240]
        [BENDING_YIELD:33000]
        [BENDING_FRACTURE:33000]
        [BENDING_STRAIN_AT_YIELD:47]
        [SHEAR_YIELD:33000]
        [SHEAR_FRACTURE:33000]
        [SHEAR_STRAIN_AT_YIELD:113]
        [TORSION_YIELD:33000]
        [TORSION_FRACTURE:33000]
        [TORSION_STRAIN_AT_YIELD:113]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:1000000]
        [IMPACT_STRAIN_AT_YIELD:2222]
        [TENSILE_YIELD:33000]
        [TENSILE_FRACTURE:33000]
        [TENSILE_STRAIN_AT_YIELD:47]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:1000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:2222]
        [MAX_EDGE:15000]
        [ITEMS_HARD]
        [IS_GLASS]

    Clear glass

    [MATERIAL:GLASS_CLEAR] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL_SOLID:CLEAR]
        [STATE_NAME_ADJ:SOLID:clear glass]
        [STATE_COLOR:LIQUID:RED]
        [STATE_NAME_ADJ:LIQUID:molten clear glass]
        [STATE_COLOR:GAS:RED]
        [STATE_NAME_ADJ:GAS:boiling clear glass]
        [STATE_NAME_ADJ:SOLID_POWDER:ground clear glass]
        [STATE_NAME_ADJ:SOLID_PASTE:clear glass paste]
        [STATE_NAME_ADJ:SOLID_PRESSED:pressed clear glass]
        [BASIC_COLOR:3:0]
        [BUILD_COLOR:3:0:0]
        [TILE_COLOR:7:7:1]
        [MATERIAL_VALUE:5]
        [SPEC_HEAT:700]
        [MELTING_POINT:13600]
        [BOILING_POINT:16000]
        [SOLID_DENSITY:2600]
        [LIQUID_DENSITY:2240]
        [BENDING_YIELD:33000]
        [BENDING_FRACTURE:33000]
        [BENDING_STRAIN_AT_YIELD:47]
        [SHEAR_YIELD:33000]
        [SHEAR_FRACTURE:33000]
        [SHEAR_STRAIN_AT_YIELD:113]
        [TORSION_YIELD:33000]
        [TORSION_FRACTURE:33000]
        [TORSION_STRAIN_AT_YIELD:113]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:1000000]
        [IMPACT_STRAIN_AT_YIELD:2222]
        [TENSILE_YIELD:33000]
        [TENSILE_FRACTURE:33000]
        [TENSILE_STRAIN_AT_YIELD:47]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:1000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:2222]
        [MAX_EDGE:15000]
        [ITEMS_HARD]
        [IS_GLASS]

    Crystal glass

    [MATERIAL:GLASS_CRYSTAL] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL_SOLID:CLEAR]
        [STATE_NAME_ADJ:SOLID:crystal glass]
        [STATE_COLOR:LIQUID:RED]
        [STATE_NAME_ADJ:LIQUID:molten crystal glass]
        [STATE_COLOR:GAS:RED]
        [STATE_NAME_ADJ:GAS:boiling crystal glass]
        [STATE_NAME_ADJ:SOLID_POWDER:ground crystal glass]
        [STATE_NAME_ADJ:SOLID_PASTE:crystal glass paste]
        [STATE_NAME_ADJ:SOLID_PRESSED:pressed crystal glass]
        [BASIC_COLOR:7:1]
        [BUILD_COLOR:7:0:1]
        [TILE_COLOR:7:7:1]
        [MATERIAL_VALUE:10]
        [SPEC_HEAT:700]
        [MELTING_POINT:13600]
        [BOILING_POINT:16000]
        [SOLID_DENSITY:2600]
        [LIQUID_DENSITY:2240]
        [BENDING_YIELD:33000]
        [BENDING_FRACTURE:33000]
        [BENDING_STRAIN_AT_YIELD:47]
        [SHEAR_YIELD:33000]
        [SHEAR_FRACTURE:33000]
        [SHEAR_STRAIN_AT_YIELD:113]
        [TORSION_YIELD:33000]
        [TORSION_FRACTURE:33000]
        [TORSION_STRAIN_AT_YIELD:113]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:1000000]
        [IMPACT_STRAIN_AT_YIELD:2222]
        [TENSILE_YIELD:33000]
        [TENSILE_FRACTURE:33000]
        [TENSILE_STRAIN_AT_YIELD:47]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:1000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:2222]
        [MAX_EDGE:15000]
        [ITEMS_HARD]
        [IS_GLASS]

## See also

- Glass industry
- Glassmaker
