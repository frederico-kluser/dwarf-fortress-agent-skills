# Military testing (parte 3/3)

| \#1 vs \#1: | Short-sword | 86 (14 double kills were ignored) | 2 | 20 | 48 | 16 |
| \#1 vs \#1: | Spear | 94 (6 double kills were ignored) | 18 | 16 | 51 | 9 |
| \#1 vs \#1: | War hammer | 95 (5 double kills were ignored) | 63 | 0 | 32 | 0 |
| \#1 vs \#1: | Mace | 91 (9 double kills were ignored) | 36 | 0 | 55 | 0 |
| \#1 vs \#1: | Pickaxe | 92 (8 double kills were ignored) | 4 | 45 | 28 | 15 |

**Results for giant kills:**

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| Side & Creature | Weapon | Dead giants | Regular corpses | Mutilated corpses | Mangled corpses | Mangled Mutilated corpses |
| \#2 vs \#3: | Battle axe | 95 (1 stalemate and 4 losses were ignored) | 95 | 0 | 0 | 0 |
| \#2 vs \#3: | Short-sword | 97 (3 losses were ignored) | 94 | 0 | 3 | 0 |
| \#2 vs \#3: | Spear | 99 (1 stalemate were ignored) | 90 | 0 | 9 | 0 |
| \#2 vs \#3: | War hammer | 95 (2 stalemate and 3 losses were ignored) | 0 | 0 | 95 | 0 |
| \#2 vs \#3: | Mace | 85 (2 stalemates and 13 losses ignored) | 0 | 0 | 85 | 0 |
| \#2 vs \#3: | Pickaxe | 98 (2 losses were ignored) | 20 | 0 | 78 | 0 |

**Tester's conclusion:**

Dwarf 28: How fragile we are... I must not succumb to fear!

edit: All weapons used in this test were made out of copper. In a recent fort I played, a dwarf with an Adamantine battle axe were able to mutilate a giant with a hack to the head. Not sure how other materials will perform.

## Skilled Miner vs average soldier (by NeckRomancer)

Mining is very easy to train up. But how good is a miner with an armor piercing pick in a fight? Training soldiers can take a long time. In this test the soldiers only get half the skill of the miner. Please note that soldier training also boosts the attributes more than mining does, the effect of that is unknown.

note: *When the pickaxe was tested, the raws were edited so that it uses the Axe skill instead of Mining, since the Mining skill can't be increased in the Arena. The default file is ...\DF\raw\objects\item_weapon.txt but each save also has its own copy of it.*

**Creatures**

|  |  |  |  |
|----|----|----|----|
| Side & Creature | Number | Skills | Items |
| \#1: Miner | 1 | Pickaxe 14 / (Mining skill by default) | Steel Pickaxe |
| \#2: Soldier | 1 | Fighter 7 / Axeman 7 / Dodger 7 / Shield User 7 / Armor user 7 | Iron battle axe / Fungiwood shield / iron mail shirt / iron helm / iron breastplate / iron greaves / 2 iron gauntlets / 2 iron high boots |

**Times run:** 100 per set

**Initial setup:** Only dwarven females (gender should not matter), fighting in a 7x7 room, fighters start at opposite walls

**1v1 Results**

|                 |                                                |
|-----------------|------------------------------------------------|
| Side & Creature | Victories                                      |
| \#1 vs \#2      | Miner won 38/91 (1 stalemate, 8 double kills)  |
| \#1 vs \#2      | Miner won 39/86 (1 stalemate, 13 double kills) |

**10v10 Results**

|  |  |  |
|----|----|----|
| Side & Creature | Victories | Comment |
| \#1 vs \#2 | Miners won 18/99 (1 all died) | 74/1000 miners alive, 448/1000 soliders alive |

**Tester's conclusion:**

Skilled unarmored miners can definately put up a fight in 1v1. But they perform poorly as an army.

## Hit locations (by NeckRomancer)

What body parts are hit the most?

