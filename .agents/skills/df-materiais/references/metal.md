# Metal

> Fonte: [Metal](https://dwarffortresswiki.org/index.php/Metal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Metal** is a material extracted from ore at a smelter, turning the ore into **bars** of pure metal. (One special metal becomes wafers instead of bars.) The metal bars resulting from smelting are used to make items such as weapons, armor, furniture, and crafts at a forge.

Metals may sometimes be combined to form an **alloy** metal (see below), which is also measured by the bar. An alloy usually improves on the properties of its components to give more uses or increased value.

Smelting pure ores into the corresponding bars raises the base value from that of stone (3) to that of bars (5). This value is then multiplied against the material multiplier of the metal to give the final value for the bar.

## Alloys

There are eleven pure metals in *Dwarf Fortress*, plus a twelfth special metal, many of which can be mixed together to create another fourteen **alloys** of one type or another. In some cases, making alloys will result in an overall increase in value, or the resultant alloy will be more powerful when used to forge weapons or armor, though many alloys result in no overall increase in utility or created wealth. (These increases in value can be compared in the "Difference" column of the table below.)

There are many uses for alloys:

- Increased performance for armor or weapons.
- Increased value (particularly when a silver-bearing ore is substituted for silver)
- Stretching your supply of scarce metals.
- Creating items with distinct colors (for instance, rose gold is magenta) for furniture, color-coding rooms or levers, or artistic constructions (including floor mosaics).
- Increasing happiness or perceived room value for a dwarf who particularly likes a given alloy.
- Decreased fuel consumption if making the alloy directly from ores (e.g. bronze requires only one smelter task to make 8 bars from 2 stones of ore).

The number of bars used to create an alloy always equals the number of bars produced: the number of bars input equals the number of bars of output. However, the number of bars produced from smelting ores is four times greater (X ores in = 4X bars out).

## List of metals

### Pure metals

Metal / Name
Tile Color
Source Ore(s)
Density (g/cm3)
Melting point
Material / value
Value difference
Notes and / Other Uses

(ASCII)
(Tileset)

Aluminum
≡‼7:7:1

Native aluminum
2.70
11188 °U
40
+0

Bismuth
≡‼5:5:1

Bismuthinite
9.78
10488 °U
2
+1
Only useful for alloying into bismuth bronze

Copper
≡‼6:4:0

Native copper, Malachite, Tetrahedrite
8.93
11952 °U
2
+0, +0, -1*
Can be used to forge all weapons, armor, ammunition, and picks

Gold
≡‼6:6:1

Native gold
19.32
11915 °U
30
+0

Iron
≡‼0:7:1

Hematite, Limonite, Magnetite
7.85
12768 °U
10
+2
Can be used to forge all weapons, armor, ammunition, picks, and anvils

Lead
≡‼0:7:1

Galena
11.34
10589 °U
2
-3*

Nickel
≡‼7:3:0

Garnierite
8.80
12619 °U
2
+0

Platinum
≡‼7:7:1

Native platinum
21.40
13182 °U
40
+0

Silver
≡‼7:7:1

Native silver / , / Horn silver / , / Galena / (50%), / Tetrahedrite / (20%)
10.49
11731 °U
10
+0, +0, / +5*, +7*
Can be used to forge melee weapons and ammunition

Tin
≡‼7:3:0

Cassiterite
7.28
10417 °U
2
+0

Zinc
≡‼7:3:0

Sphalerite
7.13
10755 °U
2
+0

*Legend:*

- **Tile Color** corresponds to how items made from that metal are displayed in game, foreground and background colors.
- **Source Ore(s)** indicates the specific ores that can provide a metal. If production of the metal is not guaranteed, a percent chance is indicated following the ore.
- **Density** is used to determine the different weight of finished objects.
- **Melting point** is used to determine if a material is magma-safe or not: magma is 12000°U.
- **Material value** is what the base value of an object made of this metal is multiplied by to determine its worth.
- **Value difference** indicates the difference in material value between the metal and the ore, separated with commas in cases where multiple ore values differ. Also keep in mind that multiple bars are produced for each ore boulder smelted, increasing the value difference even further.

**\*** - Values marked with an asterisk denote ores that can yield multiple metals. On average, the expected difference in value from smelting tetrahedrite is +1 and galena is +2.

### Alloys

*(Unless specified, ores of the ingredients may be used instead of bars for alloy reactions)*

|  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
| Metal / Name | Tile / Color (ascii) | Tile / Color (tileset) |   Reaction   | Density (g/cm3) | Melting point | Material / value | Value difference | Notes and / Other Uses |
| Billon | `≡``‼`7:3:0 |  | Silver / + / Copper | 8.93 | 11952 °U | 6 | +0 | see note 1) |
| Bismuth bronze | `≡``‼`6:6:1 |  | 1 / Tin / + 2 / Copper / + 1 / Bismuth / \* | 8.25 | 11868 °U | 6 | +4 | Can be used to forge all weapons, armor, ammunition, and picks. Combat relevant stats are identical to standard **Bronze** |
| Black bronze | `≡``‼`5:6:0 |  | 2 / Copper / + 1 / Silver / + 1 / Gold / \* | 8.93 | 11952 °U | 11 | +0 | Unique color |
| Brass | `≡``‼`6:6:1 |  | Zinc / + / Copper | 8.55 | 11656 °U | 7 | +5 | Value difference is +4.5 if tetrahedrite is used instead of copper |
| Bronze | `≡``‼`6:4:0 |  | Tin / + / Copper | 8.25 | 11868 °U | 5 | +3 | Value difference is +2.5 if tetrahedrite is used instead of copper. Can be used to forge all weapons, armor, ammunition, and picks |
| Electrum | `≡``‼`6:6:1 |  | Silver / + / Gold | 14.905 | 11828 °U | 20 | +0 | see note 2) |
| Fine pewter | `≡``‼`7:7:1 |  | 3 / Tin / + 1 / Copper | 7.28 | 10417 °U | 5 | +3 | Value difference is +2.75 if tetrahedrite is used instead of copper |
| Lay pewter | `≡``‼`3:7:0 |  | 2 / Tin / + 1 / Copper / + 1 / Lead / \* | 7.28 | 10417 °U | 3 | +1 | Unique color |
| Nickel silver | `≡``‼`7:7:1 |  | 2 / Nickel / + 1 / Copper / + 1 / Zinc / \* | 8.65 | 11620 °U | 3 | +1 |  |
| Pig iron | `≡``‼`0:7:1 |  | Iron / + / flux / stone / + / fuel / \* | 7.85 | 12106 °U | 10 | +0 | Only used to make steel |
| Rose gold | `≡``‼`5:5:1 |  | 3 / Gold / + 1 / Copper / \* | 19.32 | 11915 °U | 23 | +0 | Unique color |
| Steel | `≡``‼`7:3:0 |  | Iron / + / Pig iron / + / flux / stone / + / fuel / \* | 7.85 | 12718 °U | 30 | +20 | Can be used to forge all weapons, armor, ammunition, picks, and anvils |
| Sterling silver | `≡``‼`7:7:1 |  | 3 / Silver / + 1 / Copper / \* | 10.49 | 11602 °U | 8 | +0 |  |
| Trifle pewter | `≡``‼`7:3:0 |  | 2 / Tin / + 1 / Copper | 7.28 | 10417 °U | 4 | +2 | Value difference is +1.67 if tetrahedrite is used instead of copper |

