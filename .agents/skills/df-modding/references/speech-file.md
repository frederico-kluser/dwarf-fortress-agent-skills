# Speech file

> Fonte: [Speech file](https://dwarffortresswiki.org/index.php/Speech_file) — Dwarf Fortress Wiki (GFDL/MIT)

**Speech files**, also known as **text sets**, are text files that define sentences which can be spoken by people in adventure mode and phrases used to name books. Most of them are found in the `data/vanilla/vanilla_text/objects` folder, though the creature specific files can be found in `data/vanilla/vanilla_creatures/objects`. Like other raw files, mods can replace or introduce new sentences.

## List of files

[TABLE]

## Adding custom files

New speech tokens can be added with mods. It is also possible to add new files and associate them with custom creatures.

| Token | Example uses |
|----|----|
| SLAIN_CASTE_SPEECH | Replaces CASTE_SPEECH, SPEECH_FEMALE, and SPEECH_MALE from older versions. |
| LAIR_HUNTER_SPEECH | Minotaur (lair_hunter_minotaur.txt) |
| SPEECH | Dwarf (text_dwarf.txt), Elf (text_elf.txt) |

Creature tokens

## List of Tokens

Speech files can contain tokens in square brackets (`[]`), which are replaced with context-specific strings before the speech is displayed.

### Book title tokens

These tokens are used for book titles and specific examples of performances such as songs, poems, or dances. It is unknown if the generating tokens can be used in other text sets to generate random words.

[TABLE]

### Dialogue tokens

Character dialogue uses its own set of tokens to reference data. Scopes identify participants in a conversation and various forms of background information. They can be nested within each other in various cases. If the scopes refer to a historical object, it is expected \[verify\] that not using the TRANS_NAME argument will display the untranslated name. Strings are the arguments for scopes, outputting a specific word based on the conversation data. In certain files, they are used by themselves with an implied scope.

[TABLE]

### Context tokens

These give special information about the background of the conversation.

[TABLE]

## See also

- Speech mods

\]\] \]\]