This test is done with armor to prevent mutilation. It is untested if a lost limb can be hit again, it's just assumed that it can't. The face however can't be protected by armor, so parts like ears and noses can still be lost, and this can have an effect on the outcome.

Each test is only run for a few seconds to prevent fighters from falling unconscious (from pain or fatigue). Since an unconscious target always seem to be hit in the head, this would skew the result.

A script was used to count the hits and their locations. But the script wasn't perfect. Some face hits damage multiple parts, a tongue hit can/will also do damage to the cheek for example, which will result in double counting in those particular cases. There can also be other errors that are undiscovered. That is why the total number of hits are slightly lower than what is obtained by adding all individual hits together.

edit:*a script error was found, hands and fingers as well as feet and toes were counted together, column labels have been adjusted to show this, no data has been changed*

**Creatures**

|  |  |  |  |
|----|----|----|----|
| Side & Creature | Number | Skills | Items |
| \#1: Soldier | 1 | Fighter 5 / Weapon 5 | Copper weapon / Copper mail shirt / Copper helm / Copper breastplate / Copper greaves / 2 copper gauntlets / 2 copper high boots |

**Times run:** 100 fights per set, for just a few seconds to avoid unconsciousness as much as possible

**Initial setup:** Only dwarven males, fighting in a 7x7 room, fighters start at opposite walls

**Results for dwarf vs dwarf**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Weapon used | Weapon hits | Head | Neck/Throat | Upper body | Lower body | Upper arm | Lower arm | Hand + Finger | Upper leg | Lower leg | Foot + Toe | Only fingers | Only toes | Face parts (has double-counting) |
| Battle axes | 1743 | 137 | 45/0 | 99 | 89 | 106/113 | 133/139 | 143/126 | 51/41 | 57/55 | 146/138 | 10 | 6 | 130 |
| Battle axes | 1961 | 157 | 51/2 | 129 | 131 | 168/141 | 133/128 | 162/130 | 52/41 | 69/56 | 152/130 | 10 | 7 | 138 |
| Short-swords | 1543 | 141 | 37/0 | 90 | 101 | 104/115 | 112/98 | 117/125 | 57/38 | 34/32 | 109/134 | 12 | 5 | 105 |
| Short-swords | 1629 | 133 | 38/2 | 99 | 94 | 115/123 | 116/117 | 114/117 | 60/57 | 59/41 | 126/103 | 11 | 5 | 121 |
| Spears | 1915 | 147 | 55/1 | 134 | 135 | 132/137 | 150/135 | 155/144 | 50/58 | 62/46 | 127/124 | 22 | 4 | 131 |
| Spears | 1774 | 141 | 51/1 | 126 | 124 | 123/153 | 119/133 | 134/133 | 54/43 | 51/50 | 119/127 | 10 | 1 | 93 |
| War hammers | 1210 | 97 | 38/1 | 75 | 79 | 100/92 | 101/93 | 101/92 | 40/40 | 30/23 | 81/81 | 11 | 1 | 48 |
| War hammers | 1496 | 159 | 35/4 | 83 | 89 | 108/103 | 114/101 | 131/115 | 35/38 | 45/39 | 105/120 | 9 | 3 | 74 |
| Maces | 1410 | 118 | 48/1 | 95 | 76 | 109/96 | 109/92 | 117/101 | 54/37 | 52/35 | 101/102 | 10 | 1 | 68 |
| Maces | 1372 | 133 | 39/1 | 85 | 89 | 107/96 | 92/118 | 111/94 | 48/41 | 38/33 | 102/97 | 2 | 2 | 49 |
| Pickaxes | 1679 | 159 | 37/3 | 113 | 105 | 118/125 | 132/126 | 130/121 | 39/46 | 49/49 | 111/140 | 9 | 7 | 78 |
| Pickaxes | 1413 | 110 | 37/0 | 100 | 83 | 105/92 | 109/123 | 108/117 | 35/38 | 41/39 | 123/102 | 9 | 0 | 53 |