Notes
1\) **Billon** can be made with tetrahedrite or galena ore (instead of silver bars) for increased value: (Copper ore + Tetrahedrite: +3.5; Tetrahedrite + Tetrahedrite: +3; Copper ore + Galena: + 2.5; Tetrahedrite + Galena: + 2).

2\) **Electrum** can be made with tetrahedrite or galena ore (instead of silver bars) for increased value: (Gold + Tetrahedrite: +3.5; Gold + Galena: +2.5).

*Legend:*

- **Tile Color** corresponds to how items made from that metal are displayed in game, foreground and background colors.
- **Reaction** indicates the basic recipe for an alloy - this does not include any fuel necessary to operate the smelter. See the article for that alloy or smelting for possible alternatives.

\* - *You can use only bars of metal in this reaction, not ores.*

- **Density** is used to determine the different weight of finished objects.
- **Melting point** is used to determine if a material is magma-safe or not: magma is 12000°U.
- **Material value** is what the base value of an object made of this metal is multiplied by to determine its worth.
- **Value difference** indicates the difference between the average value of the required bars of metals vs. the value of the resulting bars of alloy - what went in vs. what comes out, measured per bar. "+0" indicates that the resulting alloy is a perfectly average value of the component metals. Note that substituting tetrahedrite for copper ore always results in a value decrease, while substituting tetrahedrite or galena for silver bars always results in a value increase.

