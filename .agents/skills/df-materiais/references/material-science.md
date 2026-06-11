# Material science

> Fonte: [Material science](https://dwarffortresswiki.org/index.php/Material_science) — Dwarf Fortress Wiki (GFDL/MIT)

Materials have a number of properties representing real-world variables that describe how they respond to inputs. In particular, the game has a number of variables that describe what happens to a material when it's put under stress.

## What is stress?

In the real world, an object is stressed when a force is applied to the object. Depending on the nature of the force applied, this stress can take a number of forms, and the object can respond differently based on its material and how that material handles different stresses.

In the material raws, whenever you see 'yield', 'fracture', or 'strain at yield', that property is a stress-related quality.

## When does *Dwarf Fortress* make stress calculations?

At present, DF seems to only apply forces during combat, and thus only stresses objects (generally armor and various body layers) at that time.

## There's a lot of stress-related properties, what do they mean?

The first thing you'll notice is that the second word in each stress variable is one of Yield, Fracture, or strain at yield. These are mechanical performance terms.

The first set of words are things like Impact, Bending, and so forth. These describe modes of applying force.

The following explanations assumes real world physics sort of apply (since Toady One chose real world properties). The game doesn't use all of these properties yet, and may not be applying them according to real world physics.

### Mechanical Performance Properties

Yield: This is almost certainly 'Yield Strength', which is the amount of stress needed to cause a material to go from elastic deformation (whereby halting stressing causes it to return to its original shape) to plastic deformation (whereby halting stressing causes it to keep its shape). Since most objects only elastically deform over small distances of deformation, high Yield values generally means it takes a lot of force to noticeably 'stretch' them (but see strain at yield).

Fracture: The fracture point is the amount of stress or force necessarily to cause the material to fail, or in other words, to break.

Strain at yield (sometimes incorrectly referred to as 'elasticity'): This variable tells you how much deformation occurs to the material while it is deforming elastically. That is, as long as the force is less than the yield strength, stress \* strain at yield = deformation distance. The smaller the strain at yield, the less deformation occurs under stress. Strain is measured as parts-per-100000, meaning that 100000 strain is 100% deformation.

Note: Strain at yield is the inverse of the relevant elastic modulus, thus a highly elastic material has low elastic modulus, and engages in less elastic collisions.

### Modes of Applying Force

Impact: Force applied by a sudden strike, like a hammer.

Compressive: Force applied by exerting pressure on an object, like trying to squish something between your hands.

Tensile: Force applied by pulling on something, like suspending one object via another. (e.g., if you suspend an elf from a metal pole, you are applying a tensile force to the pole).

Torsion: Force applied by twisting something. Note that you're twisting some portion of the object relative to itself to cause a torsion stress to be applied to it. (Consider trying to twist a metal rod by grasping at either end and attempting to wring it - yes, you'd have to apply a lot of force to succeed).

Shear: Force applied by pushing part of the material so it tries to slide relative to another part of it. Ie, pushing at the top of an object when the bottom part is fixed to the ground is going to primarily apply a shear stress to it (the top part will try to move in the direction you push, and the lower part will resist this shear stress).

Bending: Force applied by bending a material.

## Effects on Combat

The *Dwarf Fortress* combat system does not use all material properties at present (0.40.05). Weapon and armor damage/wear/decay is implemented.

The formulae below have been reverse-engineered 1 2 and experimentally proven 3 4 by several independent researchers. Below are the simplified results; for more details see links above.

### Attack Types

Both creatures and items can have \[ATTACK\] tokens. A creature can execute any of its natural attacks plus any attacks of the items it holds. The attacks marked with \[EDGE\] flag deliver *edged* damage which is governed by \[SHEAR\_\*\] tokens; they can be further differentiated by attack contact area: generally concentrated strikes (area of 50 or less) are considered *stabbing* while wider areas correspond to *slashing* attacks. This distinction shall be emphasized later.

Every other attack is considered *blunt*. \[IMPACT\_\*\] tokens affect blunt combat. Most specialised blunt weapons have small contact area; edged weapons generally also have blunt attacks with larger area values; items or creatures without defined attacks get default blunt attack with area = (size)^(2/3). Under certain circumstances edged attack can be converted to blunt, but not contrariwise.

