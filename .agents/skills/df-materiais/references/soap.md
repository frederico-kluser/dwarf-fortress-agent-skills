# Soap

> Fonte: [Soap](https://dwarffortresswiki.org/index.php/Soap) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Soap** is a particularly useful type of bar used for personal cleaning, which increases happiness ("recently took a soapy bath") and lowers the chances of an infection in case of injury, and for cleaning wounds in hospitals, preventing infections from developing. It is thus a vital commodity in dwarven health care, and one not traded in caravans: you're going to have to make soap yourself.

Soap is stored in Bar/Block stockpiles with the "soap" option enabled.

Unlike most other items, bars of soap have a "durability" level which allows jobs to partially consume them – each bar starts with 150 units, and cleaning jobs consume varying quantities of soap before ultimately using it up.

## Manufacture

Soap is made of two components, lye plus *either* tallow from butchering *or* oil from oil producing plants, and requires a dedicated workshop, the soap maker's workshop. Manufacturing these ingredients from scratch results in a somewhat complicated production process:

- for Lye: Cut down a tree to produce wood logs; turn one log into ash at a wood furnace, then turn that ash into lye at an ashery.
- Tallow *or* Oil: You have 2 options, and either works the same; you can either...
  - a\) for Tallow: Kill an animal, either domestic animal or from hunting, and butcher it at a butcher's shop. Then, render the fat from the butchering into tallow at a kitchen.

  ...*OR*...
  - b\) for Oil: Collect some oil producing plants, either via either gathering or growing crops, respectively, and then process them for their seeds\* at a farmer's workshop; these are then pressed at a screw press, producing oil.
    *(\* Rock nuts are "seeds" from quarry bushes, just with a different, specific name. Olives can be pressed for oil; this works as well.)*
- Combine one unit of lye plus one unit of either tallow or oil at a soap maker's workshop, creating a single bar of finished soap.
  *(Note: There are a number of by-products produced in either path for tallow or oil; these can be useful to a fortress, but are not relevant to soap making.)*

After it's produced, a bar of soap is given a name based on the animal or plant it was derived from; thus you can have a bar of "rattlesnake tallow soap" or "olive oil soap", etc.; this has no effective difference in game play.

Soapmaking procedure

Chop wood

Butcher an animal

Mill seeds with a quern or millstone

Press oil from olives (fruit) in a screw press

Make ash in a wood furnace

Render fat in a kitchen

Press oil from seed paste in a screw press

Make lye at an ashery

Tallow

Oil

Lye

Tallow or Oil

Make soap at a soap maker's workshop

Soap

### Work Orders

Setting up work orders for soap can be tricky, as two of the recommended conditions are wrong:

- The recommended condition for lye is "lye-containing items", but this is incorrect, as a barrel containing 10 items of lye will only count as a single lye-*containing* item. Instead, for "Type" select "Liquid" and for "Mat" select "Lye", resulting in a condition on simply "lye".
  - This is further complicated by the fact that a dwarf can take a barrel of lye and a stack of tallow and produce up to 10 bars of soap at once, which complicates planning work orders that are intended to produce a set number of items.
- The recommended condition for the output is simply "bars", which is rather unhelpful. To make a condition for just soap bars, for "Type" select "Bars", and then go into "Adj" and check "Soap items". While many soap materials are listed under "Mat", make sure none of these are selected, as these will check only for that specific kind of soap.
- There is also a complication with seed oil soap automation, where both seed paste (pressed for oil) and seed press cake (food byproduct of oil pressing) use the non-specific "Glob" type classification in work order conditions. This means that seed paste will not be triggered for production in a mill/quern until seed press cake stock is also consumed.

## Hygiene

Dwarves do not require soap to clean contaminants such as mud and blood from themselves – if necessary, they will use murky pools, artificial pools of water, brooks, or a well. However, using soap will often generate the happy thought "recently took a soapy bath". It is possible to construct bath-houses (rooms containing pools of water, a soap stockpile, and perhaps a few nice statues) so dwarves living deep underground need not venture to dangerous cave pools or surface brooks to clean off a little mud or some bloodstains. For cleaning wounds and preventing infection after surgery, however, hospitals should be kept stocked with a small amount of soap. Soap will get used up as dwarves wash themselves, and dirtier dwarves consume soap more quickly.

Dwarves have an internal "dirtiness" level, which slowly builds up over time, gets lowered when they have a bath, and lowered further when they have a soapy bath. This "dirtiness" value is connected to the chance of getting an infection if the dwarf is injured, making soap useful as a preventative as well as treatment.

|  |
|----|
| "Soap" in other / Languages / Dwarven / : / uben / Elven / : / dathe / Goblin / : / snubez / Human / : / kamven |

\

    [MATERIAL_TEMPLATE:SOAP_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:CREAM]
        [STATE_NAME:ALL_SOLID:soap]
        [STATE_ADJ:ALL_SOLID:soap]
        [STATE_COLOR:LIQUID:CREAM]
        [STATE_NAME:LIQUID:melted soap]
        [STATE_ADJ:LIQUID:melted soap]
        [STATE_COLOR:GAS:CREAM]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:7:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:800]
        [IGNITE_POINT:10508]
        [MELTING_POINT:10078]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:10000] no data
        [SHEAR_FRACTURE:10000]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [REACTION_CLASS:SOAP]
        [IMPLIES_ANIMAL_KILL]
        [SOAP][SOAP_LEVEL:2]
