# Advanced marksdwarf training guide

> Fonte: [Advanced marksdwarf training guide](https://dwarffortresswiki.org/index.php/Advanced_marksdwarf_training_guide) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Marksdwarves can be tricky to equip and train properly for the uninitiated - they often appear to refuse to use their crossbows at archery ranges. This guide goes into details explaining known bugs, and getting your marksdwarves to train properly, as well as going into details regarding various ranged weaponry.

## Understanding ranged weaponry

In vanilla *Dwarf Fortress*, the raws define three types of ranged weapons, each with their own skill and ammo.

Ranged Weapons

Ranged Weapon
Ranged Skill
Melee Skill
Ammo

Crossbow
Marksdwarf
Hammerdwarf
Bolts

Bow
Bowman
Swordman
Arrows

Blowgun
Blowgunner
Swordman
Darts

Of these, dwarves can only craft crossbows and bolts. Bows and blowguns are gained either through trade or recovery from downed enemies. If playing a modded game, replace crossbow in the following with one of the above weapons, and proper ammo type.

## Equipping your marksdwarves

### The minimum outfit

At a minimum, each dwarf requires the following to successfully use the crossbow.

- One crossbow
- One quiver
- One stack of bolts for each marksdwarf to shoot

A quiver is equipped on the upper body slot. Due to a bug, sometimes a marksdwarf will fail to pick up a quiver if wearing heavy armor, a workaround for which is given below. Wood and metal bolts are generated in stacks of 25. Bone bolts are generated in stacks of 5.

### Crossbows

Crossbows can be made with wood or bone at a bowyer's workshop, or metal at a metalsmith/magma forge. Metal crossbows can be forged out of copper, bronze, bismuth bronze, iron, steel, or (not recommended) adamantine. Quivers must be made of leather at a leatherworks. The base material of a crossbow appears to have no effect on the lethality of ranged bolts. However, when marksdwarves end up in melee, they will use their crossbow to bash. This bash attack utilizes the hammerdwarf skill and deals blunt damage, thus it has been suggested to make crossbows from the most dense material available. However, as of v50+, this difference in metal density has been minimized for combat bashing damage *(see next)*.

#### Crossbow material

Bottom line, against unarmored opponents (i.e. most animals, kobold thieves, undead, etc.), all metal is overkill and will break bones and crush skulls with ease, and even wooden bashing weapons will pound with some authority. Against any armor, all metal works about the same as any other, while any anything less (i.e. wood/bone) will be mostly ineffective, end of discussion.

This means that for crossbows (and all bashing weapons) any of the weapons-grade metals are going to be very close to the same, and *far* superior to anything wood or bone. You can safely save your steel (and even iron and bronze) and use whatever metal(s) you have in surplus, and you're not hurting your marksdwarves by any amount that anyone would notice in game play. So, while wooden crossbows are admittedly a great early addition to your fortress defense, you definitely want to replace those before sending your marksdwarves out to face a siege.

To get more technical, bashing damage works differently than cutting or piercing; it relies on weight, but now also on the speed of the swing of the weapon - and *lighter* weapons are swung faster. While Copper (density 8,930) is almost 14% heavier than iron or steel (both 7,850), that extra weight also makes a weapon slower to swing, effectively negating that advantage. Steel is the hardest of the weapons-grade metals, and may have a (very) slight advantage there, further offsetting any difference in density. But in current game mechanics, these differences become very, *very* slight (often less than 1%).

This may not be *technically* true for wooden crossbows, where, for example, oak (density 700) is close to twice as dense as willow (at 390). However, the absolute densest wood, Blood thorn (1,250), is still less than than 16% the weight of any weapons metal. Unfortunately, swing speed does not become 6x as fast, meaning any wood is going to be painfully weak for melee by any measure. (For those curious, all bone is density 500, lumping it squarely in the same ineffective range as wood.) Urist OakenBow is going to suck if it comes down to melee against anything armored, regardless.

Note that Silver (density 10,490), notably heavier than other weapons-grade metals (by 17.5% or more), is not available for crossbow manufacture.

- See Material science#Attack Momentum for more technical information.

### Quivers and bolts

Please note that bolts are assigned to a *squad*, not to individual dwarves. The number of bolts assigned to a squad will be divided evenly between all occupied squad positions. (For example, if you have a squad of 10 marksdwarves, you need to assign *at least* 250 bolts to the squad for each position to equip 25 bolts.)

Quivers can hold between 25 and 49 bolts, and dwarves will pick up multiple stacks if necessary to reach a number in this range. In other words, dwarves will continue picking up stacks of bolts until they've got at least 25 in their quiver (or they run out of squad-assigned bolt stacks). Bolt stacks are collected in last-in-first-out order (LIFO); that is, dwarves will always go for the newest bolts in your fortress, even if there is an ammo stockpile three steps away from them. Each squad with marksdwarves must be assigned ammo. As they deplete it, the game will automatically add additional ammo to the squad if there is some in the fortress, again following the principle of LIFO.

### Avoiding equipment issues

The mining, wood cutting, and hunting labors have an "invisible uniform" that conflicts with military equipment. When these labors are enabled, a dwarf will drop all assigned military equipment when going off duty, and when ordered back on duty they spend extra time collecting their equipment, and may ultimately report without some equipment. For that reason, it is recommended that you disable mining, wood cutting, and hunting on all military dwarves.

An "equipment mismatch" error sounds dire, but it's just a diagnostic message telling you that a dwarf's assigned equipment changed while the dwarf was en route to pick up the previously-assigned equipment. In almost all cases the dwarf will automatically collect the newly-assigned equipment without player intervention. One reported cause of frequent equipment mismatch spam is ammo stored in bins.

## Setting your marksdwarf's barracks

### Understanding possible training activities

The first rule of marksdwarf training is that you do **not** assign them a normal barracks if you wish them to utilize the archery target for Archer and Marksdwarf XP - if they are assigned to a barracks, they will train as hammerdwarves with their crossbows vs. actually shooting bolts at the archery target. Furthermore, as the game gives precedence to melee training, they will almost never use an archery range, even if one is assigned, if they have a choice.

When training, a dwarf has four possible options, which they will take in roughly this order:

- Squad Training (Lead/Watch demonstration)
- Individual Combat Drill
- Spar (requires Competent Fighter skill)
- Archery Training

Squad training and sparring require multiple dwarves (and yes, marksdwarves **will** spar as long as they are Competent Fighter skill level, training their melee skills while doing so). Except for archery training, dwarves require a standard barracks to conduct any of the above activities. Notably, it is possible to actually train marksdwarves via demonstration, both Crossbow and Archery skills being trainable this way. By combining this with training orders, it is possible to make archery training the only valid option, and thus get them to train consistently.

### Building archery ranges

Thus, the first step is to build a room with a bunch of archery targets, it is recommended to build one archery target per filled squad position (multiple marksdwarves cannot train at the same archery target concurrently). The room must be large enough that the marksdwarf has a one-gap space between them and the target; some people just make their "barracks" 10x10, and put an ammo stockpile in it. Notably, (and this is a change from previous versions) the dwarves *must* be able to walk up to the target; placing a channel in front of it will prevent them from training.

Once you build your range (b-A), you must define it as a room (q-r). Make it so it touches the far wall, and don't worry, range rooms can overlap. You have to do this for each archery target. Make sure the shooting direction is correct! In addition, your marksdwarf squad **must** at minimum have train set on each archery target with (q-t). Again, only one marksdwarf can use a target at any given time.

Repeat this for each range; you will have 1-10 targets overlapping each other and assigned to your marksdwarf squad (in these screenshots, they are "The Delights of Gold")

### The military management screen

This is by far the most difficult part - the military menu is confusing on the best days, but this guide will walk you through it. (To some people, this screen is designed upside down: the options to switch 'pages' or 'tabs' on this menu are at the bottom, and the specific detailed commands for the current page/tab are at the top. We will use 'page'.)

Ignore the default page **p: Positions** page for now, because you want to make the right **n: Uniforms** for your marksdwarves.

#### Uniforms

Press n to bring up the uniforms screen. Do yourself a favor and just scroll down and delete the default 'archer' uniform. It's wrong and will not work properly.

Create a new uniform with c.

You will use the hotkeys seen on the 2nd row from the top of the m screen, and to create the following uniform:

- Armor: leather armor
- Legs: leather legwear
- Helm: leather headwear
- Gloves: leather handwear
- Boots: leather footwear
- Shield: shields/bucklers
- Weapon: crossbows (do NOT use individual choice, ranged; you **will** end up with dwarves who think an *axe* is a ranged weapon) :p

Navigation is *tricky*, so let's do the first 3 selections together:

1.  Armor to show the  SELECTION  list of Armor items
    1.  Navigate → to the  SELECTION  list
    2.  Use the ↑/↓ and Enter to select "leather armor". You should now see "leather armor" listed under  SELECTION  list in the center of the screen.
    3.  Ok, that was the **easy** one. So follow these steps CLOSELY.
2.  Legs to show the to show the  SELECTION  list of Leg items
    1.  Use the ↑/↓ and Enter to select "legwear". You should now see "legwear" listed under "leather armor" under  SELECTION  list. BUT... the green leather armor means it is the selection from that column.
    2.  Navigate back ←/↓ to highlight legwear
    3.  Material to reveal the material options that will appear under the  SELECTION  column.
    4.  Navigate → to the  SELECTION  list
    5.  Use the ↑/↓ and Enter to select "leather" material. You should now see leather legwear listed under  SELECTION  list in the center of the screen.
3.  Now Helm to get your leather headwear
    1.  Use the ↑/↓ and Enter to select "headware". (It may be the first option, so just hit Enter)
    2.  Navigate back ←/↓ to highlight headware
    3.  Material to reveal the material options that will appear under the  SELECTION  column.
    4.  Navigate → to the  SELECTION  list
    5.  Use the ↑/↓ and Enter to select "leather" material. You should now see leather headwear listed under  SELECTION  list in the center of the screen.

Be careful of hitting Enter at the wrong time and duplicating or deleting an entry. Here's what it should look like if you did it right:

Now press m to switch from "Partial matches" to "Exact matches" in the upper right. This appears to fix most of the issues that result in your dwarves not picking up quivers. You might be able to get away with r "Over clting", which means the dwarves will wear this uniform over their current clothing.

At this point you have created the concept of a uniform, but you have not yet told your squad to wear this uniform.

Proceed to the next section.

### Positions

Now press p to go back to the positions menu. If you are creating l a new squad, it will prompt for a uniform, before showing a list of Vacant Squad positions and Candidates.

After selecting your recruits, switch to the e menu. Select your squad, then press U (that's capital U) to bring up the Uniform selection screen.

NOTE: If a position (for example, commander/captain) is highlighted when you hit the Uniform selection screen, your selection will ONLY apply to that individual soldier. Hit shift + enter to make sure you are assigning it to all positions in the squad.

You can also look at the top of the screen to see what your dwarves will train as (i.e. 10/10 Marksdwarves, instead of 1/1 markdwarf 9/9 wrestlers).

### Handling ammo

We're almost done. Go to the ammo screen.

(Note: This isn't possible in Steam version. There is no ammo screen)

If you're setting this by hand, here's what to know. Each squad needs the correct ammo. Bolts are assigned on a "per-item" basis, i.e., a given stack of bolts that's marked for training will only be used for training and vice versa. By default the top slot reserves ammunition for hunters. If you don't have any hunters you may want to remove that reservation from the ammunition screen to free up those bolts for your military.

### Squad training orders

Now, for the magic bit that gets them doing nothing \*but\* training. Open the schedule screen with s and look at the orders. The default is "Train, 10 minimum". **This is WRONG!**

Press x to delete the order. The schedule screen will change to show no scheduled orders.

Press o to pull up the give order screen. Press o until 'Train' is set, and then press + so it shows minimum 1, like this. Then press shift-enter to give the order. The screen will look like this:

Now do it again, until you have as many orders as total members of your squad (using a macro will allow you to repeat the process easily). You can give more than 5 orders, you just have to scroll in the orders screen to see it. When you're done it should look like this, after doing it 10 times.

Copy and paste the order to all the months. You can also set Sleep in Barracks at need to increase their training time, though this will raise the stress levels of dwarves in the squad due to tired thoughts.

You're almost done. Activate your squad, and after they finish picking up equipment, watch your bolt supplies vanish as your marksdwarves do nothing \*but\* archery training.

### Why this works

Squad training and sparring require multiple dwarves (and yes, marksdwarves \*will\* spar as long as they're Competent Fighters). Training, minimum of 1 forces them to work solo. Since they don't have a normal barracks, they can't drill, which leaves archery training as the only possible way to train. Since reloading on marksdwarves continues to be erratic, they'll frequently report "No Orders" or similar once they've finished archery training; until the game notices that a given dwarf is out of ammo, in which case they'll go pick up more.

Archery target training grants 5x less experience than live fire (6XP per bolt at archery target vs. 30XP per bolt on live targets), but no micromanagement, no hauling, one setup, and you can ignore it until you get that glorious announcement that Urist McMarksdwarf has become an Elite Marksdwarf.

## Stopping melee charges

Do **not** use the station scheduling order!

When a dwarf has line of sight on an enemy, they'll do one of two things: run away; or run up and fight. While they're running up to the enemy, dwarves will shoot bolts if they have any, but then engage the enemy using their crossbows as hammers instead of shooting. Therefore, it's imperative that you create physical barriers which make it impossible for your marksdwarves to charge the enemy. Nothing else will suffice. The Siege update made marksdwarves much less eager to engage in melee combat.

Some sources claim a Defend Burrows order may restrict marksdwarves to the area defined by the burrow. The full effectiveness of Defend Burrow orders at stopping a melee charge is unknown.\[Verify\]

The easiest way to accomplish this is to use fortification pillboxes (also known as archery towers), with a patrol order that causes them to break line of sight.

For patrol routes, marksdwarves will not reliably take a Pickup Equipment order as long as they have line of sight on their enemy; they will usually stand there and glare. Have them go through a door or something, and as soon as they lose sight of the goblin/forgotten beast/demon, they'll immediately go find bolts and reload.

An alternative approach is to forego all of this scheduling stuff, and use direct move orders. Station (move) your marksdwarves to the spot where you want them to stand, making sure that this spot is physically separated from the enemy. Remember that each dwarf will actually select a random spot within 3 tiles of your station-spot, on the same Z level, and try to walk to that spot. Make sure every such reachable spot is on *your* side of the fortifications.

In all cases, you must remember that dwarves **can and will climb** walls or fortifications to reach the enemy. To prevent marksdwarves from suicide-diving over the fortifications onto the killing ground below, build a roof (a floor on the next Z-level up) to physically block their vertical movement.
