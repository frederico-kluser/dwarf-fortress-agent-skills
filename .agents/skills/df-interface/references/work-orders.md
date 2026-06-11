# Work orders

> Fonte: [Work orders](https://dwarffortresswiki.org/index.php/Work_orders) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

**Work orders** are an advanced feature of Workshop Management that becomes available with a Manager. It allows easier management, automation and/or fine control of the various activities needed to maintain a well-oiled fort. The work order screen lists all work orders in the fortress, shows their status and allows to modify them and place new general orders. It is accessed from the main screen through the o Work Order menu button. To create a work order, click on the  button in the upper right corner of the menu.

\

## Work Order Conditions

A busy fortress' work order menu.

Condition menu accessible from Work Orders menu by clicking on .

Work Order Conditions  are incredibly versatile and equal parts daunting. There are various options that can be selected as conditions. Multiple conditions on a single work order are evaluated as logical AND - that is, ALL conditions on an order must be met before the order is begun. To create additional condition click on .

### Frequency

Switching  button determines whether and how often the work order will repeat. If no conditions have been selected, the options are:

- One-time order
- Restarts if completed, checked daily
- Restarts if completed, checked monthly
- Restarts if completed, checked seasonally
- Restarts if completed, checked yearly

If there are conditions, the options are:

- One-time order, conditions checked daily
- One-time order, conditions checked monthly
- One-time order, conditions checked seasonally
- One-time order, conditions checked yearly
- Restarts if completed, conditions checked daily
- Restarts if completed, conditions checked monthly
- Restarts if completed, conditions checked seasonally
- Restarts if completed, conditions checked yearly

### Item Condition

By far the most complex condition, and the most common one used.

Each Item condition has a set of parameters:

- Amount
- Equality
- Type
- Material
- Adjective

Unless specifically stated, the Type, Materials and Adjectives default to 'Any'

#### Amount and Equality

The part of the condition that states when it is true or false. Amount  is the number it activates on, equality  is one of the following:

- At Least (At Least 5 will activate on 5 or more)
- At Most (At Most 5 will activate on 5 or less)
- Greater Than (Greater Than 5 will activate on 6 or more)
- Less Than (Less Than 5 will activate on 4 or less)
- Exactly (Exactly 5 will activate on only 5)
- Not (Not 5 will activate on any number other than 5)

#### Type

 The type of object. Examples include Thread, Bar, Cloth, Breastplate, Stone, Fish, Plants.

#### Material

 The exact material an object is made from. Examples include Yak Tallow, Cat Soap, Hide Root Plant, Hide Root Seed, Steel, Hematite.

#### Adjectives

 A bunch of definitions for items that range from the 'type' of material (e.g. Yarn, which includes Sheep, Alpaca and Llama wool) to the state of the object (e.g. Empty, for an Empty bag or Empty Barrel). An Item can have multiple adjectives. Adjectives can be very powerful, but are also not entirely obvious what they are (and are buggy/finicky). Some useful Adjectives, examples of items with said adjectives, and uses of said adjectives are listed below.

|  |  |  |
|----|----|----|
| Adjective | Example | Usage |
| Aluminum-bearing items | Native Aluminum | Same as using 'Native Aluminium' material |
| Ammo items | Arrows, Bolts | For checking if you have some Ammo available. Useful in bolts automation. |
| Bag-processable items | Quarry Bush | For the "Process plant to bag" order (Farmer's workshop) |
| Bismuth-bearing items | Bismuthinite | Same as using 'Bismuthinite' material |
| Bone items | Yak Bone, Elf Bone, Horse Bone | For checking you have bones before doing bone crafts or making bone bolts. Can also be used to set a minimum number of bone bolts you want |
| Clay items | Fire Clay stone, Clay Loam Mug | Useful in combination with 'Stone' type to check how much Clay you have available |
| Collected items | Cave Spider Silk Thread | Used for checking if you have silk thread for making cloth, not uncollected webs |
| Cookable items | Turkey Egg, Pig Meat, Plump Helmet | Used for checking if you have enough items to make roasts |
| Copper-bearing items | Tetrahedrite, Malachite | Used for checking if you have copper ores for making alloy metals out of ores |
| Dye Items | Dimple Cup Dye, Hide Root Dye | Used for checking for dye for dye jobs, can be used to set a condition on 'mill plants'/'make dye' jobs. Note that items/materials in bags are ignored, so adjectives are the only way to check for dyes. See Dye#Work Order Conditions for details. |
| Dyable items | Pig Tail Cloth, Cave Spider Silk Thread | Used for checking for items which can be dyed |
| Dyed items | Pig Tail Cloth, Cave Spider Silk Thread | Used for checking how many items exist which are already dyed |
| Empty items | Leather Bag, Large Green Glass Pot | Useful for checking for barrels for brew jobs, and checking for empty bags for jobs that require bags to store objects in |
| Fat items | Pig Fat, Yak Fat, Crundle Fat | The adjective for fat that gets turned into Tallow |
| Flux items | Chalk Stone, Limestone Stone | Used in Steel and Pig Iron creation |
| Food Storage items | Large Gabbro Pot, Oak Barrel | Listed twice in adjectives; the first one matches both barrels and large pots, while the second one *only* matches large pots |
| Glass items | Green Glass Goblet, Raw Clear Glass | Can be used when cutting raw glass into gems to get a set number of glass gems |
| Glazable items | Stoneware Large Pot | Used for checking if there's items to glaze |
| Glaze items | Ash Bar, Cassiterite | Used for checking there's items to glaze clay items with |
| Gold-bearing items | Gold Nuggets | Same as using 'Gold Nugget' material |
| Hair/wool items | Yak Thread, Horse Thread | Not the same as Yarn items. Can be used for suturing, but not necessarily turned into cloth |
| Horn items | Yak Horn | Used for checking items required to make horn crafts |
| Iron-bearing items | Hematite, Magnetite | Better to use the specific ores, unless you want to make rock objects out of iron containing ore. |
| Ivory/tooth items | Elephant Ivory, Lion Tooth | Used for ivory crafts and decorating items with teeth. |
| Lead bearing items | Galena | Same as using 'Galena' material |
| Lye-bearing items | Ash Bar | Same as using 'Ash' material |
| Lye/milk-free items | Willow Bucket | Used for getting milk and lye, can also use Empty adjective |
| Melt-designated items | Steel Anvil | Used for checking if there's enough melt-designated objects for 'melt a metal object' order |
| Milk items | Yak Milk | Used for making cheese, can check how much milk you have for milk jobs |
| Milkable items | Purring Maggots | Only for milking Purring Maggots. Cows are not milkable items. |
| Millable items | Hide Root, Cave Wheat | For milling at a quern |
| Nearby items | Bars, Blocks | The count excludes items that are currently used in buildings or constructions. Distance does not seem to matter. |
| Nickel-bearing items | Garnierite | Same as using 'Garnierite' material |
| Non-pressed | Pig Tail Paper Slurry Glob, Rock Nut Paste | Used in various screw press jobs, for checking if items are available for pressing |
| Oil-bearing items | Rock Nut Paste, Olive | Used in Press Liquid from Paste(/Fruit) jobs, for limiting overall oil production. (Use with 'Non-pressed' to rule out unmilled seeds) |
| Paper-slurry | Pig Tail Paper Slurry Glob | Used in Plant Slurry to Sheet jobs, can be added to Mash Plant jobs to limit how many Plant Slurry Globs are made |
| Paper-slurryable | Pig Tail, Rope Reed | Used in Mash plant into slurry order, for checking if plants are available for making slurry |
| Plant items | Hemp, Hide Root, Sweet Pod, Pig Tail Cloth | Useful for cloth orders. Can check if an item is made of plant cloth through this adjective |
| Processable (to barrel) items | Sweet Pod | Used for the Process Plants (Barrel) order |
| Processable (to vial) items | Valley Herb | Used for the Process Plants (Vial) order |
| Renderable items | Pig Fat | Same as 'Fat items' |
| Sand-bearing items | Red Sand Bag | Not to be confused with Sand items, which only selects the sand in a bag. For jobs to collect Sand, Sand-bearing items is the one that works |
| Shell items | Pond Turtle Shell | Used for checking items required to make shell crafts |
| Silk items | Cave Spider Silk Cloth | Useful for cloth orders. Can check if an item is made of silk cloth through this adjective |
| Silver-bearing items | Galena, Tetrahedrite, Horn Silver, Native Silver | Used for making alloys with Silver |
| Soap items | Rock Nut Soap | Can be added to type Bars to check for amount of soap |
| Tallow items | Crundle Tallow | Used for checking if there's enough tallow for soap making jobs |
| Tin-bearing items | Cassiterite | Same as using 'Cassiterite' material |
| Undisturbed items | Cave Spider Silk Web | Used for Collect Webs orders |
| Unimproved items | Any item without encrusting | In theory could be used for checking if there's items available to be encrusted |
| Unused items | Pig Tail Cloth, Sheep Wool Thread | Useful for weaving and clothing jobs, rule out items partially consumed by hospitals |
| Written-on items | Written on Quire | Used for checking a quire is ready to be bound into a codex |
| Yarn items | Alpaca Wool Bag, Sheep Wool Thread | Useful for cloth orders. Can check if an item is made of yarn cloth through this adjective |

### Work Order Dependency

 This creates a condition where the second work order (the one being created) will only activate if the first work order (the one selected as a condition) either is completed or activated (switchable on ).

## Work Order Examples

Most work orders that a fortress will need are simple to create, but certain options that a fortress may want are more finicky to create. A set of example work orders for common needs are collated below.

### Process Plants (Plant Thread) with a maximum Plant Thread condition

This work order will keep a minimum of 20 plant thread, and activate when there are greater than 5 processable plants available.

1.  Create a 'Process Plants' work order. Set the number of times the task will be performed to 5.
2.  Ingredients Condition:
    1.  In conditions, add the suggested condition 'unrotten processable plants'.
    2.  adjust the number to be how many plants minimum you want available - in this case, 5 plants minimum will mean this activates only when all 5 process plants tasks can be accomplished.
3.  Plant Thread Condition:
    1.  Add a Condition to the Work Order.
    2.  Change Type to 'Thread'.
    3.  Change Adj to 'Plant items'.
    4.  Set the number to the maximum Plant Thread you want from this order - in this case, 20.
    5.  Press 'Change the inequality of the condition' until the condition says 'at most 20' or 'less than 20'.

### Collect Sand if there is not enough sand

This work order will activate if there are at least 5 empty bags, and if there are less than 20 bags of sand.

1.  Create a 'Collect Sand' work order. Set the number of times the task will be performed to 5.
2.  Empty Bags condition:
    1.  Add a Condition to the Work Order.
    2.  Set the Type of the item to Bag (specifically 'Bag', not any other sort of bag that has been procedurally generated for instruments).
    3.  Set the Adjective of the item to 'Empty items'.
    4.  Set the amount on the bag condition to 5.
3.  Sand Bags condition:
    1.  Add a Condition to the Work Order.
    2.  Set the Adjective of the item to 'Sand-Bearing Item'.
    3.  Set the amount on the sand bearing item condition to 20.
    4.  Press 'Change the inequality of the condition' until the condition says 'at most 20' or 'less than 20'.

\

### Collect Clay if there is not enough clay

A work order that will collect clay if there's less than 20 clay available.

1.  Create a 'Collect Clay' work order.
2.  Clay Condition:
    1.  Add a Condition to the Work Order.
    2.  Set the Type of the item to 'Boulders'.
    3.  Set the Material of the item to the type of clay you are collecting.
    4.  Set the amount to 20.
    5.  Press 'Change the inequality of the condition' until the condition says 'at most 20' or 'less than 20'.

### Make Steel Bars automatically

Using two repeating work orders, steel can be set to automatically be created. In this case the order will make 20 steel bars if there are less than 40 steel bars.

1.  Create a 'Make Pig Iron Bars' work order. Leave the amount at 10.
2.  Pig Iron Bars Conditions:
    1.  Under suggested Conditions, select Pig Iron Bars, Iron Bars, Flux Stones, and Refined Coal conditions.
    2.  For Pig Iron Bars, change the Material to 'Steel'. This will change this condition to be based on how much Steel the fortress has. Set the amount on this to 40.
    3.  Set Iron Bars, Flux Stones, and Refined Coal conditions to be **20**. This will be the amount of ingredients needed to do 10 Pig Iron bar orders, and then 10 Steel bar orders.
3.  Create a 'Make Steel Bars' work order. Leave the amount at 10.
4.  Steel Bars Conditions:
    1.  Select 'Make the activation of the work order depend on the status of another work order'. From this list, select the Pig Iron Bars work order that was already created.
    2.  Press 'Change the frequency that the conditions are checked' once, to make the steel bars order repeat upon completion.
5.  (Optional, makes things smoother) When the pig iron bars work order activates, add a 'Make the activation of the work order depend on the status of another work order' condition to the Pig Iron Bars work order, to require the Steel bars order to be completed. This will make the two orders loop on each other.

### Make Full Suits of Armor

Using a repeating order and some clever dependencies, metals can be automatically turned into full suits of armor without an excess number of \*«+steel greaves+»\*:

1.  Create a 'Forge' work order, such as 'Forge Steel Breastplate'. Set the amount to 1. This will be the first job used to activate the others
    1.  Under the suggested conditions, select the Bars condition, such as Steel Bars for the above Forge Steel Breastplate. Set the amount at 'at least 13'. You'll have to catch this job while it's running, below, so it's recommended to start with an amount you already have. You'll be revisiting this number later, but 13 should cover any viable kit and then some.
2.  For each other armor piece, Create a 'Forge' job. Set the amount to 1. Boots and gauntlets are made in pairs, so don't worry about adjusting for those jobs
    1.  Under the conditions, make the job depend on the first. Set to 'When Activated'. This will ensure that multiple forges can make each item in parallel
    2.  Set the job to repeat, since depending on another work order does *not* automatically make the job repeatable.
    3.  Not all civilizations have access to all pieces of armor, such as High Boots, so you may have to adjust your ideal suit accordingly. See Armor for a full list of recommended coverage and bar costs.
3.  Optionally, add a job for Forging a weapon to go with the suit of armor. **This is not recommended to leave up indefinitely**, as weapon usefulness varies so greatly as to make it more viable to have squadrons outfitted with differing weaponry. If you must do it this way, use Steel Battleaxes
4.  While the first set of armour is being made, **before any of them complete**, edit the first job.
    1.  Make it depend on each other job in the suit. Leave these conditions 'When Completed.' This will ensure the first job does not continue running because there's "enough" metal when that metal is going towards other pieces in the same suit.
    2.  Adjust the trigger amount at least cover a full kit. This will avoid cancellation spam.
    3.  Adjust the trigger amount higher if you want to keep some material in reserve or keep weapons on a separate set of jobs.
    4.  Add further conditions if you're mixing materials, such as leather caps or bronze greaves.

### Shearing animals

Animals with wool can be sheared roughly every 300 days. Creating a work order that runs each year will mean the animals get sheared whenever they are able to be sheared.

1.  Create a 'Shear Animal' work order. Set the number to the number of shearable adults in the fortress.
2.  On the Shear Animal Order, go into conditions and press 'Change the frequency that the conditions are checked' until the order is set to 'Restarts if completed, checked yearly'.
3.  (Optional) Shear Animal Conditions:
    1.  Add an item condition.
    2.  Set the type to 'Thread'.
    3.  Set the Adjective to 'Yarn items'.
    4.  Set the amount to the maximum yarn thread wanted ().
    5.  Press 'Change the inequality of the condition' until the condition says 'at most ' or 'less than '.
4.  Create a 'Spin Thread' work order. Set the amount to 5.
5.  Spin Thread Conditions:
    1.  Under Spin Thread Suggested Conditions, select 'Amount of unrotten hair/wool body part'.
    2.  Set the amount to 5.
    3.  Press 'Change the inequality of the condition' until the condition says 'at least '. This will mean if there are exactly 5 wool body parts it will activate, whereas if the condition is left on 'greater than' it will not.

### Make Soap bars

Creating Soap if there is not enough soap. In this case, the minimum soap required is 20, and uses Tallow. The same applies to Oil based soap.

1.  Create a 'Make soap from tallow' work order. Set the amount to 5.
2.  From suggested conditions, select 'amount of bars', and 'unrotten tallow fatty glob'.
3.  Set 'amount of bars' to be 20, and 'unrotten tallow fatty glob' to 5.
4.  Select the adjective of 'amount of bars' to be 'Soap items'.
5.  Create a new Item condition, set the amount to 5.
6.  Set the Material of the new item condition to 'Lye'.
7.  Set the Type of the new item condition to 'Liquid'.

### Make bone bolts

Creating bone bolts if you do not have 50 bone bolts, and have at least 5 bones.

1.  Create a 'Make bone bolts' work order. Set the amount to 5.
2.  From suggested conditions, select 'bolts' and 'unrotten bone body part'.
3.  Set the amount on 'unrotten bone body part' to 5.
4.  Set the amount on 'bolts' to 50.
5.  Add the adjective 'Bone items' to the 'bolts' condition.

### Make wooden furniture based on amount of wooden furniture available

For creating a variety of wooden furniture not of a specific material, the Plant adjective can be used to check that a certain amount of wood furniture has been created. This example talks about Tables, but this can be applied to any wooden item.

1.  Create a 'Make wooden table' work order.
2.  From suggested conditions, select 'Amount of tables'.
3.  On the 'Amount of Tables' condition, add the 'Plant items' adjective.

## Bugs/Finicky UI

### Adjectives

When changing the adjective of an item condition in a work order, because you can select multiple adjectives there is no automatic return to the work order conditions. To leave, you will want to Right-Click, which'll take you back to the Work Order menu, and then select the work order you're working on again.

#### Missing adjectives

- Size: There is no adjective for which creature type wearable items are sized for. The size must be selected in the Materials menu, where both material and size can be chosen.
- Wear: There is no adjective for wear level of items.
- Some adjectives can only be used on certain orders. Bug:10372 Bug:12622

### Materials

A new bug with v.50 is when selecting a material type for a job. If you select a material type but do not do it fast enough or pause the game and the job is confirmed by the manager before you change it then any material will be used for the job instead of the restricted material. An example is when setting up a job to make only rock salt doors but you do not select rock salt before the job is confirmed or you go back later and decide you only want rock salt doors, the material type is not respected and any stone will continue to be used until you cancel the order.

## See also

- Manager
