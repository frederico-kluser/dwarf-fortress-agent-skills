# Language token

> Fonte: [Language token](https://dwarffortresswiki.org/index.php/Language_token) — Dwarf Fortress Wiki (GFDL/MIT)

**Language tokens** can be used to adjust existing languages or create a whole new languages. Vanilla language definitions can be found in ```\data\vanilla\vanilla_languages\` within the language\_\*.txt raw files. Each token is permitted in a specific context.

Note: All language raw files use Codepage 437 encoding, and you should make sure you are editing these files in that format. As many text editors default to UTF-8, some characters with diacritical marks may fail to show properly. Saving one of the default language raw files in this state will overwrite these characters with the unicode question mark, which will corrupt the file. To fix this replace the file with a clean one downloaded from the distributed version of DF.

## WORD

[TABLE]

## SYMBOL

[TABLE]

## TRANSLATION

[TABLE]

## English instead of dwarven language

You can hack the language files to display english in-game with this regular expression command:

**:%s/T_WORD:\\\[A-Z\_ -\]\*\\:\[^\\\]\*\\/T_WORD:\1:\L\1\]/**

## See also

- 40d:Language (has expanded explanations of parts of the language system, which seems to still be the same in this version)
- Speech files
- **Raws**
  - language_SYM.txt

\]\]