Wrestling moves are special: **breaking bones** uses \[BENDING\_\*\] values, **pinching** utilizes \[COMPRESSIVE\_\*\] properties, and **biting** can deal \[TENSILE\] or \[TORSION\] damage depending on whether the attack is edged. Those attacks generally ignore armor.

### Contact Area

Attack contact area is the minimum of weapon contact area and armor/layer contact area. Body parts have areas dependent on their size, as with non-weapon items; part size is creature size **times** relative size of the part in proportion to whole body.

| Body part     | Relative size (human) | Kobold | Elf   | Human | Troll  |
|---------------|-----------------------|--------|-------|-------|--------|
| \| Total      | 100%                  | 20000  | 60000 | 70000 | 250000 |
| \| Upper body | 18%                   | 3599   | 10818 | 12621 | 43133  |
| \| Lower body | 18%                   | 3599   | 10818 | 12621 | 43133  |
| \| Neck       | 1.8%                  | 359    | 1081  | 1262  | 4313   |
| \| Head       | 5.4%                  | 1079   | 3245  | 3786  | 12939  |
| \| Upper arm  | 3.6%                  | 719    | 2163  | 2524  | 8626   |
| \| Lower arm  | 3.6%                  | 719    | 2163  | 2524  | 8626   |
| \| Hand       | 1.4%                  | 287    | 865   | 1009  | 3450   |
| \| Upper leg  | 9.0%                  | 1799   | 5409  | 6310  | 21566  |
| \| Lower leg  | 7.2%                  | 1439   | 4327  | 5048  | 17253  |
| \| Foot       | 2.2%                  | 431    | 1298  | 1514  | 5175   |

Armor size is calculated as underlying body part size **times** coverage/100% **times** size/100 **times** 1+(UPSTEP+UBSTEP+LBSTEP)/4; MAX count as 3 in the last sum.

| Item | Size multiplier | Body part | Dwarf | Human | Extra body parts covered (humanoid) | Notes |
|----|----|----|----|----|----|----|
| \| Cap | 0.05 | Head | 162 | 189 | none | Cloth |
| \| Mask | 0.1 | Head | 324 | 378 | none | Cloth |
| \| Helm | 0.3 | Head | 973 | 1135 | none |  |
| \| Leather armor | 0.3 | Upper body | 3245 | 3786 | Lower body, neck, upper arms, upper legs | leather |
| \| Mail shirt | 0.225 | Upper body | 2434 | 2839 | Lower body, neck, upper arms, upper legs | Chain |
| \| Breastplate | 0.2 | Upper body | 2163 | 2524 | Lower body |  |
| \| Gauntlets | 0.25 | Hands | 216 | 252 | Lower arms, fingers |  |
| \| Leggings | 0.2625 | Lower body | 2839 | 3313 | Upper legs, lower legs, toes | Chain |
| \| Greaves | 0.2625 | Lower body | 2839 | 3313 | Upper legs, lower legs, toes |  |
| \| Low boots | 0.25 | Feet | 324 | 378 | Toes |  |
| \| High boots | 0.3125 | Feet | 405 | 473 | Lower legs, toes |  |

### Attack Momentum

DF uses momentum-based combat physics, so the momentum plays central role in calculations. Since momentum = velocity \* mass, and lighter items can be swung faster, attack momentum is largely independent from weapon weight. The simplified formula is as follows:

M = Str \* Vel / ( 10⁶/Size + 10\*F/W ),

or

M = Size \* Str \* Vel / (10 \* (( 10⁵ + i_Size)/W )),

or