### Special metals

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

Metal / Name
Tile Color
Source Ore(s)
Density (g/cm3)
Melting point
Material / value
Value difference
Notes and / Other Uses

(ASCII)
(Tileset)

Adamantine
≡‼

Raw adamantine
0.200
25000 °U
300
+50
(see / below)

Divine metal
≡‼

none
1
none
300

(see / below)

**Adamantine** \* cannot be smelted directly, and must be extracted first.

- Can be used to forge anything except beds
- Blades are 10× sharper than standard metals, which when combined with its very high shear fracture/yield makes it more than 100x as effective as steel for bladed weapons
- Too light to make effective blunt weapons despite nearly unsurpassed yield and fracture values.

**Divine metal** has procedurally generated (i.e. semi-random) names associated with deities.

- Blades are 1.2× sharper than standard metals
- Low density makes it worse than all conventional metals for blunt, although it's still better than adamantine
- Overall stats make it stronger than steel but weaker than adamantine.

## Weapon and armor quality

|  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|
| Metal | Value | Density | Impact yield | Impact fracture | Impact elasticity | Shear yield | Shear fracture | Shear elasticity | Notes |
| Adamantine | 300 | 0.200 | 5000 | 5000 | 0 | 5000 | 5000 | 0 | Can be used to forge anything except beds |
| Divine metal | 300 | 1.0 | 1000 | 2000 | 0 | 1000 | 2000 | 0 | Can be used to forge all weapons, armor, ammunition, picks, and anvils |
| Steel | 30 | 7.85 | 1505 | 2520 | 940 | 430 | 720 | 215 | Can be used to forge all weapons, armor, ammunition, picks, and anvils |
| Bismuth bronze | 6 | 8.25 | 602 | 843 | 547 | 172 | 241 | 156 | Can be used to forge all weapons, armor, ammunition, and picks |
| Bronze | 5 | 8.25 | 602 | 843 | 547 | 172 | 241 | 156 | Can be used to forge all weapons, armor, ammunition, and picks |
| Iron | 10 | 7.85 | 542 | 1080 | 319 | 155 | 310 | 189 | Can be used to forge all weapons, armor, ammunition, picks, and anvils |
| Copper | 2 | 8.93 | 245 | 770 | 175 | 70 | 220 | 145 | Can be used to forge all weapons, armor, ammunition, and picks |
| Silver | 10 | 10.49 | 350 | 595 | 350 | 100 | 170 | 333 | Can be used to forge melee weapons and ammunition |
| Platinum | 40 | 21.4 | 350 | 700 | 152 | 100 | 200 | 164 | Only available as artifact weapons. |

- *Combat information* is used internally by the game to determine the combat properties of weapons and armor made from this metal:
  **Density**: Used in conjunction with other factors - heavier weapons (higher numbers) hit with more force, light weapons tend to have less penetration. Denser armor absorbs more force from being transmitted through it as well, though low elasticity is much more reliable protection. Value shown here is g/cm3, which is the raw value divided by 103
  **Impact yield**: Used for blunt-force combat; *higher* is better for weapons, but *lower* is better for armor. This is the raw value divided by 103 (i.e., kPa).
  **Impact fracture**: Used for blunt-force combat; *higher* is better. This is the raw value divided by 103 (i.e., kPa).
  **Impact elasticity**: Used for blunt-force combat; *lower* is better. This is the raw value.
  **Shear yield**: Used for cutting calculations in combat; *higher* is better. This is the raw value divided by 103 (i.e., kPa).
  **Shear fracture**: Used for cutting calculations in combat; *higher* is better. This is the raw value divided by 103 (i.e., kPa).
  **Shear elasticity**: Used for armor protection vs cutting weapons in combat; *lower* is better. This is the raw value.
