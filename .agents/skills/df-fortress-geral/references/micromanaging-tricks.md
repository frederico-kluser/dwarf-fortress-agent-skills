# Micromanaging tricks

> Fonte: [Micromanaging tricks](https://dwarffortresswiki.org/index.php/Micromanaging_tricks) — Dwarf Fortress Wiki (GFDL/MIT)

While some aspects of Dwarf Fortress appear to be designed to discourage micromanagement, others reward or require constant user manipulation. This page is a collection of tricks to micromanage your dwarves and compensate for Dwarven AI.

## General

- Use a civilian alert burrow to keep your dwarves in - and out of - specific locations.
- Instantly locking doors can reliably keep a dwarf in a specific location (and doing a specific job), or prevent them from doing something ridiculously stupid.
- Order a dwarf to go to a specific location by building an unconnected lever, setting the profile on the lever to the specific dwarf, then ordering the lever be pulled. This works for Nobles too, but can be delayed by any other jobs the dwarf is currently tasked with.
- Order a dwarf to go to a specific area by drafting him into the military and issuing a "move" (station) order. Note that this can make your dwarf charge \*towards\* any nearby enemies.
- You can burrow children (eventually) by assigning them to the burrow and to beds inside. Once they take a sleep job inside the burrow they will be unlikely to leave the burrow. You can stock the safe room with food, drink, and beds and leave the children there permanently.
- Cancel a "Store item in stockpile" job by finding the item in question and forbidding it. This can keep your dwarves from running through an active battlefield to collect the enemy's severed limbs. You can also set the default status for some items to forbidden under the standing orders menu.
- If you stop an active task in progress via joblist - the dwarf may not accept similar jobs for about a week.

## Mining

- The default priority for mining can be counter-intuitive to new users. To avoid miners running from one side of the fort to another for no apparent reason, it is recommend to designate areas to mine in batches with a unique priority. Designation priority explanation here: DF2014:Designations_menu#Priority.

## Advanced Mining Micromanagement

- Miners will select mining jobs with priority based on 1) decreasing Z coordinates (lower first), 2) increasing X coordinates (West first), and 3) increasing Y coordinates (North first).
- Avoid mining designations that will cause your miners to run back and forth between job sites repeatedly (such as channeling a moat in the North and South simultaneously).
- Use a locked door or burrows to limit mining in a specific area to a single dwarf (reliably prevents channeling "accidents"). Designate one tile for mining, wait until your dwarf is through the door, then lock it and designate all the tiles to be mined. Don't forget to free your miner after the work is complete.
- Remove a mining designation then re-designate it to transfer the job from a distant/slow dwarf to a close/fast dwarf who has already completed all the other mining in a specific area (will not work if the nearby dwarf has already taken another job elsewhere).
- After finishing a mining job, miners will automatically accept any adjacent mining jobs before reevaluating jobs by priority. Note that this does not work if the adjacent job has already been claimed by a different miner. (To avoid that you can distract your other miners with higher-priority designations elsewhere.)
- Single-tile wide tunnels are the most efficient designation. Use diagonal corners to avoid exposing two designated tiles (which will result in another free miner taking one of the two and potentially delaying mining significantly).
- To keep a single miner working in one area, you can manually designate one new mining tile immediately after he completes the previous one. (Best for limited jobs in high-risk areas; for larger jobs a locked door or burrow is highly recommended.)

## Building

- Buildings are prioritized according to a LIFO (last in first out) queue, meaning your most recently ordered construction will be built first. To increase priority on a previously-ordered construction, cancel it and re-order the construction.
- Designate a stockpile/dump near large construction projects so your masons/carpenters/metalworkers don't have to carry the construction materials across the map by themselves.
- If using a local stockpile, only order construction of as many buildings as can be supplied by your stockpile--any additional constructions will A) result in your builders dragging material across the map, and B) be completed \*first\*, so your stockpile won't deplete and your haulers won't be able to haul any more materials.
- Items (such as blocks) that are currently selected for a hauling task are unavailable for use in buildings. To free an item, pause the game, forbid the item, unforbid it, then issue the build order using the item before unpausing the game. You can also forbid an item that is currently being hauled and the hauler will drop it when he realizes it is forbidden.

## Cooking

- Use the 'z' Kitchen tab to select exactly which ingredients you want cooked.
- Combine large stacks of meat with a dwarf's "preferred" ingredient to create a large stack of "preferred" meals (for more happy thoughts).
- Multiple linked stockpiles feeding into a kitchen can force some variety in ingredient selection, and is necessary to effectively use liquid ingredients.

## Military

- Move (Station) orders only cause your dwarves to move to a 7x7 non-contiguous area around the location selected. To force them to move to a specific location (such as adjacent to a fortification), build statues (preferred), walls, or designate restricted traffic areas then order your dwarves to move from one side to the other.
- Alternatively, the move command does guarantee your dwarves will move to the Z-level selected. You can build your fortifications such that the only passable tiles on that Z-level are in the positions that you desire. (Note that dwarves will also run outside your fortifications to stand on any free tiles if possible.)

## Strange moods

- If you construct all the moodable workshops in your fortress with a specific type of material (e.g. chalk blocks), you can use the 'z' stocks menu to quickly forbid all your moodable workshops. Note that workshops need to be forbidden *before* the game notifies you of the strange mood.
- Placing unforbidden moodable workshops behind a locking door with stockpiles/dumps of your most valuable materials will result in high-value artifacts. You can even select the specific items used by forbidding all the items in the locked room, then unforbidding those you want your moody dwarf to use.
- Forbidding a specific item that a moody dwarf has collected will send him to fetch a replacement (if still in the collection phase) or remove it from the recipe (if already constructing).