M = Size \* Str \* Vel / (10⁶ \* (1 + i_Size/(w_density\*w_size) )

where:

- **M** is the momentum.
- **Str** is the creature's strength (e.g. 1250 for the average dwarf)
- **Vel** is the weapon's velocity modifier if present (e.g. 1.25x, 2x)
- **Size** is the average creature size (e.g. 60000 for dwarves)
- **i_Size** is the specific creature's size
- **F** is "fatness modifier" (also includes muscle) = i_Size/Size; dwarf with size of 66150 will have F=66150/60000=1.1025
- **W** is weapon mass in kilograms (Γ)
- **w_density** is the weapon's material's density
- **w_size** is the weapon's size.

Or, to sum up:

A stronger, smaller creature from a larger species wielding a more massive weapon hits with more momentum. A stronger, smaller creature from a larger species wielding a larger, denser weapon hits with more momentum.

For dwarves, the formula becomes

M = 6\*10⁴ \* Str \* Vel / (10 \* ( 10⁵ + i_Size/W )) = 6\*10⁴ \* Str \* Vel / ( 10⁵ + i_Size/W )

or

M = 0.06 \* Str \* Vel / (1 + i_Size/(w_density\*w_size) )

There are 28 possible sizes for your dwarves from 33750 to 93750; strength can vary from 0 to 5000 with an average of 1250; velocity can vary from 1 (pommel strikes) to 5 (whip lashes); weapon size can vary from 100 (whips) to 1300 (great axes, which are unwieldable by dwarves; the largest wieldable weapon is size 800, in the form of battle axes and maces).

| Dwarf Size | Adamantine | Divine metal | Steel | Iron | Bismuth bronze | Bronze | Copper | Silver |
|----|----|----|----|----|----|----|----|----|
| 33750 | 77.4194 | 89.9550 | 93.2489 | 93.2489 | 93.2730 | 93.2730 | 93.3092 | 93.3745 |
| 42750 | 73.9827 | 88.9944 | 93.1161 | 93.1161 | 93.1467 | 93.1467 | 93.1923 | 93.2748 |
| 44100 | 73.4934 | 88.8520 | 93.0963 | 93.0963 | 93.1277 | 93.1277 | 93.1748 | 93.2599 |
| 45000 | 73.1707 | 88.7574 | 93.0830 | 93.0830 | 93.1151 | 93.1151 | 93.1632 | 93.2500 |
| 45900 | 72.8509 | 88.6630 | 93.0698 | 93.0698 | 93.1025 | 93.1025 | 93.1515 | 93.2400 |
| 47250 | 72.3764 | 88.5217 | 93.0499 | 93.0499 | 93.0836 | 93.0836 | 93.1340 | 93.2251 |
| 54150 | 70.0444 | 87.8066 | 92.9485 | 92.9485 | 92.9871 | 92.9871 | 93.0447 | 93.1489 |
| 55860 | 69.4895 | 87.6312 | 92.9235 | 92.9235 | 92.9632 | 92.9632 | 93.0226 | 93.1301 |
| 56250 | 69.3642 | 87.5912 | 92.9177 | 92.9177 | 92.9577 | 92.9577 | 93.0176 | 93.1258 |
| 57000 | 69.1244 | 87.5146 | 92.9067 | 92.9067 | 92.9473 | 92.9473 | 93.0079 | 93.1175 |
| 57624 | 68.9262 | 87.4509 | 92.8976 | 92.8976 | 92.9386 | 92.9386 | 92.9999 | 93.1107 |
| 58140 | 68.7632 | 87.3983 | 92.8900 | 92.8900 | 92.9314 | 92.9314 | 92.9932 | 93.1050 |
| 58800 | 68.5558 | 87.3312 | 92.8804 | 92.8804 | 92.9221 | 92.9221 | 92.9847 | 93.0977 |
| 59850 | 68.2283 | 87.2245 | 92.8650 | 92.8650 | 92.9075 | 92.9075 | 92.9711 | 93.0861 |
| 59976 | 68.1893 | 87.2117 | 92.8631 | 92.8631 | 92.9057 | 92.9057 | 92.9695 | 93.0847 |
| 60000 | 68.1818 | 87.2093 | 92.8628 | 92.8628 | 92.9054 | 92.9054 | 92.9692 | 93.0845 |
| 61200 | 67.8119 | 87.0878 | 92.8452 | 92.8452 | 92.8887 | 92.8887 | 92.9537 | 93.0713 |
| 61740 | 67.6468 | 87.0332 | 92.8373 | 92.8373 | 92.8811 | 92.8811 | 92.9467 | 93.0653 |
| 62424 | 67.4388 | 86.9642 | 92.8273 | 92.8273 | 92.8716 | 92.8716 | 92.9379 | 93.0578 |
| 63000 | 67.2646 | 86.9061 | 92.8189 | 92.8189 | 92.8636 | 92.8636 | 92.9305 | 93.0514 |
| 64260 | 66.8866 | 86.7794 | 92.8004 | 92.8004 | 92.8460 | 92.8460 | 92.9142 | 93.0376 |
| 66150 | 66.3277 | 86.5901 | 92.7728 | 92.7728 | 92.8197 | 92.8197 | 92.8899 | 93.0168 |
| 71250 | 64.8649 | 86.0832 | 92.6983 | 92.6983 | 92.7487 | 92.7487 | 92.8242 | 92.9607 |
| 73500 | 64.2398 | 85.8615 | 92.6655 | 92.6655 | 92.7175 | 92.7175 | 92.7953 | 92.9360 |
| 75000 | 63.8298 | 85.7143 | 92.6436 | 92.6436 | 92.6966 | 92.6966 | 92.7760 | 92.9196 |
| 76500 | 63.4249 | 85.5676 | 92.6217 | 92.6217 | 92.6758 | 92.6758 | 92.7567 | 92.9031 |
| 78750 | 62.8272 | 85.3485 | 92.5890 | 92.5890 | 92.6446 | 92.6446 | 92.7278 | 92.8784 |
| 93750 | 59.1133 | 83.9161 | 92.3711 | 92.3711 | 92.4370 | 92.4370 | 92.5357 | 92.7143 |

Momenta for dwarves of strength 1250 hacking (velocity 1.25) with battle axes (size 800), rounded to 3 decimal places

There is also a hard velocity limit (10000) that might skew these calculations, but it's actually impossible to reach in unmodded game. (Well, okay, if you're a zombie adventurer with maxed out strength you *might* reach the limit using an adamantine whip -- but why?)

