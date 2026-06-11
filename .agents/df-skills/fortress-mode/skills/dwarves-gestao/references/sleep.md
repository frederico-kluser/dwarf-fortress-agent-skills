# Sleep

> Fonte: [Sleep](https://dwarffortresswiki.org/index.php/Sleep) — Dwarf Fortress Wiki (GFDL/MIT)

Dwarves that have been awake for a long time will eventually become tired and desire **sleep**. Along with eating and drinking, sleep is a necessary maintenance activity that your dwarves will need to perform at intervals, a few times every season. Drowsy dwarves are indicated by a blinking gray arrow. Dwarves who are unable to sleep for 6 months may go insane.

Dwarves getting proper sleep and having a bed to sleep in is one of the more prominent, key components to a dwarf's happiness.

## Mechanics

Dwarves that are tired will work more slowly, and produce poorer-quality results. However, dwarves generally will not remain drowsy for long; upon getting sleepy they usually finish their current task, find a bed, and fall asleep. If no bed is available, they will fall to the floor immediately after completing their last task (a group of drunken dwarves sleeping upon barrels of hard liquor is quite a common sight). If there is an unassigned bed located closer to them than their assigned room, they will sometimes choose to sleep there instead. Dwarves will not sleep in beds located in hospitals.

As one might imagine, having to sleep in the dirt is not a happy occurrence, and will give your dwarves unhappy thoughts. While dwarves will tolerate sleeping on smoothed floor without any thoughts, they won't actively seek it out so it relies on them getting sleepy while inside fortress grounds. On the other hand, sleeping on a nice bed, in a nice room will give them a happy disposition upon waking. The exact arrangement of living conditions (bedroom design) is a big part of fortress design; some players lavish their dwarves' rooms and see it as an easy way to increase their happiness, some see bedrooms only as necessary provisions, and some do away with them entirely, preferring easier-to-create, easier-to-maintain public dormitories instead (these do have the advantage of making vampire-spotting a piece of cake). Nonetheless, the need to prevent your dwarves from sleeping under the stars more than a few times at the very beginning is a universally agreed-upon point of importance.

Dwarves do not follow natural sleeping cycles. There is no "night" in fortress mode, beyond references in the form of night creatures (in adventurer mode, however, this is a different story entirely). Instead, they will sleep according to their own internal clock. At the very beginning, dwarves that arrive at the same time will tend to nod off at the same time, but as time progresses, they will diverge into their own cycles. After some time, at most a quarter of the fortress may be asleep at a time.

Other unhappy thoughts associated with sleep are caused by being tired, collapsing from exhaustion, and being disturbed by nearby noise. Noise can cause uncomfortable or troubled sleep, or wake the dwarf entirely, with increasingly negative thoughts.

Collapsing from exhaustion only really happens in the military. Dwarves on active military service (stationed or attacking) will forgo sleep for duty, but will be unhappy when they finally do get to sleep. Military dwarves can nonetheless spontaneously fall to the ground unconscious if they are exhausted. Since dwarves do not come with portable pillows, cannot munch on rations or take swigs from flasks as they can to relieve hunger and thirst, the need to sleep is the primary limiting factor on how long you can keep your military dwarves on high alert before they fall dangerously unconscious.

Sleeping is not the same thing as being unconscious, although the effect is the same. A dwarf may fall unconscious when they give in to pain, universally a bad thing, or when recuperating from wounds in a hospital. Finally, hunters have a tendency to fall asleep anywhere, which can cause problems with their happiness (though at a reduced penalty if they're sufficiently trained). To prevent this behavior, disable hunting from the labors.

## Detailed mechanics

Drowsiness increments by 1 during each game tick *(i.e. 1200 per day, 33,600 per month, 403,200 per year)*, possibly more if the dwarf is a mother carrying her child. When it reaches certain thresholds, the following things happen.

:\* 50000 - dwarf starts considering going to bed (1/120 chance per tick) if idle

:\* 54000 - dwarf decides to go to bed if idle

:\* 57600 - dwarf starts flashing "Drowsy"

:\* 65000 - dwarf gets an unhappy thought about being Tired

:\* 150000 - dwarf starts flashing "Very Drowsy"

:\* 160000 - dwarf gets an unhappy thought about being Exhausted

:\* 200000 - dwarf goes insane

Prior to version 0.31.07 (and going all the way back to the 2D versions), the unhappy thoughts resulting from hunger/thirst/drowsiness occurred at the exact same time that the dwarf started flashing, but all of the other numbers were otherwise the same. Additionally, in earlier versions (most notably 40d and earlier) dwarves cancelled jobs for food/drink/sleep much more readily.

## See Also

- Bedroom design
- Noise
- Sleeping in adventurer mode
