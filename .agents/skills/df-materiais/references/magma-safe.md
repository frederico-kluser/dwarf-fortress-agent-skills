# Magma-safe

> Fonte: [Magma-safe](https://dwarffortresswiki.org/index.php/Magma-safe) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Magma-safe materials** are materials which will not melt, burn, evaporate, or otherwise take damage when in close contact with magma. Most frequently, this comes into play when using floodgates operated by mechanisms, or when operating a magma pump.

For reactions and custom buildings using the \[MAGMA_BUILD_SAFE\] token, only a material which is solid and stable at the temperature 12000 °U (i.e. MELTING_POINT/BOILING_POINT/IGNITE_POINT/HEATDAM_POINT greater than 12000 and COLDDAM_POINT less than 12000) is considered magma-safe.

In order to construct mechanisms, blocks or other pump components from a magma-safe material, you have several choices:

1.  You can specify a magma-safe rock for your mechanisms and other components at the workshops by clicking the detail () icon next to the order.
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

In the game, magma's temperature is exactly 12000 °U .

The chance of striking a magma-safe stone is roughly around 32%, not including the natural abundance of certain stone. It is important to note whether or not your fortress may already have access to magma-safe resources before attempting to deliberately find some.

## Magma-safe material

The following materials will not melt when submerged in magma. Although true for any item/construction, it's worth specifically mentioning that this includes doors, floor hatches, floodgates, bridges, screw pumps, pipe sections, and mechanisms.

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Type | Material | Appearance1 | Melting Temperature °U (°F, °C)2 | Found in | Uses / Notes |
| Stone | Alunite |  / \` • | 13,690°U (3722°F/2051°C) | All Igneous extrusive**(L)**, Kaolinite**(L)** |  |
| Stone | Anhydrite |  / v • | 12,610°U (2642°F/1450°C) | Gypsum**(S)**, Satinspar**(1)**, Alabaster**(1)**, Selenite**(1)** |  |
| Stone | Basalt |  / \# • | 12,160°U (2192°F/1200°C) | Igneous extrusive layer stone |  |
| Stone | Bauxite |  / + • | 13,600°U (3632°F/2000°C) | All Sedimentary**(L)** | dark red |
| Stone | Calcite |  / " • | 12,902°U (2934°F/1613°C) | Limestone**(S)**, Marble**(S)** | flux stone |
| Stone | Chert |  / = • | 13,101°U (3133°F/1723°C) | Sedimentary layer stone |  |
| Stone | Chromite |  / = • | 13,645°U (3677°F/2026°C) | Olivine**(V)** |  |
| Stone | Dolomite |  / \` • | 16,507°U (6539°F/3619°C) | Sedimentary layer stone | Flux, Highest melting point of any common stone. |
| Stone | Gabbro |  / ▒ • | 12,160°U (2192°F/1200°C) | Igneous intrusive layer stone |  |
| Stone | Ilmenite |  / . • | 12,457°U (2489°F/1365°C) | Gabbro**(S)** |  |
| Stone | Kaolinite |  / = • | 13,150°U (3182°F/1751°C) | All Sedimentary**(L)** | dark red, porcelain |
| Stone | Mica |  / v • | 12,295°U (2327°F/1275°C) | All Metamorphic**(L)**, Granite**(L)** |  |
| Stone | Obsidian |  / ▒ • | 13,600°U (3632°F/2001°C) | Igneous extrusive layer stone | value 3, can be "manufactured" |
| Stone | Olivine |  / % • | 13,168°U (3200°F/1761°C) | Gabbro**(L)** | green |
| Stone | Orthoclase |  / % • | 12,250°U (2282°F/1250°C) | All Igneous intrusive**(L)**, All Metamorphic**(L)** | yellow |
| Stone | Periclase |  / , • | 15,040°U (5072°F/2803°C) | Marble**(S)** |  |
| Stone | Petrified wood |  / % • | 12,970°U (3002°F/1650°C) | All Sedimentary**(S)** | bright red / density = 2200 / 6 |
| Stone | Pitchblende |  / \* • | 12,070°U (2102°F/1149°C) | Granite**(S)** | purple / density = 7600 / 6 |
| Stone | Quartzite |  / - • | 12,970°U (3002°F/1650°C) | Metamorphic layer stone |  |
| Stone | Rutile |  / \` • | 13,285°U (3214°F/1826°C) | All Metamorphic**(S)**, Granite**(S)** | purple |
| Stone | Sandstone |  / \# • | 12,070°U (2102°F/1149°C) | Sedimentary layer stone |  |
| Stone | Talc |  / \| • | 12,700°U (2732°F/1500°C) | Dolomite**(L)** |  |
| Metal | Adamantine |  / X ≡ | 25,000°U (15,032°F/8333°C) |  | Highest value / utility material in game / density = 200 / 6 |
| Metal | Iron |  / X ≡ | 12,768°U (2800°F/1538°C) |  | Armor / weapons / density = 7850 / 6 |
| Metal | Nickel |  / X ≡ | 12,619°U (2651°F / 1455°C / density = 8800 / 6 / ) |  |  |
| Metal | Pig iron |  / X ≡ | 12,106°U (2138°F/1170°C) |  | used in steel making process / density = 7850 / 6 |
| Metal | Platinum |  / X ≡ | 13,182°U (3214°F/1768°C) |  | High value metal / density = 21,400 / 6 |
| Metal | Steel |  / X ≡ | 12,718°U (2750°F/1510°C) |  | Armor / weapons / density = 7850 / 6 |
| Metal | Divine metal |  / X ≡ | None |  | Found only in / vaults / and in geodes deep underground / density = 1000 / 6 |
| Ore | Cassiterite |  / £ \* | 12,025°U (2057°F/1124°C) | Granite**(V)** | Ore of tin |
| Ore | Galena |  / £ \* | 12,005°U (2037°F/1113°C) | All Igneous extrusive**(V)**, All Metamorphic**(V)**, Granite**(V)**, Limestone**(V)** | Ore of lead and silver |
| Ore | Hematite3 |  / £ \* | 12,736°U (2768°F/1520°C) | All Sedimentary**(V)**, All Igneous extrusive**(V)** | Ore of iron3 |
| Ore | Magnetite3 |  / ~ \* | 12,768°U (2800°F/1538°C) | All Sedimentary**(L)** | Ore of iron3 |
| Ore | Native platinum |  / £ \* | 13,182°U (3214°F/1768°C) | Olivine**(V)**, Magnetite**(V)**, Chromite**(S)** | Ore of platinum |
| Ore | *Sphalerite*4 |  / £ \* | *12,133°U (2165°F/1185°C)* | All Metamorphic**(V)** | Ore of zinc4 |
| Wood | Nether-cap5 |  / ♠ ▬ | N/A | Cavern (depth 3) | Naturally cold5 |
| Special | Raw adamantine |  / £ \* | 25,000°U (15,032°F/8333°C) | The depths | Ore of adamantine |
| Special | Slade |  / ░ \* | None | The depths | Intended to be unmineable |
| Leather | Fire imp |  / ß | None |  |  |
| Bone | Fire imp |  / ² | None |  |  |
| Bone | Dragon |  / ² | None |  |  |
| Soap | Fire imp |  / ≡ | 15,000°U (5032°F/2780°C) |  |  |
| Soap | Dragon |  / ≡ | 55,000°U (45032°F/25,044°C) |  |  |
| Glass | Green glass |  / X ■ | 13,600°U (3632°F/2001°C) |  |  |
| Glass | Clear glass |  / X ■ | 13,600°U (3632°F/2001°C) |  |  |
| Glass | Crystal glass |  / X ■ | 13,600°U (3632°F/2001°C) |  |  |
| Ash | Ash |  / X ≡ | None |  |  |
| Ash | Potash |  / X ≡ | None |  |  |
| Ash | Pearlash |  / X ≡ | None |  |  |

**Notes:**

1\) Each stone is one of 16 colors in the game. Different un-mined stone of the same color have a different symbol to distinguish between them. Once mined, the individual stones themselves can sometimes look identical if the color is the same. Click to look at items or mouse over the terrain for specific information.

2\) **°U** = degrees in Urist, the measure of temperature within the *Dwarf Fortress* world. As far as is known, there is no functional difference between a material that melts at 12005 °U or 55000 °U — they are both equally "magma safe".

3\) There are three iron ores in the game (four if you count Goblinite). Of these, only hematite and magnetite are magma safe.

4\) Sphalerite has *no* melting point, but *sublimates* at 12133 °U . This still qualifies as being magma-safe.

5\) Nether-cap logs have a fixed temperature of 10000 °U , rendering them magma safe for use as components. However nether-cap products dumped into magma and nether-cap minecarts filled with magma are destroyed.

6\) For when weight is a consideration, one way or the other. Petrified Wood and Pitchblende are notable as the least and most dense non-economic magma-safe stones, with all the others listed above weighing very close to 2650, the generic "stone density". See Density for full table and discussion.
