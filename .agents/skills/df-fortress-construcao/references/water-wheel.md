# Water wheel

> Fonte: [Water wheel](https://dwarffortresswiki.org/index.php/Water_wheel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **b - m - h**
- **═ ═ ═ X X X**
- **X**
- **X**
- **X**
- **Icon**
- **Construction**
- **Materials:** Labors
- **3 Logs:** Carpentry
- **Power**
- **Needs 10 power. Generates 100 power. Net gain of 90 power.**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Water wheels** provide power via water flow. To build one, select build menu and choose machines/fluids. It requires 3 wood and generates 90 net power, which can be used to operate one or more pumps or mills. You can use axles and gears to distribute the power of a water wheel, or connect the machinery directly.

Water wheels do *not* work with waterfalls, or magma—they need "flowing" water, according to the definition of the game.

(\* Dwarf Fortress' version of "flow" is not intuitive—see below.)

*For a basic overview of how the different machine parts work together, see machinery.*

## Construction

Animation of a water wheel connected to a millstone.

The carpentry labor is needed for construction.

A water wheel occupies 3 adjacent tiles (N-S or E-W axis, no diagonals). It is the color of the first wood selected for it, so you could build a red wheel with one piece of goblin-cap and two of any other wood.

While you can build a water wheel on solid ground, it won't provide any power. A useful water wheel is built in an empty tile with no floor (you need to dig a ramp going down) so it can be powered by water from tiles one z-level below. Build the water wheel with its central tile orthogonally next to a gear assembly, a horizontal axle, a screw pump, or the central tile of a pre-existing water wheel.

Don't hang the water wheel from a gear assembly you wish to control with a switch, as a disconnected ("switched off") gear assembly can't support anything and will cause the water wheel to deconstruct.

A water wheel produces power as long as it has flowing water with a minimum depth of 4/7 under at least one of its three tiles. The easiest way to do it is by placing the water wheel over a river or brook. **With a brook, you must first channel through the surface**, since brooks have a floor of sorts over them.

Furthermore, the water beneath the water wheel must be flowing in the right **direction** for it to work. For example, placing a N-S water wheel over water flowing straight east or west will be useless. Since most water in Dwarf Fortress flows diagonally, this is rarely an issue.

## Designs

    Key:

      #    = Wall
      ○    = Millstone
      +    = Floor
      ~    = Water
      W    = Water Wheel
      *    = Gear Assembly
      ═    = Axle

\

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | \+  | \+  | \+  | \+  | ~   | \+  |
| \#  | \+  | \+  | \+  | \+  | ~   | \+  |
| \#  | ○   | \+  | \+  | \+  | W   | \+  |
| \#  | \*  | ═   | ═   | ═   | W   | \+  |
| \#  | \+  | \+  | \+  | \+  | W   | \+  |
| \#  | \+  | \+  | \+  | \+  | ~   | \+  |
| \#  | \+  | \+  | \+  | \+  | ~   | \+  |

**Basic watermill design** {style="border: 1px solid #0b0; background: #dfd"}

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | \+  | \+  | \+  | \+  | ~   | ~   |
| \#  | \+  | \+  | \+  | \+  | ~   | ~   |
| \#  | ○   | \+  | \+  | \+  | W   | W   |
| \#  | \*  | ═   | ═   | ═   | W   | W   |
| \#  | \+  | \+  | \+  | \+  | W   | W   |
| \#  | \+  | \+  | \+  | \+  | ~   | ~   |
| \#  | \+  | \+  | \+  | \+  | ~   | ~   |

**Dual watermill design** {style="border: 1px solid #0b0; background: #dfd"}

This is by no means the limit of water power from one location, depending on the width of your river/brook/channel you can stack many water wheels side-by-side (really big assembles will need to be artificial as there is a limit to how wide the game created water flows get). Just remember to make sure there is a support structure in place before you place the next wheel.

## Perpetual Motion

Due to the relatively low power draw of a screw pump, a *self-powering* assembly can be made with a water wheel that still leaves plenty of excess power for other uses. This is undeniably an exploit and possibly a bug.

To get it working, you must start the pump manually.\*

*(\* Exceptions are aquifers, which can sometimes have a natural flow. This can be good if, for example, you want the wheel **not** to provide any power while building a pump next to it. It is not clear what causes an aquifer to keep a flow. It is difficult to replicate and might be lost with additional channeling, so designs will have to be adapted if found.)*

It is good to have a ready source of water to refill the machine, as water tends to escape and evaporate. As the water level decreases, the water wheel may intermittently stop providing power; when the level falls below 4/7, the wheel stops providing power altogether.

**\*REMEMBER TO BUILD AN ORTHOGONAL PUMP, HORIZONTAL AXLE, OR GEAR ASSEMBLY BEFORE THE WATER WHEEL\***

### Dwarven Water Reactor

This compact two-wheel design produces 170 surplus power (less additional power train). While the water reactor provides a constant source of mechanical power in high amounts, the use of several reactors can cause performance issues in the game. When building your water reactor, it is recommended that you include a method to stop it once started *(explained below)*.

|  |  |  |
|----|----|----|
| Lower / Level |  | Upper / Level |
| ╔ / ═ / ╦ / ═ / ╗ / ║ / ≈ / ║ / ≈ / ║ / ║ / ≈ / ║ / ≈ / ║ / ║ / ≈ / O / ≈ / ║ / ╚ / ╗ / ≈ / ╔ / ╝ / █ / ╚ / ═ / ╝ / █ |  | ╔ / ═ / ═ / ═ / ╗ / ║ / W / + / W / ║ / ╝ / W / X / W / ╚ / + / W / X / W / + / + / + / ≈ / + / + / + / + / + / + / + |

Reactor with Mist Generator attached.

Lower Level water channel

**Key**

║ ═ ╔ ╗\
╦ O ╚ ╝ = **Wall**

+ = **Floor**

W = **Water Wheel** with floor underneath

W = **Water Wheel** with water underneath

≈ = **Water** on current level

≈ = **Water** on level below

X = **Screw Pump** output to north\
X = **Screw Pump** drawing from south *(and temporary initial operator location, to start process)*

Dig the V-shaped channel, then fill it with water (either by designating it as a pond and letting your dwarves haul water in buckets, or via connecting to an existing source of water). On the top level, channel out two tiles under each wheel: one tile under the center of the wheel and another one by the pump output. Build the pump pumping from the south, then the two water wheels.

Start the pump manually ( q, Enter )—if there is enough water\*, the "reactor" will start immediately and the pump operator will leave. The water from the north end of the pump will spill over the top-most floor tile, filling that to 7/7 and the two tiles east and west of it to ~5/7, but will not overflow back past the water wheel to the walkway area. Note that for the upper level, no southern walls are shown as none are needed, unless you don't follow the design and do something to create water pressure.

- *(\* Estimated minimum depth to prime the reactor is 3/7 to 4/7, though this is not guaranteed as ~some~ water will be in motion on the z-level above via the pump action.)*
- The ideal amount of water in this design is apparently 63 units of water. In other words, six tiles below the V are full (7/7), and three more above are also full up to 7/7, which will generate a reliable, permanent flow without ever losing any of that water to evaporation. An easy way to do this is to simply leave your pond fill command on after the reactor activates. They will eventually fill it up to the optimal level and stop.
- When you first start the pump, you are likely to have at least some excess water splash out while the fluid level achieves equilibrium - don't locate this in an area that you don't want any mud in.
- If the reactor is connected to a load totaling more than 100 power (including that used by the water wheels and pump), it may sometimes fail to start. Using a gear assembly to disconnect the load from the reactor before starting it can fix this.

The reactor can be safely halted either by blocking the tile the pump draws water from or "overloading" the reactor (since drawing more power than the reactor supplies will stop the pump that keeps the cycle going until the load is reduced and the pump is manually restarted by dwarf-power). An easy way to halt the reactor is to place a lever-linked hatch cover over the tile the pump draws from. When the cover is closed, the pump can't draw any water, and the reactor stops. More drastically, the reactor will obviously be halted by deconstructing the pump. Deconstructing one wheel will cause a flood (and almost immediately cancel any job order to deconstruct the other components), and deconstructing the pump will cause both wheels to collapse (unless they are attached to machinery outside them, not shown).

Power can be routed up from the pump or off to the side from a wheel; the bottom of the pump is difficult to access without danger of water escaping. Routing power from a wheel is typically safe in practice, but it's not impossible for a small amount of water to escape the reactor if it is temporarily overfilled. Power can also be routed out of the reactor via a gear or horizontal axle over the pump's intake tile; while this does not interfere with the pump's operation or present a danger of flooding, it makes it more difficult to shut down the reactor. In either case, it's typically wise to place a gear assembly linked to a lever early in the power train in order to allow disconnecting the power at that point, as opposed to needing to halt the entire reactor to stop the power supply.

Expanded versions can produce more power, and can be added later with minimal advance planning; such extensibility is easily attainable by placing dis-engageable gears on either side of the two water wheels, then attaching minireactors at your leisure, or halting the original reactor by other means. Alternatively, it may be easier to simply produce a second reactor, then connect to the power train at another location.

*Note: If created in an aquifer, there is a chance that the channeled tiles will have a natural water flow - this will cause the pump to start the moment the first wheel is finished, flooding the work area for the second.*

- This can be countered by connecting something that consumes \>90 power while building the water wheels -19 Gear assemblies works

### Mini Water Reactor

This alternative is even more compact than the original dwarven water reactor, but it can be used in tight spots where you don't need more than 80 units of power surplus. You can consider this an extension unit to the DWR, as it can be added to one or the other side to provide an additional 80 power to the resulting power train.

To safely build a mini reactor and add it to a previous reactor without the risk of flooding and/or loss of power, you need to **first turn off the original reactor**.

It is better if you plan ahead; for example, build a larger reactor from the start, if you need more than 170 units of power

As stated previously, the design below produces 80 surplus power (less additional powertrain).

|  |  |
|----|----|
| Lower / Level | Upper / Level |
| ╔ / ═ / ╗ / █ / ║ / ≈ / ║ / █ / ║ / ≈ / ║ / █ / ║ / ≈ / ╚ / ╗ / ╚ / ╗ / ≈ / ║ / █ / ╚ / ═ / ╝ | ╔ / ═ / ═ / ╗ / ║ / W / + / ║ / ╝ / W / X / ╚ / + / W / X / + / + / + / ≈ / + / + / + / + / + |

When building the mini reactor, follow the same order as for the DWR. The channel, however, is slightly different—you only need one water wheel. If it is an addition to a full size reactor or set of reactors, all channels will need to be fairly full with water to start the reactor.

### Micro Water Reactor

Replacing the pump with a dumping minecart, the micro reactor is even more compact and produces up to 90 surplus power per water wheel (less additional power drain).

\

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
|   |   | z |   |   |   |   | z | - | 1 |   |
|   | + | + | + |   |   |   | ╔ | ═ | ╗ |   |
|   | + | ─ | + |   |   |   | ║ | ■ | ║ |   |
|   | + | ─ | ═ |   |   |   | ║ | ▲ | ║ |   |
|   | + | ─ | + |   |   |   | ╚ | ═ | ╝ |   |
|   | + | + | + |   |   |   |   |   |   |   |

Channel two adjacent tiles to create a trench, remove the ramp from one trench tile and build a track stop dumping into the other trench tile. Optionally link a lever to the track stop (to disable and enable the reactor later). Add a minecart to the track stop, build a water wheel over the trench, and use a pond zone to fill the ramp tile. The reactor requires 11 units of water for continuous operation; any excess will simply disappear. Once filled, the minecart will dump water into the ramp tile. The water will then flow back to the minecart tile, refilling the minecart and repeating the process endlessly. It's best to use a metal minecart for this, as wooden ones may be pushed from the track stop by the moving water.

For more power, each trench can operate two water wheels and multiple trenches can be arranged in a row to provide as much power as needed. (Each trench should remain isolated to avoid interference.) This example provides 356 surplus power with only 4 tiles of moving water:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   | z |   |   |   |   |   | z | - | 1 |   |   |
|   | + | + | + | + | + |   |   |   |   |   |   |   |   |
|   | + | ─ | + | ─ | + |   |   |   |   |   |   |   |   |
|   | + | ─ | ═ | ─ | ═ |   |   | ╔ | ═ | ╦ | ═ | ╗ |   |
|   | + | ─ | + | ─ | + |   |   | ║ | ■ | ║ | ■ | ║ |   |
|   | + | ─ | + | ─ | + |   |   | ║ | ▲ | ║ | ▲ | ║ |   |
|   | + | ─ | ═ | ─ | ═ |   |   | ╚ | ═ | ╩ | ═ | ╝ |   |
|   | + | ─ | + | ─ | + |   |   |   |   |   |   |   |   |
|   | + | + | + | + | + |   |   |   |   |   |   |   |   |

\
For a more compact design, several trench rows can be staggered to produce a solid block of water wheels, scaling to whatever size necessary. The example below provides 538 power with 8 tiles of moving water:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   | z |   |   |   |   |   | z | - | 1 |   |   |
|   | + | + | + | + | + |   |   |   | ╔ | ═ | ╗ |   |   |
|   | + | + | . | + | + |   |   |   | ║ | ■ | ║ |   |   |
|   | + | ─ | ─ | ─ | + |   |   |   | ║ | ▲ | ║ |   |   |
|   | + | ─ | ─ | ─ | ═ |   |   | ╔ | ╩ | ╦ | ╩ | ╗ |   |
|   | + | ─ | ─ | ─ | + |   |   | ║ | ■ | ║ | ■ | ║ |   |
|   | + | ─ | ─ | ─ | + |   |   | ║ | ▲ | ║ | ▲ | ║ |   |
|   | + | ─ | ─ | ─ | ═ |   |   | ╚ | ╦ | ╩ | ╦ | ╝ |   |
|   | + | ─ | ─ | ─ | + |   |   |   | ║ | ■ | ║ |   |   |
|   | + | + | . | + | + |   |   |   | ║ | ▲ | ║ |   |   |
|   | + | + | + | + | + |   |   |   | ╚ | ═ | ╝ |   |   |

\
Note: To avoid access problems, large blocks of micro-reactors should be built and filled one layer at a time.

## Flowing Water

Water wheels over a patch of "flowing" water

A screw pump produces pressurized water that flows off the map edge through carved fortifications, flagging the water as flowing.

The water movement can be cut off and the water retains the "flowing" flag.

Water wheels need flowing water. The game considers it to be flowing water under two circumstances:

1\. When deeper water flows into shallower water ("gradient flow"). Water which does not have a gradient—such as stretches of water 7/7 deep—is generally not considered to be flowing water even if the water technically flows through those tiles.

2\. When water flows off the map edge or into an aquifer. (Water entering an aquifer vanishes from the map, since the aquifer can never become full, even if it's only a single tile). This type of flow returns from a map edge or an aquifer sink, giving the water the "flowing" quality. Water flowing off the map counts as flowing even at full 7/7 depth. This kind of flow is found in brooks, streams and rivers. Artificial water channels work just as well, as long as they flow off the map.

A tile marked as flowing off the map will keeps this quality even if the water movement is later blocked. This is evident in that a dammed river will continue to power water wheels, even though the water is no longer flowing off the map. This works just as well for dwarf-made water channels, the flowing quality is so persistent that it will remain even if the area is completely drained and refilled, although while the tiles contain less than 4/7 water they won't power water wheels regardless.

Adventure mode doesn't handle flowing water predictably. Water reactors may suddenly stop providing power each time the map is loaded in. Water won't regain flow status even as the minecart continues to dump fluid. Aquifer drains don't create flow. Even river water may become still after freezing and thawing. (Map edge drains don't have anywhere to drain, and may lead to Fun instead!)

### Legitimate Artificial Rivers

You can create an underground river with 7/7 water to power water wheels by letting water from a river, lake, sea, or aquifer flow off the map edge in a cavern. For this, you need to build an aqueduct and bring the river to the map edge. Be careful: if the water spreads significantly before flowing off the map edge, the game won't consider it flowing water. Water flowing from a higher elevation (Z level) to a lower one is also considered flowing water.

### Flowing Water Reactors

You can exploit the game's definition of flowing water to create bodies of water that power water wheels despite the absence of actual water flow. When a channel is dug into an aquifer, it will sometimes have a "natural flow". However, if water is pumped into an aquifer channel, the channel will always have a "natural flow" because water is regarded as disappearing from the map at that point, and the tiles are marked as flowing water, and will power water wheels—even if the pump is removed.

The other way to create water movement is letting water flow off the map edge—most commonly through a fortification carved into a map edge, although a map edge on the surface or in a cavern also works. The water will be considered flowing water, even if the map edge gets blocked by a floodgate or a raising bridge. You can even do this with stagnant water pools (e.g. murky pools); for example, digging out a channel next to a map edge, building a floodgate to seal the map edge drain, filling the channel with 4/7 water, opening the floodgate, closing it, and filling it back up to 4/7 water.

The ethics of these reactors are not very different from constant motion machines, these using water wheels to generate power and a fraction of said power to move the water with a screw pump. A water wheel generates 100 units of power and consumes 10 units of power, the latter 10 presumably being the energy the water wheel requires to move the water in front of its blades. But if the water wheel moves water in and of itself, the pump actually becomes unnecessary. The water wheel itself both moves the water and is moved by the water.

Circular version works much better than the triangular one.

|  |
|----|
| "Water wheel" in other / Languages / Dwarven / : / arel kol / Elven / : / alu rere / Goblin / : / esp sost / Human / : / thomo pobe |
