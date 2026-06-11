# Weapon (parte 2/2)

- **wIY** is the weapon's impact yield in MPa (i.e. raw value divided by 106).\[Verify\]

Failure means the attack bounces off, meaning denser, larger armor resists blunt attacks better, but larger blunt weapons with smaller contact areas and higher impact yields get through armor better. This also means adamantine armor is some of the worst in the game at outright deflecting attacks, due to its poor density, but this is not typically relevant, as impact yields are typically at least 10 times larger than density values for the actual metals available, so this step is routinely passed by most weapons regardless of relative materials.

On success, the following test is applied:

M \>= (2\*aIF - aIY) \* (2 + 0.4\*a_quality) \* A,

where:

- **aIF** is the armor's impact fracture in MPa (i.e. raw value divided by 106)
- **aIY** is the armor's impact yield in MPa (i.e. raw value divided by 106).

Note that the armor wants as high impact fracture as possible to make this test fail. The armor also wants low impact yield, although the weapon's impact fracture does not matter, and high quality and high contact area.

On a success, attack momentum is decreased by some 5% and the layer is considered punctured/severed, and the process continues to the next layer, including working through layers of the defender's body. If the attack was edged, it becomes edged again. On a failure, the momentum is multiplied by SHEAR_STRAIN_AT_YIELD/50000 for edged attacks or IMPACT_STRAIN_AT_YIELD/50000 for blunt attacks, then it becomes \*permanently\* blunt, and is passed on to the next layer. This means most rigid metal armor will reduce blocked attacks by 98%-99%, but elastic armor, such as a mail shirt, has both strain at yield values raised to 50000, so it multiplies by 1 at this step (i.e. does nothing to the momentum, but does still convert it to blunt) regardless of material.

## Combat testing

In regards to edged weaponry: adamantine and steel take first and a distant second place respectively, with iron a slightly less distant third best material in the game, nearly matched by the bronzes. Beyond that is copper, the second worst material, and silver is the worst weapon material available (and due to the existence of training weapons, not even useful in that regard).

Additionally, with regards to blunt weapons, almost all of the non-adamantine materials perform equally well, with a very slight edge towards steel and silver. Here is the thread with the details: [2].

Keep in mind that, given how unbelievably complicated this system is, very little should be taken as word of law yet.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
|  | Best | Better | Good | Fair | Poor | Terrible | Notes |
| Armor | Adamantine | Steel | Iron | Bronze, Bismuth Bronze | Copper |  |  |
| Edged Weapons | Adamantine | Steel | Iron | Bronze, Bismuth Bronze | Copper | Silver | For piercing iron armor, copper is better than bronze, but when piercing copper or bronze armor, bronze is better than copper. |
| Ammunition | Steel, Iron, Bronze, Bismuth Bronze, Copper, Silver |  | Adamantine |  |  |  | Adamantine bolts deflect off of adamantine armor, but otherwise their performance is on par with bolts made out of other metals. |
| Blunt Weapons | Platinum, Slade | Steel, Silver | Copper, Bismuth Bronze, Bronze, Iron |  |  | Adamantine | All six standard weapon metals perform nearly identically. Steel has a slightly higher rate of critical wounds, while silver is slightly more likely to penetrate armor. Platinum (only available as artifact weapons) has twice the density of silver and several other improved properties, making it the best metal for impact weapons, though very limited in production. Adamantine's light weight makes it a terrible choice for blunt weapons, roughly the same as making a weapon out of featherwood or cork. |

Cross referencing this table with the table at the top of this section seems to indicate that low densities, high impact fractures, and high shear fractures contribute to the killing power of edged weapons.

### Analysis

Testing of weapons (15 dwarves-versus-15 dwarves combat) in the object testing arena shows that the best dwarven-made weapon against unarmored humanoids is the battle axe, while the war hammer performs the best against armored targets.

Even in 15×(steel armor+silver war hammer) versus 15×(adamantine armor+adamantine battle axe) matches, hammerdwarves won with less than 50% casualties (mostly one-strike kills). However, when the dwarves in question were without armor or only wearing leather/cloth, the result was inverted — axedwarves won with less than 50% casualties. In battles against megabeasts, 6 silver hammerdwarves were barely able to scratch a bronze colossus (attacks were glancing away) due to bronze being a better "weapon" material.

This is because silver has the highest solid density of all materials that can regularly be made into weapons by dwarves. Tests show that indeed gold and platinum (increasingly dense) do increasing amounts of damage, and that war hammers remain the tool of choice, however they can only be produced by a moody dwarf (and a very lucky one at that).

For more on ranged ammunition see the forum thread Dwarven Research: A Comparison Study on the Effectiveness of Bolts vs Armors.

More arena tests are available in the Military testing article.

## Bugs

- Equipping weapons/armor on military is erratic. This is likely due to a single piece of weapons/armor being erroneously assigned to multiple dwarves and seems to occur when dwarves are upgrading their equipment or going on raids. Removing and reassigning equipment for all military dwarves can temporarily fix this problem.Bug:535
- In the Premium version, the sprite sheets for equipped gear are mostly incomplete. The material of equipped gear is currently distinguished for dwarves, for elves' and kobolds' armor (including metal armor), and for elves' wooden weapons; everything else has a default, 'gray' color palette.
- The Premium version has placeholder sprites for equipped artifact gear (which can be any material), but these are not used for gear of nonstandard materials spawned in the object testing arena, resulting in creatures that use them appearing un-equipped.

## See also

- Outstanding research on weapons and armor by Shinziril


---
*Parte 2 de 2 de «Weapon». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Weapon*
