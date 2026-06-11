# Minecart (parte 2/3)

| ░ |  | : |  | W | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ║ | , | ═ | , | ╔ | , | ╚ | , | ╗ | , | ╝ |  | : |  | T | r | a | c | k | / | R | a | m | p |  |  |  |  |  |  |  |  |  |  |
| ▼ |  | : |  | D | o | w | n |  | R | a | m | p |  | ( | e | m | p | t | y |  | s | p | a | c | e | ) |  |  |  |  |  |  |  |

Also, if you want to have a cart following a below-derail speed, the following track works well:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| z |  | \+ | 0 |  |  |  |  | z |  | \+ | 1 |  |  |  |  | z |  | \+ | 2 |  |  |  |  | z |  | \+ | 3 |  |  |
|  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |
|  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ═ | ═ | ░ | ░ |  |  |  | ░ | ▼ | ▼ | ║ | ░ |  |  |  | ░ | ░ | ░ | ▼ | ░ |
|  | ░ | ║ | ░ | ░ | ░ |  |  |  | ░ | ▼ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ║ | ░ |  |  |  | ░ | ░ | ░ | ▼ | ░ |
|  | ░ | ║ | ▼ | ▼ | ░ |  |  |  | ░ | ▼ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ═ | ═ | ░ |
|  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |
| ░ |  | : |  | W | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ║ | , | ═ |  | : |  | T | r | a | c | k | / | R | a | m | p |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ▼ |  | : |  | D | o | w | n |  | R | a | m | p |  | ( | e | m | p | t | y |  | s | p | a | c | e | ) |  |  |  |

In this elevator, the cart collides with the walls in the corners, but then realigns on the ramp, picks up speed, checkpoints through the next ramp, and slams into the next wall. It is slower (10 ticks per floor) but produces reliable speeds, and will exit the impulse elevator at little more than push speeds.

\
A sort of opposite effect to impulse ramps also exists: ramps lacking the proper "up" and "down" connections are treated as flat track, even if they actually go up or down z-levels. This allows building "anti-impulse" slopes consisting entirely of ramps only connected up, which a minecart can travel up forty levels and more, needing no more than a single push.

### Controlling traffic

#### Switching

As tracks are constructions or tile features, doors and other furniture can be built on them. A door or floodgate can be turned on or off by a lever, effectively controlling the flow of automated minecarts. This may be ~~dangerous~~ fun, however.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  |  |  |  |  |  |  | \- | \> |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | A |  | ═ | ═ | ═ | ═ | ┤ | ≡ | ═ | ═ | ═ | ═ |  | B |  |  |  |  |  |  |  |  |  |  |  |
| ┤ |  | : |  | r | o | l | l | e | r |  | p | u | s | h | i | n | g |  | t | o |  | E | a | s | t |
| ≡ |  | : |  | d | o | o | r |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

The roller pushes the cart east, but until the "departure condition" is fulfilled, the door remains closed and blocks the path.

Bridges can also act as tracks, but only if they're lowered or not retracted. This property can enable levers to turn tracks on and off. However, care should be taken to ensure that such bridges are never operated while a cart is on top of them, as the cart will be flung off the track. It's worth noting that it's often faster, and cheaper, to construct large bridges than long sections of constructed track.

A powered track switch can be constructed by building an "inverted" corner as illustrated below.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  |  |  |  |  |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  | B |  |  |  |  |  |  |
|  |  |  |  |  |  | ║ |  |  |  |  |  | \- | \> |  |  |  |  |  |  | ║ |  |  |  |  |  |  |
|  |  |  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  |  |  |  | ║ |  |  |  |  |  |  |
|  |  | ═ | ═ | ═ | ═ | ╚ | ═ | ═ | ═ |  |  |  |  |  |  | ═ | ═ | ═ | ═ | ├ | ═ | ═ | ═ | ═ |  |  |
|  | A |  |  |  |  |  |  |  |  | C |  |  |  |  | A |  |  |  |  |  |  |  |  |  | C |  |
| ├ |  | : |  | r | o | l | l | e | r |  | p | u | s | h | i | n | g |  | t | o |  | W | e | s | t | . |

If the cart is pushed East from the stop at 'A' while the roller is activated, it will arrive at 'B'. If the roller is not running, it will arrive at 'C'. The switch works by the roller first reversing the incoming cart's movement and the cart *then* following the track corner.

This switch is very reliable, reacts instantly to on/off signals, and carts of any speed can be switched by this design, although very fast carts will require rollers that are several tiles long, up to three. The requirement for power can be inconvenient or impractical. Non-powered solutions may use controlled derailment, or a connecting bridge.