**Averaged results in %**\
The face hits value is uncertain since it is known to contain double counting. By using the value for total number of hits, the double counting can be adjusted for, and it is found to be 0.8% units too high. When all % values are added they become 99.4%, the missing 0.6% comes from rounding.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Comment | Head | Neck/Throat | Upper body | Lower body | Upper arm | Lower arm | Hand + fingers | Upper leg | Lower leg | Foot + toes | Only fingers | Only toes | Face parts |
| Left/Right bodypart | 8.6 | 2.7 / 0.1 | 6.4 | 6.2 | 7.3 / 7.2 | 7.4 / 7.3 | 8.0 / 7.4 | 3.0 / 2.7 | 3.1 / 2.6 | 7.3 / 7.3 | 0.6 | 0.2 | 5.6 (adjusted value is 4.8) |
| Combined | 8.6 | 2.7 / 0.1 | 6.4 | 6.2 | 14.5 | 14.7 | 15.4 | 5.7 | 5.7 | 14.6 | 0.6 | 0.2 | 5.6 (adjusted value is 4.8) |

**Combined averaged results in % with hands/fingers and feet/toes separated**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Comment | Head | Neck/Throat | Upper body | Lower body | Upper arms | Lower arms | Hands | Upper legs | Lower legs | Feet | Fingers | Toes | Face parts |
| Combined | 8.6 | 2.7 / 0.1 | 6.4 | 6.2 | 14.5 | 14.7 | 14.8 | 5.7 | 5.7 | 14.4 | 0.6 | 0.2 | 4.8 |

**Armor pieces and their % chance of recieving a hit**

|                            |                                     |
|----------------------------|-------------------------------------|
| Armor piece                | approximate % chance of getting hit |
| Mail shirt / leather armor | 35.6                                |
| Helm                       | 8.6                                 |
| Breastplate                | 12.6                                |
| Greaves / leggings         | 17.6                                |
| Gauntlets                  | 30.1                                |
| High boots                 | 20.3                                |
| Low boots                  | 14.6                                |

**Tester's conclusion:**

It appears that all weapons use the same hit location calculation. There is one minor trend where the left limbs of the body are hit more, which could be explained by the attacker holding the weapon in his right hand. War hammers and Maces have 9.5% and 9.0% head hits respectively, slightly higher than average, I think this can be explained by the fact that blunt weapons can kill through helmets and after that happen that particular fight is over and no longer generate any new hits and this will skew the numbers in favor of the head.

A thought on low vs high boots: Even though gauntlets are more likely to break, the boots are also hit fairly often. If there is a concern about them breaking, the low boots would be the better choice, since the legs have a low chance of being hit the greaves / leggings are pretty safe already and the lower body have several overlapping armor pieces. The lower legs have a low chance of getting hit, so having double armor on them is not that important, especially when compared to the risk of loosing the boots entirely if they were to break. An item breaks the 5th time it takes damage, and blunt weapons of any material, especially the war hammer, can damage and break all kinds of armor (not tested on adamantium).

As a side note: Leggings have both the \[shaped\] and \[elastic\] tags, which seems incorrect since they should be mutually exclusive. It appears as if leggings can stop blunt damage just like greaves do, but they will never get damaged by blunt hits.

## Shields vs Bucklers in melee combat (by NeckRomancer)

Straightforward test, one side has shields and the other bucklers, who wins the most? Trying both a 7x7 room and a 1x15 tunnel.

**Creatures**

|  |  |  |  |
|----|----|----|----|
| Side & Creature | Number | Skills | Items |
| \#1a: Shield soldier | 1 | Fighter 5 / Axeman 5 / Shield User 5 | Copper battle axe / Fungiwood shield |
| \#1b: Skilled shield soldier | 1 | Fighter 5 / Axeman 5 / Shield User 10 | Copper battle axe / Fungiwood shield |
| \#2a: Buckler soldier | 1 | Fighter 5 / Axeman 5 / Shield User 5 | Copper battle axe / Fungiwood buckler |
| \#2b: Skilled buckler soldier | 1 | Fighter 5 / Axeman 5 / Shield User 10 | Copper battle axe / Fungiwood buckler |

