# Pressure

> Fonte: [Pressure](https://dwarffortresswiki.org/index.php/Pressure) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Dwarf Fortress* features some pretty complex behavior in an attempt to simulate **fluid mechanics**. One aspect of this behavior is seen in the form of **pressure**. The basic idea here is quite simple - certain forms of **fluids** movement exert **pressure**, causing them to potentially move *upwards* into other areas.

## Summary

In *Dwarf Fortress*, contrary to what many people may believe, pressure is **not** a property of a body of liquid. It's simply one of three rules by which liquids can be moved - the others are simple *gravity* (when the tile beneath contains less than 7/7 of liquid and it simply falls downward) and *diffusion* (when the liquid levels of two adjacent tiles are averaged, possibly pushing items around).

The following types of liquid movement follow the rules of pressure:

- Water falling downward into *more* water
- River/brook source tiles (whether the map edge or the "delta" where the river itself begins) generating water
  - Lakes (surface or subterranean), oceans, and the magma sea refilling from the map edge do **not** exhibit pressure
- Screw pumps moving water **or** magma

When a liquid is moved (or created) with pressure, it attempts to locate the nearest tile on the same Z-level as its destination tile (for falling water, this is 1 Z-level *beneath* its original location) by moving north, south, east, west, down, or up. As it tries to locate an appropriate destination, the liquid will first only try to move sideways and downward - only when this fails will it attempt to move upward. Pressure will not propagate through diagonal gaps.

**Speculation**, from a simple test, it appears that water falling on an open tile can still spill up z-levels if it is not dispersing fast enough, \*before\* having filled up the entire z-level. The solution to this is to pump the water ingress tile directly.

## A demonstration of pressure using U-Bends

A U-Bend is a channel that digs down, and curves back up. With **pressure** a fluid will be pushed up the other side of the u-bend. By understanding how pressure works in a u-bend you should be able to adapt this knowledge to use fluids in any configuration you desire without any unexpected surprises that could make life in your fortress more **fun** than anticipated. **Water** and **magma** behave very differently with regards to pressure, so read carefully.

### Water in a U-Bend

The key to understanding how high a z-level water will reach is to understand which tile(s) pressure is being *exerted on*. Pressure will cause the water level to go *as high as* the tile upon which pressure is being exerted, but *no higher*.

The following three diagrams demonstrate different ways water might behave in a u-bend. In all three cases, the water source is on the left side of the diagram and water is filling the larger area to the right.

Diagram A
Diagram B
Diagram C

▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓
▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓
▓ / ▓ / ÷ / ÷ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓

Undammed River
Dammed River
Screw Pump

(All diagrams are side views, and cover 4 z-levels of water, plus a "bottom" z-level of stone/soil.)

\
In the first example (**Diagram A**), we have water taken directly from a (flat) river used to fill a u-bend. In this case, the river is free to flow off the edge of the map, so the only pressure comes from the water tile on the top of the u-bend's left side (highlighted in green) falling downward (into the tile highlighted in red), so the water on the right side stops one level below the river itself, because even though the *source* tile is at river level, the *destination* tile (in red), whose height the water will reach because of pressure, is one z-level *below* the source tile.

In the next example (**Diagram B**), a **dam** (*not shown*) has been placed, which now prevents the river from flowing off the edge of the map. In this case, since it no longer has a "preferred" area to flow into, the pressure exerted by the river source (highlighted in red) allows the water to fill up the remaining level of the u-bend. Use caution when placing a dam on your river.

- Note that this situation also applies **on a map where the river is running into the sea**. Rivers running into the sea are not free to flow off the edge of the map, as the sea itself actually "dams" them.

The final example (**Diagram C**), demonstrates how a **screw pump** exerts pressure - in this case, the water fills up to the same level as the pump's output tile (highlighted in red).

With these three simple examples, you should be ready to go build your enormous plumbing masterpiece, and be relatively safe from any unanticipated flooding. If you plan to work with magma as well, however, you should read further.

### Magma in a U-bend

**Magma** does *not* exert pressure when *it falls downward*. In our first magma example (Diagram A) we show how this works by creating a short u-bend and connecting it up to a magma pipe - it simply fills the lowest point and makes no further attempt to go back up.

|  |  |
|----|----|
| Magma Pipe / (side view) | Screw Pump / (side view) |
| ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ | ▓ / ▓ / ÷ / ÷ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ≈ / ≈ / ▓ / ▓ / ≈ / ≈ / ≈ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ / ▓ |
| Diagram A | Diagram B |

In the second diagram (Diagram B) we see how with the addition of a single screw pump, the entire situation changes dramatically. When the screw pump moves magma to the right side, it does so using the rules of pressure and allows the area to fill up to the level of the pump. Accidentally flooding your fortress with magma is considerably more fun than a flood of water.

## Advanced Pressure

### Lazy model

Pressure is a lazy model, but will *always* behave like above. For example, a system on z0 receives water from a cistern z3 in amounts of ~3/tick. This system consists of a tree of passages, one tile wide, and contains 'underpasses' on z-1. Water will flow into the system to a depth of 7 before coming up on the other side of a the first underpass, as is expected. However, if faced with *two* underpasses, it will choose the nearest one and fill all the system on the other side of that underpass to a depth of 7 before filling the system on the other side of the far underpass. Similarly, if faced with multiple exits from the system, the whole flow will flow out of *one* exit, the nearest lowest one.\[Verify\]

### Waterfalls

Waterfalls are of special concern. When drawing water from a waterfall it is important to understand that, since the water is falling **on top of** the river's surface, the pressure exerted when it falls down into the river will permit it to pass through U-bends that would normally not be filled when using a flat undammed river - if you tap into a river below a waterfall just as you would above it, you could very easily flood your fortress.

## Neutralizing pressure

There are three methods for neutralizing fluid pressure: diagonal connections, screw pumps, and active control systems. Knowing how to manipulate pressure as needed allows you to quickly move fluids wherever you wish in your fortress allowing you to build things a dwarf can be proud of. Note that fortifications do *not* neutralize pressure.

### Diagonal flow

Liquids moving via pressure can only move to orthogonally adjacent tiles. When faced with a diagonal gap, pressure will fail to move the liquid, forcing the liquid to instead spread out. By forcing fluids through a diagonal connection you can prevent pressure from propagating past a certain point.

This does not work on a vertical basis - water only travels straight up and down to different Z-levels, never diagonally.

If you wish to maintain the rate of **flow** after de-pressurizing, it's recommended that you have more diagonals than water tiles - that is, if the source is 3 tiles wide, you may wish 4 or more diagonal passages.

**Top view**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| \> | \> | \> | \> | \> |   |   |   |   |   |   |   |   |   | ▒ |   |   |   | \> |   |   | \> |   |   | \> |   |   |
| 4 | Z |   | P | r | e | s | s | u | r | e |   |   | ▒ |   |   | 1 | Z |   | P | r | e | s | s | u | r | e |
| \> | \> | \> | \> | \> |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | \> |   |   | \> |   |   | \> |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

**Side view**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ≈ | ≈ | ≈ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ≈ | ≈ | ≈ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | R | R | R | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ |   | R | R | R |   | = |   | P | r | e | s | s | u | r | e |   | r | e | g | u | l | a | t | o | r |   | d | e | s | i | g | n |   | a | s |   | s | e | e | n |   | i | n |   | t | o | p |   | v | i | e | w |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

### Pumps

Since water pressure does not propagate through pumps, it is possible to fill a pool from a "pressurized" source using a screw pump without it overflowing. Of course, there is a downside - you still have to run the pumps and due to the source water's pressure, the pump must be powered instead of run by a dwarf, as the tile the dwarf needs to stand on is filled by water. Furthermore, the pump will likely need to be powered from above or below (as water would simply flow around a gear or axle placed next to the pump), though creative setups are still possible by using additional screw pumps to transmit power.

Your vertical axles or gear assemblies need to be placed above the solid tile of the pump, and there must not be a channel over the walkable pump tile. (Water can only flow straight upward, not up and to the side at the same time.) Multiple adjacent pumps will also transfer **power** between themselves automatically.

Side view

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| P | o | w | e | r |   |   | W | a | t | e | r |   |   |   |
| ↓ |   |   |   |   | ↓ | ↓ | ↓ | ↓ |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ║ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ║ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ |
| . | . | . | . | . | ▒ | ║ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ |
| ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ÷ | ÷ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ | ≈ |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

Key:

|     |       |                                                     |
|-----|-------|-----------------------------------------------------|
| 1\. | ▒     | Wall                                                |
| 2\. | ▒     | Wall that would flood with pressurized water if dug |
| 3\. | ÷ / ÷ | Pump facing left, with the right tile flooded       |
| 4\. | .     | Floor                                               |
| 5\. | ≈     | Pressurized water                                   |
| 6\. | ≈     | "Unpressurized" water                               |
| 7\. | ║     | Axle                                                |

Note that the screw pump *will* still exert pressure when filling the pool, but said pressure will be independent of the source and can be subsequently blocked by diagonal gaps.

### Advanced systems for fine tuning pressure

Multiple methods can be used to modify the pressure of fluids to a specific number of Z-levels. One of the simpler examples is using an active control system and mechanical cycling.

An active control system can allow some water flow while preventing pressurized water from overflowing. Such a setup is significantly more complicated than the other two options, but it can produce controlled amounts of water at varying depths and pressures. While there are many different ways to set up a control system, a relatively simple example is shown below:

#### Simple example using mechanical cycling

Side view

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| 8 | Z |   | P | r | e | s | s | u | r | e |   | ≈ |   | + | ≈ | ≈ | ≈ | ≈ | ≈ | + |   | ≈ |   |   | 2 | Z |   | P | r | e | s | s | u | r | e |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

Two doors ('+') are connected to a control system (such as levers or a minecart loop). The control system is designed to only open one of the doors at a time. When the left door is open, the pressurized water fills a reservoir. When the right door is opened, the reservoir provides reduced pressure and limited flow. The cycling can be controlled manually (by pulling levers), or automated (minecarts, pressure plates, etc.). Throughput is limited by how quickly the doors can be cycled; pressure plates normally have a 99 tick refractory period, but clever design can reduce that significantly.

#### Advanced examples using constructed pressure regulators

Side view

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 8 | Z |   | P | r | e | s | s | u | r | e |   | ≈ |   | R | R | R |   | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   | R | R | R |   | = |   | P | r | e | s | s | u | r | e |   | r | e | g | u | l | a | t | o | r |   | d | e | s | i | g | n |   | a | s |   | s | e | e | n |   | a | b | o | v | e |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ |   | ≈ |   |   | 2 | Z |   | P | r | e | s | s | u | r | e |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

In this setup, we can use a diagonal flow pressure regulator to convert our 8Z pressure to 1Z pressure. This will then enter our chamber as 1Z, fall down a single Z and turn into 2Z pressure.

Side view

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 8 | Z |   | P | r | e | s | s | u | r | e |   | ≈ |   | R | R | R |   | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   | R | R | R |   | = |   | P | r | e | s | s | u | r | e |   | r | e | g | u | l | a | t | o | r |   | d | e | s | i | g | n |   | a | s |   | s | e | e | n |   | a | b | o | v | e |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ |   | ≈ |   |   | 3 | Z |   | P | r | e | s | s | u | r | e |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

Here is another example showing how to expand the concept to a 3Z level output pressure. This setup can be modified to fit any Z level of pressure. It is important to note that the output pressure is at the bottom of the mechanism, and will therefore follow the above rules for water in a U-bend.

Side view

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 8 | Z |   | P | r | e | s | s | u | r | e |   | ≈ |   | R | R | R |   | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   | R | R | R |   | = |   | P | r | e | s | s | u | r | e |   | r | e | g | u | l | a | t | o | r |   | d | e | s | i | g | n |   | a | s |   | s | e | e | n |   | a | b | o | v | e |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ |   | ≈ |   |   | 9 | Z |   | P | r | e | s | s | u | r | e |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

Here is a example we can see how to generate 9Z level pressure, 1Z greater pressure than our input pressure

Side view

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| 8 | Z |   | P | r | e | s | s | u | r | e |   | ≈ |   | ≈ | ≈ | ≈ |   | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   | ≈ | ≈ | ≈ |   | = |   | P | r | e | s | s | u | r | e |   | r | e | g | u | l | a | t | o | r |   | N | O | T |   | p | r | e | s | e | n | t |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ≈ | ≈ | ≈ | ≈ | ≈ |   | ≈ |   |   | 1 | 7 | Z |   | P | r | e | s | s | u | r | e |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

In this final example, to illustrate the usage of pressure regulators in modifying and obtaining custom pressures, when the regulator is omitted the output pressure will be the sum of both the input pressure, and the drop pressure.

## Hatches

Hatches can be placed over channels, stairs, ramps, etc. to prevent water from moving vertically but will still allow the tile to be used, even as a water source (and possibly still for fishing too). Note that the construction of a hatch over the input tile of a Screw pump prevents water from being pumped.

## Plumbing schemes

Using the information above, you can devise a number of ways to get the water where you want it to be. The following schemes provide a starting point for beginners:

### Safe well

**Side view**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | X | ▒ | ≈ | ≈ | ≈ |   | \ | - | - |   | p | o | t | a | b | l | e |   | w | a | t | e | r |   | s | o | u | r | c | e |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | X | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | ○ |   |   | ▒ | ▒ | \> | \ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ |   | ▒ | ▒ | ▒ | ▒ | X | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ |   |   |   | ▒ | ▒ | ▒ | X | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | \# | ▒ | ▒ | ▒ | ▒ | X | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ |   |   |   |   |   | X | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | \ | ▒ |   | \ | - | - | u | p |   | s | t | a | i | r |   | ( | t | o |   | w | a | t | e | r |   | s | o | u | r | c | e | ) |
| ▒ | \> | ▒ | ▒ |   | \ | - | - | d | o | w | n |   | s | t | a | i | r |   | ( | t | o |   | r | e | s | e | r | v | o | i | r | ) |   |
| ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

Dig the up/down stairs ('X') near a source of good clean water (river, stream), and tunnel to the location below where you want your well. Make sure to add the pressure regulator ('\>\<') at the height of the well by digging another stairway diagonally adjacent to the first. Dig out the reservoir on the left side, channel down into the supply tunnel, and add a floor grate ('#') directly below the well (this grate keeps enemies from entering your fort via the well). Finally, channel a connection between the water source and your supply tunnel to fill the reservoir, and build your well ('○'). You can also build additional wells directly above the first, as long as you channel a clear path straight down into the reservoir.

### Pillar of pools

Can be used to provide each level with a pool. A central 'pillar' of water extends all the way down and provides the water.

**Top floor, top view**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| . | \_ | ▒ | \> | \| | ≈ | ≈ | ≈ |   | \ | - | - |   | w | a | t | e | r |   | t | u | n | n | e | l |   | ( | e | . | g | . |   | c | o | m | i | n | g |   | f | r | o | m |   | a |   | r | i | v | e | r |   | o | r |   | y | o | u | r |   | c | i | s | t | e | r | n | ) | . |   | \| |   | = |   | f | l | o | o | d | g | a | t | e |
| . | \_ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

**Top −1, top view**

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| ▒ | ≈ | ▒ | X | ▒ | \_ | . |
| ▒ | ≈ | ≈ | ▒ | ▒ | \_ | . |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

**Top −2, top view**

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| . | \_ | ▒ | X | ▒ | ≈ | ▒ |
| . | \_ | ▒ | ▒ | ≈ | ≈ | ▒ |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

Keep the central block (with up/down staircase) aligned on each level. For lower levels simply continue alternating the -1 and -2 layouts.

Don't forget to add a lever and hook it up to the top floodgate so you can shut off the main flow if you're experiencing ~~flooding~~ fun.

You can also add additional floodgates on each level if you like:

**z-1, top view**

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| ▒ | ≈ | ▒ | X | ▒ | \_ | . |
| ▒ | ≈ | \| | ▒ | ▒ | \_ | . |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

**z-2, top view**

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |
| . | \_ | ▒ | X | ▒ | ≈ | ▒ |
| . | \_ | ▒ | ▒ | \| | ≈ | ▒ |
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |

## See Also

- Hydrodynamics Education forum thread
- Flow
- River