|     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     | B   |     | ╥   |     |     |     |     |     |     |
|     |     |     |     |     |     | ║   |     |     |     |     |     |     |
|     |     |     |     |     |     | ║   |     |     |     |     |     |     |
|     | ╞   | ═   | ═   | ═   | ═   | ╝   |     | ═   | ═   | ═   | ═   | ╡   |
|     | A   |     |     |     |     |     | D   |     |     |     |     | C   |

Here the track between A and C is not continuous. The only continuous track is A-\>B, with a corner (not a T section). Fast moving carts will tend to derail at D and rejoin the track to C. Placing a door at D will prevent the derailment, so the cart continues to B. The door is operated by mechanisms elsewhere (typically, a lever, but some fun can be had with pressure plates).

Since it depends on derailing, this switch requires a very fast cart, faster than what can be achieved with rollers alone. To gain sufficient speed, a cart must be accelerated further, usually by descending several levels or through impulse ramps. The high speed makes the cart much more dangerous and harder to control.

If carts are moving too slowly to derail at the corner, a retractable bridge may be used as a connector between A and C.

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     | B   | ╥   |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     | ║   |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     | ║   |     |     |     |     |     |     |     |     |
|     | A   | ╞   | ═   | ═   | ═   | ═   | b   | b   | b   | ═   | ═   | ═   | ═   | ╡   | C   |

The bridge must overlap the corner. Bridges behave like a track crossing, allowing carts to pass in a straight line. When retracted, the corner reappears, so the carts will continue to B. Bridges take 100 steps to react to a signal, necessitating rather long "lead times" when switching tracks via bridge.

As mentioned above, special care must be taken to make sure the bridge doesn't change state while the cart is passing over it. Retracting bridges will throw the cart, causing it to stop dead. Raising bridges can even crush the cart.

#### Controlling Speed

Minecarts can reach extremely high speeds, especially when descending multiple Z-levels. A minecart will derail at a track corner if its speed exceeds 0.5 t/st (tiles per step), **unless** the route in the direction of travel is blocked:

Will derail at \> 0.5 t/st:

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     | i   | n   |     | ═   | ═   | ╗   |     | \-  | \>  |     | d   | e   | r   | a   | i   | l   | i   | n   | g   |
|     |     |     |     |     |     | ║   |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     | o   | u   | t   |     |     |     |     |     |     |     |     |     |     |     |     |

Will not derail at \> 0.5 t/st:

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     | i   | n   |     | ═   | ═   | ╗   | O   |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     | ║   |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     | o   | u   | t   |     |     |     |     |     |     |     |     |
| O   |     | :   |     | w   | a   | l   | l   | /   | c   | o   | l   | u   | m   | n   | .   |

This behavior can be used to build a "speed limiter", that will ensure that when a minecart exits it is traveling below derail speed, as illustrated in these three examples:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  |  |  |  |  |  | ░ | ░ | ░ | ░ |  |  |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  |  |  |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  |  |  |  |
|  | i | n |  |  | ═ | ╔ | ═ | ╗ | ░ |  |  |  |  |  | ░ | ╔ | S | ╗ | ░ |  |  |  |  |  |  |  |  | ░ | ╔ | S | ╗ | ░ |  |  |  |  |  |  |
|  | o | u | t |  | ═ | ╬ | ═ | ╝ | ░ |  | o | u | t |  | ═ | ╗ | ═ | ╝ | ░ |  |  |  |  | o | u | t |  | ═ | ╗ | ═ | ╝ | ░ |  |  |  |  |  |  |
|  |  |  |  |  | ░ | ╚ | S | ╝ | ░ |  |  |  |  |  | ░ | ╚ | ═ | ╝ | ═ |  | i | n |  |  |  |  |  | ░ | ╚ | S | ╝ | ░ |  |  |  |  |  |  |
|  |  |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  |  |  | ░ | ░ | ░ | ░ |  |  |  |  |  |  |  |  |  |  | ║ | ░ | ░ | ░ |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | i | n |  |  |  |  |  |  |  |
| ░ |  | : |  | w | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| S |  | : |  | T | r | a | c | k |  | S | t | o | p |  | ( | H | i | g | h |  | F | r | i | c | t | i | o | n |  | o | r |  | l | o | w | e | r | ) |

If the minecart is traveling below derailment speed, it will not be affected; if fast enough to derail at a turn, it will jump the open turn to the alternate path, be slowed as it crosses the Track Stop, and get put back into the main path only once it can take a corner. (Granted, you could do the same just with any track corners, but it may take a lot of turns and time.)

Since all the derailings, bounces and ramps can impart a sideways component of speed small enough to start visible drift many tiles away (say, in the middle of a bridge), track turns have one more use: forcing the carts to move strictly along the grid directions. Carts passing a turn below derailing speed convert one component of velocity into another, thus eliminating the drift.