**Times run:** 100 per set

**Initial setup:** Only dwarven females (gender should not matter), fighting in a 7x7 room / 1x15 tunnel, fighters start at opposite walls

**Results**

|  |  |  |
|----|----|----|
| Side & Creature | Victories | Comment |
| \#1a vs \#2a | Bucklers won 40/98 (1 stalemate, 1 double kill) | 7x7 room |
| \#1a vs \#2a | Bucklers won 44/97 (3 double kills) | 7x7 room |
| \#1a vs \#2a | Bucklers won 44/98 (2 double kills) | 7x7 room |
| \#1b vs \#2b (skilled) | Bucklers won 47/100 | 7x7 room |
| \#1b vs \#2b (skilled) | Bucklers won 40/97 (1 stalemate, 2 double kills) | 7x7 room |
| \#1b vs \#2b (skilled) | Bucklers won 50/98 (2 double kills) | 7x7 room |
| \#1a vs \#2a | Bucklers won 23/47 (1 stalemate, 2 double kills) | 1x15 tunnel |
| \#1a vs \#2a | Bucklers won 25/50 | 1x15 tunnel |
| \#1a vs \#2a | Bucklers won 23/46 (3 stalemates, 1 double kill) | 1x15 tunnel |
| \#1a vs \#2a | Bucklers won 19/48 (2 double kills) | 1x15 tunnel |
| \#1a vs \#2a | Bucklers won 19/48 (2 double kills) | 1x15 tunnel |
| \#1a vs \#2a | Bucklers won 21/47 (2 stalemates, 1 double kill) | 1x15 tunnel |

**Tester's conclusion:**

Shields perform a bit better in melee combat than bucklers.

\

# v50 (v50.07) tests

## Heavy Armor vs Medium Armor (tested by: someguy)

**Times run:**

100 times each

**Initial setups and Results:**

|  |  |  |  |
|----|----|----|----|
| Side & Creature | Skills | Items | Victories |
| \#1: 15 Dwarves | -no skills- | Steel Short Sword, Wood Shield, Full set of steel armor | 43 |
| \#2: 15 Dwarves | -no skills- | Same but without Greaves and Breastplate | 57 |

|  |  |  |  |
|----|----|----|----|
| Side & Creature | Skills | Items | Victories |
| \#1: 5 Dwarves | swordsdwarf 7 | Steel Short Sword, Wood Shield, Full set of steel armor | 43 |
| \#2: 5 Dwarves | swordsdwarf 7 | Same but without Greaves and Breastplate | 53 |

|  |  |  |  |
|----|----|----|----|
| Side & Creature | Skills | Items | Victories |
| \#1: 5 Dwarves | swordsdwarf 14 | Steel Short Sword, Wood Shield, Full set of steel armor | 56 |
| \#2: 5 Dwarves | swordsdwarf 14 | Same but without Greaves and Breastplate | 42 |

**Methodology:**

All experiments featured 100 fights. When there were no survivors the fight was excluded from the final numbers. For the unskilled test 5 15x15 dwarf combats were generated in a classic arena map and then the map was reloaded 20 times. For the other tests 25 5x5 dwarf combats were generated in forest arena map inside 7x7 rooms made of tree trunks and the map was reloaded 4 times.

Steel Short swords were chosen for their variety of attacks.

Tests were done at different skill levels to vary the momentum of successful strikes (1.0x at unskilled, 1.5x at adept, 2.0x at grand master.)

**Notes:**

The objective of the test is to study some claims made in Armor#Encumbrance. Older testing indicated an unskilled peasant wearing heavy armor may fight at two-thirds the speed of a naked dwarf \[link\].

"Full Steel Armor" is used to mean breastplate, greaves, helm, gauntlets, high boots, and mail shirt.

Steel short swords wielded by typical dwarves will not pierce steel mail shirts. Instead the benefit of shaped armor in this situation was to decrease blunt damage from torso and leg strikes.

