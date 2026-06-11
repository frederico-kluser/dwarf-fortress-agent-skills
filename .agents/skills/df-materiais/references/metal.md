# Metal

> Fonte: [Metal](https://dwarffortresswiki.org/index.php/Metal) — Dwarf Fortress Wiki (GFDL/MIT)

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

\|} *Legend:*

:\* **Tile Color** corresponds to how items made from that metal are displayed in game, foreground and background colors.

:\***Source Ore(s)** indicates the specific ores that can provide a metal. If production of the metal is not guaranteed, a percent chance is indicated following the ore.

:\***Density** is used to determine the different weight of finished objects.

:\***Melting point** is used to determine if a material is magma-safe or not: magma is 12000°U.

:\***Material value** is what the base value of an object made of this metal is multiplied by to determine its worth.

:\***Value difference** indicates the difference in material value between the metal and the ore, separated with commas in cases where multiple ore values differ. Also keep in mind that multiple bars are produced for each ore boulder smelted, increasing the value difference even further.

**\*** - Values marked with an asterisk denote ores that can yield multiple metals. On average, the expected difference in value from smelting tetrahedrite is +1 and galena is +2.

### Alloys

*(Unless specified, ores of the ingredients may be used instead of bars for alloy reactions)*

\|}

Notes
1\) **Billon** can be made with tetrahedrite or galena ore (instead of silver bars) for increased value: (Copper ore + Tetrahedrite: +3.5; Tetrahedrite + Tetrahedrite: +3; Copper ore + Galena: + 2.5; Tetrahedrite + Galena: + 2).

2\) **Electrum** can be made with tetrahedrite or galena ore (instead of silver bars) for increased value: (Gold + Tetrahedrite: +3.5; Gold + Galena: +2.5).

*Legend:*

:\* **Tile Color** corresponds to how items made from that metal are displayed in game, foreground and background colors.

:\***Reaction** indicates the basic recipe for an alloy - this does not include any fuel necessary to operate the smelter. See the article for that alloy or smelting for possible alternatives.

\* - ''You can use only bars of metal in this reaction, not ores.

### Special metals

\|} **Adamantine** \* cannot be smelted directly, and must be extracted first.

- Can be used to forge anything except beds
- Blades are 10× sharper than standard metals, which when combined with its very high shear fracture/yield makes it more than 100x as effective as steel for bladed weapons
- Too light to make effective blunt weapons despite nearly unsurpassed yield and fracture values.

**Divine metal** has procedurally generated (i.e. semi-random) names associated with deities.

- Blades are 1.2× sharper than standard metals
- Low density makes it worse than all conventional metals for blunt, although it's still better than adamantine
- Overall stats make it stronger than steel but weaker than adamantine.

## Weapon and armor quality

\|}

- *Combat information* is used internally by the game to determine the combat properties of weapons and armor made from this metal:

  **Density**: Used in conjunction with other factors - heavier weapons (higher numbers) hit with more force, light weapons tend to have less penetration. Denser armor absorbs more force from being transmitted through it as well, though low elasticity is much more reliable protection. Value shown here is g/cm³, which is the raw value divided by 10³

  **Impact yield**: Used for blunt-force combat; *higher* is better for weapons, but *lower* is better for armor. This is the raw value divided by 10³ (i.e., kPa).

  **Impact fracture**: Used for blunt-force combat; *higher* is better. This is the raw value divided by 10³ (i.e., kPa).

  **Impact elasticity**: Used for blunt-force combat; *lower* is better. This is the raw value.

  **Shear yield**: Used for cutting calculations in combat; *higher* is better. This is the raw value divided by 10³ (i.e., kPa).

  **Shear fracture**: Used for cutting calculations in combat; *higher* is better. This is the raw value divided by 10³ (i.e., kPa).

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

For edged weapons and armour, adamantine and steel take first and a very distant second place respectively, with iron the third best material in the game. Beyond this, bronze is in a close tie with copper as the second worst material. As in older versions, silver continues to hold steady as the worst material available (no longer beneficial with wooden training weapons being available now) in regards to edged weaponry.

For blunt weapons, all of the standard materials (so, not adamantine or divine metal) perform respectably well, with a very slight edge towards steel and silver. Here is the thread with the details:

Keep in mind how unbelievably complicated this system is; nothing here should be taken as word of law. These results also ignore the impact of the *weight* of equipment on your dwarves. Dwarves, especially weak ones without high Armor User skill, will move much more slowly when wearing heavy armor and carrying heavy weapons and ammunition. This may be a more important consideration than a marginal improvement in protection.

|  | Best | Better | Good | Fair | Poor | Terrible | Notes |
|----|----|----|----|----|----|----|----|
| Armor | Adamantine | Divine metal, Steel | Iron, Bronze, Bismuth Bronze |  | Copper |  |  |
| Edged Weapons | Adamantine | Divine metal, Steel | Iron | Bronze, Bismuth Bronze | Copper | Silver | For piercing iron armor, copper is better than bronze. For piercing copper or bronze armor, bronze is better than copper. Adamantine is over 20x as good as divine metal, and is the only metal that can reliably cut through armor even for slashing attacks. |
| Ammunition | Steel, Divine metal | Adamantine | Iron | Bronze, Bismuth Bronze, Copper | Silver |  | Adamantine bolts deflect off of adamantine armor due to their low momentum, but this is an unusual circumstance. Density does not matter for bolts above 1.333 g/cm³, which all ordinary metals exceed at least 5-fold. |
| Blunt Weapons | Platinum (artifact only) | Steel, Silver | Copper, Bismuth Bronze, Bronze | Iron | Divine metal | Adamantine | All six standard weapon metals perform nearly identically. Steel has a slightly higher rate of critical wounds, while silver is slightly more likely to penetrate armor. Platinum (only available as artifact weapons) has twice the density of silver and several other improved properties, making it the best metal for impact weapons, though very limited in production. |

Cross referencing this table with the table at the top of this section seems to indicate that low densities, high impact fractures, and high shear fractures contribute to the killing power of edged weapons

## See also

- Some outstanding research on armor vs. different weapon types by Shinziril.
- Bolt material analysis (old research is outdated now that is fixed).

\|0
