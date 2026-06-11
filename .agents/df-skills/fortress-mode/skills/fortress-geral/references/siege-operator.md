# Siege operator

> Fonte: [Siege operator](https://dwarffortresswiki.org/index.php/Siege_operator) — Dwarf Fortress Wiki (GFDL/MIT)

**Siege operators** are responsible for manning siege weapons, loading them with any available ammunition, and firing on command or at will. A sufficiently skilled siege operator will always fire them perfectly straight (to the north, south, east, or west), never veering off to the sides.

This is a task sometimes delegated to peasants as a cheap labor, as it can get them skilled swiftly. Catapults are also sometimes used to destroy unwanted stone.

Siege operators cannot "aim" sideways - they always try to fire perfectly straight, but if they're unskilled there's a chance that the shot will "go wild" and veer off to either side by a random amount. In the case of catapults, however, these "wild" shots will actually calculate their arc height based on whatever enemy units are present off to that side (rather than based on what would've been directly ahead).

As for the actual amount of variance, siege engines aim at a location exactly 60 tiles away and up to 10 tiles to either side (if the shot is "unskilled"), which works out to a 19 degree spread (9.5 degrees to each side). As of version 0.47.04, the game generates 3 random numbers from 0 to 14 and checks if any of them are less than the unit's effective Siege Operator skill level (where Dabbling is 0 and Legendary is 15, and status ailments such as Nausea/Winded/Stunned/Fever/etc. can each reduce the level by as much as 50%) to see if the sideways drift should be eliminated. This works out to the following probabilities:

| №   | Level        | Accuracy |
|-----|--------------|----------|
| 0   | Dabbling     | 0%       |
| 1   | Novice       | 18.7%    |
| 2   | Adequate     | 34.9%    |
| 3   | Competent    | 48.8%    |
| 4   | Skilled      | 60.6%    |
| 5   | Proficient   | 70.4%    |
| 6   | Talented     | 78.4%    |
| 7   | Adept        | 84.8%    |
| 8   | Expert       | 89.8%    |
| 9   | Professional | 93.6%    |
| 10  | Accomplished | 96.3%    |
| 11  | Great        | 98.1%    |
| 12  | Master       | 99.2%    |
| 13  | High Master  | 99.76%   |
| 14  | Grand Master | 99.97%   |
| 15  | Legendary    | 100%     |

While viewing a dwarf's general stats, this skill is grouped with the combat skills instead of the typical labor skills.
