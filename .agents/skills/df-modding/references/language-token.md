# Language token

> Fonte: [Language token](https://dwarffortresswiki.org/index.php/Language_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Language tokens** can be used to adjust existing languages or create a whole new language. Vanilla language definitions can be found in `\data\vanilla\vanilla_languages\` within the language\_\*.txt raw files. Each token is permitted in a specific context.

Note: All language raw files use Code Page 437 encoding, and you should make sure you are editing these files in that format. As many text editors default to UTF-8, some characters with diacritical marks may fail to show properly. Saving one of the default language raw files in this state will overwrite these characters with the Unicode question mark, which will corrupt the file. To fix this, replace the file with a clean one downloaded from the distributed version of DF.

Urist asks...
I want to create a language for my custom civilization. Are there any programs built to support the in-game dictionary?

You can generate a language with / DFLang / from a list of sample words. / You will need to update DFLang's copy of / language_words.txt / with the most recent version ( / mirrored here / ), as new words have been added since the last program release. / If you use accent marks or special characters, make sure to save your input file with Code Page 437 encoding. / LangCreate / is a more limited alternative, but can generate from a smaller sample.

## WORD

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NOUN | singular / plural | Begins defining a noun usage of a word. |
|  ADJ | adjective | Begins defining an adjective usage of a word. |
|  PREFIX | prefix | Begins defining a prefix usage of a word. |
|  VERB | present first person / present third person / preterite / past participle / present participle | Defines a verb usage of a word. |
|  ADJ_DIST | number 1-7 | Determines what order the adjective being defined comes in when in a string of multiple adjectives. |
|  THE_NOUN_SING |  | Lets the singular noun form of the word be used after "the" ("The X of Y", where X is the word with the tag). |
|  THE_NOUN_PLUR |  | As above, but with plural ("The Xs of Y"). |
|  THE_COMPOUND_NOUN_SING |  | Lets the singular noun form of the word be used as part of a compound noun after "the" ("The Z-X of Y"). |
|  THE_COMPOUND_NOUN_PLUR |  | As above, but with plural ("The Z-Xs of Y"). |
|  THE_COMPOUND_ADJ |  | Lets the adjective form of the word be used as part of a compound noun after "the" ("The Z-X of Y"). |
|  OF_NOUN_SING |  | Lets the singular noun form of the word be used after "of" ("The Y of X"). |
|  OF_NOUN_PLUR |  | As above, but with plural ("The Y of Xs"). |
|  FRONT_COMPOUND_NOUN_SING |  | Lets the singular noun form of the word be used at the front of a compound noun ("XY", as in surnames). |
|  FRONT_COMPOUND_NOUN_PLUR |  | As above, but with plural. |
|  REAR_COMPOUND_NOUN_SING |  | Lets the singular noun form of the word be used at the rear of a compound noun ("YX", as in surnames). |
|  REAR_COMPOUND_NOUN_PLUR |  | As above, but with plural. |
|  FRONT_COMPOUND_ADJ |  | Lets the adjective form of the word be used at the front of a compound noun. |
|  REAR_COMPOUND_ADJ |  | As above, but at the rear instead. |
|  FRONT_COMPOUND_PREFIX |  | Allows the prefix form to be appended as a prefix to a compound noun. |
|  THE_COMPOUND_PREFIX |  | Allows the prefix form to be appended as a prefix to a compound noun following "the". |
|  STANDARD_VERB |  | Allows the verb to be used in a compound noun and for its participles to be used as adjectives. |

## SYMBOL

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  S_WORD | WORD | Specifies the given WORD (defined in \#REDIRECT language_words.txt) as belonging to the symbol being defined. A given word can belong to multiple symbols. |

## TRANSLATION

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  T_WORD | WORD / translation | Specifies a translation from a given WORD (defined in language_words.txt) into the language being defined. |

## English instead of Dwarven language

You can hack the language files to display English in-game with this regular expression command:

**:%s/T_WORD:\\\[A-Z\_ -\]\*\\:\[^\\\]\*\\/T_WORD:\1:\L\1\]/**

A procedural version can also be found at Lua scripting#Identity language.

## See also

- 40d:Language (has expanded explanations of parts of the language system, which seems to still be the same in this version)
- Speech files
- Utilities#Language tools
- **Raws**
  - language_SYM.txt