- General Term Explanations (From Wikipedia)
  **Yield Strength** - The stress at which material strain changes from elastic deformation to plastic deformation, causing it to deform permanently.
  **Fracture Strength** - The stress coordinate on the stress-strain curve at the point of rupture.
  **Stress** - Force per area = F/A
  **Strain** - Deformation of a solid due to stress = Stress/Young's Modulus

So...

Explanations!

**Yield Strength** is the amount of stress required to permanently deform (bend) a material (plastic deformation)

**Fracture Strength** is the amount of stress required to permanently break (rupture) a material

**Elasticity** (or *IMPACT_STRAIN_AT_YIELD* in RAWs) is the amount of deformation (bending) that occurs at the yield point, in parts-per-100,000

Implications to *Dwarf Fortress* Combat

Yield combined with Elasticity can tell what a material will do under stress (be it from a hammer, axe, or arrow)

Higher yield means that it takes more stress to deform

Lower elasticity means that it will deform less when stress is applied

### Preliminary combat testing and analysis

For edged weapons and armour, adamantine and steel take first and a very distant second place respectively, with iron and bronze being closely tied for third place. Copper is the second worst material, and as in older versions, silver continues to hold steady as the worst material available (no longer beneficial with wooden training weapons being available now) in regards to edged weaponry.

For blunt weapons, all of the standard materials (so, not adamantine or divine metal) perform respectably well, with a very slight edge towards steel. Here is the thread with the details:

http://www.bay12forums.com/smf/index.php?topic=53571.0

Keep in mind how unbelievably complicated this system is; nothing here should be taken as word of law. These results also ignore the impact of the *weight* of equipment on your dwarves. Dwarves, especially weak ones without high Armor User skill, will move much more slowly when wearing heavy armor and carrying heavy weapons and ammunition. This may be a more important consideration than a marginal improvement in protection.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|  | Best | Better | Good | Fair | Poor | Terrible | Notes |
| Armor | Adamantine | Divine metal, Steel | Iron, Bronze, Bismuth Bronze |  | Copper |  |  |
| Edged Weapons | Adamantine | Divine metal, Steel | Iron | Bronze, Bismuth Bronze | Copper | Silver | For piercing iron armor, copper is better than bronze. For piercing copper or bronze armor, bronze is better than copper. Adamantine is over 20x as good as divine metal, and is the only metal that can reliably cut through armor even for slashing attacks. |
| Ammunition | Steel, Divine metal | Adamantine | Iron | Bronze, Bismuth Bronze, Copper | Silver |  | Adamantine bolts deflect off of adamantine armor due to their low momentum, but this is an unusual circumstance. Density does not matter for bolts above 1.333 g/cm3, which all ordinary metals exceed at least 5-fold. |
| Blunt Weapons | Platinum (artifact only) | Steel, Silver | Copper, Bismuth Bronze, Bronze | Iron | Divine metal | Adamantine | All six standard weapon metals perform nearly identically. Steel has a slightly higher rate of critical wounds, while silver is slightly more likely to penetrate armor. Platinum (only available as artifact weapons) has twice the density of silver and several other improved properties, making it the best metal for impact weapons, though very limited in production. |

Cross referencing this table with the table at the top of this section seems to indicate that low densities, high impact fractures, and high shear fractures contribute to the killing power of edged weapons

Different types of pure metals.

## See also

- Some outstanding research on armor vs. different weapon types by Shinziril.
- Bolt material analysis (old research is outdated now that Bug:5516 is fixed).

|  |
|----|
| "Metal" in other / Languages / Dwarven / : / kel / Elven / : / lethi / Goblin / : / snusm / Human / : / rigu |
