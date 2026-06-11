# Cheese

> Fonte: [Cheese](https://dwarffortresswiki.org/index.php/Cheese) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cheese** is a food item made from milk at the farmer's workshop with the cheese making labor. It can be eaten as is or cooked into prepared meals.

A single "Make cheese" job will take a barrel of milk to the workshop and produce several stacks of cheese of size 5 or less - for example, a barrel containing 17 units of milk will produce 3 stacks of 5 cheese and 1 stack of 2 cheese. A container of frozen milk will, obviously, not be made into cheese.

The milk of any milk-producing animal can be converted to cheese. With the exception of dwarven cheese, which is made from dwarven milk, all cheeses are priced at the value of 10☼.

|  |
|----|
| "Cheese" in other / Languages / Dwarven / : / shokmug / Elven / : / fetha / Goblin / : / ursus / Human / : / anig |

Note that while milk in a barrel won't rot, cheese outside a food stockpile will.

|                |       |                    |                  |                  |
|----------------|-------|--------------------|------------------|------------------|
| Name           | Price | Dwarven trade good | Human trade good | Elven trade good |
| Dwarven cheese | 20☼   | No1     | No               | No               |
| Other cheeses  | 10☼   | Yes                | Yes              | No               |

**Cheese pricing and trade information**

1: By default, dwarven milk or cheese is not available on embark or dwarven caravans Bug:1449. See this section for a workaround.

Tilsit cheese. Tastes *exactly* like Tilsit cheese, because that's what it is.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
You are likely acquainted with the dwarven fondness for cheese, but did you know that a dwarf actually invented cheese? She was trying to ferment milk and turn it into a new kind of alcohol, and was quite surprised when she ended up with something else entirely. That's why the dwarven word for cheese is 'shokmug.' She was **sho**c**k**ed that it couldn't be drunk from a **mug**. Meanwhile, the goblin word for cheese is 'ursus', which is a whole new can of worms.

Some humans have divined a positive correlation between possessing an enormous amount of cheese and enormous amount of friends.

Rarely, a migrant may appear with a dream of creating a masterwork wheel of cheese. This is presumably a bug, as cheese currently lacks quality levels. Since an eternally unfulfilled goal may make the dwarf moody and prone to tantrums, the best solution to the problem is to arrange them an audience with royalty.

    [MATERIAL_TEMPLATE:CREATURE_CHEESE_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:YELLOW]
        [STATE_NAME:ALL_SOLID:cheese]
        [STATE_ADJ:ALL_SOLID:cheesy]
        [STATE_COLOR:LIQUID:YELLOW]
        [STATE_NAME:LIQUID:melted cheese]
        [STATE_ADJ:LIQUID:melted cheesy]
        [STATE_COLOR:GAS:YELLOW]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:4:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10338]
        [MELTING_POINT:10078]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:1200]
        [LIQUID_DENSITY:1200]
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
        [SHEAR_YIELD:10000] no data
        [SHEAR_FRACTURE:10000]
        [SHEAR_STRAIN_AT_YIELD:50000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:50000]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [REACTION_CLASS:CHEESE]
        [CHEESE_CREATURE]
        [EDIBLE_VERMIN]
        [EDIBLE_RAW]
        [EDIBLE_COOKED]
        [ROTS]
        [GENERATES_MIASMA]