A powered setup using corner rollers to decelerate carts can also be used:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | i | n |  | ═ | ╔ | ╔ | ╔ | ╔ | ╔ | ╔ | ╔ |  |  |  |  |  |  |  | i | n |  | ═ | ┤ | ┤ | ┤ | ┤ | ┤ | ┤ | ┤ |  |  |  |  |  |
|  |  |  |  |  | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ═ |  | o | u | t |  |  |  |  |  |  | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ═ |  | o | u | t |
| ┤ |  | : |  | r | o | l | l | e | r |  | p | u | s | h | i | n | g |  | t | o |  | E | a | s | t |  |  |  |  |  |  |  |  |  |

Each roller reduces cart speed by 50000. When speed is finally reversed, the cart is sent south at a predictable 0.5 t/st, then directed west again. This design is suitable for extremely fast minecarts; the above layout capable of taking a cart moving over 6 t/st to below derail speed in a single step! As long as the cart lands on one of the roller tiles, all previous tiles apply their deceleration. (A cart fast enough to skip over the entire roller will not be slowed at all.) The linear design also means you can send a bunch of carts into it at once without collisions.

### Loading liquids

Water and magma can also be loaded into minecarts by submerging them to a depth of at least 6/7 while standing still or moving at speeds of at most 10000. Loading fluids onto minecarts can be difficult because the added friction provided by fluids can stop a cart in a submerged tile. Curiously, filling a minecart with magma does not injure a dwarf *riding* it. A minecart will hold enough fluid to increase the depth of a single tile by 2. This amount is listed as "**833 units**" (rather than "depth 2"), which weighs 459Γ (water) or 999Γ (magma). An iron or steel cart filled with magma weighs 1313Γ, while an adamantine cart filled with magma weighs 1007Γ. Since you need a minecart above the liquid's level, possible arrangements may include pressure-activated sluices, rollers (with magma-safe chains for magma), pouring from above to "submerge" it briefly on the same level and drain excess away (dig deeper and leave a vaporizer, though if you could have power for rollers, may as well use a pump) and exploits with ramps (not necessarily impulse ramps, "same height" passing dip does it). The liquids can be dumped by a constructed track stop.

## Quirks

