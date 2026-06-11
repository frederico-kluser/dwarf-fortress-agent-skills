# Leather

> Fonte: [Leather](https://dwarffortresswiki.org/index.php/Leather) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Construction**
- **Used for**
- **Leatherworking**
- **Base value:** Size
- **5☼:** 5,000 cm³
- **Browse other items**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Leather** is the tanned hide of an animal, and is a fairly versatile material. Leather can be used to make bags, quivers, backpacks, waterskins, clothing, shields, armor, and decorations, all at a leather works. Leather crafts are made at a craftsdwarf's workshop.

Although most of these items can be made from other materials, it is the only sensible option for making quivers and backpacks (the only alternative being adamantine), meaning some source of leather is practically essential for a well-rounded military.

Plenty of leather can usually be acquired through trade with dwarves and humans. Raw hides can be acquired by hunting or by butchering domesticated animals, and these can then be turned to leather at a tannery. Smaller animals will never produce a hide, so you will never, for example, have kea or rat leather. The raw hide of larger animals can produce more than 1 item of usable leather; this seems to start with animals about the size of an adult mule (size ~150,000 cm3).

|                                   |                   |
|-----------------------------------|-------------------|
| Leather items per raw hide |                   |
| Animal                            | Leather per adult |
| Rabbit                            | 0                 |
| Dog                               | 1                 |
| Cat                               | 1                 |
| Sheep                             | 1                 |
| Pig                               | 1                 |
| Goat                              | 1                 |
| Llama                             | 1                 |
| Alpaca                            | 1                 |
| Donkey                            | 1                 |
| Reindeer                          | 1                 |
| Mule                              | 2                 |
| Horse                             | 2                 |
| Cow                               | 2                 |
| Yak                               | 2                 |
| Water buffalo                     | 2-3               |

Small amounts of leather can also be found near groups of cavern-dwelling animal people. Obtaining leather this way is rather dangerous, as these creatures are generally hostile to dwarves and are often armed with blowguns shooting lethally poisonous blowdarts.\[Verify\]

\

## Leather industry

Different types of leather in different colors.

Because it only overlaps in the use of end products, the *leather industry* is part of the meat industry, not the clothing industry.

Making leather requires a tanner's shop, a raw hide or skin from an animal, and a dwarf with the tanning labor turned on - rotten hides or skin cannot be tanned. The human and dwarven caravans usually sell various boxes of leather, which can be useful if few butcherable animals inhabit the map. Each butchering job yields a single hide, and each unrotten hide yields one or more units of usable leather depending how large the creature was. The value of the leather depends on the critter it comes from; leather made from the skins of rare or dangerous animals can be quite valuable. Tanners can turn a skin from a severed part of an animal into the full-size leather.

Dwarven tanners have a skill unknown to mere humans, such that they can make the softest skin of the tiniest animal as equally hardy as that of the most heavily protected live creature. Whether they make flimsy skin into a rock-like substance, or tough hide silky and supple, remains a mystery.

Dwarves will not claim and wear clothes made from the leather of sentient creatures as part of their civilian attire. This taboo may be caused by dwarven ethics, which forbid the butchering of sentient creatures. Craftsdwarves will fashion the leather of such creatures into clothing and such clothes will be collected and traded normally. Dwarves will wear clothes made of the leather of sentients if ordered to do so as part of a military uniform.

## Leather armor

Leather armor is made in a leather works, and requires one unit of any leather. Leather is significantly lighter than other forms of armor, and thus is less likely to cause encumbrance penalties, but also provides less protection. It is weak against blunt damage – since it is so flexible, it doesn't absorb much force. The source animal of the leather (e.g. "dog leather" or "roc leather") does not alter the weight or protection of the armor, though the item quality likely does. Leather armor is useful for hunters since they can move fast to keep up with their quarry.

Leather shields are extremely light and are just as protective as wooden or metal shields, thus useful for keeping your forces mobile.

## See also

- Meat industry
- Armor

\

    [MATERIAL_TEMPLATE:LEATHER_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:BROWN]
        [STATE_NAME:ALL_SOLID:leather]
        [STATE_ADJ:ALL_SOLID:leather]
        [STATE_COLOR:LIQUID:BROWN]
        [STATE_NAME:LIQUID:n/a]
        [STATE_ADJ:LIQUID:n/a]
        [STATE_COLOR:GAS:BROWN]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:6:0:0]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:420]
        [IGNITE_POINT:10508]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:50000]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:50000]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:50000]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:50000]
        [SHEAR_YIELD:25000] -- was 15 to 37 MPa in animal byproducts net pdf
        [SHEAR_FRACTURE:25000]
        [SHEAR_STRAIN_AT_YIELD:50000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:50000]
        [MAX_EDGE:0]
        [ABSORPTION:40]
        [IMPLIES_ANIMAL_KILL]
        [LEATHER]
        [ITEMS_LEATHER]