#### Situational Modifiers

Momentum can be further increased with weapon skill, status effects, attack modifiers etc. For example:

- Skill adds gradual multiplier, up to 2x at Grand Master.
- Quick attacks halve momentum, wild and heavy attacks add 50%.
- Attacking a prone opponent doubles momentum value.

#### Ranged Attacks

Attacks from missile launchers are entirely dependent on the launcher's \[SHOOT_FORCE\] and \[SHOOT_MAXVEL\] tags:

|  | SHOOT_FORCE | SHOOT_MAXVEL | Maximum Velocity | Magic Density / Constant Momentum |
|----|----|----|----|----|
| Bows and Crossbows | 1000 | 200 | 20 | 1666 / 50 |
| Blowguns | 100 | 1000 | 100 | 250 / 5 |

Specifically, as long as projectile is heavy enough, it is fired with a momentum of SHOOT_FORCE/20; if this would make its speed exceed SHOOT_MAXVEL/10, it is capped at this value instead. (As usual, momentum = velocity times weight.) This gives the launcher a magic density above which momentum becomes a constant and velocity decays, shown in the table; below this density, velocity is constant (SHOOT_MAXVEL/10), and momentum decays.

Vanilla bolts and arrows end up with a momentum of 50 (velocity nearly 20, at density 1667), as long as their density exceeds 1666. Divine ammo (1.5kg) has momentum 30 (velocity 20), bone and most wood (0.75kg) get 15 (velocity 20), and adamantine bolts (0.3kg) have only 6 (velocity 20). Wooden darts (0.1kg) usually have 5 (velocity 50).

#### Weapon Traps

Traps always have a fixed attack velocity of 200, no matter the weapon weight; the momentum thus is 200 times weight. This includes shot ammunition.

### Attack Momentum Costs

The attack generally needs some momentum threshold to break through each armor/tissue layer. If the attack is **edged**, it also can cut through it instead. For latter it has to have momentum no less than:

M \>= (rSY + (A+1)\*rSF) \* (10 + 2\*Qa) / (S \* Qw),

where:

- **rSY** is the ratio of layer's to weapon's SHEAR_YIELD
- **rSF** is ditto with SHEAR_FRACTURE
- **A** is attack contact area
- **S** is weapon material sharpness multiplier (1x for most metals, 1.2x for divine metal, 1.5x for glass, 2x for obsidian, 10x for adamantine and 0.1x for all other materials)
- **Qw** is quality sharpness multiplier (1x for normal quality, 1.4x for fine, 2x for masterwork (or artifact) etc.)
- **Qa** is armor quality multiplier (same but x3 for artifacts)