This little quirk concerns dwarf-managed minecarts. If a track which was previously open becomes blocked (ex. flipping a switch connected to a floodgate you've built on the track to raise it) and the conditions for departure are met, instead of refusing to ride/guide the minecart or ride/guide it until it reaches the obstacle, the dwarf will pick up the minecart off the tracks and haul it to its scheduled destination on foot. If the distance is long enough and the weight of the cart heavy enough (due to being filled with heavy items such as stones), the dwarf may drop the cart because of fatigue/hunger/thirst before reaching the destination. This will cancel that vehicle setting job and make another dwarf come by and attempt to haul the cart to the nearest appropriate stockpile where another dwarf will pick up the cart and attempt to haul it to its initial stop. If the stockpile is far enough from initial stop, this second dwarf who is attempting to place the minecart on its tracks may also drop the minecart out of fatigue/hunger/thirst creating a loop that will go on until a dwarf with enough endurance manages to place the minecart where it belongs.

In fact, it seems dwarves are more than happy to attempt to carry a minecart from one stop to another even if just waiting until the track is open again would be the more sane option.

Dwarves will also carry a minecart to its next stop if the direction specified is incorrect (or invalid). This can often occur when using the default departure settings and forgetting to set the direction of each condition.

Dwarves can admire buildings while riding mine carts. Dwarves will not fall asleep during a ride (at least not from being drowsy). If riding on a continuous powered track loop, the dwarf will die of dehydration/starvation as they can not jump off to get sustenance.[5] Dwarves riding in submerged minecarts will gain experience in swimming.[6]

Tracks block wagon access to trade depots, unless they're on a ramp. Bridges can also be used, as they function as tracks but do not block wagons.

## Physics

Minecart physics depend greatly on the departure mode set in the route stop conditions.

When set to "Push" or "Ride", minecarts will move according to the regular laws of momentum, gaining speed when going downhill, losing it slowly due to friction when on a flat plane, and more quickly when going uphill. In these modes, minecarts will move in a straight line until they either are brought to a stop by friction or an obstacle, or until they encounter a turn. A minecart will roll straight past "blocked" ends of T-junctions or track ends, they have no power to restrict a cart's movement. The cart's behavior is largely independent of the weight of its contents (including fluids and dwarves): heavily loaded carts gain more momentum when accelerating, but this only plays a role in collisions: a heavy cart gains just as much speed and is as easy to stop as a light one. In either case, dwarves can not push nor ride an unpowered cart up a ramp. The cart will stall and roll back towards the direction it came. At best, this is a waste of time; at worst, it will give your cart-pushing dwarf a fun surprise. To solve this, the player can either use Rollers (see below) or set the cart to be Guided.

The difference between "Push" and "Ride" is whether the dwarf will go along with the cart or not.

Push: the dwarf will give the cart an initial push, not enough to go up a ramp, but enough to go some way along flat track. The dwarf will remain at the first stop, ready for a new job.

Ride: the dwarf will give the cart the same initial push and then hop aboard the cart riding it to the next stop.

Guide: the dwarf will steadily walk the cart to its destination while seemingly ignoring all laws of physics.

While being guided by a dwarf, minecarts will:

- Ignore the weight of any and all items inside.
- Ignore active working rollers.
- Will *not* collide with other guided carts even when a full frontal collision would be expected.
- Will ascend ramps with ease like a crundle scaling a cliff.

Because of these quirks, minecarts being guided will always move at the speed of the dwarf that is guiding them. It is thus recommended to pick the most agile of your dwarves for cart-guiding tasks. It also means for simple non-powered rail systems, "Guide" is the recommended method of transport despite it diverting a dwarf from other, potentially more important tasks.

Some samples with behavior:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | A |  | \ |  | B |  |  |  |  | A |  | \ |  | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A |  | \ |  | B |  |  |  |  |
|  |  |  |  | B |  |  |  |  |  |  |  |  |  |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | B |  |  |  |  |  |  |  |
|  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ║ |  |  |  |  |  |  |  |
|  | A | ═ | ═ | ╝ |  |  |  |  |  |  |  | A | ═ | ═ | ╩ | ═ | ═ | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A | ═ | ═ | ╬ | ╗ |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | Y | o | u |  | c | a | n |  | o | n | l | y |  | g | o |  | A | \- | \> | B |  |  |  |  |  | ╚ | ╝ |  |  |  |  |  |  |
|  |  | W | o | r | k | s |  |  |  |  |  | w | h | e | n |  | t | h | e |  | c | a | r | t |  |  |  |  |  |  |  |  |  |  | W | o | r | k | s |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | i | s |  | i | n |  | G | u | i | d | e |  | m | o | d | e | . |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

In the second example above, a cart "pushed" from B will go over the junction and roll off into the unknown south.

### Numbers behind the scenes

According to early research by **expwnent**[7]:

The minecart has 3 variables for velocity. Velocity can be thought of as tiles per 100000 ticks, so a velocity of one hundred thousand means a cart travels one tile per tick. By going down a large number of ramps, a maximum velocity of 270,000 can be reached, which presents the limit for most practical applications. Short bursts of (much) higher speeds are possible through carefully planned collisions of high-speed carts.[8] (See Perfectly Elastic Collisions.)

Every tick the cart adjusts sub-tile position units by the amount of their velocity, as well as adjusts velocity depending on current tile (speed is reduced by the "friction" of the tile, or accelerated if going "down" a ramp). On flat (non-ramp) tiles, the cart will move to the next tile when the sub-tile position goes 50000 away from the centre of the tile, denoted by the no-fraction integer value - tile 15 e.g. has its centre at the exact value 15 and its borders at co-ordinates 14.5 and 15.5.

Since most deceleration and acceleration is applied per step, with the notable exception of corners, a cart going at twice the speed of another one can travel about four times the distance before coming to a stop when going in a straight line, but only twice the distance along a winding track with very many corners.

A push will teleport a cart to the middle of the next tile in one tick with 19990 speed (10 speed is lost due to track friction), while a roller will directly give a cart the roller's set speed (minus friction) and the cart starts accumulating distance from its standing position. When a cart leaves a ramp it will emerge after one tick at the very end of the next regular tile.

Friction of tiles:

Tile
Friction
Comment

Tracks
10

Ground/Floor
200

Unusable ramp
10

Upwards ramp
4910 (10+4900)

Downwards ramp
-4890 (10-4900)

Roller
±100000 (but capped by the set speed)

Corner track
10
Speed reduced by 1000 upon leaving the corner tile

Track stop (highest)
50000

Track stop (high)
10000

Track stop (medium)
500

Track stop (low)
50

Track stop (lowest)
10

Water 1-6
Additional (WaterLevel - 1) * 100
See Skipping

Magma 1-6
Additional (WaterLevel - 1) * 500

Empty space
0

Water of depth 7/7 provides a friction of about 10000 per step. Maximum-depth magma causes at least as much friction, possibly more. This higher friction may not apply to very slow-moving carts.

Impulse sources:

|                |       |
|----------------|-------|
| Feature        | Speed |
| Push           | 20000 |
| Roller lowest  | 10000 |
| Roller low     | 20000 |
| Roller medium  | 30000 |
| Roller high    | 40000 |
| Roller Highest | 50000 |

Note, again, that nearly all of these values are applied *per tick*, rather than *per tile*. The exceptions are curves, which is 1k deceleration per direction change at the end of the tile, and rollers, which *set* the speed every tick. This makes rollers particularly useful in high-deceleration situations, such as underwater, but require that *nearly every tile* in such high-deceleration situations have a roller.

A cart heading up a ramp can experience deceleration on multiple ticks, (and stays on the tile more ticks the slower it is going, resulting in greater deceleration,) and as such, a cart leaving a "Highest Speed" roller with 50k velocity will not be able to climb 10 consecutive straight ramps, since they are *not* "5k deceleration each". In fact, the first ramp not on a roller will be -15k velocity, and, depending slightly upon other factors of "remainder" x position, the second may completely cancel forward momentum, and send it rolling back down, where it will bounce off the roller repeatedly. Using rollers to power carts up ramps reliably requires rollers every other un-rollered ramp. Fortunately, rollers can be built upon ramps, themselves, which allows for rollers to only need to be built every other floor. (Exploiting the checkpoint effect can allow one to bypass this requirement.)

There are two important speed values which affect carts' behaviour:

"Derailing" can happen when a cart moves at speeds in excess of 50000 - carts will ignore track corners unless forced to obey them by walls or other obstacles blocking the straight path.

The "shotgun" effect takes place when a collision changes a cart's movement speed by more than 55000: loaded carts subject to such a change eject their contents, which then keep on moving in a ballistic trajectory, in the direction and at the speed the cart had before the collision (with a small random vector added). This effect entirely rides on the amount of speed *change* - a speeding cart crashing into a wall can be subject to it just as well as a standing cart accelerated by a speedy cart smacking into it. It can even happen when two relatively slow-moving carts (down to speeds below 20000 in extreme cases) collide head-on.

### Sub-tile Positions and Velocity

Carts store six values that are unique to them. Three sub-tile position values, and three velocity values. (X, Y, and Z.)

Note that the Z position and velocity only matter when a cart is in flight. (See Falling and Cart Jumps.)

Each non-ramp tile is functionally composed of 100,000 individual minimal-length positions *within* the tile in both dimensions. When a cart has velocity, it is added or subtracted from the current position every tick, and then a friction force is applied to the cart.

In essence, every sub-tile position unit is a decimal value of a tile, 0.00001 tiles, in a game that largely prefers integer values.

The exact cart coordinates shown e.g. by a DFHack script must be rounded arithmetically (up or down to the nearest integer) to find the current tile: a cart in the centre of a tile will be at sub-tile zero in all directions, and it will cross into the next tile when subtile value is more than 50 000 higher or lower than the full number.

When carts move beyond the borders of a tile, they physically move a tile on the map, and start at the far end of the sub-tile position the next tile. (I.E., traveling West, a cart that starts a tick 15,000 X away from the border and has an X velocity of -20,000 will move -5000 X past the adjacent border of the next tile in direction -X. It will also lose 10 velocity in that tick due to friction with the track if it is on a track, or 100 velocity if it is on regular ground, or no velocity if it is airborne.)

Ramp tiles are longer, approximately 141,420[9] in the direction where it "slants downward", (to approximate a 45 degree slope, it is square root of two times longer,) with a centre-to-border distance of 70,710. Because of this, a cart with no velocity dropped from a hatch will land at the center of a tile, 70,710 away from the tile's borders in both directions, and will start rolling in the ramp's "downward" direction, picking up the ramp's acceleration (4890 per tick in the direction of the ramp's "downward" direction) every single tick, then moving that sub-tile amount every tick. (This results in a cart that takes 5 ticks of acceleration to leave its ramp - 6 ticks overall - and to leave the ramp with about 23k velocity, slightly more than a push.) When it enters another ramp *facing the same direction downwards*, a cart will start at the -70710 or +70710 position, and have twice as far to travel. This means that if a cart enters a ramp from the side, it will gain twice the momentum of simply starting at the midpoint of a ramp.

