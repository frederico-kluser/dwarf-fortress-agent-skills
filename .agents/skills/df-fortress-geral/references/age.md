# Age

> Fonte: [Age](https://dwarffortresswiki.org/index.php/Age) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*This article is about creature age. For world generation "ages", see Calendar#Ages.*

One of them has their whole life ahead of them.

**Age** is a creature attribute describing how long the creature has been alive, including creatures born before the beginning of time in terms of world generation (year zero). Age determines the life stage of creatures and, until it is fully grown, is the most important element of the creature's body size. All creatures have an age associated with them, but in fortress mode only your own dwarves will have observable ages in the thoughts and preferences screen. The age of a creature is determined based on the exact time of its birth, but is displayed in the game as an integer that is ticked up every time it reaches a birthday.

## Effects

The age of a creature has an important effect on its overall size and maturity. The starkest example of this in the game is the case of the dragon, which is born 6,000 cm3 in size then takes a thousand years to reach its full size of 25,000,000 cm3. However, the vast majority of the non-sapient creatures your dwarves encounter take one year to mature to adulthood and two years to reach full size; elephants and giraffes are notable exceptions, as their young take ten years to mature (though they reach full size in only 5 years). Upon reaching adulthood, non-sapient creatures can reproduce, be trained, milked, sheared, revert to wild status, and various other effects.

The life cycle of dwarves is slightly more complicated: juveniles ages zero to one are considered babies, and must be carried about by their mothers; between the ages of one to eighteen they are considered children, and can perform some limited tasks; and once they reach 18 years of age, they are considered adults. The process is the same for other civilized races, the original animal people, and the humanoid semi-megabeasts.

Another aspect that is controlled by age is lifespan. This is determined by the [`[MAXAGE]`](/index.php/Creature_token#MAXAGE "Creature token") token, which if present determines the minimum age at which a given creature may die of old age, and the maximum age that may be reached before death is guaranteed. Most organic creatures will eventually die of old age (including fortuitous fortress dwarves), usually within a range of 1-100 years. Giant versions of animals inherit their normally-sized brethrens' lifespans, while animal people usually have somewhat longer lifespans than their representative creatures. A few species, such as elves, goblins, and some unintelligent and unnatural creatures, will live until they are killed. Megabeasts, the undead, night creatures, and the procedurally generated forgotten beasts and titans are similarly immortal. This immortality is due to such creatures either lacking a `[MAXAGE]` token, or having acquired the NO_AGING syndrome tag. Immigrants may sometimes show up with incorrect ages (future birthdates) Bug:3945 or incorrect life stages (4 month old children) Bug:3752. This normally does not cause a problem, and life stages get rechecked every birthday. Note that only an intelligent civilized creature vulnerable to death by expiration will seek necromancy, which means goblins and elves never become practitioners of the dark arts.

Age does not interfere with a creature's physical or mental skills, attributes or behavior; a 150 year old dwarf is as capable as an 18 year old one. Despite most vermin possessing a noted `[MAXAGE]`, they do not seem to be affected by aging; a tamed vermin creature will last forever, even if it would otherwise die after a single year.

The game checks if a creature will die of old age at the beginning of every new year, on the 1st of Granite. In longer-running fortresses, several animals and livestock with short life spans could die at the same time. A creature's lifespan is determined at birth, so restoring from a previous seasonal autosave will *not* give them a chance to live longer.

Historical figures existing in year 1 are born in a "time before time" and described with "the appearance of one who is X years old". This includes your starting seven, in young worlds.

## Sample list of age characteristics

|  |  |  |  |  |
|:---|----|----|----|----|
| Name | Age of Adulthood | Age of Full Size | Minimum Age of Death | Maximum Age of Death |
| Ant | 0 | 0 | 1 | 1 |
| Bat | 0 | 0 | 2 | 3 |
| Antman | 0 | 2 | 5 | 8 |
| Dog | 1 | 2 | 10 | 20 |
| Lion | 3 | 2 | 10 | 20 |
| Unicorn | 1 | 2 | 10 | 20 |
| Elephant seal | 1 | 5 | 15 | 25 |
| Sponge | 0 | 0 | 20 | 30 |
| Carp | 1 | 5 | 20 | 30 |
| Ogre | 10 | 20 | 20 | 30 |
| Elephant | 10 | 5 | 50 | 70 |
| Serpent man | 12 | 12 | 60 | 80 |
| Sperm whale | 1 | 10 | 70 | 80 |
| Human | 18 | 18 | 60 | 120 |
| Sea serpent | 6 | 20 | 150 | 170 |
| Dwarf | 18 | 18 | 150 | 170 |
| Kobold | 18 | 18 | 150 | 170 |
| Troll | 10 | 20 | 800 | 1,000 |
| Elf | 18 | 18 | 99999— | 99999Immortal |
| Goblin | 18 | 18 | 99999— | 99999Immortal |
| Dragon | 10 | 1,000 | 99999— | 99999Immortal |
| Minotaur | 18 | 18 | 99999— | 99999Immortal |

## Mechanics

The mechanics of aging are defined by creature tokens within creatures' raw files, and can easily be modified by those looking to make changes to their game.

- `[CHILD:#]`: Age at which children become adults. Set to 1 for most creatures, up to 10 for a few (giraffe, elephant), and is set to 18 for most sapient creatures.
- `[BABY:#]`: For sapient creatures, age at which babies become children. Always set to 1.
- `[BODY_SIZE:#:#:#]`: Controls the body size of the creature, typically two or more are used to constrain its growth pattern. The first number is age in years; the second additional age in days. The third number is its size in cm3. The body size points are independent of the age of adulthood for the animal: many animals are adults in one year, but take two years to reach their full size, for instance.
- `[MAXAGE:#:#]`: The first number given is the minimum natural lifespan of a creature, while the second is the maximum. The distribution of deaths from natural causes in between the two values is linear (you can test this yourself using this script); the moment of death-by-old-age of a creature is stored from birth. If this tag is not present at all, the creature is biologically immortal.

|  |
|----|
| "Age" in other / Languages / Dwarven / : / anam / Elven / : / eyo / Goblin / : / abo / Human / : / thad |
