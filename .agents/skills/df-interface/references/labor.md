# Labor

> Fonte: [Labor](https://dwarffortresswiki.org/index.php/Labor) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

***"To get a job done, a dwarf has to do it."** - Boss Urist McOverstates-the-obvious*

**Labor** is how jobs get done in a fortress; which labors are restricted to a dwarf determines which jobs they can or can't do. The skill level and attributes of an individual determine how effectively they perform a job.

The game provides many flexible options to the player to allow or disallow certain actions of their dwarves, which can further add efficiency to a fortress. Visiting citizens can also perform some labors.

## Introduction to labor

-

  Your dwarves function as semi-autonomous entities, usually fulfilling their own basic needs, and sometimes performing jobs when able.

- Most jobs correspond to a **labor**, which dwarves can be restricted from doing.

- Labors can be restricted to specific dwarves in groups called **work details**.

- **Jobs**, the specific tasks to be completed, are created in various ways, including designations, zones, workshop tasks, and manager work orders, and once created, an idle dwarf who does not have that labor disabled will be assigned the job.

- As dwarves perform jobs, their **skill** in those areas increase. (The terms labor and skill are **not** synonyms. Skill is a measure of proficiency for a given labor, while a labor is the ability to do the work.)
  - Some skills don't correspond to jobs, like social skills and miscellaneous abilities like swimming.

## Labor menu

The **Labor** menu tab is accessed with y or the fourth menu button y at the bottom-left of the main interface. It contains four sub-tabs; Work details, Standing orders, Kitchen, and Stone use.

### Work details

The **Work details** tab lists the current sets of labors and who is allowed to do them. The work details are listed on the left side of the screen, selecting one shows a list of all labor assignable citizens in your fortress on the right. Each line shows the citizen's name, profession, applicable skill levels for this detail, specialization button, assigned details, and finally a check mark for this selected work detail. Clicking the specialization button will toggle specialization for that citizen, but clicking **any** other part of the line will toggle this selected work detail for that citizen, even other work detail icons.

Above the list, each work detail has a setting controlling how it is assigned to citizens:

- When "Only selected do this" is selected, the work detail will be assigned to any citizen with a check in the rightmost box on their line.
- With "Everybody does this" selected, all citizens in the fortress will have permission to do the work detail's labors. (Any checked boxes will be white, showing that the citizen in question will do this job even if specialized).
- When "Nobody does this" is selected, all citizens in the fortress will be *banned* from doing the work detail's labors. This does *not* override permission given by other works details. Any check marks/permissions set up before selecting "Nobody does this" will go red, showing that they are paused and they will be restored if you go back to "Only selected do this".

Labors associated with a dwarf's occupation (such as being a Doctor) are always allowed.

Additionally, each citizen has the option to be **specialized**; shown by the hammer and lock icon just to the right of their name (it can also be viewed and interacted with from the u Citizens menu). When this setting is on (icon is red ), the citizen will only accept tasks given by workshops/occupations they are assigned to, and labors which have been assigned to them, and are not restricted to "Nobody does this".

Here are all the possibilities:

|  |  |  |
|----|----|----|
|  | Specialized  | Unspecialized  |
|  The dwarf is assigned to the workshop or lever giving this job. | Yes | No, unless a Yes applies |
|  The dwarf is assigned to the occupation giving this job. | Yes | Yes |
| The dwarf is / selected / under any work detail containing this job set to: / "Everybody does this" OR / "Only selected do this" | Yes | Yes |
| No work detail contains this job OR / the dwarf is / unselected / under any work detail containing this job set to / "Everybody does this" | No, unless a Yes applies | Yes |

A dwarf can take a job if *any* of the Yes conditions below are satisfied:

#### Default work details

By default, the work details, and the labors associated with them, are as follows[1]

|  |  |
|----|----|
| Miners† | Mining |
| Woodcutters† | Woodcutting |
| Hunters† | Hunting |
| Planters | Farming (fields) |
| Fisherdwarves | Fishing |
| Plant gatherers | Plant gathering |
| Stonecutters | Stonecutting |
| Engravers | Stone engraving |
| Haulers | All / hauling / labors |
| Orderlies | Suturing / Dressing wounds / Feed patients / prisoners / Recovering wounded |

† The Mining, Woodcutting, and Hunting labors are only accessible from these default work details.

#### Custom work details

**Utilities**

If you would like more control or information for labor assignments, Dwarf Therapist and/or DFHack can help, when available.

Additional work details can be defined. Click "Add new work detail", select which labors will be associated with it, and then click done. You can then rename the new work detail.

There is currently no way to choose the work detail's icon, so you are stuck with what the game chooses. The roman numerals are in the file `Dwarf Fortress\data\vanilla\vanilla_interface\graphics\images\interface_bits_labor.png` and can be changed, but will still be used in order.

### Standing orders

### Kitchen

This tab lists all item types currently within the fortress that can be used for either cooking or brewing. It is separated into four tabs:

- Vegetables, fruit, and leaves
- Seeds
- Drinks
- Meat, fish, and others.

On each tab, the items are listed in the left most column (Ingredient Type). The second column (Number) lists the number of each ingredient currently possessed. The last column (Permissions) is subdivided into two additional columns, cooking and brewing. This is the most important part, as it shows you whether dwarves are currently allowed to use the ingredient for the given task. Possible values are:

-  or  (+C or +B in ASCII mode) - This item could be used for the task, but is currently disallowed.
-  or  (+C or -B in ASCII mode) - This item is enabled for use in the task, and dwarves have permission to do so.
-  or  (XC or XB in ASCII mode) - This indicates that the given item cannot be used in this way. For example, Deer meat cannot be brewed (Any alcohol can be cooked).

Note that when a new food is obtained, the default is  and  (XC or XB). This includes recently butchered animals, foodstuffs gained from trading, first crops from seeds, and plants gathered from the wild. Item types for which all items have been designated as forbidden will not be listed on this menu.

Cooking permission is also used/needed for cheesemaking from milk items\[Verify\]

### Stone use

The stone use tab is separated into two tabs, Economic Stone and Other Stone. Economic Stone lists all economic stone (stones that have a value and purpose besides masonry) that can exist in the game. As an example, chalk can be used in the process of creating steel. Other Stone lists all non-economic stone.

Both tabs allows you to control what stone is used for menial purposes (masonry, building construction, walls, etc.). By default all economic stone, except layer stones present on the map, is disallowed and all other stone is allowed.

The Economic Stone tab also provides a full list of each economic stone's uses and if it is magma-safe or not.

## Tool requirements

For a few specific jobs, a matching **tool** is also required for a dwarf to obey the job assignment. Any active miner needs a pick, any active wood cutter needs a battle axe, and any active hunter needs a crossbow (with quiver and bolts). If a labor needs a tool, the labor is considered **exclusive** such that you can only assign one of the three labors listed to any single dwarf at any one time.

This means that a dwarf cannot be, for instance, a Miner and a Hunter simultaneously, since both labors require a tool. If a dwarf is assigned a tool-labor and another tool-labor was previously assigned to said dwarf, the (old) tool-labor is automatically and silently unassigned, and that tool is immediately dropped where they stand at the time.

Additionally, the assignment of these tools **overrides** any uniform assigned to a dwarf's squad, so military dwarves should never be assigned any of the aforementioned labors.

To be used, a tool cannot be forbidden, nor in possession of another dwarf (even one that does not currently have a job), and a path must be available from the dwarf to that type of tool. If a tool is not available, the dwarf will typically attempt to fulfil other needs. It is possible, by using locked doors etc. to limit the paths, to force a specific tool to be assigned to a dwarf, but otherwise the tool will be randomly assigned, sometimes involving a dwarf walking long distances and past perfectly useful tools to find the one they think they want.

## Facility requirements

Many jobs require a workshop or some other facility in order to be completed. Jobs are designated by way of the workshop, and any dwarf with the corresponding labor associated with the workshop will go to the shop, provided they are not eating, sleeping, drinking, etc..., and begin to complete the task. Most workshop jobs also require some raw materials in order to complete the production.

## Managing labor and demand

This can be done from the labor menu y under the work details tab.

- You can view a list of all current, queued, and suspended jobs, as well as which dwarves are doing them, on the tasks menu t.
- A manager is incredibly useful for managing production jobs (workshop based). They can queue up a significant list of jobs without the need to select the various workshops, and place orders in bulk (or to be repeated). That said, there are some caveats, the most important being that queued jobs must be done in the correct order of materials required, or the orders will auto cancel. Also, you should not assign your manager to labors that are in high demand, as this will keep them from going to their office to place the orders.
- Migrating dwarves will typically arrive with certain work details already assigned. You will likely want to change these to put them to work in a way that best suits your fortress.

## Advanced labor management and design

Managing your dwarves can be a tricky business. If the in-game labor menu is not to your liking, Dwarf Therapist or DFHack are both useful tools that can assist you in managing your labors.

As your fortress grows, so will your labor pool, and the way you assign that labor will change over time. Typically at embark, you will have at least one Miner, a Wood cutter, Farmer, Carpenter, Mason/Stonecrafter, Cook/Brewer, Mechanic/Architect, one of which will also be a Broker/Appraiser. There are multiple combinations but this is typical (see Embark and Starting build). Early on, you will probably want to focus on fortress design and development, such that you will place priority on mining and masonry, supplemented by carpentry.

In order to maximize the benefit of highly skilled labor, you will eventually want to specialize your labor such that each dwarf has a very limited number of labors assigned. Keep in mind, however, that some dwarves experience minor negative feelings at not being able to perform a craft or a martial art for too long.

Hauling: Nothing can bog down your production like the distraction of hauling jobs. Losing your fort to a siege is fun, but losing because all your skilled laborers spend all their time hauling stuff is no fun. One solution is to use dedicated haulers. The migrants who appear having no skilled labor, and whose attributes pretty much suck all around, aka peasants, are best used as dedicated haulers.

## Labor, skill, and product quality

The amount of experience a dwarf has with a certain labor will determine how well they go about performing this labor; the more experience, the greater the skill. Certain job types can be completed more quickly, based on the skill in the labor. There are exceptions, such as nursing and hauling which will never be completed more quickly, regardless of skill.

Certain labors will produce products that have a quality tag, typically those associated with the production of an item from a workshop. The table below lists in which labors the dwarf's experience will impact the quality of produced items and in which labors a higher experience will only be beneficial for the speed of production.

- Many labors, most notably hauling, have no associated skill, do not generate experience, and do not improve with practice.

## Strange moods

A dwarf under a strange mood will perform a specific task to create an artifact that is outside of the player's control. Until they complete the task, both they and the workshop they claim will be unavailable for any labor. If the dwarf cannot complete the artifact, they will go insane and be permanently unable to perform any labor.

|  |
|----|
| "Labor" in other / Languages / Dwarven / : / èrith / Elven / : / equa / Goblin / : / akul / Human / : / ebe |

## List of labors

Category
Labor
Skill
Benefits of higher skill

Miner
Mining
Miner
speed only

Woodworker
Carpentry
Carpenter
speed; item and furniture quality

Crossbow-making
Bowyer
speed; weapon quality

Wood cutting
Wood cutter
speed only

Stoneworker
Masonry
Mason
speed only

Stone carving
Stone carver
speed; items and furniture quality

Stonecutting
Stonecutter
speed only

Stone engraving
Engraver
speed; engraving quality

Ranger
Animal training
Animal trainer
speed; training quality

Animal care
Animal caretaker
none (not implemented)

Hunting
Ambusher
reduced chance of being detected

Trapping
Trapper
success rate? trap quality?[Verify]

Small animal dissection
Animal dissector
speed only

Doctor
Diagnosis
Diagnostician
speed; chance of accurately diagnosing a syndrome

Surgery
Surgeon
speed, amount of bleeding caused, chance of failure

Setting bones
Bone doctor
speed only

Suturing
Suturer

Dressing wounds
Wound dresser

Other Healthcare
Feed patients/prisoners
No associated skill

Recovering wounded

Farmer
Butchery
Butcher
speed only

Tanning
Tanner
speed only

Farming (fields)
Planter
speed; crop yield (stack size)

Dyeing
Dyer
speed; dye quality

Gelding
Gelder
less likely to be injured

Soap making
Soaper
speed only

Wood burning
Wood burner
speed only

Potash making
Potash maker
speed only

Lye making
Lye maker
speed only

Milling
Miller
speed only

Brewing
Brewer
speed only

Plant gathering
Herbalist
speed; success and plant yield (stack size)

Plant processing
Thresher
speed only

Cheese making
Cheese maker
speed only

Milking
Milker
speed only

Shearing
Shearer
speed only

Spinning
Spinner
speed only

Cooking
Cook
speed; meal and ingredient quality

Pressing
Presser
speed only

Beekeeping
Beekeeper
speed only[Verify]

Fishery worker
Fishing
Fisherdwarf
speed; fish stack size

Fish cleaning
Fish cleaner
speed only

Fish dissection
Fish dissector
speed only

Metalsmith
Furnace operating
Furnace operator
speed only

Weaponsmithing
Weaponsmith
speed; weapon quality

Armoring
Armorsmith
speed; armor quality

Blacksmithing
Blacksmith
speed; item and furniture quality

Metalcrafting
Metal crafter
speed; craft, item, decoration, designed building quality

Jeweler
Gem cutting
Gem cutter
speed; gem craft quality

Gem setting
Gem setter
speed; decoration quality

Craftsdwarf
Bookbinding
Bookbinder
?

Papermaking
Papermaker
?

Leatherworking
Leatherworker
speed; clothing, decoration, craft quality

Woodcrafting
Wood crafter
speed; craft quality

Stonecrafting
Stone crafter
speed; craft quality

Bone carving
Bone carver
speed; craft, decoration quality

Glassmaking
Glassmaker
speed; craft, item, furniture quality

Weaving
Weaver
speed; cloth quality

Clothesmaking
Clothier
speed; clothing, decoration quality

Strand extraction
Strand extractor
speed only

Pottery
Potter
speed; craft, item, furniture quality

Glazing
Glazer
speed; glaze quality

Wax working
Wax worker
speed; craft quality

Engineer
Siege engineering
Siege engineer
speed; part, ammunition quality

Siege operating
Siege operator
speed; accuracy

Mechanics
Mechanic
speed; mechanism, furniture quality

Pump operating
Pump operator
none

Hauling
Stone hauling
No associated skill

Wood hauling

Item hauling

Burial

Food hauling

Refuse hauling

Furniture hauling

Animal hauling

Trade Good Hauling

Water Hauling

Push/Haul Vehicle

Other Jobs
Cleaning
No associated skill

Lever operation

Road building

Wall/floor construction

Some jobs are not associated with a labor: eating, drinking, sleeping, going on break, partying, cleaning themselves, and resting.

A few things are listed as "No Job" but can be considered labors in a different sense: running scared, not having a path to any place useful, and being insane.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Take note before trying to get dwarves to do stuff, they probably won't do it. it's just the sad truth....dwarves are so stupid that when they run out of food, they won't even step outside to get that juicy plant sitting right outside the gate, unless you micro-manage them to death. another famed example: a forgotten beast is walking through a tunnel to your fort, so smart ol' you, decides to build a wall. You then tell someone to do it. Luckily for you, Urist McForgotWhatSide builds the wall. He will take a stone, most likely from across the map, haul to the wall, begin building, and have to get a drink. He drops the stone to get some beer, well, while he's up there, he might as well take a quick nap. well, he finally wakes, goes down to build a wall, only to see Urist McMason stole his rock, so he goes across the map for another boulder. He finally finishes the wall, but hears voices on the other side, "You built from the wrong side!" he then hears a hiss from down the tunnel. The forgotten beast walks up to Urist McForgotWhatSide, and bites him in the head: the severed part sails off in an arc. Poor old Urist, "died of old age".

"Put both your backs into it!"

\
