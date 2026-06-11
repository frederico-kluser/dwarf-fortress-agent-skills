# Minecart (parte 3/3)

This is caused by the fact that a cart, after turning the bend in the track and entering e.g. a flat tile, will be subject to the checkpoint effect which applies 5k acceleration opposed to the last amount of ramp acceleration it received. Since the cart has just passed a corner, this compensatory speed adjustment now goes to the "outside" of the corner and creates enough lateral velocity to carry the cart off the track after eleven steps. (Down corner ramps do not have this problem, as the downward direction is in line with the past-corner movement direction and the checkpoint effect works on the only remaining movement vector.)

There are two fixes to this problem. One is to simply not put corners on up ramps. The other is to "cancel" the lateral speed after a cart has passed the ramp, either by sending the cart through another corner or by putting a high-friction track stop on the exit tile. In the latter case, the cart will lose 10000 speed in the desired direction, but the same speed loss will apply to the undesired lateral speed, nullifying it.

### Checkpoint Effect

The checkpoint effect, explained in depth by Larix, is an odd and highly exploitable feature of ramps where minecarts "teleport" through the next tile of track, ignoring nearly all minecart physics (except that they stop at all walls or other obstacles and only respect curves with no backing wall and invalid ramps if they are below derail speed) and passing through that tile in just a single tick, and to the very end of the next tile.

This effect occurs when a cart leaves a downward ramp for any other direction of tile. (This includes ramps which accelerate in different directions, even a ramp which goes from accelerating East to accelerating North due to a bend in a chain of standard down ramps in a curve.) This allows, for example, two valid straight ramps directly next to one another with a cart dropped onto one or the other with no momentum to have the cart pick up acceleration going "down" the ramp as normal, but then flying up through the "up" ramp it travels into with no loss of momentum, as though it had come from an impulse ramp. If the two ramps had at least one space of distance between them, and then a cart were dropped in, the cart would instead "rock" back and forth between the two ramps.

This seems to be because ramps have a slightly longer length than regular tiles—141,420, rather than 100,000 distance. When this "snaps back" after a ramp, it seems to project the cart suddenly further along the track, making it jump a tile ahead even when otherwise moving at relatively low speeds.

This bug is the cause of a *wide array* of unexpected behavior among people who do not take this bug into account. It causes derailments or failure to climb up seemingly valid impulse elevators. In general, it makes a system that behaves extremely counter-intuitively, and operates *any time a cart encounters a valid ramp*. At the same time, when its effect is accounted for, it is highly exploitable: It causes "perpetual motion devices" using no power when two opposing ramps are placed next to one another, since the "uphill" effect of the opposing ramp is ignored, preventing deceleration.

Another useful thing to note about this exploit is that carts traveling at no less than 71,000 or so speed (enough to travel half a ramp tile in a single tick) can travel through every tile in just one tick at no change in velocity as long as the tiles alternate between impulse ramp or actual down ramp and any other tile type. The cart checkpoints through the non-down-ramp tiles, and can pass through the (impulse) down ramp tiles in a single tick, before they can actually start gaining momentum.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  |  | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |
| ═ | ▲ | ═ | ▲ | ═ | ▲ | ═ | ▲ | ═ | ▲ | ═ |  |  |  | ═ | ╚ | ═ | ╚ | ═ | ╚ | ═ | ╚ | ═ | ╚ | ═ |  |
| ▒ |  |  |  | : |  | W | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ═ |  | : |  | N | o | r | m | a | l |  | t | r | a | c | k |  |  |  |  |  |  |  |  |
| ▲ | / | ╚ |  | : |  | N | / | E |  | T | r | a | c | k | / | R | a | m | p |  |  |  |  |  |  |

If the cart enters from the West at less than 72,000 speed, some of those ramps will cause Eastward acceleration.

This means that an impulse ramp not contiguous to other impulse ramps has a top speed of around 75k:

