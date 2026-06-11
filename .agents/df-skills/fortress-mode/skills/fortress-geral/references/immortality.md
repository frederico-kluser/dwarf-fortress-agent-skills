# Immortality

> Fonte: [Immortality](https://dwarffortresswiki.org/index.php/Immortality) — Dwarf Fortress Wiki (GFDL/MIT)

**Immortality** in *Dwarf Fortress* refers to any creature that will not die as the result of old age. Immortality can be inherent to a species, or acquired via a variety of different methods. Note that immortal creatures *can* still be killed by traditional methods.

## Inherent immortality

The following creatures are inherently immortal, and thus will never die of old age in an unmodded game:

- Elves
- Goblins
- Semi-megabeasts, like minotaurs or ettins
- Megabeasts, including dragons and hydras
- All randomized titans and forgotten beasts
- Some other fanciful creatures, like nightwings and satyrs
- Inorganic creatures, like gabbro men and amethyst men

All of these creatures lack the \[MAXAGE:#:#\] tag in their species file, granting them their immortality.

Creatures that are inherently immortal will *not* seek the secrets of life and death, as they, somewhat obviously, have no mortality to become obsessed with. For this reason, there are generally far fewer elven and goblin necromancers than human and dwarven ones.

## Acquired immortality

*Dwarf Fortress* has several methods by which a creature might acquire immortality. Each of these has accompanying effects (that may or may not be desirable), and multiple can affect the same creature. These are:

- Becoming undead, via mist. This is slightly different from other methods, and includes a non-optional hostility to all things living
- Becoming a vampire
- Becoming a werebeast
- Becoming a necromancer (learning the secrets of life and death)

These conditions each have their own limitations, which can be found on their respective pages.

## Fortress mode

Immortality, as it applies to fortress mode, is far from necessary. After all, it is a very small percentage of fortresses that last long enough for death by old age to become an issue, and your fortress will be most concerned with *removing* the undying condition of most immortals it will encounter. Still, it can be useful to acquire immortals for your fortress for one purpose or another.

The easiest method, by far, is to receive a vampire in a migrant wave. After you've successfully discerned and separated your vampire, you may now have an immortal ~~meat shield~~ watchcreature, lever puller, or super-soldier.

Another straightforward method is to acquire the secrets of life and death in book form. This can be done by retiring an adventurer with the book at your fortress, waiting for a necromancer to invade you with (hopefully) the book in their inventory, or raiding a nearby tower with your squads (original books are considered artifacts). If you have a library available, the book will be stored in it and read by your dwarves in their spare time as though it were any other book. Gradually your whole fortress will be converted into necromancers, and the process can be accelerated if you make your scribes write copies of the book.

Acquiring a werebeast for your fortress is more difficult, and less sustainable, but still with its uses. Werebeasts of the same species will not attack each other, and the condition increases your soldiers' survivability dramatically - all wounds are healed fully upon transformation. Infecting a permanently crippled dwarf may be similarly beneficial. As long as you're careful to keep the infected separate from the rest of your fortress, they can make an excellent asset.

Currently, undead are not a practical choice due to their unending hatred of the living. However, necromancers from within your civilization can and will immigrate to your fortress.

## Adventurer mode

Acquiring immortality in adventurer mode is a more straightforward task than in fortress mode, and can ensure your character's survival in legends long beyond their \[MAXAGE:#:#\].

- To acquire vampirism, one simply needs to drink the blood of a (preferably recently-deceased) vampire, or topple a statue in a temple to be cursed by the gods with vampirism, though the latter has an equal chance of turning you into a werebeast, instead.
- To become a necromancer, you must steal and read something containing the "secrets of life and death" from a necromancer's tower. Their slab is a guarantee, but there's probably books with the secrets lying around as well. You need at least Novice reader skill.
- To become a werebeast, one must be bitten by said werebeast. The bite must come into contact with your flesh and you won't turn on the night you were infected. Toppling a statue in a temple may also curse you into a werebeast, though it may turn you into a vampire instead.
- To become a mist zombie/husk/thrall (same thing), you must walk into a cloud of contaminating fog/dust/mist that induces huskification. Probably wise to expose a companion to a cloud first in order to make sure it doesn't give you something else.

It is very much worth noting that these can stack in several ways. One can be both a vampire and necromancer, or werebeast and necromancer, but *not* both a vampire and werebeast. Finally, a vampire, werebeast, necromancer, or acceptable combination thereof can become a mist zombie, *but* a mist zombie cannot become a vampire or werebeast.

## DFHack

You can make any creature immortal without the downside of any of the above-listed creatures.

To do this, you must go to the creature's profile while in the game, then in DFHack run . Return to the game, you will find yourself in a menu called "GameMaster's editor". Use until you find and , replace existent values on these two options with -1 by using . After the changes are made, press to return to the game.

You can also use this method to see when it is likely the creature will die of old age even if you don't intend to change the values.

This method works as far back as v0.34.

## Notes

- Somewhat counterintuitively, ghosts of deceased dwarves can grow up (if they were a 'ghostly' child) and die of old age, and thus are not immortal.
