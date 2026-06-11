# Milk

> Fonte: [Milk](https://dwarffortresswiki.org/index.php/Milk) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Milk** is a product extracted from milkable creatures. Milk can be made into cheese or used in cooking prepared meals. It cannot be consumed "as is". Milk is found under "Liquid" in the Stocks screen k.

Female versions of certain animals are milkable. In order to perform milking, you must have a dwarf with the milking labor active, a farmer's workshop, an empty bucket and a mature, non-pet, milkable animal.

## Milkable creatures

The following creatures can be milked:

- Alpaca
- Camels, both one-humped camel† and two-humped camel†, and the giant one-humped camel† and giant two-humped camel†
- Cow
- Donkey
- Goat
- Horse
- Kangaroo† and giant kangaroo†
- Llama
- Pig
- Purring maggot‡
- Reindeer
- Sheep
- Tapir† and giant tapir†
- Water buffalo
- Yak

† These animals are not domesticated and can't be brought on embark. Savage giant and animal man versions grant the same milk as the normal-sized species, though animal people can't be milked due to ethics.\

‡ Purring maggots are an unusual case in that they are vermin and not livestock. Unlike livestock, they can only be milked when **not** tamed. Bug:3670.\

## Milking creatures

Queue a "Milk Creature" job at a farmer's workshop. The milker will not necessarily pick the closest animal available. Caging, pasturing or restraining the milkable creatures near the workshop might be a good idea, but is not mandatory. The animal must also have milk available. Once milked, the creature will be free to roam. If the creature was previously caged, pastured or restrained, some dwarf will be assigned the job of taking it back. You can avoid these pasture animal jobs if the farmer's workshop is in the animal's pasture.

Milk should eventually be transferred from its bucket into a barrel or large pot for long-term storage. If you plan to make cheese, it's a good idea to let the milk accumulate so that you get stacks of cheese (up to size 5) instead of single (size 1) cheeses.

The frequency with which animals are able to be milked is defined in the raw files with the tag `[``MILKABLE``:LOCAL_CREATURE_MAT:MILK:20000]`. All milkable creatures currently have this tag set to 20000 ticks, which, at 1200 ticks per day, means they all can be milked every 17 in-game days. Due to this time-out, using repeating jobs to milk creatures is infeasible if only a few milkable animals are available. Alternating repeating "Milk Creature" and "Make Cheese" jobs tend to work poorly, since transfer of the milk to storage can interfere with continued work, so that sooner or later the cheesemaking job will be cancelled, eventually canceling the milking job as well.

An exploit to maximise embark point returns is to take 1 of each kind of milk - milk costs only 1 point at embark and comes with a separate barrel for each type, effectively giving you free barrels, and (after some work) stacks of 1 cheese from each unit of milk for your prepared meals, worth 10 times what the milk is worth.

Milk from milkable animals domesticated by a civilization can be ordered in trade agreements with that civilization. Each barrel of milk brought by a caravan contains 10 units of milk.

### Dwarven ice cream

Milk has a freezing point of 10000 °U , the same as water. If milk is left in conditions below this temperature, even on a tile marked inside, it will freeze, and become "frozen *{animal}'*s milk". Frozen milk is treated as a cookable solid Bug:2787, and may show up as an ingredient in your roasts--at 1/10th of the value of cheese, if the roasts do not just melt entirely. There is no entry for frozen milk in stockpile menus, so dwarves will not haul a frozen milk barrel to any type of stockpile. Bug:3398 Careless attempts to dump the barrel to an indoor garbage dump may result in dwarves hauling the frozen milk and the barrel separately, resulting in a puddle of milk when it thaws. Dwarves will not make cheese out of frozen milk. For these reasons, milking industries should be set up underground, as Armok intended.

If your trade depot is outdoors in freezing weather, any barrels of milk (or lye) brought by a caravan will be frozen and appear as empty barrels in the Trading screen. They can be distinguished from empty barrels by having a price 10☼ higher than the price of the barrel, or by viewing their contents.

To move frozen milk to an indoor garbage dump without spilling it, do not use the Designations Menu. Instead, just mark the barrel for dumping.

## Bugs

- After finishing a milking job, the milker may generate a cancellation message if trying to take another job immediately: "Urist McMultitasking cancels job, handling dangerous animal". They will subsequently just leave the milked animal to wander away on its own and retask anyway.
- It is unclear why pets cannot be milked; this seems to be a bug because milking is a requirement for some animals and presumably the Animal Care dwarf would be aware of this and oversee their regular milking.
- Frozen milk melts while being cooked, leaving unusable milk items unside the kitchen. Bug:2787
- Tamed purring maggots can't be milked. Bug:3670
- After being milked (or attempting to milk them?), purring maggots are left inside the workshop as an item unless you assign them to a cage. Bug:3668
- Cooks will only cook milk and other fluids as a last resort, instead preferring to cook solid foods with solid foods. Bug:2393 For more information, see the kitchen page.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Dwarven milk does not in fact come from dwarves. This is generally a relief to human caravans, until they find out where it really comes from.

Because milk is not considered a drink, dwarves will not drink it, even if they are dying of thirst. Indeed, dwarves consider any drink that isn't alcoholic to be no better than water, and refuse to drink milk because it's of better use as cheese. Another theory is that dwarves refuse to imbibe milk because it would make them puny milk-drinkers. What is for certain, however, is that unlike in real life, dwarves have yet to discover how to make alcoholic fermented milk beverages, such as kumis or kefir.

Got Dwarf?

    [MATERIAL_TEMPLATE:MILK_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:WHITE]
        [STATE_NAME:ALL_SOLID:frozen milk]
        [STATE_ADJ:ALL_SOLID:frozen milky]
        [STATE_COLOR:LIQUID:WHITE]
        [STATE_NAME:LIQUID:milk]
        [STATE_ADJ:LIQUID:milky]
        [STATE_COLOR:GAS:WHITE]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:7:0:1]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10338]
        [MELTING_POINT:10000]
        [BOILING_POINT:10180]
        [HEATDAM_POINT:NONE]
        [COLDDAM_POINT:NONE]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:1000]
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
        [SHEAR_YIELD:6600] used high salinity ice
        [SHEAR_FRACTURE:6600]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:500]
        [ABSORPTION:100]
        [REACTION_CLASS:MILK]
        [MATERIAL_REACTION_PRODUCT:CHEESE_MAT:LOCAL_CREATURE_MAT:CHEESE]
        [EDIBLE_VERMIN]
        [EDIBLE_RAW]
        [EDIBLE_COOKED]
        [ROTS]
        [GENERATES_MIASMA]
        [LIQUID_MISC_CREATURE]