|     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| ▒   | ▒   | ▒   | ▒   | ▒   |     | ▒   | ▒   | ▒   | ▒   | ▒   |
| ▒   | ╔   | ═   | ╗   | ▒   |     | ▒   | ╔   | ═   | ╗   | ▒   |
| ▒   | ╚   | ▲   | ╝   | ▒   |     | ▒   | ╚   | ╗   | ╝   | ▒   |
| ▒   | ▒   | ▒   | ▒   | ▒   |     | ▒   | ▒   | ▒   | ▒   | ▒   |

This setup makes a cart that travels clockwise at a speed that fluctuates around 75k velocity. If the cart has more than 72k velocity, it fails to accelerate in the ramp, as it leaves the ramp in a single turn due to checkpointing to the halfway point. After that, the curves sap 1k velocity, and every tick saps 10 velocity.

Two contiguous impulse ramps with a same-facing "downwards slope", however, do not suffer the checkpoint effect in the second tile, giving functionally triple the space to accelerate. This means it will add velocity (at the standard rate of 4.9k per tick) up to a maximum speed of 216k.

|     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| ▒   | ▒   | ▒   | ▒   | ▒   | ▒   |     | ▒   | ▒   | ▒   | ▒   | ▒   | ▒   |
| ▒   | ╔   | ═   | ═   | ╗   | ▒   |     | ▒   | ╔   | ═   | ═   | ╗   | ▒   |
| ▒   | ╚   | ▲   | ▲   | ╝   | ▒   |     | ▒   | ╚   | ╗   | ╗   | ╝   | ▒   |
| ▒   | ▒   | ▒   | ▒   | ▒   | ▒   |     | ▒   | ▒   | ▒   | ▒   | ▒   | ▒   |

This example results in a cart moving three times as fast as the previous cart.

Three successive ramps results in the highest attainable speeds.

In practical terms, this means that only consecutive ramps should be used for high acceleration, but singleton ramps can be used to have speeds that are somewhat regulated.

### Stacking

If a minecart lands on top of another minecart, they may form a stack, with the upper cart on the z-level above the lower. Subsequent carts do not form a stack, but rather quantum stockpile in the same space. This behaviour is useful for megaprojects and trap design with minecarts as the weaponry. Moderation should still be exercised: carts take longer to fall into a "stacking" tile already occupied by other carts and will spend that time "hanging" in the air above the stack. This can lead to following carts striking them, which can cause all kinds of malfunctions. The extra time is two game steps for every cart already in the stack, which doesn't hurt stacks of ten carts very much but makes stacks of 100+ rather impractical.

These minecarts on the upper level generally need to be struck with another minecart to move out, or have their support removed. The latter option is safest done by shooting it away with another minecart, manual removal of a stack-supporting cart typically causes the next cart from the stack to fall on top of the hauler.

### Perfectly Elastic Collisions

Minecart collisions are perfectly elastic, meaning that not only do minecarts not take damage, but that two carts that are rolling which have frontal collisions of near-similar speed, and where one cart is no more than twice the mass of the other cart, will result in a billiard-ball-like effect of the lighter cart bouncing off the heavier cart with a proportional speed increase dependent upon the relative momentum behind the heavier cart.

Using this trick with carts already at the 270,000 maximum speed from ramps can result in "supersonic" carts traveling at speeds in the millions (travelling a dozen tiles per tick), but where they are suddenly subject to 10,000 units of "terminal velocity" friction per tick. Thread with SCIENCE here.

While hypothetically capable of launching a minecart into orbit when used in conjunction with a ramp, no cargo can be contained in the launched cart, as the collisions will force ejections of the cargo. Your "unwilling volunteer" goblin space pioneers will simply become paste underneath the wheels of an extreme high-speed cart.

## Non-standard uses

