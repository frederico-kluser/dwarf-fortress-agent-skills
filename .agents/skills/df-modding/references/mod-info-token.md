# Mod info token

> Fonte: [Mod info token](https://dwarffortresswiki.org/index.php/Mod_info_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\

**Mod info tokens** are used in a mod's info.txt file.

## Info.txt Tokens

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Usage | Description |
|  ID | id | Required | The ID of the mod. This should be unique, with no two mods sharing the same ID. IDs starting with "vanilla\_" are reserved for vanilla raws. |
|  NUMERIC_VERSION | integer | Required | An **integer** version number for the mod. Must be greater than or equal to EARLIEST_COMPATIBLE_NUMERIC_VERSION. "Integer" here means 0, 1, 2, and so on. Negatives are allowed. Anything that is not an integer will not work; 0.2 will be read as "0". |
|  DISPLAYED_VERSION | string | Required | The version of the mod, as displayed in-game. This is only a display, and will have no effect. |
|  EARLIEST_COMPATIBLE_NUMERIC_VERSION | integer | Required | The earliest compatible numeric version of the mod. Installed mods are automatically updated, if a later compatible version is available. **This must be at most the same as NUMERIC_VERSION, and doing otherwise will result in an error.** |
|  EARLIEST_COMPATIBLE_DISPLAYED_VERSION | string | Required | The earliest compatible numeric version, as displayed in-game. |
|  AUTHOR | string | Required\[Verify\] | The name of the author (usually you). |
|  NAME | string | Required\[Verify\] | The name of the mod. |
|  DESCRIPTION | string |  | A description of the mod, shown in the mod loading screen. |
|  REQUIRES_ID | string |  | Mod cannot be used unless mod with given ID is also loaded. |
|  REQUIRES_ID_BEFORE_ME | string |  | Mod cannot be used unless mod with given ID is earlier in the mod load list. |
|  REQUIRES_ID_AFTER_ME | string |  | Mod cannot be used unless mod with given ID is later in the mod load list. |
|  CONFLICTS_WITH_ID | string |  | Mod cannot be used if mod with given ID is also loaded. |

\

## Steam Workshop tokens

These tokens are required for the mod to function properly on Steam Workshop.

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Token | Type | Req? | Description | Example | External Doc |
|  STEAM_TITLE | single string | Req | The title of the mod on Steam Workshop. | *\[STEAM_TITLE:Imani's Tweaks\]* | SetItemTitle |
|  STEAM_DESCRIPTION | single string |  | The description of the mod on Steam Workshop. Maximum size is 8000 bytes (about 400 words). / Will overwrite the existing description of the mod on the workshop, can be omitted to avoid this behavior. | *\[STEAM_DESCRIPTION:This is my collection of small changes and additional content.\]* | SetItemDescription |
|  STEAM_TAG | multi string |  | Any number can be used. Use a separate STEAM_TAG for each one. Each string must be under 255 chars. | *\[STEAM_TAG:ui\]\[STEAM_TAG:tweak\]* | SetItemTags |
|  STEAM_KEY_VALUE_TAG | multi string1, string2 |  | Any number can be used. |  | SetReturnKeyValueTags |
|  STEAM_METADATA | multi string |  | Sets arbitrary metadata for an item. This metadata can be returned from queries without having to download and install the actual content. Toady doesn't know what it does [1]. |  | SetItemMetadata |
|  STEAM_CHANGELOG | single string |  | A brief description of the changes made. (Optional, set to NULL for no change note). The log message is only for the version you're uploading. This should be different each time you update a mod, and only include the changes in the new version. Steam Workshop congregates all version changelogs, so a full changelog can be seen there. | Initial example: / \[STEAM_CHANGELOG:Initial release\] / Update example: / \[STEAM_CHANGELOG:Update the mod compatible with...\] |  |
|  STEAM_FILE_ID | uint64 | Req, autogen | Connects the mod to an entry on the Steam Workshop. / Generated automatically the first time you upload a mod to Workshop, / do not include it manually / . If you upload a mod with an existing STEAM_FILE_ID token, it will update the Workshop entry connected to the ID. (Presumably only if you're the original uploader of said mod.) |  |  |

\

## See Also

- Info.txt file
- Clear this page cache and reload:
