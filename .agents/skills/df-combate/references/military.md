# Military

> Fonte: [Military](https://dwarffortresswiki.org/index.php/Military) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **military** is one of the most important aspects of a successful fortress. Even with many traps, drawbridges and other defenses, your military will still need to fend off goblin sieges, megabeasts, titans, and fiendish underground beasties. Using a combination of squad orders and scheduling, you can set up an elaborate offensive, defensive, or balanced military structure for your well-equipped soldiers to follow. Turning your dwarves from useless migrants into bloodthirsty killing machines never hurts (except the enemy, of course).

**WARNING! Mining, woodcutting, and hunting have a "civilian uniform" that conflicts with *all* military equipment. Assigning any dwarf with the mining, woodcutting, or hunting labors enabled to the military is strongly discouraged.**Bug:1451

The military system is rather extensive and complex, and there is a lot of documentation. Here is a list of key documents categorized by expertise level:

- **Beginner:**
  - Attack is a *very* simple "How to attack a target" guide. This is useful if you don't know anything about the military, and just want to order some (untrained) dwarves to (suicide) attack something, *now*.
  - Military quickstart will teach you to set up and train your very first properly-organized squad.

- **Intermediate:**
  - Squads helps you understand everything about squads.
  - Military interface contains mostly complete documentation on the *military screen*.
  - Scheduling describes the squad scheduling system in more detail.
  - Military F.A.Q. is a list of frequently asked questions.

- **Advanced:**
  - Training will give you insights about combat training.
  - Military Design provides specific advice on how to get your soldiers prepared for any threat.
  - Security Design will give you specific suggestions on the physical defenses that will defend your military.
  - Defense Guide is a general overview of threats and considerations for fortress defense.
  - Trap Design contains information on complex traps that are not a minor/optional part of a larger defensive plan (but might be adapted or plugged into one).
  - The Marksdwarf Training Guide is an in-depth guide on getting marksdwarves reliably training, while noting and providing workarounds for bugs related to marksdwarfs, reloading, and ammunition.
  - The Military Testing page contains community tests of different combat scenarios carefully planned out in the Arena, and results of each. You may find some useful information about results of combat variables contained within.

The rest of this guide contains an overview of military features (with links to associated sections of other documents).

## Quick Reference

From the main menu:

- The **squad** screen is accessible through the q key.
- The **burrows** screen is accessible through the U key.

## Creating a Military

While it may be confusing to a new player, the military system makes up for its initial impenetrability with its versatility. Using the military interface, squads can be assigned, reordered and restructured at will, dwarves can be set to equip a highly specified uniform along with the rest of their squad or stand out and equip something unique, and you can give incredibly detailed commands and programming to your squads to follow out based on time of year, circumstance, location, and user convenience. That being said, there's a lot to be learned.

### Squads

**Squads** are the groups of soldiers that make up your military. Your military is led by the appointed **militia commander** (or, if the monarch is present, the general), and has many other squads led by **militia captains** (or captains) under them. Creating a squad in the military screen is one of the first things you should do when starting your military.

### Equipping Soldiers

Rather than simply pick a level of equipment and hope your dwarves pick up the right stuff, you can select what your dwarf will wear by item type or specific item, or create a new uniform template and apply it to a dwarf or entire squad all at once. This includes the material and color of your soldiers' uniform. For example, you can create identical armored units with intimidating red cloaks or just slap something together based on need and circumstance, up to and including artifact weapons/armor.

## Directing Soldiers

Getting your military to actually *do* something is somewhat difficult. It is possible to give your squads different monthly **schedules**, create different **alert levels** which will cause squads to follow out user-programmed instructions depending on circumstance, give **direct orders** to **attack** one or more specific targets or **move** to a specific location, or follow **patrol routes** and **stations** with greater accuracy.

There is a clear difference between *active* orders and *passive* orders-- the latter is programming that a dwarf will follow to the letter and acts more as a defense method, and the former is used for taking the fight to the enemy. The *squads* menu is predominantly used for active commands, and the *alert* and *scheduling* menus are used for passive commands.

### Active Command

Orders in the squad menu

In the military, soldiers operate much more like part-time militiamen than full-time warriors. When soldiers are not passively doing their civilian duties or following their schedule programming, they can be actively sent to do small tasks to aggressively defend your fortress. After these orders have been carried out or cancelled, your dwarves will happily return to their passive programming as if they were never interrupted. It is possible to select multiple squads or specific dwarves to carry out these orders.

Your forces can be commanded to carry out two types of orders: **Move** orders and **Attack** (or **kill**) orders. Move orders are much like the 'station squad' command in previous versions; your selected dwarves will run to wherever you've sent them. Similarly, attack orders will select an enemy (by location on screen, general area on screen, or list) and send your dwarves charging off that way.

Soldiers following orders will attack any hostiles they encounter on their way to their destination as well as wild animals and whatever other creatures they might encounter, whether you like it or not. As a result it is very difficult to attack members of an enemy group with any sort of precision, and if your dwarves cannot take down their target there is no real way to get them out of combat; it's do-or-die. It is unknown whether this is a bug or a feature.

Orders can be cancelled through the squads screen, but your dwarves tend to be so enthusiastic that they'll just ignore you in their bloodlust. This is likely a bug.

### Passive Command

The **alert level** and **scheduling** system is a feature that is both incredibly versatile... and, initially, completely impenetrable. Once you learn the system, though, you will find that you barely need to manage your military at all. Effectively, a schedule is programming for a squad to follow within an alert, broken up by month, and alerts can be quickly and easily swapped in order to apply different schedules of your choosing to different squads of your choosing. Without scheduling, alert levels would do nothing; without alert levels scheduling would be horribly inefficient; the two functions co-exist and rely on each other.

It is possible to give your squads different monthly schedules, create different alert levels which will cause squads to follow out user-programmed instructions depending on circumstance, give direct orders to attack one or more specific targets or move to a specific location, or follow patrol routes and stations with greater accuracy. The entire system (including alert names) is completely configurable, and in time you will find yourself using complicated scheduling to rotate squads between training and defending/patrolling specified areas over the course of a year without any user input, or to start defending the fort entrance or trader route with a few easy key presses.

Civilian alert levels are also possible - civilians can be restricted by **burrow** to where they can roam should the need to tuck them away into a panic room arise. If a dwarf restricted to a burrow is not there, he will do his best to make the journey.

The scheduling screen is broken up into a list of squads, months, alert types and **order criteria**. Each order (applied to one month; multiple orders can be stacked on one month as well) can be given criteria to define how many dwarves within a squad will follow its programming at once, allowing you to make a few dwarves out of the squad active at a time while the rest go about their business or to make the entire squad always active for a matter of the utmost importance, foregoing food, sleep, and booze. You can also choose which positions in a squad the order will prefer to utilize when forcing a squad to follow it.

Four types of orders can be given (as well as the 'inactive' command), defining different types of patrolling or stationary defending. Squads can spar and be given combat demonstrations in the **barracks**, defend a **burrow**, patrol a **route**, or defend a single **station**. The monthly schedules can be named so as to better suit your needs, and a copy/paste system is available to eliminate some of the tedium in creating fancy scheduling for many months. The display can also be flipped around.

Barracks can serve the needs of multiple specific squads at once. A barracks can be defined as a place to train, sleep, store squad equipment, store individual equipment, or any combination of the above, in any weird overlapping combination of barracks you like. Barracks are necessary for training.

When dwarves are being ordered to train, squad leaders will set up training classes for particular skills, or they will have dwarves spar. Any dwarves in the squad that don't qualify for these will default to individual training. In the current release, training classes are bugged where if a squad leader sets up a training class, he will wait forever (Or until you change his orders) for students, even if nobody shows up. Likewise, if students decide to request a class and the squad leader is doing individual training, they will wait for him to finish, even if they start starving. Thus, at the moment it's best to alternate your forced training schedules with downtime so the longest a dwarf will be stuck waiting is a game month (which isn't long enough to die), or just leave them off duty all the time and have them do individual training only, at least until this issue is fixed.

## Frequently Asked Questions

## Bugs

- When selecting new dwarves to place in a squad the cursor always returns to the first available dwarf instead of remaining where it is.
- There are still various problems with dwarves not equipping what they should; most notably, dwarves will not remove conflicting clothing to don assigned armor. Toggling to "replace clothing" is recommended, at least temporarily.Bug:535 Note, however, that soldiers may unequip clothing before armor for that part is available.
- Mining, Hunting, and Wood cutting labors have "invisible uniforms" that conflict with military uniforms (and each other).Bug:1451
- Military dwarves going on duty carry any currently-hauled items with them to training, pickup equipment, and even into battle.Bug:2561
- If a Marksdwarf claims a stack of bolts in a chest, no other Marksdwarves will take from that chest.
- Marksdwarves won't pray, which will cause them to get increasingly angry until they go insane.
- Marksdwarves may not grab bolts if there were no bolts available on squad creation. Bug:0012008