Minecarts include some interesting characteristics that have motivated uses beyond hauling. They can be useful for creating fully-automated quantum stockpiles, garbage disposals, water reactors, and portable drains. Storing perishable goods (meat, meals, etc.) inside a minecart appears to guard against rot and vermin. Minecarts can be used as weapons, or as (hopefully non-fatal) triggers to restart stalled health care. They can also be used to time/control game events, either using a basic repeater or much more advanced minecart logic. Minecarts trigger pressure plates, which means a trap can be designed to trigger when a thief attempts to steal a minecart. A pressure plate can be used as automatic and more precise custom "launch when full enough" system - as long as weight of your minecarts stays the same. You cannot build a hatch or roller on the same tile, so launch by bumping with another cart.[12] Dwarves riding minecarts can attack enemies within reach (which goes back to dev log). This applies to shooting, and they actually can hit targets while riding by.[13] Whether a minecart protects the rider and how it interacts with dodging is not known yet. Minecart riders can also train swimming and detect ambushers.

## Simple Example Layouts

### 2-way Minecart Route

This is an example of how a 2 way route can be established.

- Stop 1 is non dumping, frictionless (Feeder Stockpile from North in this example)
- Stop 2 friction and dump (dumps South in this example)
- Stop 3 is non dumping, frictionless (Feeder Stockpile from North in this example)
- Stop 4 friction and dump (dumps South in this example)

Now you create a Route hauling your desired items from Stop 1 to Stop 2 . Immediately guide the empty cart to Stop 3 (because the stop has no friction, a pushed cart will overshoot the stop). Haul desired items from Stop 3 to Stop 4. Immediately guide the empty Cart to Stop 1.

### Automated Minecart Funicular (Elevator that also goes sideways)

This is an example to set up stone delivery from multiple Z levels with a common set of tracks while automatically returning the cart to where it is supposed to go. In this example, the South track goes upwards towards the drop off point, the North track goes downwards for cart return. The design pictured consists of the following:

- Two ramps next to a wall spaced one tile apart
- Tracks on top of the ramps to make an inclined track
- A 3X1 channel dug down next to the ramps on the side opposite the wall
- 2 gear assemblies, one between the ramps, one over the middle channel
- Rollers on the upward track pointing towards the wall (South ramp in this example)
- A hatch over the channel next to your downwards ramp (North ramp in this example)
- A wall diagonally adjacent to the to the upwards channel
- Tracks leading from the hatch to the single wall
- A wall next to the curved section of track
- A pressure plate set to trigger on minecarts on the track underneath the minecart. Link the pressure plate to the hatch
- Set up a minecart route with one stop where the minecart is. Set the condition to push the minecart in the direction of the channel with any condition and contents you wish
- Each subsequent level needs to be shifted one tile in the direction of the ramp down

The unloading level just needs to pass the cart over a track stop set to dump in whatever direction you want, then send it back down the return track. It also needs to provide power to the rollers, 12 power is required per level.

How it works

- The minecart sitting on the pressure plate keeps the hatch open so that other carts may pass
- When the cart is off the pressure plate the hatch closes. This causes the cart to pass over the hatch back to its loading position

## Adventure mode

In addition to being used for hauling, minecarts can also be ridden in adventure mode. (Adapted from forum thread [14])

1.  If the minecart is in your inventory, drop it. If it is already on the ground, proceed to step 2.
2.  Press u when you are 1 tile away from the minecart (or standing on the same tile as the minecart).
3.  You will be presented with the following options:

