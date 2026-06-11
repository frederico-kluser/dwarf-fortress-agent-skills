# Swimmer

> Fonte: [Swimmer](https://dwarffortresswiki.org/index.php/Swimmer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Skill: Swimmer

Association
 

Profession
None

Job Title
Peasant

Labor
None

Tasks

Getting in and out of water / Staying calm underwater

Workshop

None

Attributes

Strength / Agility / Endurance / Willpower / Spatial Sense / Kinesthetic Sense

**Swimmer** is a skill used by creatures to move through tiles containing deep liquid (primarily water), and generally avoid drowning. Creatures may have a [`[GAIT]`](/index.php/Creature_token#GAIT "Creature token") creature token that defines their movement speed while swimming. However, a creature's effective swimming speed can be modified by its Swimmer skill level, up to its maximum gait limit at Legendary skill.

## Drowning

Octopus man drowning in air.

Dwarves with Dabbling (level 1) or no experience as Swimmers will start drowning immediately upon contact with deep surface water (i.e. surface water of 7/7 depth). Those of Novice (level 2) experience or greater can be in deep surface water without drowning. Any dwarf will start drowning in 7/7 water if there is more water on levels above them (e.g. at the bottom of a two-level-deep cistern, or the bottom of the ocean). A bridge (or, presumably, any other building that prevents access to the air above the water) will also cause non-aquatic/amphibious creatures to begin drowning in 7/7 water--this can be useful for disposing of trolls in a drowning pit.

A way to delay the drowning of a dwarf (allowing them to survive long enough to become a Novice swimmer) is to drain a tiny amount of water, so that some tiles in the body of water are 6/7. If one of these 6/7 tiles strays over the dwarf, their drowning timer will be reset.

Any conscious, uninjured, non-stunned dwarf finding themselves in water of depth 4/7 or greater will try to leave, if they can find a path out of around 20 tiles in length or less.[1] If they can't find an exit within that distance, they won't move. This even goes for babies and/or dwarves that cannot walk and are laying prone - they are able to breathe regardless until they learn enough swimming to crawl out.

Dabbling swimmers require a ramp or stairway within 20 tiles to have any chance of getting out of deep water. Fortunately, every natural shallow body of water has ramps.

Novice swimmers are able to get out of deep water safely without needing a ramp or stairway, but they will start drowning if stunned. Once that happens, it can be difficult to get them out, as they lose the ability to exit anywhere and behave just like an untrained or dabbling swimmer. Everyone is stunned by falling into water, rather than entering it calmly, which is what normally happens when they aren't entering it of their own free will. Adequate (level 3) swimmers do not panic and start drowning in that situation, even when attacked, so training to this level is highly recommended - higher levels only increase speed while swimming. Note that you can drown in magma as well, but most creatures tend to melt first.

## Teaching swimming

Water's level: 7\
Swimming skill: Novice

It can be useful to teach swimming to your dwarves, especially your military, to help them survive avoidable death (such as dodging into a murky pool or a river). Dwarves will normally refuse to enter tiles with more than 3/7 water, and a depth of 4/7 (but less than 7/7, lest they drown) is necessary to train the skill, but with a specially designed swimming pool it can easily be done.

Animal people can't learn swimming due to a bug.Bug:9853 Creatures who are innate swimmers (for example, fish like carp) do not build up Swimmer skill, as they have no use for it.

## Other Activities

Dwarves cannot fight while swimming - adults won't initiate most activities, but they may continue what they were doing before being submerged - even sleeping underwater, and gaining swimming experience for it!

Dwarves trapped in a swimming pool will often try to climb up a wall to escape the water, which is relatively safe for the climbing dwarf, as the water will cushion their fall - maybe not so for any dwarves that they land on.

## Adventure Mode

In adventurer mode, as a novice swimmer or better, by standing next to a body of water and moving carefully (alt+direction) in the direction of the water (falling 1 or 2 z-levels is not an issue), you can swim about and train your skill. To get out, alt-move against a shoreline and select the option to move above it, or simply move toward the shore if it has ramps. You can also hold onto a (non-smooth) rock wall or tree above the water's edge in order to climb out, even without any skill in climbing. It is advisable to train your skill in swimming above novice because getting stunned, winded, or tired will make you flounder and, most likely, die, even if you're just one or two tiles from a ramp. While floundering, there is a small chance to successfully move, so you might get lucky enough to make it out of the water, but don't count on it.

Swimmers can also dive and rise through the z-axis by pressing \> and \ respectively. Note that air-breathers will be unable to breathe without air in the tile above them, and without returning to the surface will eventually drown. (Sadly, there's no oxygen meter as of yet (Unless you're using DFhack!), so you'll never know when they're about to expire. Don't linger too long.)

In adventure mode, water preference can be switched between "when possible" and "necessary" by pressing m.

### How long can you hold your breath?

The time before you drown is based on the following formula:

    ticks = ((ES+TS) / 4) + 200

Where:

- ES = Endurance score
- TS = Toughness score
- ticks = ticks before you drown

The scores are based on the following table, using the dwarven average:

|                          |                       |                |
|--------------------------|-----------------------|----------------|
| Endurance                | Toughness             | Drowning Ticks |
| absolutely inexhaustible | basically unbreakable | 1262-2700      |
| indefatigable            | incredibly tough      | 1137-1262      |
| very slow to tire        | quite durable         | 1012-1137      |
| slow to tire             | tough                 | 887-1012       |
| (no description)         | (no description)      | 638-887        |
| quick to tire            | flimsy                | 513-637        |
| very quick to tire       | very flimsy           | 388-512        |
| extremely quick to tire  | remarkably flimsy     | 263-387        |
| truly quick to tire      | shockingly fragile    | 200-262        |

Example: a dwarf with an average score of endurance and toughness will have 762 ticks to get out of the water, or drown.

However, keep in mind that drowning **rapidly** trains Endurance and Toughness, so by the time your dwarf drowns they might've trained both attributes slightly, giving you a few more ticks of leeway.

### Training your party

To teach companions to swim, some patience is necessary. Enter a body of water until they follow you inside, then immediately get out. They will flounder around and attempt to get out before they drown, but as long as they make it back on land, they will gain swimming experience - repeat until they manage to swim without drowning. Drowning itself can also be beneficial, as certain attributes (notably toughness and endurance), greatly benefit from the strain caused by the experience. Provided that this experience does not reach its fatal conclusion, the toughness of your band should reach a point where it can only be exceeded by the larger or more powerful supernatural entities.

If the temperature (press P) is "freezing" or "cold" and close to sundown, the water may freeze while you are swimming, which instantly kills you, and leaves your frozen corpse encased in ice - a valuable find for archaeologists.