Should it exceed this value, attack momentum is decreased by some 5% and the layer is considered punctured/severed. Calculations then repeat for the underlying layer. Otherwise damage is converted to blunt *just for this layer* and proceeds as following.

**Blunt attacks** can be entirely deflected by armor if weapon's IMPACT_YIELD is especially low relative to armor's density:

2 \* Sw \* IYw \= (2\*IF - IY) \* (2 + 0.4\*Qa) \* A,

where **IF** and **IY** are layer's impact fracture and impact yield in MPa, **Qa** is armor quality multiplier and **A** is contact area as above. Again, on success layer is considered thrashed, momentum is reduced by about 5% and next layer is tested.

If both edged and blunt momenta thresholds haven't been met, attack is *permanently* converted to blunt and its momentum may be greatly reduced. Specifically, it is multiplied by SHEAR_STRAIN_AT_YIELD/50000 for *edged* attacks or IMPACT_STRAIN_AT_YIELD/50000 otherwise. I.e., most metals reduce blocked attacks by 98%-99%, but see below. Note that elastic armor, such as a mail shirt, has both strain at yield values raised to 50000, so it multiplies by 1 at this step (i.e. does nothing to the momentum, but does still convert it to blunt) regardless of material.

### Elastic Material Modifiers

Clothing with \[STRUCTURAL_ELASTICITY\_\*\] tokens has its stress properties modified.

Items with \[STRUCTURAL_ELASTICITY_CHAIN_ALL\] or metallic items with \[STRUCTURAL_ELASTICITY_CHAIN_METAL\] have their \[\*\_STRAIN_AT_YIELD\] increased to 50000, which means that blocked attack will not be dampened; it still may be converted to *blunt*, however. Metal leggings and chainmail shirts have this property in vanilla.

Items made of cloth (including adamantine!) with \[STRUCTURAL_ELASTICITY_WOVEN_THREAD\] additionally have their SHEAR values reduced to negligible 20-30 kPa. This makes candy clothing especially useless in combat. Caps and all clothing have this tag in vanilla.

### Penetration Depth

Penetration depth affect how deep stabs go. Unlike contact area, penetration depth is the maximum shear distance the weapon can go before an edged force stops and converts into a blunt force. If the penetration depth is greater than the size of the struck body part, the body part may be sliced off entirely. This means that weapons like morningstars mainly deal surface damage but can still damage arteries, nerves, tendons, toes, and the like.

### Pulping

Pulping appears to work by evaluating the layers in a body part. If each layer meets any one of the following criteria then the body part is pulped:

- 100% bruised/burned/frostbite/melt/necrosis/blister/boil/freeze/condense (i.e. 10000+ in layer_effect_fraction)
- 250% dented (i.e. 25000+ in layer_dent_fraction)
- 100% cut (i.e. 10000+ in layer_cut_fraction) (cut in this case is synonymous with fracture)

Spines, skulls, and perhaps other body parts have the \[PREVENTS_PARENT_COLLAPSE\] token which prevents the parent body part (such as the head, upper body, or lower body) from being pulped until the sub-part is broken. It appears that only external body parts can be pulped, not internal organs. You will find that boneless body parts that don't contain a spine/skull part will pulp VERY easily (i.e. eyes/ears).

There does not appear to be any distinctions between the combat text descriptions of the pulping, beyond the messages being appropriate to the weapon used (edged, blunt, or creature body part).

## Material and item properties

As can be seen from above, importance of different material/item properties greatly varies in different scenarios. Below are some guidelines to estimating weapon/armor merit.

- When dealing with dwarf-sized targets, layer **contact areas** usually lay in 200~10000 range. The majority of vanilla weapons, however, has contact areas either below or above that (dagger is the lone exception); it therefore can be said, as a rule of thumb, that weapons with area of five or six digits assume their target's contact area, whereas the others use their own.
- Weapon **weight** matters very little past a certain threshold: for example, a platinum war hammer in dwarven hands only gets about 12% more momentum over a steel one, despite being thrice as heavy. (An adamantine hammer, however, only has 1/7th as much.) Thus, since all common weapon metals have about the same density, it can be safely ignored.
  - The only exception are *weapon traps*, which are much more effective with heavy weapons loaded.
