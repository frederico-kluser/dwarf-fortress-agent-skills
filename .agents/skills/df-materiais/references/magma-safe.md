# Magma-safe

> Fonte: [Magma-safe](https://dwarffortresswiki.org/index.php/Magma-safe) — Dwarf Fortress Wiki (GFDL/MIT)

**Magma-safe materials** are materials which will not melt, burn, evaporate, or otherwise take damage when in close contact with magma. Most frequently, this comes into play when using floodgates operated by mechanisms, or when operating a magma pump.

For reactions and custom buildings using the \[MAGMA_BUILD_SAFE\] token, only a material which is solid and stable at the temperature (i.e. MELTING_POINT/BOILING_POINT/IGNITE_POINT/HEATDAM_POINT greater than 12000 and COLDDAM_POINT less than 12000) is considered magma-safe.

In order to construct mechanisms, blocks or other pump components from a magma-safe material, you have several choices:

1.  You can specify a magma-safe rock for your mechanisms and other components at the workshops by clicking the detail (magnifying glass) icon next to the order.
2.  Build your mechanisms out of iron or steel.
3.  Build your pump components out of iron, steel, glass, or nether-cap.
4.  Place a stockpile with the desired stones around your mechanic's workshop and set it to "Give To a Pile/Workshop".
5.  Use a burrow that contains only the workshop and the desired materials.
6.  Simply ensure that the desired materials are the closest available to your worker. This does not always work, but is usually good enough if you request several jobs, hoping that at least one uses the correct material.

When linking a trigger to an object, the *first* mechanism selected is attached to the object, and the *second* is attached to the trigger. Unless the trigger itself will be submerged in magma (as could be the case with a pressure plate), only the first mechanism (attached to the object that will be submerged) needs to be magma-safe. If you do not have any magma-safe stones available, you can also work around floodgate-based flow control by using screw pumps to pump the magma over wall-barriers, or using water to form obsidian to plug flows and channel through them to reopen them (necessity and invention and all that).

This property is also relevant when choosing the appropriate method for disposing of unneeded items, which can impact FPS when in large numbers. Items made of non magma-safe materials can be simply dumped into magma, which is the easiest disposal method; however, magma-safe items will need more drastic measures. For instance, wooden floodgate will hold back magma indefinitely if it stays closed (it'll only catch fire once it's opened), and a wooden drawbridge will only hold back magma if it's against its outer edge (e.g. if it raises to the right, then lava flowing from the left onto the "center" of the bridge will very quickly burn it up).

Constructions that resist magma are:

- Constructions (Wall, Floor, Ramp, and Stairs) of any material can never melt or burn - there is nothing wrong with a wooden magma reservoir. Natural (i.e. non-constructed) ice walls/floors/ramps/stairs will melt if exposed to sufficient heat.
- Fortifications will allow the passage of magma; however, if fortifications fill up to 7/7 depth, magma creatures will be able to swim freely through them.
- If not submerged (that is, not opened to let magma flow over/past/around them), doors, floodgates, and raised bridges (provided that there is no magma on the space the bridge would occupy when lowered) of non-magma-safe stone or metal are safe. So long as they are just in contact with magma, only acting as a passive "wall", they are fine. If opened, they will melt.
  - Raised drawbridges have a notable exception, in that allowing magma to flow over the center of the area that the bridge would normally occupy when lowered *will* cause the bridge's components to heat up and potentially melt.
- A pump made with magma-safe material for pipes, screws and blocks is fully magma-safe, and will not melt even when submerged in magma. Pumps containing any item that is not magma safe will be destroyed after prolonged operation.

## Game calculations

In the game, magma's temperature is exactly .

The chance of striking a magma-safe stone is roughly around 32%, not including the natural abundance of certain stone. It is important to note whether or not your fortress may already have access to magma-safe resources before attempting to deliberately find some.

## Magma-safe material

The following materials will not melt when submerged in magma. Although true for any item/construction, it's worth specifically mentioning that this includes doors, floor hatches, floodgates, bridges, screw pumps, pipe sections, and mechanisms.

\|}

**Notes:**

1\) Each stone is one of 16 colors in the game. Different un-mined stone of the same color have a different symbol to distinguish between them. Once mined, the individual stones themselves can sometimes look identical if the color is the same. Click to look at items or mouse over the terrain for specific information.

2\) **°U** = degrees in Urist, the measure of temperature within the *Dwarf Fortress* world. As far as is known, there is no functional difference between a material that melts at or — they are both equally "magma safe".

3\) There are three iron ores in the game (four if you count Goblinite). Of these, only hematite and magnetite are magma safe.

4\) Sphalerite has *no* melting point, but *sublimates* at . This still qualifies as being magma-safe.

5\) Nether-cap logs have a fixed temperature of , rendering them fully magma safe, except that nether-cap products dumped into magma are destroyed.

6\) For when weight is a consideration, one way or the other. Petrified Wood and Pitchblende are notable as the least and most dense non-economic magma-safe stones, with all the others listed above weighing very close to 2650, the generic "stone density". See Density for full table and discussion.

 \|  Ru:Magma-safe
