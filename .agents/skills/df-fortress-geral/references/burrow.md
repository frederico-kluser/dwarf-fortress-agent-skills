# Burrow

> Fonte: [Burrow](https://dwarffortresswiki.org/index.php/Burrow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Burrows** are user-defined areas in your fort for restricting jobs or/and dwarves. They are a way to permanently or temporarily:

- limit the jobs for a dwarf or group of dwarves
- limit what items they use
- limit where they go

A single burrow can be used for one or more of the above at the same time, and can become an important tool for organizing your fortress, its workers and its defense.

## Burrows Menu

Open the burrows menu with U.

Initially, you will only be given the option to Add new burrow (see next, below). Once you have one or more burrows designated, the screen will look more like this:

The above example has only 2 burrows currently designated. Each burrow consists of 2 rows of information:

- First Row

- Burrow Symbol *(click on the icon to change)*
- Name of Burrow *(click on feather icon to change)*

*and*

- : recenter the map on the burrow
- : to repaint the burrow
- : delete the burrow

- Second Row

- Number of currently assigned citizens
- : manage who is currently assigned to this burrow (dwarves and other citizens)

*and*

-  *or* : designate whether workshops in the burrow will or won't source materials from *outside* the burrow
-  *or* : designate whether the burrow is active or suspended

### Designating Burrows

Clicking the "Add new burrow" button prompts you to paint what the burrow encompasses (similar to designating a zone or stockpile), then provides a menu for specifying the burrow's symbol and colors.

- Note: When designating a burrow, consider *all* the needs of the dwarves that will be assigned to that burrow, possibly including jobs and workshops, stockpiles, eating/drinking/socializing, worshiping, sleeping, and so on. Or not - you might want a group of dwarves to focus on a job until you release them - it's all up to you.

Note that a dwarf *can* walk out of a burrow to get to another part of it. A burrow does not need to be contiguous and can extend into other z-levels, and even into unrevealed space and overlap other burrows. In the latter case, it can be helpful to use different burrow symbols and/or colors to easily tell them apart.

### Assigning Citizens

Citizens can be assigned to any number of burrows, including none at all.

The burrow assignment menu appears as follows:

On the top you can quickly assign all civilians (those not in a military squad) to the burrow, remove all civilians from the burrow (by selecting none), and similarly for soldiers.

Citizens assigned to 1 or more active (i.e. non-suspended) burrows will only accept jobs from within their assigned burrow(s). Furthermore, they will not venture outside of their assigned burrows to collect resources for a job, no matter what the setting is for workshops sourcing materials outside the burrow.

Note that active military orders (kill/train/etc) *override* burrow assignments (for example, soldiers will perform training in their barracks if ordered/scheduled to do so, regardless of whether they are assigned to burrows that encompass the barracks). See \#Limiting civilian citizen jobs for caveats and problems that this can cause.

All this can lead to some non-intuitive behavior, and a lot of job cancellation spam. An example of such odd behavior is that when a citizen is assigned to 2 burrows (with material sourcing from anywhere), they will bring materials from 1 burrow to the other burrow to perform a job, but will not haul items from one burrow to stockpiles in the other.

Citizens not assigned to any active burrows will completely ignore burrow designations. For example, they may perform jobs within any burrow (or outside of any burrow designations), haul items into/out of any burrow, sleep/eat/drink/worship/socialize anywhere, etc.

### Suspending Burrows

"Assigned citizens will not respect burrow restrictions"; when a burrow is suspended, the game behaves as if you had deleted this specific burrow, until you turn it back on again.

For example, this can be useful to define a "safe" burrow with food and drinks, locked away from the outside world. Assign all of your non-military, keep the burrow "suspended" by default, and only activate it when a threat shows up, to pull your civilians back to a safe part of the map. This can serve the function of the now defunct civilian alert (and is recommended for advanced forts).

### Workshops Material Sourcing

Normally, materials for a job can be pulled from anywhere, sometimes from far, far across the map. With this function (), jobs for workshops inside the burrow will not allow for the material to be brought from outside of the burrow. With creative drawing of a burrow, this can specify raw materials to use (or not to use).

This can be used as an alternative to (or in combination with) linked stockpiles. See \#Limit workshops to burrow.

## Uses for Burrows

### Limiting civilian citizen jobs

Activation: Select the burrow with secondary selection keys, then press c to view citizens & resident list⁎, scrolling through it with those same keys and using Enter to add or remove one or more to/from the burrow.

A citizen limited thus will only accept jobs and items inside the burrow. When a citizen is in multiple burrows, they can accept jobs and items from all of them. Note that "job" here covers nearly anything a dwarf may do outside of walking, fighting and socializing, including tasks such as idle individual combat drills†, picking up babies or equipment, or even sleeping. Nor will they try to eat or drink anything outside the burrow until starving or dehydrating.

An illustration demonstrating that a burrow does \*not\* restrict a dwarf's movement--the metalcrafter marched right out of his burrow to pull the right lever.

**Burrow assignments do not restrict citizen movements**; An idle dwarf can take a stroll outside the burrow they're assigned to and they'll stand wherever they happen to be until assigned a task inside the burrow which they can path to. Additionally, citizens may walk from one point of the burrow to another point even if the path they walk on is not part of the burrow. If you define a burrow which is split into two areas, the citizens may walk between those two areas, outside of the burrow you defined.

Furthermore, this setting doesn't restrict jobs itself either. Should a job request an item not in the burrow, the dwarf will cancel the job. Then they'll look for a job again - often the one they just cancelled, thus entering a loop.

As such, a dwarf's burrow should include:

- All places they work at, sleep, eat, drink.
- All tools, raw materials, fuel and items they need for above.
- All stockpiles they store items in.
- All stockpiles they take items from.
- For wheelbarrowed haulers, all the tiles they push the wheelbarrow on.

Take care to avoid dwarves having labors that result in them taking jobs that demand items outside the burrow:

- Food hauling and food stockpile that takes from anywhere.
- Feed Patients/Prisoners and a patient with buckets/water sources out of range.
- Seek Infant and a baby dropped outside the burrow.

Should one still need to use hauling labors, they should limit their stockpiles to links only and use Minecart hauling systems to move the requisite goods from outside the burrow to in. Otherwise, dwarves not assigned to the burrow can still do jobs in its area, including moving food inside.

⁎ The order of the citizens in the list is based on an internal ID number, which only loosely correlates with arrival time.

† However, active military dwarves are unaffected and can even perform those same drills.

### Limit workshops to burrow

Activation: Select the burrow with secondary selection keys, then press w to toggle the limit.

This setting behaves as if workshop or furnace or trap is linked to take from stockpile. A building is considered affected by this setting when their center tile is in the burrow. A building limited by multiple burrows will be able to use materials from all of them.

- Like with stockpile links, take care to include *all* items a job needs in the burrow area.

There are some notable differences from using links, however:

- Burrows will not generate jobs, nor will they keep any items inside them from being hauled away to a stockpile elsewhere.
- Burrows are not considered buildings, and as such have greater freedom of placement; allowing one to limit their looms to all webs in safe areas, masons to nearby freshly dug stone, or smelter to take both nearby ore and bars in another smelter.
- Items dropped in center tile of workshop must necessarily be available to it, which can result in unwanted behaviour such as decorations on old clothes.
- It is easier to verify whether a given workshop is limited by burrows, as you only need to scroll through your burrow list while looking at it.

Keep in mind that this affects only workshops and furnaces, and not any other buildings that accept items for their jobs such as traps, stockpiles, farms, etc...

Unfortunately, this feature can be enabled accidentally - (pressing w twice enters the burrow menu and toggles workshop restrictions for the first burrow). Due that it can be desirable to reassign one of these keys.

### Civilian Alerts

In previous versions, civilian alerts could be used to force all civilians and animals to remain inside a burrow, ignoring their individual assignments for the time being. In the current version v50.07, this feature is missing due to UI and time constraints. The ability to assign all civilians to a burrow replicates some of its functionality. DFHack adds the full feature back to the UI if you have it installed.

### Defending an Area

*Full article: Scheduling*

Burrows are one of the ways you can give passive orders to squads and civilians during alerts. Under the squad schedule menu (Press m s) you can add an order to any particular month for the chosen alert with o or edit their existing orders with e. On the Give Orders menu, use o to cycle through the orders given to squads. The order "Defend Burrows" **cannot** be given without first creating burrows to assign defenders to. Under a "Defend Burrows" order, dwarves in the squad will go to exactly in the specified tile(s) and will defend it proactively - however, schedules don't switch until next day arrives.

### Broker to the Depot, STAT

You can define your trade depot as a burrow, then when the traders appear, add your broker to that burrow. He will then only accept jobs at the trade depot, though he may be delayed if he is asleep or fulfilling an urgent need. This is particularly useful if your broker insists on performing other jobs instead of manning the depot.

### Alternative to Hot Keys

You can define small burrows to areas you would like to zoom to. Then by pressing "w", select the burrow, "z" to 'center on burrow' your view will be moved to earliest map block where burrow still has placed tiles. This is useful when you run out of hotkey slots.

### Causing and Managing Insanity

If a dwarf is assigned to a burrow with no beds, then that dwarf can't sleep. If he stays Very Drowsy long enough, then he'll go insane. Whether this is a goal or danger to be avoided depends on your play style. It's easy to accidentally do this to children, since they'll keep on playing without giving much of a sign that they're about to have a mental breakdown.

Ironically, some dwarves going insane can be easily managed with a burrow. Despite their wild and irreversible mental state, dwarves can comply with the limited area of the burrow. This can be extremely useful for keeping insane and potentially harmful dwarves away from the general population, as well as keeping others from seeing the corpse of the insane person when they inevitably die.

## Bugs

Burrows can be powerful tools, but that also means they have the potential to cause many problems.

- Dwarves cancel repeating workshop jobs which they personally cannot complete due to their burrow lacking materials.Bug:2262
- Burrow-assigned dwarves abandon wheelbarrows when passing through non-burrow tiles.Bug:6484
- Dwarves get stuck trying to perform jobs at edge of burrow.Bug:2416
- Dwarves may remain restricted to a deleted burrow.Bug:1735
- Spouse room assignments behave oddly when spouses are in different burrows.Bug:2442
- Dead dwarves cannot be removed from burrows, and will still appear in the count after death. Bug:8121