Note that passing from one direction of ramp to another or to flat terrain causes unintuitive behavior, "teleporting" to the end of another tile in what is called the "checkpoint effect".

Note, however, that all sub-tile positions are carried over from tile-to-tile. This separate tracking of velocity and position between X and Y can lead to problems with diagonal motion:

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| z   | 0   |     |     | z   | \-  | 1   |     |     |     |     |     |     |     |     |     |     |     |     |
| ▒   | ║   | ▒   |     | ▒   | ▒   | ▒   |     |     |     |     |     |     |     |     |     |     |     |     |
| ═   | ▼   | ═   |     | ▒   | ╬   | ▒   |     |     |     |     |     |     |     |     |     |     |     |     |
| ▒   |     | ▒   |     | ▒   | ║   | ▒   |     |     |     |     |     |     |     |     |     |     |     |     |
| ▒   |     |     |     | :   |     | W   | a   | l   | l   |     |     |     |     |     |     |     |     |     |
| ═   | ,   |     | ║   |     | :   |     | T   | r   | a   | c   | k   |     |     |     |     |     |     |     |
| ╬   |     |     | :   |     | T   | r   | a   | c   | k   |     | a   | n   | d   |     | R   | a   | m   | p   |

If a cart is passing West-to-East over this setup, the valid ramp to the South will apply "Southward" acceleration to the cart (-Y velocity) as it passes through the ramp tile. Assuming it only spends two ticks in that tile, it will have gained a lasting -5k Y velocity, which will still apply motion Southward. If the cart continues travelling over straight track for another ten steps, it will have accumulated enough Southward motion to try to move a tile South, even if all tracks are facing East-West.

