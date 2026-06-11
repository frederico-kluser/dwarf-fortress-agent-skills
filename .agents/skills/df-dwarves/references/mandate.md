# Mandate

> Fonte: [Mandate](https://dwarffortresswiki.org/index.php/Mandate) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

 A **mandate** is a noble's request that your dwarves produce a certain item or type of item, or an export ban on certain items. Starting nobles such as the expedition leader will not make mandates; upgraded nobles like the mayor will. Fulfilling the mandate gives the noble a happy thought.

Mandates should not be confused with demands.

Only some nobles make mandates, and the number of mandates that can be active simultaneously varies:

- **1 mandate:** Baron, Mayor
- **2 mandates:** Count
- **3 mandates:** Duke
- **5 mandates:** Monarch

Mandates are announced on the left of the screen as their own announcement, but to see the actual details of the mandate or if a noble is mandating anything you need to check the noble's screen. If the uppercase bracketed word '\[MANDATE\]' next to a noble's name is grey, he is making no mandates. If brown, he is making a production mandate, and you have a lot of time to complete it. If yellow, you have a month or two before the mandate expires. If red, the mandate will expire very soon. If white, then it is an export ban.

The mandates of a noble will end automatically when the noble dies. The mandates of a mayor end instantly when they are voted out of office, but will remain in force if a mayor is replaced by nominating another one from the nobles screen. If the replaced mayor has no other administrative position, such a lingering mandate will only be displayed on the dwarf's personal thoughts page, not on the nobles screen, and is thus easy to overlook and accidentally violate.

## Production Mandate

When a noble makes a production mandate, you will have roughly half a year to fulfill it. These mandate the production of certain goods, specifying the desired type, just like export bans. In previous versions, items (of any type) of a desired material could be mandated.

Getting the required items from a caravan will not fulfill a mandate. If a production mandate expires without being fulfilled, the noble will get an unhappy thought, and one or more dwarves will be sentenced to punishment for the 'violation of production order' crime. The dwarf chosen tends to have a skill appropriate to the mandate, but random dwarves may be chosen as well. If the noble can't sentence any dwarves for punishment because all your dwarves are nobles, or the sentenced dwarves can't be punished because no officer is assigned, he will get another unhappy thought. Delaying fulfillment of an easily-achieved production mandate may prevent another, worse, mandate from being enacted (for a few months, at least). The color of the mandate indicator on the Nobles screen changes from brown to bright yellow to red, as the deadline approaches. You can determine your progress towards fulfilling the mandate by viewing the n (then hit enter on the Noble with a mandate), and you will see the mandate listed like this example "Mandates: Make floodgates (2/3)", where in this example we have produced one floodgate and still need to produce two more. Once you produce the mandated items, the mandate goes away and nothing special happens to the items. They just go into your inventory, so on the not-outside chance the noble actually requests something useful (like armor, a weapon, or furniture) it's not a total waste. Choosing a Baron with a preference for useful items can help with this (as discussed below).

In a busy fortress, it's easy to miss the announcement of a production mandate. One way to avoid this is to change the NEW_MANDATE line in announcements.txt to \[NEW_MANDATE:A_D:D_D:P\] Another option is using the manager to create a work order for three goods every quarter.

## Export Bans

Export bans forbid the export of a certain item type, like greaves. These bans are temporary, they last about half a year (approximately the same length of time as a production mandate) and then are ended by your noble.

Violating an export ban by trading any of the item away is a crime for each of the haulers who brought a prohibited item (that was sold) to the trade depot - each dwarf will be incriminated the instant the item is carried off the map (whether by a pack animal or a wagon). While selecting goods to be brought to the depot, the "culling on mandates" option will prevent banned objects from being selected, though if a finished goods bin contains a single banned object, the entire bin will be excluded. Items that are subject to export bans are displayed in purple text in the trade window. Note that if an item is traded to a caravan and is subsequently placed under an export ban, dwarves **will** be punished even though the trade took place before the ban went into effect, so if the caravan hasn't already left, any banned goods should be immediately purchased back from the traders; if a good was *offered*, then nothing can be done (aside from exploiting various oddities in the trade system, or arranging an unfortunate accident). Oddly, trading banned items which were carried to the depot in bins (but not the bins themselves) does *not* result in any perceived crimes, perhaps because only the bin was brought to the depot, not the items inside it; however, the noble that issued the mandate will receive an unhappy thought that nobody could be punished.\[Verify\]

Melting a banned item also does not violate the restriction.

## Mandates & preferences

Personal preferences determine what type of items a noble bans for export or wants to have produced via mandates. Nobles with a preference for a specific item will either ban that item or mandate its production. Nobles with no preference for a specific item type will never issue any mandates.

Nobles with preferences for items you don't want excluded from trade or that are just too hard to produce (a judgment call) will be a problem for your fortress. You have, however, (limited) control over choosing one noble who makes mandates, for example when appointing your baron, or overriding dwarven elections by appointing a mayor you prefer. Choose your baron or mayor wisely: take a look at their preferences, and decide if they might be a problem. For example, anvils take three bars (or nine adamantine wafers) to make, and can only be produced from a few weapons-grade metals (and many good sites lack iron ores), thus regular mandates for their production may be hard to fulfill. But even a ban on the export of mugs can be a problem if a fort relies on them as a trade good. If unavoidable, such nobles may be destined for an unfortunate accident - for the good of the fortress as a whole.

## Requirements

These are the criteria for a noble to issue a mandate[1]:

- Hasn't made a mandate/demand lately, the period can be adjusted in difficulty settings.
- Isn't dead, hasn't left the map, isn't a projectile, and isn't caged
- Isn't insane (or in the middle of a mood)
- Isn't incapacitated (unconscious, webbed, or paralyzed)
- Isn't nauseated, winded, stunned, dizzy, or feverish
- Isn't bleeding
- Has a soul
- Is a member of your fortress

It isn't currently known if exposure to cave spider venom, which causes permanent mild dizziness, is sufficient to prevent mandates. Other procedurally-generated syndromes can cause temporary illnesses, which may also block mandates if applied periodically.

## Bugs

- A mandate will remain in effect even after the noble who issued it (a mayor, for example) has been replaced.Bug:3047