- **Shear yield** doesn't actually matter. Even with dagger/bolt's contact area of 5 it contributes only ~15% to piercing cost, and since it equals about half of shear fracture for most metals, it can be approximated as such without much error.
- Blunt weapons only use **impact yield** value. **Impact fracture** *protects* from blunt attacks instead. Curiously, layer impact yield actually decreases blunt fracturing cost, so *lower yield is better* for armor.
  - Most dedicated blunt weapons cannot be deflected by anything but slade, so their impact yield can in fact be ignored.
- Chain mail cannot block attacks via momentum cost thresholds; it still can blunt slashing attacks and then deflect them. Thus, the best defence can be reached by wearing *dense* (like copper) mail shirt under a *rigid* (like candy) one.
- **Strain at yield** values are used in comparison to 50000. Since all metals have much less strain values than this, they all can be considered to have *zero* elasticity.
- Adamantine clothing is *absolutely useless* as armor.
- Armor quality doesn't matter much: masterwork armor provides only about 15% more protection than low-quality one.
- Blunt weapon quality appears to not affect damage at all.

With that in mind, here are some numbers for vanilla weapon/armor materials:

| Material | Density | Impact Yield | 2\*(Impact Fracture) - Impact Yield | Shear Fracture | Elasticity | Sharpness |  | Bolt | adj. | Sword | adj. | Mace | min M |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| \| Adamantine | 0.20 | 5.00 | 5.00 | 5.00 | 0 | 10 |  | 6 | 300 | 9 | 450 | 31 | 200 |
| \| Bone/shell | 0.50 | 0.20 | 0.20 | 0.13 | \<1% | 0.1 |  | 15 | 0.20 | 19 | 0.25 | 60 | 8 |
| \| Bronze | 8.25 | 0.60 | 1.08 | 0.24 | \<=1% | 1 |  | 49 | 12 | 75 | 18 | 138 | 43 |
| \| Copper | 8.93 | 0.25 | 1.30 | 0.22 | \<1% | 1 |  | 49 | 11 | 77 | 17 | 138 | 52 |
| \| Divine metal | 1.00 | 1.00 | 3.00 | 2.00 | 0 | 1.2 |  | 30 | 72 | 31 | 74 | 86 | 120 |
| \| Glass | 2.6 | 1.00 | 1.00 | 0.04 | 4%/\<1% | 1.5 |  | -- | -- | 53 | 3.2 | 116 | 40 |
| \| Iron | 7.85 | 0.54 | 1.62 | 0.31 | \<1% | 1 |  | 49 | 15 | 75 | 23 | 137 | 65 |
| \| Leather | 0.50 | 0.01 | 0.01 | 0.03 | 100% | -- |  | -- | -- | -- | -- | -- | 0.4 |
| \| Obsidian | 2.67 | 1.00 | 1.00 | 0.04 | 4%/\<1% | 2 |  | -- | -- | 54 | 4.3 | 117 | 40 |
| \| Platinum | 21.4 | 0.35 | 1.05 | 0.20 | \<1% | 1 |  | -- | -- | 86 | 17 | 145 | 42 |
| \| Silver | 10.49 | 0.35 | 0.84 | 0.17 | \<1% | 1 |  | 49 | 8.3 | 79 | 13 | 140 | 34 |
| \| Slade | 200 | 4.00 | 6.00 | 5.00 | \<1% | 0.1 |  | -- | -- | 93 | 46 | 149 | 240 |
| \| Steel | 7.85 | 1.51 | 3.54 | 0.72 | 2%/\<1% | 1 |  | 49 | 35 | 75 | 54 | 137 | 142 |
| \| Wood | 0.50 | 0.01 | 0.01 | 0.04 | 2% | 0.1 |  | 15 | 0.06 | 19 | 0.076 | 60 | 0.4 |

Clarifications:

On the left side of the table there are some raw values. Density and impact yield are important for a blunt weapon; 4th column is adjusted impact fracture that appears in the formula for blunt defense. Shear fracture is important for edged attacks and defense. Elasticity is in %s of 100000; as you can see, it is universally low.

On the right side there are some typical weapon momenta. From left to right: bolt momentum; ditto multiplied by SF and sharpness (signifies piercing ability); short sword momentum in dwarven hands; ditto multiplied by sharpness and SF; dwarf swinging a mace; and minimum momentum **some** mace needs to break through armor of **this** material.
