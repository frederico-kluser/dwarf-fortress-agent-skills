# Body token

> Fonte: [Body token](https://dwarffortresswiki.org/index.php/Body_token) — Dwarf Fortress Wiki (GFDL/MIT)

**Body tokens** are one of the fundamental parts of creatures, and determine their bodily structure. There are two major types of body tokens: *body templates* (BODY) and *body parts* (BP).

A creature uses the creature token to list all of the body templates it includes. Each part listed in each template is then included in the creature. In other words: a creature lists the *body templates* it is made of. Each *body template* contains a set of *body parts*. Each *body part* specifies which other body part it is attached to.

Body parts can connect specifically to another body part, or generally to any body part of a certain category. These connections are handled by the CON and CONTYPE body part tokens respectively.

Body parts can be renamed with a bodygloss, allowing someone to reuse an existing template instead of defining a similar template with only the names of the body parts changed.

[TABLE]
