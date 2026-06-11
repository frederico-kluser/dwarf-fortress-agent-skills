# Creature token

> Fonte: [Creature token](https://dwarffortresswiki.org/index.php/Creature_token) — Dwarf Fortress Wiki (GFDL/MIT)

The `[OBJECT:CREATURE]` token begins the definition of a *Dwarf Fortress* creature raw file. Each creature definition that follows begins with the token, and the creature's exact properties and behavior are then specified by the use of further creature tokens. All known creature tokens are listed below.

Vanilla creature definitions can be found in ```\data\vanilla\vanilla_creatures\`. Creature ID is also used with graphics tokens to make customizable graphics sets.

The caste tokens allow defining sub-species within the broader creature definition, including true biological castes and lesser variations, such as sexes. Creature tokens can either be 'Creature' or 'CASTE-only' type which can only be applied to creature or cast respectively, or 'CASTE' which can be applied to both. In the table bellow, creature type distinguish tokens that can be applied to creature only, cast only and both ('creature', 'CASTE-only', and 'CASTE' respectively)

## A

[TABLE]

## B

[TABLE]

## C

[TABLE]

## D

[TABLE]

## E

[TABLE]

## F

[TABLE]

## G

[TABLE]

## H

[TABLE]

## I

[TABLE]

## L

[TABLE]

## M

[TABLE]

## N

[TABLE]

## O

[TABLE]

## P

[TABLE]

## R

[TABLE]

## S

[TABLE]

## T

[TABLE]

## U

[TABLE]

## V

[TABLE]

## W

[TABLE]

## Attack Tokens

Attacks can use four different part selection criteria; while all vanilla attacks use only BODYPART (e.g. ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP), there are other options available.

[TABLE]

[TABLE]

## Tissue Layer Tokens

Tissue layers are added to a creature's body parts by the creature tokens TISSUE_LAYER, TISSUE_LAYER_OVER, TISSUE_LAYER_UNDER, and the body detail plan token TL_LAYERS.

These tissue layers are not the same thing as tissues, which are defined at creature level, but rather applications of the tissues. If the SKIN tissue of a creature is the more general and abstract notion of what skin is for that creature, then a tissue layer may be the "actual" skin on the creature's nose, head, or second toe. As most creatures have more than one body part, tissue layers are normally selected en masse.

Some tissue layer tokens are analogous to tissue definition tokens, e.g. TL_CONNECTS to CONNECTS.

[TABLE]

## See Also

- Body detail plan token
- Body token
- Material definition token
- Syndrome
- Tissue definition token
- Creature examples