Weapon skill likely affects parrying chance as well as momentum, so varying skill level ultimately influenced combat length, and therefore the importance of fatigue, in an unknown way. Collapse from over-exertion was common.

The 95% confidence intervals for these results are about +-10 combats.

**Tester's conclusions:**

In no sample set of 100 combats was a statistically significant difference from equality of the groups observed. Furthermore at low and medium weapon skill levels the medium-armored dwarves performed somewhat better. These results are consistent with the advice that for military dwarves with low armor skill, the encumbrance of wearing multiple pieces of 15+ weight armor makes the extra protection not worth it. However, the difference does not appear to be backbreaking, metaphorically speaking. For comparison, in Neckromancer's win ratio tests above, a naked but shielded axedwarf with 2 ranks in each relevant skill defeated a similar dwarf with 1 rank in each relevant skill 83 out of 100 times.

# v50 (v50.11) tests

## Best weapon to fight dragons (tested by: Mimi-limonite)

3 dwarves with full iron armor + shields and decent skills are set against 1 default dragon. 4 variations are tested: swords, spears, warhammers and axes.

**Times run:** 200, each, 800 total

**Initial setup:** 3 dwarves with skill level 9(professional) in fighter, dodger, armor user, shield user, observer and discipline, skill level 6(talented) in biting, kicking, striking and wrestling, and skill level 9 in the skill for their weapon(axedwarf, speardwarf, etc.) are tested. They are given an iron breastplate, iron greaves, high boots, and gauntlets, iron shields and helms, as well as an iron warhammer/battle axe/short sword/spear. The dragon had a level 6 skill in observer, biter, archer, fighter, striker and dodger, which are the default ones for a dragon spawned in the arena. They are put in a 4x4 room with the dragon in one corner and the dwarves in the opposite one. This is done in 40 rooms, and repeated 5 times for each weapon.

**Results:**

|                          |              |                |                 |
|--------------------------|--------------|----------------|-----------------|
| Side & Creature          | Wins(\*note) | Percentage Win | Survivors total |
| \#1: Dragon              | 56           | 28%            | 56/200          |
| \#2: 3 Warhammer dwarves | 144          | 72%            | 310/600         |

|                           |              |                |                 |
|---------------------------|--------------|----------------|-----------------|
| Side & Creature           | Wins(\*note) | Percentage Win | Survivors total |
| \#1: Dragon               | 24           | 12%            | 24/200          |
| \#2: 3 Battle axe dwarves | 176          | 88%            | 474/600         |

|                      |              |                |                 |
|----------------------|--------------|----------------|-----------------|
| Side & Creature      | Wins(\*note) | Percentage Win | Survivors total |
| \#1: Dragon          | 18           | 9%             | 18/200          |
| \#2: 3 Sword dwarves | 182          | 91%            | 514/600         |

|                      |              |                |                 |
|----------------------|--------------|----------------|-----------------|
| Side & Creature      | Wins(\*note) | Percentage Win | Survivors total |
| \#1: Dragon          | 7            | 3.5%           | 7/200           |
| \#2: 3 Spear dwarves | 193          | 96.5%          | 511/600         |

**Comparison of differently armed dwarves:**

|  |  |  |  |
|----|----|----|----|
| Weapon | Wins + ties | Percentage win or tie | Survivors(out of 600) |
| \#1: Spear dwarves | 193 | 96.5% | 511 |
| \#2: Sword dwarves | 182 | 91% | 514 |
| \#3: Battle axe dwarves | 176 | 88% | 474 |
| \#4: Warhammer dwarves | 144 | 72% | 310 |

**Tester's conclusion:** Hammerdwarves are the worst by far, and axedwarves after them. Speardwarves and swordsdwarves have very similar survival rates but speardwarves lost significantly less, suggesting that when swordsdwarves win, it's less likely some of them died while doing so, while speardwarves are more reliable.

**Notes:** (\*) due to ease of counting, dwarf wins and draws are counted together, as it was much easier to count the number of remaining dragons(equivalent to dragon wins), ie number of surviving team 1 members, than check every room individually.

