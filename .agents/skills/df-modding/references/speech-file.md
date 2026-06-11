# Speech file

> Fonte: [Speech file](https://dwarffortresswiki.org/index.php/Speech_file) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\
**Speech files**, also known as **text sets**, are text files that define sentences which can be spoken by people in adventure mode and phrases used to name books. Most of them are found in the `data/vanilla/vanilla_text/objects` folder, though the creature specific files can be found in `data/vanilla/vanilla_creatures/objects`. Like other raw files, mods can replace or introduce new sentences.

## List of files

|  |  |  |
|----|----|----|
| Textset ID | Uses | Example |
|  AB_SPECIFIC_HF_SEEKER |  | seek out \[CONTEXT:HIST_FIG:TRANS_NAME\] at \[CONTEXT:ABSTRACT_BUILDING:TRANS_NAME\] over in \[CONTEXT:SITE:TRANS_NAME\] |
|  ANIMAL_SLAYER |  | I have taken down \[CONTEXT:NUMBER\] \[CONTEXT:RACE:NUMBERED_NAME\] while stalking \[CONTEXT:PLACE:TRANS_NAME\]. |
|  ARCH_INFO_JUSTIFICATION |  | It is said that the \[CONTEXT:ARCH_ELEMENT\] of \[CONTEXT:ABSTRACT_BUILDING:TRANS_NAME\] \[CONTEXT:JUSTIFICATION\] \[CONTEXT:DEF_SPHERE\] for the glory of \[CONTEXT:HIST_FIG:TRANS_NAME\]. |
|  BOOK_ART | Used when naming books. | And \[ANY_PRONOUN\] Sang '\[NAME\]!' |
|  BOOK_INSTRUCTION | Used when naming books. | A Course on \[NAME\] |
|  CHILD_AGE_PROCLAMATION |  | I'm \[CONTEXT:NUMBER\]! |
|  CURRENT_PROFESSION_NO_YEAR |  | I am a \[CONTEXT:UNIT_NAME\]. |
|  CURRENT_PROFESSION_YEAR |  | This is my \[CONTEXT:ORDINAL\] year as a \[CONTEXT:UNIT_NAME\]. |
|  CURSE |  | Who dares to enter my house? I curse you! |
|  SLAIN_DWARF | Used when boasting about killing a dwarf. See also Creature token#SPEECH. | whose hammer shattered on the anvil of my power |
|  SLAIN_ELF | Used when boasting about killing an elf. See also Creature token#SPEECH. | whose fragile bones shattered before the power of my contempt |
|  FAMILY_RELATIONSHIP_ADDITIONAL |  | \[CONTEXT:HIST_FIG:PRO_SUB\] is also my \[CONTEXT:FAMILY_RELATIONSHIP\] |
|  FAMILY_RELATIONSHIP_ADDITIONAL_DEAD |  | \[CONTEXT:HIST_FIG:PRO_SUB\] was also my \[CONTEXT:FAMILY_RELATIONSHIP\] |
|  FAMILY_RELATIONSHIP_NO_SPEC |  | I have \[CONTEXT:INDEF_FAMILY_RELATIONSHIP\] named \[CONTEXT:HIST_FIG:TRANS_NAME\] |
|  FAMILY_RELATIONSHIP_NO_SPEC_DEAD |  | I had \[CONTEXT:INDEF_FAMILY_RELATIONSHIP\] named \[CONTEXT:HIST_FIG:TRANS_NAME\] |
|  FAMILY_RELATIONSHIP_SPEC |  | my \[CONTEXT:FAMILY_RELATIONSHIP\] is named \[CONTEXT:HIST_FIG:TRANS_NAME\] |
|  FAMILY_RELATIONSHIP_SPEC_DEAD |  | my \[CONTEXT:FAMILY_RELATIONSHIP\] was named \[CONTEXT:HIST_FIG:TRANS_NAME\] |
|  GENERAL |  | who lies dead, now only an embarrassing memory |
|  GOODBYE_WORSHIP_1 |  | upon arising in the mornings, |
|  GOODBYE_WORSHIP_2 |  | always remember to |
|  GOODBYE_WORSHIP_3 |  | speak the praises of \[SPEAKER:HF_LINK:DEITY:RANDOM_DEF_SPHERE\] |
|  GREET | Used when greeting another person. | Greetings. My name is \[SPEAKER:TRANS_NAME\]. |
|  GREET_BABY | Used when greeting a baby. | A baby! How adorable! |
|  GREET_REPLY | Used when replying to another person's greeting. | Ah, hello. I'm \[SPEAKER:TRANS_NAME\]. |
|  GREET_REPLY_AFTER_HERO | Used by NPCs when replying to the player character's greeting after becoming a hero. | I am \[SPEAKER:TRANS_NAME\]. How can I be of service? |
|  GREET_REPLY_DIFF_LANGUAGE | Used when replying to the greeting of a person who is of another race. | Hello, \[AUDIENCE:RACE\]. I am \[SPEAKER:TRANS_NAME\]. |
|  GREET_REPLY_UNUSUAL_FIRST | Used when replying to the greeting of a person whose first name is unusual.\[Verify\] | You know, you don't meet many people with the name \[AUDIENCE:FIRST_NAME\] |
|  GREET_WORSHIP | Used for greetings by priests and faithful people.\[Verify\] | This servant of \[SPEAKER:HF_LINK:DEITY:TRANS_NAME\] greets you. |
|  GUARD_PROFESSION | Used by guards when you ask them about their profession. See also soldier_profession. | I am a guard. |
|  GUARD_WARNING |  | Don't start any trouble. |
|  HIST_FIG_SLAYER |  | It is I that felled \[CONTEXT:HIST_FIG:TRANS_NAME\] the \[CONTEXT:HIST_FIG:RACE\]. |
|  HUNTING_PROFESSION |  | I hunt great beasts in \[CONTEXT:PLACE:TRANS_NAME\]. |
|  HUNTING_PROFESSION_YEAR |  | I have hunted great beasts in \[CONTEXT:PLACE:TRANS_NAME\] for \[CONTEXT:NUMBER\] of my years. |
|  JUSTIFICATION_ANTITHETICAL |  | can be thought of as the antithesis of |
|  JUSTIFICATION_EXPERIENCE |  | can allow one to experience |
|  JUSTIFICATION_PROXIMITY |  | can bring one near to |
|  JUSTIFICATION_REMINDER |  | can remind one of |
|  JUSTIFICATION_REPRESENTATION |  | can be thought of as a representation of |
|  LAIR_HUNTER_MINOTAUR | Used by minotaurs while hunting adventures in their lairs. See also Creature token#LAIR_HUNTER_SPEECH. | I'll eat you whole! |
|  MERCENARY_PROFESSION |  | I seek fortune and glory by offering my skill at arms in \[CONTEXT:PLACE:TRANS_NAME\]. |
|  MERCENARY_PROFESSION_YEAR |  | I have sought fortune and glory by offering my skill at arms in \[CONTEXT:PLACE:TRANS_NAME\] for \[CONTEXT:NUMBER\] of my years. |
|  NO_FAMILY | Used by NPCs when you ask them about their family, but they don't have any. | I have no family to speak of. |
|  PAST_HUNTING_PROFESSION |  | In the past, I hunted great beasts. |
|  PAST_MERCENARY_PROFESSION |  | In the past, I sought fortune and glory by offering my skill at arms. |
|  PAST_PROFESSION_NO_YEAR |  | I was once a \[CONTEXT:UNIT_NAME\]. |
|  PAST_PROFESSION_YEAR |  | I was a \[CONTEXT:UNIT_NAME\] for \[CONTEXT:NUMBER\] of the years of my life. |
|  PAST_SNATCHER_PROFESSION |  | Once it was my calling to rescue lost children. |
|  PAST_THIEF_PROFESSION |  | I once sought great treasures. |
|  PAST_WANDERING_PROFESSION |  | I once wandered the wilds. |
|  POSITIVE | Used to express positive feelings. | wonderful! / fantastic! / very good |
|  SAME_SITE_AB_SPECIFIC_HF_SEEKER |  | seek out \[CONTEXT:HIST_FIG:TRANS_NAME\] here in \[CONTEXT:SITE:TRANS_NAME\] at \[CONTEXT:ABSTRACT_BUILDING:TRANS_NAME\] |
|  SAME_SITE_SPECIFIC_HF_SEEKER |  | seek out \[CONTEXT:HIST_FIG:TRANS_NAME\] here in \[CONTEXT:SITE:TRANS_NAME\] |
|  SITE_SPECIFIC_HF_SEEKER |  | seek out \[CONTEXT:HIST_FIG:TRANS_NAME\] over in \[CONTEXT:SITE:TRANS_NAME\] |
|  SLAYER |  | bane / death / nemesis / vanquisher |
|  SNATCHER_PROFESSION |  | I rescue lost children and bring them back to \[CONTEXT:PLACE:TRANS_NAME\]. |
|  SNATCHER_PROFESSION_YEAR |  | For \[CONTEXT:NUMBER\] of my years, I have been rescuing lost children and bringing them back to \[CONTEXT:PLACE:TRANS_NAME\]. |
|  SOLDIER_PROFESSION | Used by soldiers when you ask them about their profession. See also guard_profession. | I am a soldier. |
|  TASK_RECOMMENDATION |  | \[CONTEXT:ANY:TRANS_NAME\] might have a task for you |
|  TEMPLE_ALREADY_MEMBER |  | your task is simple; / all you need is to |
|  TEMPLE_BECOME_MEMBER |  | Welcome to \[CONTEXT:ENTITY:TRANS_NAME\]. Praise be to \[CONTEXT:ENTITY:WORSHIP_HF:TRANS_NAME\]! / As a member of \[CONTEXT:ENTITY:TRANS_NAME\], you can now seek the higher mysteries of \[CONTEXT:ENTITY:WORSHIP_HF:TRANS_NAME\]. |
|  THIEF_PROFESSION |  | I seek treasures and bring them back to \[CONTEXT:PLACE:TRANS_NAME\]. |
|  THIEF_PROFESSION_YEAR |  | I seek treasures and bring them back to \[CONTEXT:PLACE:TRANS_NAME\] and have done so for \[CONTEXT:NUMBER\] of the years of my life. |
|  THREAT | Used by NPC bandits\[Verify\] before attacking you. | Prepare to die! |
|  UNKNOWN_HF_SEEKER |  | seek out \[CONTEXT:HIST_FIG:TRANS_NAME\], wherever \[CONTEXT:HIST_FIG:PRO_SUB\] might be |
|  WANDERING_PROFESSION |  | I wander \[CONTEXT:PLACE:TRANS_NAME\]. |
|  WANDERING_PROFESSION_YEAR |  | I have wandered \[CONTEXT:PLACE:TRANS_NAME\] for \[CONTEXT:NUMBER\] of my years. |

## Adding custom files

New speech tokens can be added with mods. It is also possible to add new files and associate them with custom creatures.

|  |  |
|----|----|
| Token | Example uses |
| SLAIN_CASTE_SPEECH | Replaces CASTE_SPEECH, SPEECH_FEMALE, and SPEECH_MALE from older versions. |
| LAIR_HUNTER_SPEECH | Minotaur (lair_hunter_minotaur.txt) |
| SPEECH | Dwarf (text_dwarf.txt), Elf (text_elf.txt) |

Creature tokens

## List of Tokens

Speech files can contain tokens in square brackets (`[]`), which are replaced with context-specific strings before the speech is displayed.

### Book title tokens

These tokens are used for book titles and specific examples of performances such as songs, poems, or dances. It is unknown if the generating tokens can be used in other text sets to generate random words.

|  |  |  |
|----|----|----|
| Token | Meaning | Example |
|  NAME | Inserts a name relevant to the book's topic, or a random noun for art and star charts. Notably, these may or may not be plural and/or have an article. | The Tower "Tower (necromancy)"), The Tree, Bronzemurder, Likot Ubendeb, Animal Behaviours |
|  NO_ART_NAME | "No article name." As NAME, but never has an article. | Tower, Tree, Bronzemurder, Likot Ubendeb, Animal Behaviours |
|  NOUN | A random noun pulled from language_words.txt or a hardcoded list. May or may not be plural. | Despair, Roots, Scrolls, Wheel-and-axles |
|  ADJ | A random adjective from language_words.txt. | Boyish, Inky, Angry, Bronzed |
|  ANY_AGE | References an age that has occurred in the world's history. | The Age Of Legends, The Age Of Hill Titan and Dragon |
|  ANY_PRONOUN | Chosen from among singular and plural subject pronouns (not "Us" or "Them"). | He, She, We, They |
|  PHRASE | A random phrase of a noun/pronoun, a verb, and some other words. | The Fool Laughs, The Day Can Say It In The End, It Foretells Afterwards, The Day Mourns |

### Dialogue tokens

Character dialogue uses its own set of tokens to reference data. Scopes identify participants in a conversation and various forms of background information. They can be nested within each other in various cases. If the scopes refer to a historical object, it is expected \[verify\] that not using the TRANS_NAME argument will display the untranslated name. Strings are the arguments for scopes, outputting a specific word based on the conversation data. In certain files, they are used by themselves with an implied scope.

|  |  |  |
|----|----|----|
| Token | Type | Meaning |
|  SPEAKER | base scope | The person speaking the dialogue. |
|  AUDIENCE | base scope | The person receiving the dialogue. Has buggy behavior without a defined audience, such as when shouting out to everyone. |
|  CONTEXT | base scope | Holds additional information depending on the subject of conversation. Must use HIST_FIG as its argument to retrieve personal info from a creature that isn't present. |
|  HIST_FIG | scope | Usually written as \[CONTEXT:HIST_FIG\], this refers to a historical figure referenced by the speaker. |
|  PLACE | scope | A location, such as a biome. |
|  SITE | scope | A site given by the context. |
|  HF_LINK | scope | Looks for historical figures associated with the scope. |
|  DEITY | scope | An argument for \[HF_LINK\], in this case referring to a (presumably, devoutly worshipped) deity. |
|  TRANS_NAME | string | The full translated name of the referenced object. |
|  FIRST_NAME | string | The first name of the referenced creature. |
|  PRO_SUB | string | The referenced creature's subject pronoun (she, he, it). |
|  PRO_OBJ | string | The referenced creature's object pronoun (her, him, it). |
|  PRO_POS | string | The referenced creature's possessive pronoun (her, his, its). |
|  ABSTRACT_BUILDING | string | The first name of the referenced creature. |
|  RACE | string | The name of the context's species. |
|  NUMBER | string | A number (expressed as plain text rather than numerals?). |
|  ORDINAL | string | An ordinal number, such as first or second. |
|  UNIT_NAME | string | The unit type of the referenced creature. |
|  ARCH_ELEMENT | string | An architectural element given by the context. |
|  ABSTRACT_BUILDING | string | A named building given by the context. |
|  JUSTIFICATION | string | A justification chosen by the context. |
|  DEF_SPHERE | string | A divine sphere chosen by the context. |
|  RANDOM_DEF_SPHERE | string | A random sphere associated with the scope. |
|  FAMILY_RELATIONSHIP | string | The relationship given by the context. |

### Context tokens

These give special information about the background of the conversation.

|  |  |  |
|----|----|----|
| Token | Meaning | Example |
| \[CONTEXT:ABSTRACT_BUILDING\] | building | ab_specific_hf_seeker / : the building in which the historical figure that the speaker wants you to seek is |
| \[CONTEXT:HIST_FIG\] | creature | ab_specific_hf_seeker / : the historical figure the speaker wants you to seek |
| \[CONTEXT:NUMBER\] | number | animal_slayer / : number of animals slain / child_age_proclamation / : age in years of the child |
| \[CONTEXT:ORDINAL\] | number | current_profession_year / : the number of years the speaker has had their profession |
| \[CONTEXT:PLACE\] | site | animal_slayer / : the place where the speaker slew the animals |
| \[CONTEXT:RACE\] | race | animal_slayer / : the race of the animals the speaker has slain |
| \[CONTEXT:SITE\] | site | ab_specific_hf_seeker / : the site where the historical figure the speaker wants you to seek is |
| \[CONTEXT:UNIT_NAME\] | text | current_profession_no_year / : the name of the speaker's profession |

## See also

- Speech mods