A single tile spent on the ramp will not grant lasting southward motion, because the acceleration will be neutralised through the checkpoint effect when the cart leaves the ramp again, but the cart will be displaced about 5k sub-tiles southward, which can cause it to gain more or less speed than an undisplaced cart when meeting another south- or north-accelerating ramp.

**Non-curving tracks do not correct this motion**.

They don't "tip back over" without adjustments in the track. Any value of sideways motion on tracks larger than 990 will lead to a derailment. (Lower values will be nullified by friction before they are enough to lead to derailment, but there is currently no way to apply such a small amount of velocity.)

If the tile to the South is a wall at that point, it will be considered a collision with a wall that *halts all motion*. If the tile is open, the cart will simply leave the track and travel over the terrain beside it. In almost any circumstance, this is undesirable behavior.

The only way to appropriately deal with this is to either cancel out this behavior with an equal amount of acceleration in the opposite direction, or to take a curve.

Note, again, that sub-track position is saved in both directions, so when a cart approaches a curve, it will already have a shorter or longer distance past the curve when it makes the turn.

Curves are applied at the end of a tile. If a cart is moving East, and approaches a North-West track corner at 30k velocity, and friction is eliminated for the purposes of a cleaner demonstration, then when it enters the tile on the western (X coordinate) border of the tile, but in a central North-South (Y) orientation (sub-tile -50k X and 0 Y due to arithmetic rounding), it will then move 30k East (+X) the next tick, and be at -20k X sub-tile position, and 0 Y sub-tile position. Next tick, it is at +10k X sub-tile position, and 0k Y sub-tile position. Two more ticks would take it to +70k X, but that's past the tile border, so it stops at 50k, turns (and thus loses 1k velocity, but translates the rest from X-velocity to Y-velocity) and travels another 20k. It is now at 0k X sub-tile position, and -20k Y sub-tile position (i.e. it's re-set from the end to the middle of the tile with respect to the X co-ordinate). Next tick, it travels at 29k velocity North, and so moves to 0k X sub-tile position, and +9k Y sub-tile position. Then in two more turns, it leaves to the North.

In the case of diagonal motion due to having velocities in X and Y at the same time, it is critical which tile the cart actually tries to enter next. Only if the path into that tile is blocked by the corner branches will the cart take the corner and rewrite its velocity, otherwise it leaves the corner tile without changes to its motion. If the cart is redirected by the corner, all sideways velocity is lost, as forwards velocity *overwrites* sideways velocity in a curve. If, in that example in the paragraph above, the cart entered at -50k X sub-tile position with 30k X velocity, and 40k Y sub-tile position and -1k Y velocity, it would take that "curve" (or rather, redirection of velocity) on the fourth turn, while it is at 37k Y sub-tile position to start with, and then move to -53k Y sub-tile position at the end of that tick. It would then move to -26k Y sub-tile position in the following turn, and take 3 turns to clear the tile.

But, most importantly, it would be centered in the X sub-tile position, and all sideways velocity is safely removed.

There are two common ways to gain sideways velocity: Rollers facing perpendicular to the cart's travel path (which, as covered above, are almost always a bad idea, as it is easier to push *against* the travel direction of a cart into a curve, which redirects all velocity in the new direction,) and corner ramps, and require a curved track to compensate for sideways velocity within a few tiles.

### Track Direction Irrelevance

Carts that are traveling independently (that is, not guided) only care that tracks *are* on the tile, not which direction the tracks actually move. Tracks respect only curves (with two exits) and ramps.

This means, for example, that the following tracks, when a (non-guided) cart travels from West-to-East, are functionally identical in effect:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| A | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | B |  |  |  |  | A | ╬ | ║ | ╚ | ╔ | ╣ | ╩ | ╦ | ╠ | ╥ | ╨ | ╞ | ╡ | B |

This is because so far as the cart is concerned, only valid ramps and curves with two exits where there is no exit in the path they are traveling matters.

