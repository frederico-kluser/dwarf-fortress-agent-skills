# Thirst

> Fonte: [Thirst](https://dwarffortresswiki.org/index.php/Thirst) — Dwarf Fortress Wiki (GFDL/MIT)

Dwarves, given time, will eventually get **thirsty**, as indicated by / blinking over the thirsty dwarf. If a dwarf fails to drink in time, the thirst will proceed to dehydration and eventually death. A dwarf needs to drink about once in every three weeks.

A thirsty dwarf prefers to drink booze - if none is available, they will go to the nearest water source and drink, ideally being a well inside the fortress, but they will drink from a river, brook, or even murky pools if there are no other sources of water. A dwarf can live indefinitely on water alone, but without alcohol they will suffer bad thoughts, reduced movement speed/workrate, and combat abilities: making a dwarf's efficiency highly alcohol-dependent. While dwarves prefer an abundance of alcohol, dwarves give water to other dwarves when a dwarf is resting and when a dwarf can't find something to drink on their own.

Dwarves seem to be capable of subsisting on vomit and slime in particularly dire times, though this is (as to be expected) traumatizing and will quickly result in mental breakdowns and insanity. This will usually only happen in cases of dwarves walling themselves in and being forgotten, and in challenging embark locations.

A resting dwarf will not do anything on their own until they have recovered from recent injuries (preferably inside a hospital), and will depend on others to provide them with food and drink. They will not be given booze but receive water carried in buckets.

Any baby being carried by its mother will effectively leech drink from her, causing her to become thirsty at double the usual rate. This does not, however, count as alcohol - when a baby is close to 1 year old, it will have severe withdrawal.

Vampires and necromancers never dehydrate and thus never drink water, but still enjoy consuming alcohol. In previous versions, werebeasts also needed not to drink, but this has since been fixed.

Most types of humanoids who join a fortress, such as humans and elves need to drink, eat, and sleep.

## Detailed mechanics

Thirst increments by 1 during each game tick *(i.e. 1200 per day, 33,600 per month, 403,200 per year)*, possibly more if the dwarf is a mother carrying her child. When it reaches certain thresholds, the following things happen.

:\* 20000 - dwarf starts considering getting something to drink (1/120 chance per tick) if idle

:\* 22000 - dwarf decides to go get something to drink if idle

:\* 25000 - dwarf starts flashing

:\* 35000 - dwarf gets an unhappy thought about being Thirsty, cancels current job to get something to drink

:\* 50000 - dwarf starts flashing

:\* 60000 - dwarf gets an unhappy thought about being Dehydrated

:\* 75000 - dwarf dies of thirst

Completing a drink job decreases the relevant counter by 50,000 (to a minimum of zero), though they may also decrement it additional times during the job's progress.

Being dehydrated for even a single tick will cause a miscarriage among pregnant dwarves.

Prior to version 0.31.07 (and going all the way back to the 2D versions), the unhappy thoughts resulting from hunger/thirst/drowsiness occurred at the exact same time that the dwarf started flashing, but all of the other numbers were otherwise the same. Additionally, in earlier versions (most notably 40d and earlier) dwarves cancelled jobs for food/drink/sleep much more readily.
