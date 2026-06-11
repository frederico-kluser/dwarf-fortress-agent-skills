# Position token

> Fonte: [Position token](https://dwarffortresswiki.org/index.php/Position_token) — Dwarf Fortress Wiki (GFDL/MIT)

Position tokens define noble positions for Dwarf Fortress mode. They are defined inside Entity tokens. In the vanilla game, position token definitions can be found in ```\data\vanilla\vanilla_entities\objects\entity_default.txt`.

## Position tokens

These tokens belong in an entity definition. These tokens apply to a position (such as monarch) and should follow the \[POSITION:POSITION_NAME\] token.

[TABLE]

## Responsibilities

[TABLE]

## Related tokens

The following two ENTITY tokens are not actually position tokens, but bear mentioning on this page because they can modify the way that a civilization's positions behave:

[TABLE]

## Why won't my positions appear?

The way DF determines what positions will actually *appear* in your fortress is somewhat counter-intuitive and fairly limiting. This guide should help you understand what you can do to actually get your positions working properly.

There are five tokens governing which positions appear in your fortress - LAND_HOLDER, REQUIRES_POPULATION, APPOINTED_BY, ELECTED, and REPLACED_BY. The first two determine when your fortress is eligible for a new position, the next two determine how a new position for which your fortress is eligible can be added, and the fifth allows you to clear up obsolete positions. Unfortunately, they also interact in some strange ways that makes creating interesting position structures difficult.

When you start a new fortress, DF compiles a list of your initial positions. To do this, it looks at the requirements for each position - any position whose only requirement is less than seven dwarves (either because they have no requirement tokens, or because their only requirement tokens are \[REQUIRES_POPULATION: =\< 7\] or \[LAND_HOLDER:some trigger whose only requirement is some number of dwarves equal to or less than 7\]). Most importantly, *any* position whose only requirement is a LAND_HOLDER requirement, regardless of what the trigger for that requirement is, will be added if another eligible starting position is REPLACED_BY it. **A non-LAND_HOLDER position that is REPLACED_BY a LAND_HOLDER position will never appear.** With this list compiled, the game culls all positions that are REPLACED_BY another eligible position, and then culls all positions that have the APPOINTED_BY token. **You may not embark with any appointed positions.** Any remaining positions are then filled by a dwarf chosen at random.

**Positions do not automatically appear when you reach their requirements.** For example, if you remove the ELECTED token from the Mayor, then the Mayor will never appear, even once you reach their required number of dwarves. **For a position that does not appear at embark to appear in your fortress, it must be APPOINTED_BY another position or ELECTED.**

Naturally, this is more complicated than it looks. **APPOINTED_BY positions must be appointed by another position already in your fortress, or a civ-level position. Only LAND_HOLDER positions may be appointed by civ-level positions.** LAND_HOLDER positions that are APPOINTED_BY civ-level positions are inherently tied to civ-level tokens with the ESTABLISH_COLONY_TRADE_AGREEMENTS responsibility. If a fortress meets the LAND_HOLDER_TRIGGER for a new LAND_HOLDER tier when a caravan leaves, then the next time the outpost liaison or equivalent arrives, they will offer to make you an official colony, which will allow you to select all positions for that LAND_HOLDER level. **Each time they appear, the outpost liaison will only promote your fortress one tier up the LAND_HOLDER track.** The biggest problem with this system is that you may set your LAND_HOLDER_TRIGGERS such that you are eligible for the first tier of LAND_HOLDER positions at embark. **If you are eligible for the first tier of LAND_HOLDER positions at embark, then all first-tier positions will appear twice - once at embark, and again when the outpost liaison comes to appoint you to the first tier.**

If civ-positions are neither APPOINTED_BY nor ELECTED, they still will be filled.