Hence, if a minecart encounters the end of the track or a T junction with no "exit" in its movement direction, it will simply leave the track and continue on its course in a straight line until it encounters an obstacle, slows to a stop, or encounters another track even if the tile at which it joins the new track instantly sends it around a corner.

In fact, in a track designed for pushes or rides, a "║", a "╦", a "╬", and a "╥" are *only different in appearance*, and are ignored by an unguided cart, which will continue in its current direction, regardless of the track. For any purpose but guided tracks, *only curves and ramps matter at all*.

Tracks like T-junctions, however, *are* respected by dwarves guiding carts, who will lift and carry carts if they cannot find a valid track to their destination, and can choose to follow any orthogonal direction at a four-way junction in much the same way as they normally pathfind. What this functionally means is that T and four-way junctions *only guide dwarves hauling a cart, not carts, themselves*.

Carts only check for curves when they are halfway through a tile. When they get there, they look to see if their path has no exit. (That is, if it is traveling East, it checks if there is an East exit.) If there is, it ignores all other track directions, and keeps traveling. If there is not, it checks to see if there are only two exits to the track, and if one of those directions was the direction it "came from". (That is, if traveling West from the East, it checks if there is a valid exit to the West, and if not, if there is an East exit and EITHER a North or South exit.) If there is not, it ignores the track anyway, and keeps on traveling as though it were still on track.

If there is a curve the cart will respect, it checks for derailment. Carts derail if their speed is higher than 50k. Carts at this critical speed will then check for blockages of their forward path. If there is an obstacle to their path, which may be a wall or even furniture or buildings like a door, they will not derail and respect the curve, anyway. Derailing carts do not "jump" unless they hit completely untracked tile or an invalid ramp, but simply ignore the layout of the tracks entirely. With invalid ramps, this means not respecting the ramp, and likely results in collision with a wall, zeroing of all velocity, and a cart that requires manual retrieval.

If the cart is traveling at a speed that will not derail, or is forced to turn by a supporting wall, it will subtract 1000 from the "forwards" velocity of the cart, and redirect all forward velocity to the direction of the curve. This change in the direction of velocity *overwrites* any "diagonal" velocity, which can prevent diagonal velocity derailments, but any perpendicular velocity is not preserved, and is instead discarded.

### Valid and Invalid Ramps

Ramps are functionally defined for cart purposes as being a tile which exerts an acceleration force upon its "downward slope", and which allows connection to tracks a z-level above or below. This downward slope requires a cart to have at least one track branch touching a wall tile and one *and exactly one* carved exit to the tile that is the "bottom" of the ramp. Ramps accelerate carts in this "downward" direction (possibly leading to diagonal movement), and the deceleration of an "uphill" ramp is actually just the acceleration being applied against the direction of a cart's movement.

This is where players can find an exploit in the behavior of ramps - if there are *two* "downhill" exits to a ramp (such as a "T junction" on a ramp where only one exit faces a wall), then the ramp provides no acceleration *or* deceleration, allowing carts to travel up ramps without any loss of momentum except for the standard "flat track" deceleration, because as far as the cart is concerned, the track *is* flat. (A T junction is also not a curve, so the track is considered flat and straight no matter what direction the cart is traveling.)

Similar effects can be achieved when there are *no* "downhill" exits to a ramp. This may be the case if you have, for example, an East-West track with a one-tile channel with a ramp in it. The cart will travel through the "dip" with no change in velocity. It can also be the case if you abuse the Track Direction Irrelevance, and set only exits *up* the ramp, and none leading *down* the ramp. For example, if a cart is traveling from West to East up a slope, only carving East exits on each tile of ramp will make the cart travel up the ramp, and then recognize the tile it is on as being a "flat" tile, thus ignoring any deceleration from traveling uphill.

Note that this effect only reliably occurs at below-derail speeds as the cart will treat the ramp as an invitation for a ramp jump otherwise. (This almost always results in a collision with a wall that will stop forward progress.)

### Falling

When falling, a minecart appears to cause no damage upon collision, possibly to allow cart "stacking" across Z-levels.[10] A dwarf riding in a minecart that is dropped multiple z-levels suffers normal fall damage. Minecarts can fall through up/down stairs.

While airborne, carts do not feel the effects of friction in any horizontal direction, and will continue until they strike an obstacle. Carts that land on tracks instantly re-rail themselves regardless of track directionality.

Falling carts accelerate similarly to the way that a ramp will accelerate a cart in a special z-only velocity that only applies to airborne carts. (Actually, since a tile is notionally 1.5 times as high as it is wide/long, acceleration due to gravity in freefall appears slightly *slower* than ramp acceleration, since it has to move the cart (or any other object) a greater distance.) Ramp acceleration, while it logically should be partially z-directional, is only recorded as x- or y-directional, and there is no translation of z-directional velocity upon landing. Landing carts zero out their vertical velocity upon landing, even when landing on ramps, although carts that had horizontal momentum while falling preserve it.

