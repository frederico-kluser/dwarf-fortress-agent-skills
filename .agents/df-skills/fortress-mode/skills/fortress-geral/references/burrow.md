# Burrow

> Fonte: [Burrow](https://dwarffortresswiki.org/index.php/Burrow) — Dwarf Fortress Wiki (GFDL/MIT)

**Burrows** are user-defined areas in your fort for restricting jobs or/and dwarves. They are a way to limit the jobs your dwarf takes, what items they use or where they go, thus being an important tool for Fortress Defense. A burrow can be used for one, multiple, or all of the above at once.

## Defining a new burrow

To enter the "define burrow" mode, press .

You'll be presented with a list of all of your existing burrows. Change which burrow is selected with your secondary selection keys (,,, & ).

To add a new burrow to the list, press . The new burrow created this way starts with no tiles and a default name.

To configure an existing burrow, select it, then press to set the burrow's ame, hange the symbol used, and define what tiles it encompasses by setting/easing tiles. Defining the burrow's tiles can be done using keyboard to make rectangles or drawing with the mouse much like designating tiles. A burrow does not need to be contigious and can extend into unrevealed space and other burrows - in the latter case, it can help use different colors and symbols to help tell them apart.

### Deleting Burrows

Deleting a burrow is easy, just enter "define burrow" mode by pressing , select the burrow to delete, then press , and confirm with . Uniquely to burrows, erasing all tiles in a burrow will not delete it.

## Uses for Burrows

### Limiting civilian citizen jobs

Activation: Select the burrow with secondary selection keys, then press to view citizens & resident list⁎, scrolling through it with those same keys and using to add or remove one or more to/from the burrow.

A citizen limited thus will only accept jobs and items inside the burrow. When a citizen is in multiple burrows, they can accept jobs and items from all of them. Note that "job" here covers nearly anything a dwarf may do outside of walking, fighting and socializing, including tasks such as idle individual combat drills†, picking up babies or equipment, or even sleeping. Nor will they try to eat or drink anything outside the burrow until starving or dehydrating.

**Burrow assignments do not restrict citizen movements**; An idle dwarf can take a stroll outside the burrow they're assigned to and they'll stand wherever they happen to be until assigned a task inside the burrow which they can path to. Additionally, citizens may walk from one point of the burrow to another point even if the path they walk on is not part of the burrow. If you define a burrow which is split into two areas, the citizens may walk between those two areas, outside of the burrow you defined.

Furthermore, this setting doesn't restrict jobs itself either. Should a job request an item not in the burrow, the dwarf will cancel the job. Then they'll look for a job again - often the one they just cancelled, thus entering a loop.

As such, a dwarf's burrow should include:

- All places they work at, sleep, eat, drink.
- All tools, raw materials, fuel and items they need for above.
- All places the stockpiles they store items in draw from.
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

Activation: Select the burrow with secondary selection keys, then press to toggle the limit.

This setting behaves as if workshop or furnace or trap is linked to take from stockpile. A building is considered affected by this setting when their center tile is in the burrow. A building limited by multiple burrows will be able to use materials from all of them.

- Like with stockpile links, take care to include *all* items a job needs in the burrow area.

There are some notable differences from using links, however:

- Burrows will not generate jobs, nor will they keep any items inside them from being hauled away to a stockpile elsewhere.
- Burrows are not considered buildings, and as such have greater freedom of placement; allowing one to limit their looms to all webs in safe areas, masons to nearby freshly dug stone, or smelter to take both nearby ore and bars in another smelter.
- Items dropped in center tile of workshop must necessarily be available to it, which can result in unwanted behaviour such as decorations on old clothes.
- It is easier to verify whether a given workshop is limited by burrows, as you only need to scroll through your burrow list while looking at it.

Keep in mind that this affects only workshops and furnaces, and not any other buildings that accept items for their jobs such as traps, stockpiles, farms, etc...

Unfortunately, this feature can be enabled accidentally - (pressing twice enters the burrow menu and toggles workshop restrictions for the first burrow). Due that it can be desirable to reassign one of these keys.

### Civilian Alerts

Activation: In main menu, hit to bring up the military menus, and for alerts.

(Optionally, using and arrow keys, select an alert you want civilians to currently use with (default first entry, marked with ) in leftmost column - optionally creating a new one with or using to rename one.)

Then, navigate to the right and use and arrow keys to select the burrow(s) you want civilians to be restricted to with .

To unactivate, unassign the burrow(s) or choose another alert to restrict civilians to.

Unlike individual citizen burrow assignments, a civilian alert will apply to all fort civilians and animals. It will order them to go and stay inside the burrows defined in the alert for as long as the alert is active and includes any. Additionally, for that time individual assignments are ignored.

Most jobs and activities will be cancelled when cut off by civilian alert. However, one should take a look around for any heavy item carrying stragglers that are trying to slowly move their items to inside the burrow, and stop their job so they can drop the item and flee faster.

### Defending an Area

''Full article: Scheduling

Burrows are one of the ways you can give passive orders to squads and civilians during alerts. Under the squad schedule menu (Press ) you can add an order to any particular month for the chosen alert with or edit their existing orders with . On the Give Orders menu, use to cycle through the orders given to squads. The order "Defend Burrows" **cannot** be given without first creating burrows to assign defenders to. Under a "Defend Burrows" order, dwarves in the squad will go to exactly in the specified tile(s) and will defend it proactively - however, schedules don't switch until next day arrives.

### Broker to the Depot, STAT

You can define your trade depot as a burrow, then when the traders appear, add your broker to that burrow. He will then only accept jobs at the trade depot, though he may be delayed if he is asleep or fulfilling an urgent need. This is particularly useful if your broker insists on performing other jobs instead of manning the depot.

### Alternative to Hot Keys

You can define small burrows to areas you would like to zoom to. Then by pressing "w", select the burrow, "z" to 'center on burrow' your view will be moved to earliest map block where burrow still has placed tiles. This is useful when you run out of hotkey slots.

### Causing Insanity

If a dwarf is assigned to a burrow with no beds, then that dwarf can't sleep. If he stays Very Drowsy long enough, then he'll go insane. Whether this is a goal or danger to be avoided depends on your play style. It's easy to accidentally do this to children, since they'll keep on playing without giving much of a sign that they're about to have a mental breakdown.

## Bugs

Burrows can be powerful tools, but that also means they have the potential to cause many problems.

- Dwarves try to store equipment they're no longer using outside their burrows, spamming cancellations when unable.

- Haulers in burrows stand around contemplating hauling jobs they can't perform.

- Dwarf cancels Store Item: Item inaccessible" message spam results from idle dwarves being in a burrow that contains a stockpile but not the item the stockpile wants to have. If you want to move items from outside the burrow to the inside without generating cancellations, you can put a stockpile on the boundary (to be accessed by non-burrowed dwarves) and use a minecart with a track stop set to dump onto a link-only stockpile inside the burrow. This way, the stockpile outside the burrow will not generate (impossible) jobs for the burrowed dwarves and the items will be moved to the inside by the non-burrowed dwarves, then happily to be picked up by the burrowed ones.

- Civilians assigned to a burrow while hauling constantly spam "drop-off inaccessible".

- Dwarves cancel repeating workshop jobs which they personally cannot complete due to their burrow lacking materials.

- Burrow-assigned dwarves abandon wheelbarrows when passing through non-burrow tiles.

- Mothers spam cancellations when attempting to recover a baby outside of their burrow.

- Dwarves get stuck trying to perform jobs at edge of burrow.

- Dwarves may remain restricted to a deleted burrow.

- Spouse room assignments behave oddly when spouses are in different burrows.