## Warhammer Material Testing (Testing by Jonaut)

It has been debated many times as to if a blunt weapon's material affects its usefulness. This data was only collected using war hammers, though it can be presumed that it also applies to maces. Platinum should theoretically do the most damage, it has quite low impact elasticity, and an exceptionally high density. Steel, on the other hand, should be quite bad for warhammers, it has a very low density comparatively, and a surprisingly high impact elasticity. Silver is in the middle, still having more density than steel, yet half that of platinum. Its impact elasticity is much lower than steel's, but higher than platinum's. Silver is the densest weapons-grade metal. It is also much more accessible, as platinum is not a weapons-grade metal, meaning it must be made into weapons exclusively through strange moods.

**Platinum vs Steel:** Note: The number is the amount of wins it had out of 25, then the percentage of wins.

*Platinum*

|                |            |          |
|----------------|------------|----------|
| Skill & Armour | Unarmoured | Armoured |
| Unskilled      | 9, 36%     | 8, 32%   |
| Grand Master   | 17, 68%    | 16, 64%  |

*Steel*

|                |            |          |
|----------------|------------|----------|
| Skill & Armour | Unarmoured | Armoured |
| Unskilled      | 16, 64%%   | 17, 68%  |
| Grand Master   | 8, 32%     | 9, 36%   |

**Silver vs Steel:**

*Silver*

|                |            |          |
|----------------|------------|----------|
| Skill & Armour | Unarmoured | Armoured |
| Unskilled      | 10, 40%    | 10, 40%  |
| Grand Master   | 19, 76%    | 21, 84%  |

*Steel*

|                |            |          |
|----------------|------------|----------|
| Skill & Armour | Unarmoured | Armoured |
| Unskilled      | 15, 60%    | 15, 60%  |
| Grand Master   | 6, 24%     | 4, 16%   |

**Conclusions:** From this data we can make a few crucial inferences. First of all, at low skill levels silver and platinum's weight is a net loss, as it wears the dwarf out faster, and the decreased hit-rate of unskilled dwarves means that a lot of the extra damage is wasted. At high skill levels, the weight is a net gain, as the reduced stamina drain of skilled dwarves and their increased hit-rate leads to the weight giving an extreme damage boost compared to the steel. We can also infer that platinum's increased density is more detrimental than beneficial, even at grand master level, and silver is a better choice. Finally, we can infer that at higher levels, for example legendary +20, platinum's damage may surpass the stamina loss, leading it to be more effective than silver. There is, unfortunately, no convenient way to test this theory as arena mode only allows up to grand master skill. It is also worth noting that high density warhammers, whether they are in the hands of skilled or unskilled dwarves, will offer much greater burst damage, meaning that if the dwarf can kill their opponent before getting tired, they will perform much better than lower density metals. This is particularly true for squads of warhammer dwarves, as an entire squad's quick burst of damage before tiring is likely enough to kill many things.

*Combat Testing* After a quick test, minotaurs can be dispatched by a squad of dwarves, unskilled and skilled with platinum warhammers, with the unskilled dwarves taking one death, and the skilled dwarves taking zero damage. Bronze colossuses easily dispatch the squads, both skilled and unskilled, as it appears their weaponry is unable to damage it. Dragons are also too strong for the squads, though the deaths were exclusively from the dragonfire, meaning a squad with better shield user skill would likely have won. Rocs, being the generally-considered weakest of the megabeasts, was taken out with zero injuries by the skilled squad, and with 5 losses by the unskilled squad. Finally, a hydra was able to fully dispatch an unskilled squad, but could not inflict even a single injury upon the skilled one. A squad of unskilled dwarves with only iron spears was still able to kill the roc with less losses, only 3, but considering blunt damage's main weakness is pure size, the hammerdwarves did surprisingly well. Against armoured enemies, they would likely fare better than any other weapon.


---
*Parte 3 de 3 de «Military testing». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Military_testing*
