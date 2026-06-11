# Status

> Fonte: [Status](https://dwarffortresswiki.org/index.php/Status) — Dwarf Fortress Wiki (GFDL/MIT)

*If you are looking for the symbols that **flash over a dwarf icon**, see status icon.*

Pressing during Dwarf Fortress Mode brings up the **status screen**.

This screen contains a large amount of useful information about your fortress and its residents.

## Title Bar

The very top row of the screen shows the settlement name and class, followed by the year and season.

## Menu Bar

Along the top of the status screen, are various choices for sub-menus. Each can be highlighted with and (or and ), and then selected with . The menu bar consists of the following options:

- Animals - The Animal Status screen allows you to manipulate animals belonging to your dwarves.
- Kitchen - The Kitchen Status screen allows you to set cooking (including cheesemaking) and brewing permissions for any ingredients currently in your fortress.
- Stone - The Stone Status screen allows you to alter permissions on various types of stones that may be reserved for specific uses by default.
- Stocks - The Stocks Status screen allows you to examine the number of various items that your fortress and its residents possess.
- Health - The Health screen gives you an overview of the current health statuses of your dwarves. This will only show up on the status screen when you have a Chief medical dwarf assigned. This is part of the Healthcare system.
- Justice - The Justice Status screen becomes available once you qualify for a Sheriff (even if you don't have one). It allows you to examine any offending dwarves as well as their crime and sentence.

## Main Status Screen

This is the screen that appears by default when you press . It lists a bunch of useful information, and grows more useful as your dwarves gain skills.

- The upper left hand corner lists the amount of wealth created by your fortress. This figure is slightly misleading; it is the total value of goods that currently exists in your fortress that you have created, and that you have not exported. Presumably, this is one of the ways that the game calculates how advanced your fortress is, for determining how likely you are to receive immigration, get besieged, or get better trade goods from caravans. Note that this figure will only show if you have a broker with appraisal.
- Below that, the status screen lists trade information. This also requires a broker with the appraisal skill.
  - Imports represent the total value of foreign made goods in your fortress. Therefore this includes the value of things such as the clothes brought in by immigrants, the equipment dropped by dead goblin invaders, and so forth. However, foreign made goods that have been decorated, processed or consumed (such as food) do not count towards this total. Goods that are stolen (by rhesus macaques, for example) seem to count towards this total despite the fact that they are no longer on the map.
  - Exports represent the total value of goods made by your fortress that you have traded to other civilizations.
  - A hypothetical example:
    - You buy worth 50. This increases imports by 50. You then make this into a worth 100. This reduces imports by 50 (since it is no longer considered by the game to be foreign-made). Fortress wealth increases by 100. You then export this bag. Fortress wealth decreases by 100, and exports increase by 100.
- Below that, you will see a list of your food stores. These all come with question marks, until you have a bookkeeper with the record keeper skill. Depending on how skilled he is, and how accurate you want the counts, you will get better numbers. Note that the bookkeeper will need an office to take inventory, and it will take some time for him to count. Also note that the 'Other' class includes immediately edible items (e.g. prepared meals, cheese), potentially edible items (e.g. flour, syrup), and inedible items (e.g. dye), and is therefore an unreliable indicator of a fortress' food stores.

- The rest of the screen is taken up by your population display, indicating the number of dwarves in your fortress, and their occupations. Only the dwarves' most skilled occupation counts for this screen. It allows you to see at a glance who you have available, which gets increasingly useful the larger your population grows.
  - An important note is that the right hand side, displaying military dwarves, only includes dwarves that are currently active in the military. When deactivated, these dwarves are displayed in the left column, under their civilian job.

## Animal Status Screen

This screen is separated into two tabs ( and ). They can be switched between using and .

### Creatures

This screen shows a list of all animals that are owned by the fortress or its residents, but does not include any wild animals in the region, nor animals belonging to invaders or caravans.

The animals are listed down the left hand column () of the screen. Some useful information about this list:

- The word "stray" indicates that the animal is not any dwarf's pet. In the case of war or hunting animals, it means the animal has not been assigned to a dwarf.
- Named animals are often a result of being named before joining your fortress, and usually means they are owned by an immigrant. Named animals may also have made a kill.

The second column shows training status for each animal.

- Training level:
  - (none) - This animal is wild.

  - \- This animal is semi-wild.

  - \- This animal is trained.

  - \- This animal is well-trained.

  - \- This animal is skillfully trained.

  - \- This animal is expertly trained.

  - \- This animal is exceptionally trained.

  - \- This animal is masterfully trained.

  - \- This animal is domesticated.

- Trainer status:
  - \- This animal can be trained by any animal trainer.

  - \- This animal can be trained by any unassigned animal trainer.

  - \- This animal can be trained only by a specific animal trainer.

- Type of training:
  - \- This animal is marked for hunting training.

  - \- This animal is marked for war training.

The third column () lists the current status of each individual animal in your fortress. This status can take one of several forms:

- \- This animal is available for adoption as a pet.

- \- This animal has been trained as either a hunting or war animal, and has not been assigned an owner.

- \- This animal currently cannot be claimed as a pet.

- \- Cats, being superior to all other creatures, cannot be assigned as pets. Instead, they will adopt an owner at their whim.

- \- This animal belongs to the listed dwarf. Pets can provide happiness to their owners.

- \- This animal will be butchered when a butcher becomes available.

- \- This animal is wild and requires taming.

The fourth column lists animals marked for gelding.

- \- This animal will be gelded when a gelder becomes available.

Controls:

- \- Toggles its availability. This can only be done on "available" or "unavailable" creatures.

- \- Marks or unmarks an animal for slaughter. Note that you cannot mark animals for slaughter once they belong to a dwarf. Also, some animals may not be slaughterable.

- \- Marks or unmarks an animal for gelding. Note that you cannot mark animals for gelding once they belong to a dwarf. Also, some animals (birds in particular) may not be geldable.

### Overall Training

This tab shows civilization-wide animal training knowledge. Training wild animals contributes to this knowledge.

[TABLE]

## Kitchen Status Screen

Overall, this screen contains a list of all items currently within the fortress that can be used for either cooking or brewing. It is separated into four tabs (, , , and ). You can switch between the tabs using .

The items are listed down the left hand side of the screen (). The second column () lists the number of each ingredient currently possessed.

The last column () is subdivided into two additional columns, one for cooking and one for brewing. This is the most important part of this tab, as it shows you whether dwarves are currently allowed to use the given ingredient for the given task. Possible values are:

- or  - This item could be used for the task, but is currently disallowed.

- or - This item is able to be used for the task, and dwarves have permission to do so.

- \- This indicates that the given item cannot be used in this way. For example, Deer meat cannot be brewed (Any alcohol can be cooked).

Note that when a new food is obtained, the default is and . This includes recently butchered animals, foodstuffs gained from trading, first crops from seeds, and plants gathered from the wild. Items that have been designated as forbidden will not be listed on this menu.

Cooking permission is also used/needed for cheesemaking from milk items.

Controls:

- \- Toggles permission to cook the highlighted item.

- \- Toggles permission to brew the highlighted item.

- \- Cycles through tabs.

## Stone Status Screen

The stone status screen is separated into two tabs ( and ). The first tab () lists all economic stone (stones that have a value and purpose besides masonry) found within the game. As an example, chalk can be used in the process of creating steel. The second tab () lists all non-economic stone.

Both tabs allows you to control what stone is used for menial purposes (masonry, building construction, walls, etc.). By default all economic stone, except layer stones present on the map, is and all other stone is . It also tells you if a stone is or not.

The first tab () also provides a full list of each economic stone's uses. By pressing or , you can move the highlighted selector over to this list on the right. Pressing when highlighting a recipe, (like when looking at calcite), will let you see all the ingredients to the recipe.

Note that this screen is also mouse-enabled: All objects within it can be left-clicked upon, and right-clicking scrolls through the lists.

Controls:

- \- Toggles stone type availability.

- \- Switches between tabs.

## Stocks Status Screen

The stocks screen shows you a list of all of the goods in your fortress. Its accuracy relies heavily upon the bookkeeper.

The left side of the screen lists the categories of all the items in your fortress. To the right of this, are two columns, listing numbers. The number to the left is the number of items accessible to use, (in a stockpile or scattered on the floor) and beside that in red is the number of inaccessible items. (parts of buildings, remains of pets and citizens, marked forbidden, marked for melting or dumping, belonging to traders, etc.)

To the right of these numbers are the goods themselves. By pressing you can toggle between the detailed mode, which shows each item individually, along with relevant name/quality data, or the list mode, which shows items in stacks.

## Health Status Screen

The Health screen gives you an overview of the health statuses of your dwarves. It requires a chief medical dwarf before becoming available to the user. It tells you what type of injuries your dwarves have, and what kind of medical treatment they require.

## Justice Status Screen

This option only appears when a fortress is large enough to need a sheriff to dispense justice.

In the upper right of this screen is "Cages & Chains", which shows the total number of combined cages plus restraints designated for justice out of the total currently available. It's important to note that although it says "chains", it's counting both *ropes* and chains as well as cages - and ropes are not as desirable as chains when used as restraints for this purpose. If you have adequate chains and cages (at least 1 cage, rope or chain for every 10 dwarves) the number will be blue, or red if you don't have enough.

Along the left hand side is a list of known criminals. The right side lists all of the dwarf's crimes (including the victim of each crime), as well as any pending punishments (including the officer performing the punishment).
