# Sphere

> Fonte: [Sphere](https://dwarffortresswiki.org/index.php/Sphere) — Dwarf Fortress Wiki (GFDL/MIT)

A **sphere** is an aspect where a being has influence. Deities, forces, angels, demons, megabeasts, semi-megabeasts, forgotten beasts and titans may be associated with one or more spheres, and civilizations may prefer certain spheres when selecting creatures to worship. There are currently a total of 130 spheres.

## Understanding spheres

A being such as a deity, demon or megabeast may come to represent or epitomize certain things like emotions, qualities, terrain types, and items, which are called "spheres". As an example from real-world mythology, the Greek goddess Athena is goddess in the "spheres" of wisdom, warfare, handicrafts and reason.

Gods and adored megabeasts can grant secrets related to their spheres. In unmodded *Dwarf Fortress*, this means that death gods can teach the secret of life and death to their worshipers, turning them into necromancers.

Dwarves and other creatures will come to worship certain "powerful beings" and, as such, will follow the "religion", and have a relationship with its "deity".

A historical figure with associated spheres that generates in the wild or as a god will be named after its spheres. The symbols associated with the sphere will be used to generate first names, compound names, and titles. If an interaction from a deity creates an artifact, then that artifact will be named using the spheres of the god who gave the blessing.

## Creatures with pre-determined spheres

While many procedurally generated creatures in *Dwarf Fortress* are given random spheres upon creation, there are others who have static spheres, which remain constant across all save files:

- Bogeyman: Misery, night, nightmares
- Bronze colossus: Metals, strength, war
- Cyclops: Light, longevity, minerals, strength, thunder
- Dragon: Fire, wealth
- Ettin: Speech, strength
- Experiment: Deformity, night
- Giant: Food, strength
- Hydra: Muck, rebirth, strength
- Minotaur: Caverns, chaos, darkness, deformity, strength
- Nightmare: Misery, night, nightmares
- Roc: Hunting, sky, wind
- Werebeast: Animals, chaos, moon, night
- Night troll: Death, Night

## Sphere tokens

According to Toady: "*Spheres have a parent/child list, a friend list, and a preclude list. A deity has either one or two base spheres, and then they pick friends of those spheres, while never choosing a precluded or parent/child sphere of any of the spheres they already have. I tried to be pretty lax with the preclude list so that interesting relationships could pop up.*"

As extracted from the string dump, the spheres available are unchanged from 40d; their relationships with each other may also be unchanged.

Creatures and inorganic materials can be assigned spheres with the \[SPHERE:\] token.

Secrets use any number of \[IS_SPHERE\] tokens to determine what spheres it is available to.

Available sphere tokens are:

[TABLE]