- If you Push the minecart, it will move a few tiles in the direction you chose. Physics comes into play here, so it will gain/lose speed depending on the usual factors.
- If you Ride the minecart, you will hop into the minecart, even if you were a tile away, and it will move in the chosen direction with you in it. It will gain/lose speed depending on the usual factors. Whilst the minecart is in motion, you should press . to skip your turn; if you attempt to move whilst the minecart is still in motion, the laws of physics come into play, and you will take damage. However, it is currently possible to jump out of a moving minecart safely.Bug:10104 Alternatively, you can push the minecart whilst it's still in motion (although it's unclear how one can bend physics so as to push a moving minecart whilst inside the minecart). If you push it in the same direction you are already travelling in, you will greatly increase the minecart's velocity. You can also push it in different directions, and this will cause it to gradually change direction-the amount of pushes this requires depends on the minecart's velocity. Once the minecart has stopped moving, you may move out of it safely, or you may want to give it another push. Note that if you push a minecart right after having ridden it (still on the same tile as the minecart), it will act as though you chose to *ride* it.
- When the minecart is on a track, options appear to Guide it in directions that the tracks lead. This moves the cart 1 tile in the direction it is guided. Guiding the cart is the only way to move a minecart from a maximum friction track stop (other than taking it into inventory.)

Minecarts in adventure mode are not restricted by a lack of tracks. However, they are hindered by natural ramps. Attempting to go up a slope will lead up the cart slamming into the wall. The good news is you'll make it over the ramp. The bad news is you likely won't stick the landing.

Note that while carts are a powerful weapon if heavy and fast enough, they have their limits, and a collision can sharply reduce the speed of a cart depending on what you hit, potentially enough to eject the rider. Trying to run over a human will send them flying, while trying to ram a dragon will not end well.

If you want to test this out without creating an adventurer, the object testing arena allows you to spawn minecarts (k-c-n)

## Forging and Melting

- Metal minecarts cost **two** metal bars to forge, or **six** adamantine wafers.
- When a non-adamantine metal minecart is melted down, it will return **1.8** metal bars, for an **efficiency of 90%**.
- When an adamantine minecart is melted down, it will produce **1.8** wafers, for an **efficiency of 30%**.

## See also

- The "How Does Minecart" Thread by **Girlinhat** et al.
- SCIENCE: Quantifying minecart physics by **Snaake** et al.
- How to build a Multi-cart Ore to Magma Minecart Project without needing power by **WanderingKid**. (Images recovered from wayback machine and posted here: https://imgur.com/gallery/LpRsDwO)
- My very own Minecart Education Thread. Ten Lessons, now complete. by **Larix**.
- Real-life railcarts/conveyor hybrid which uses similar mechanics.

## Bugs

- A dwarf will drop her baby, if she has one, when boarding a minecart set to be ridden.
- Dwarves have no concept of traffic safety and will walk into busy minecart lines to retrieve objects, often with deadly consequences. This is especially problematic in clever applications depending on dwarves riding the carts very frequently, because they have a bad habit of dumping their worn clothes on the tracks after a minecart ride. Adding an automatically-operated hatch cover at the end of such a ride can help prevent unfortunate accidents.
- Dwarves cannot guide a minecart through an unlocked door unless another dwarf opens the door.Bug:6056
- It is possible for a creature and minecart moving towards each other to pass without collision if they exchange tiles in the same tick.
- After a minecart ride, a dwarf will sometimes haul the minecart to a storage stockpile, leaving another dwarf to haul the vehicle back to the route.
- Minecarts falling onto a floor injure creatures in the tile below the floor.Bug:6068
- If a minecart travelling at high speed hits a wall, it and its contents may go through the wall, or even end up embedded in it.Bug:5996
- A minecart's initial velocity is not affected by weight, when pushed or launched from rollers.Bug:6296
- Removing a stop that has a vehicle waiting on it may cause the game to crash.Bug:5980
- Jumping out of a minecart in motion does not lead to injury.Bug:10104
- Jumping into a stationary minecart can lead to significant injury.Bug:10229

    [ITEM_TOOL:ITEM_TOOL_MINECART]
    [NAME:minecart:minecarts]
    [VALUE:50]
    [METAL_MAT]
    [WOOD_MAT]
    [TOOL_USE:TRACK_CART]
    [FURNITURE]
    [TILE:254]
    [INVERTED_TILE]
    [SIZE:40000]
    [MATERIAL_SIZE:6]
    [CONTAINER_CAPACITY:500000]


---
*Parte 3 de 3 de «Minecart». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Minecart*