This means a cart falling onto a track ramp is accelerated as if starting from the middle of the ramp - i.e. to the same speed, no matter how many Z-levels it was dropped, vertical velocity is negated. [11] As a consequence, the fall damage to passengers is also negated.

Carts falling onto a floor can, however, cause damage to creatures *one tile below the floor*. This can be used in an exploit called a "thumper", where carts are caused to repeatedly fall on a floor above an entrance to the fort, inflicting significant damage (as though it were a collision) on those below the cart.

### Cart Jumps

Carts that cross off of "up" ramps relative to their current direction of travel, which do not have a ceiling above them, are traveling above derail speed, and do not have valid ramp track before them can translate a portion of their horizontal velocity into vertical velocity, causing a cart to be projected into the air until vertical velocity is negated and overcome by the gravitational acceleration. Because downwards acceleration is applied per-tick, this creates a reasonable facsimile of the parabolic motion of an actual object rolled up a ramp and launched with significant speed.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| z | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  | z | 0 |  | h | i | d | i | n | g |  | r | a | m | p | s |  |  | z | \+ | 1 |  | A |  |  |  |  |  |  |  |  |  |  | z | \+ | 1 |  | B |  | ( | h | i | d | d | e | n |  | r | a | m | p | ) |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  |  |  | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  |  |  | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  |  |  |
| ═ | ▲ | ▲ | ▲ | ▲ | ▲ | ═ | ═ | ▲ | ▒ | ▲ | ═ |  |  |  | ═ | ╚ | ╚ | ╚ | ╚ | ╚ | ═ | ═ | ═ | ▒ | ═ | ═ |  |  |  |  |  |  | ▼ | ▼ | ▼ | ▼ | ▼ |  |  | ▼ | ═ | ▼ |  |  |  |  |  |  |  | ▼ | ▼ | ▼ | ▼ | ▼ |  |  | ▼ | ╚ | ▼ |  |  |  |  |  |  |
| ▒ |  |  |  | : |  | W | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ═ |  | : |  | t | r | a | c | k |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ▲ |  |  | : |  | R | a | m | p |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

In this diagram, if there is no ceiling above it, the track in z+1 A will launch its carts airborne when they travel across the ramp. z+1 B (with a ramp on the tile on the hill) will not launch the cart. The cart would also not be launched with *any* valid ramp, even if it does not travel in an appropriate direction, such as North/South (which the cart will ignore, as it is not a curve, anyway, although it may produce acceleration that may cause diagonal movement.)

Carts will also start "jumping" from the track if it hits an un-tracked tile, flying over and ignoring any tracks until it is ready to land. Carts that land upon tracked tiles re-rail themselves, and clever designers use this feature to jump over curved track sections in one direction or another. (Retracting bridges over untracked tiles can cause jumps or not cause jumps depending upon the status of the bridge.) Minecart speed must be carefully regulated to ensure reliability of jump length.

Hitting untracked tiles at around 70k velocity creates a vertical component to acceleration that allows for jumps of around 6 (horizontal) tiles that do not actually leave the z-level the cart is on, but which do apply z-direction velocity on the cart, as per falling.

At the start of a jump, there is a takeoff period before the cart stops interacting with terrain and starts counting as a projectile(i.e the cart will fly over open space, but will still bump into fortifications, activate checkpoint effects etc.). The "runway" length before takeoff is affected by the velocity of the cart. After flying through the runway, the cart starts acting as a projectile. However, if the last tile of the runway is not open space - for instance, it is a track or a floor - the cart will not act as a projectile for 1 extra tile. In other words, the runway is extended by 1 tile if its last tile is not open space.

Carts that approach a downward slope at a high enough velocity will also make a jump, (or rather, ignore the ramp and fly forwards) but will not do so if the Checkpoint Effect is exploited through an impulse ramp before the actual downhill as the impulse ramp "tricks" the cart into thinking it has already started going downhill.

### Skipping

If a minecart is moving fast enough, it can skip over water or magma of level 5 or higher, making splashes of mist (or magma mist) as it attempts to move on them horizontally. This horizontal movement is independent of the minecart and its content's weight.

Skipping causes significant friction on the cart, and even a cart going at max speed from ramps can only make about 50 tiles without requiring re-acceleration. (Carts that decelerate enough that they do not trigger the skipping effect will, of course, sink.)

### Corner Ramp Derail

Corners on upward ramps can cause diagonal movement, forcing a derail even if the cart has a wall next to it, which will force a stop when it touches a wall that forces dwarves to manually reset the cart.


---
*Parte 2 de 3 de «Minecart». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Minecart*
