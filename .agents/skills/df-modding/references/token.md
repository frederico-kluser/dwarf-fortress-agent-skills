# Token

> Fonte: [Token](https://dwarffortresswiki.org/index.php/Token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
In *Dwarf Fortress*, a **token** is a piece of text that defines the properties of an object. An "object" could be a material, a type of tissue, an organ, a piece of armor, a creature, a biome, a civilization, or anything else in the game; a "property" could be how large something is, what it is made from, its melting temperature, its name, its biome preference (for civilizations) or anything else that makes it unique. All information associated with the properties of an object in the game is defined using tokens. Tokens are used in the raws, which can be easily modified, allowing users to create (and distribute) new content.

- Audio tokens define audio metadata, and the triggers to play music and sound.
- Biome tokens reference environments for creatures, plants and entities.
- Building tokens define buildings.
- Body tokens determine bodily structure and materials.
  - Bodygloss tokens perform a single-word substitution of a creature's body parts.
- Body detail plan tokens define some details of a body, similar to body tokens.
- Creature tokens determine the properties of creatures, while Creature variation tokens are used to modify creatures.
- Descriptor color tokens - not to be confused with color schemes - define colors used in text-based descriptions, while Descriptor pattern tokens define color patterns, and Descriptor shape tokens define shapes.
- Entity tokens define entities, or civilizations.
  - Position tokens define noble titles and administrative positions in entities.
- Graphics tokens define tile-based graphics.
- Item tokens reference the most basic form of items (made specific by material tokens). Item tokens are mainly used in reactions.
- Item definition tokens are used to define various types of item.
  - Ammo tokens define ammunition, such as arrows and bolts.
  - Armor tokens define armor.
  - Instrument tokens define instruments.
  - Trap component tokens define weapons used in traps.
  - Tool tokens define tools, similar to weapon tokens.
  - Weapon tokens define weapons.
- Interaction tokens define interactions.
- Labor tokens reference labors.
- Language tokens define a language's vocabulary. Since fictional languages in *Dwarf Fortress* are currently only used in names, language tokens do not define grammar.
- Material tokens are used to refer to materials, similar to item tokens.
- Material definition tokens are used to define materials that appear in a number of object types.
  - Inorganic material definition tokens are specific to defining inorganic materials.
- Plant tokens define plants.
- Reaction tokens define crafting recipes.
- Skill tokens reference skills.
- Speech files define strings used for certain lines of dialog and book titles.
- Syndrome tokens define syndromes (ie: conditions, diseases, bonuses and maluses).
- Tissue definition tokens define tissues.
- Unit type tokens reference by tilesets and entities, for purposes of professions and the like.
- World tokens are used in advanced world generation.

Also note the `[LOG_CURRENT_ENTRY]` token, available for all object types. For information regarding use, see Modding#Modifying the vanilla objects.

## See also

- Raw file
- Modding
- Lua scripting
