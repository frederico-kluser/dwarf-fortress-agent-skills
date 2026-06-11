# Graphic set

> Fonte: [Graphic set](https://dwarffortresswiki.org/index.php/Graphic_set) — Dwarf Fortress Wiki (GFDL/MIT)

A **graphic set** is an additional custom tileset intended for creatures. While this is eventually planned for all objects in game, only creatures can currently be assigned to graphic sets. Graphic sets are placed in (as well as the raw folder of each save); a corresponding text file assigns tiles to objects.

## Documentation

### Location and size

The text files are placed directly in the folder while the graphic sets themselves should be in subfolders. Graphic sets don't need to have the same tile size as the main tileset, they will be resized automatically to match it. As the automatic resizing algorithm might introduce artifacts or unintended aliasing to your art, it is recommended to draw them in the intended dimension from the beginning. The number of tiles and their spatial arrangement doesn't matter; see Notes for details.

### Possible graphics

*You can find a detailed list below.*

All creatures can have separate graphics assigned to their adult and child states, undead, and their -men and giant variants. In addition, the major civilizations can have separate graphics for all professions (such as miner, mason, caravan guard, and ghost). You can assign one graphic to several creatures/states, and you can set each tile to either be displayed as it appears or let the game color them. Vermin and different genders cannot have separate graphics assigned to them.

### Text file syntax

A graphic set needs a text file that tells the game which tile is used for which creature. You can use separate text files for each graphic set, or a single one for several. Each text file consists of a header, one or more graphic set definitions (called "") and several creature graphics entries, each of which has subentries for professions.

The structure of a typical text file would look like this:

- Header
- Tile page definition
  - Creature graphic entry
    - profession subentry
    - more
    - profession
    - subentries
  - next creature
    - with
    - more
    - professions
- new tile page definition
  - a creature
    - with adult
    - and child graphics
  - and another creature
    - adult
    - child

Below is an example of such a file:

`graphics_mygraphics ← `**`The first line of the header. You'll be saving the text document as this name (graphics_mygraphics.txt)`\
`This name should match the folder name you will be using in "raw/graphics".`**\
` [OBJECT:GRAPHICS] `\
**`This concludes the header. Each graphic set text file needs to contain these lines.`**\
`------------------------------`\
`below are dwarves ← `**`text outside brackets gets ignored. You can use it for comments and organizing your file visually with lines`**` `\
` [TILE_PAGE:MYDWARVES] ← `**`Here you are defining properties of a single graphic set image.`\
`The title MYDWARVES will be used in creature graphic entries to refer to that graphic set. The title doesn't have to match any creature, folder, or image name.`**` `\
`       `[`1`` ← `**`The subfolder where the graphic set is located (relative to this text file) and its filename, including the file`\
`extension.`**\
`       [TILE_DIM:16:16] ← `**`Height:Width - Pixels per tile, so DF knows where one tile ends and another begins`**\
`       [PAGE_DIM:5:3] ← `**`Width:Height - Tiles per image and how they're arranged in rows and columns.`**` `\
`        `**`This concludes the first TILE_PAGE definition.`**` `\
`       `**`Next are the creature graphic entries. Syntax is: [Profession:TILE_PAGE:X:Y:Color:State]`**` `\
`       `**`X and Y are the coordinates of the tile on the image. More information below.`**` `\
`[CREATURE_GRAPHICS:DWARF] ← `**`The value (DWARF in this case) is the name the creature has in the raws. This NEEDS to be spelled correctly.`**\
`       [DEFAULT:MYDWARVES:0:0:`**`ADD_COLOR`**`:DEFAULT]`\
`                                  ↑ `**`The ADD_COLOR value tells DF to give the tile the same colors as the default graphic`**\
`       [STANDARD:MYDWARVES:1:0:`**`AS_IS`**`:DEFAULT]`\
`                                  ↑ `**`AS_IS takes the tile as it is. Most likely this is the setting you want`**\
`       [MINER:MYDWARVES:2:0:AS_IS:DEFAULT]`\
`                  ↓ `**`We defined the tile page above. it refers to the image mydwarves.png`**\
`       [CHILD:`**`MYDWARVES`**`:3:0:AS_IS:DEFAULT]`\
`       [BABY:MYDWARVES:4:0:AS_IS:DEFAULT]`\
`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\
`humans `\
` [TILE_PAGE:MYHUMANS] ← `**`The next TILE_PAGE definition. You could put that (and its creature graphic entries) in a separate text file, but it would have to contain`\
`its own header.`**\
`       `[`2`` ← `**`This file is in another subfile`**\
`       [TILE_DIM:16:16]`\
`       [PAGE_DIM:1:4] `\
` [CREATURE_GRAPHICS:HUMAN]`\
`       [DEFAULT:MYHUMANS:0:0:AS_IS:DEFAULT]    `\
`   `**`Notes can go here too.`**`        `\
`       [SWORDSMAN:MYHUMANS:0:1:AS_IS:DEFAULT]`\
`       [`**`RECRUIT`**`:MYHUMANS:0:2:AS_IS:`**`ADVENTURER`**`] ← `**`An ADVENTURER with no weapons`**\
`       [`**`SWORDSMAN`**`:MYHUMANS:0:3:AS_IS:`**`ADVENTURER`**`] ← `**`An ADVENTURER with a sword`**\
`==============================`\
`animals `\
` [TILE_PAGE:MYANIMALS]`\
`       [``FILE:Other_Graphics/animals`**`.bmp`**`] ← `**`Pictures can be in .BMP format, too.`**\
`       [TILE_DIM:16:16]`\
`       [PAGE_DIM:6:2] `\
` [CREATURE_GRAPHICS:DOG]`\
`       [DEFAULT:MYANIMALS:0:0:AS_IS:DEFAULT]`\
`       [CHILD:MYANIMALS:1:0:AS_IS:DEFAULT]`\
`       [`**`TRAINED_HUNTER`**`:MYANIMALS:4:0:AS_IS:DEFAULT] ← `**`TRAINED_HUNTER profession only works with animals that have `` or ``.`**\
`       [`**`TRAINED_WAR`**`:MYANIMALS:5:0:AS_IS:DEFAULT] ← `**`TRAINED_WAR profession only works with animals that have `` or ``.`**\
`[CREATURE_GRAPHICS:CAT]`\
`       [DEFAULT:MYANIMALS:0:1:AS_IS:DEFAULT]`

### Coordinates

The value in the section defines how many columns and rows a given (graphic set) has. The first value is the x-axis ("width"), the second value the y-axis ("height"). The origin (0,0) is at the top left.

This is how the coordinates would work with the image from the example above:

|     |     |     |         |     |
|-----|-----|-----|---------|-----|
| 0:0 | 1:0 | 2:0 | **3:0** | 4:0 |
| 0:1 | 1:1 | 2:1 | 3:1     | 4:1 |
| 0:2 | 1:2 | 2:2 | 3:2     | 4:2 |

The position of the dwarven child graphic from the example above () is shown in bold.

Note that the coordinates start at 0, not 1. So, *the last column in a 5 tile wide image is at 4*, not at 5.

### Notes

The total number of tiles in a sheet cannot number more than 1024, regardless of how big (18×18) or how small (8×12) each tile is. Thus, a sheet that has its graphics organized into 22 rows and 44 columns works fine (as 22 × 44 = 968, which is less than 1024. However, a sheet that has 24 rows and 44 columns (24 × 44 = 1056) will not work.

The order of a text file is fairly flexible. You can have several TILE_PAGEs in succession and the entries of each all together, or have one TILE_PAGE followed by all of its entries, before you define the next TILE_PAGE with its entries. The only limitation is that the TILE_PAGE *must be before its entries*.

## List of professions, creatures and states

As shown in the example above, the syntax is

`[CREATURE_GRAPHICS:`**`Creature name`**`]`\
`      [`**`Profession`**`:MYHUMANS:0:0:AS_IS:`**`Texture Token`**`]`

In the following, you will find tables with valid values.

### Texture tokens

`[CREATURE_GRAPHICS:HUMAN]`\
`      [DEFAULT:MYHUMANS:0:0:AS_IS:`***`DEFAULT`***`]   `\
`      [SWORDSMAN:MYHUMANS:0:1:AS_IS:`***`DEFAULT`***`]`\
`      [RECRUIT:MYHUMANS:0:2:AS_IS:`***`ADVENTURER`***`]`

**Note that the Tokens GHOST and ANIMATED go in the *profession* spot, not the texture token as you would expect**—this means that you can't have separate graphics for miner zombies, axedwarf zombies, speardwarf zombies, etc.

[TABLE]

**Note that the Tokens GHOST and ANIMATED go in the *profession* spot, not the texture token as you would expect**—this means that you can't have separate graphics for miner zombies, axedwarf zombies, speardwarf zombies, etc.

### Professions

`[CREATURE_GRAPHICS:HUMAN]`\
`       [`***`DEFAULT`***`:MYHUMANS:0:0:AS_IS:DEFAULT]  `\
`       [`***`SWORDSMAN`***`:MYHUMANS:0:1:AS_IS:DEFAULT]`\
`       [`***`RECRUIT`***`:MYHUMANS:0:2:AS_IS:ADVENTURER]`

You can find these in as and . s are only defined under the entry for Dwarves, but all Civilizations use these definitions.

All 5 major civilizations (dwarves, elves, humans, goblins, kobolds) use at least some of these professions. Regardless, all 5 as well as animal peoples and gorlaks can have any profession available to the civilization(s) they become part of—which can be any civilization. Additionally, plump helmet men can have any profession which doesn't require talking (they cannot talk). In summary, any dwarf, elf, human, goblin, kobold, animal person, and gorlak can theoretically have any profession.

The highest skill of a creature determine which profession graphic it uses. is used when no graphic for a profession is found (not to be mistaken for the Texture token ). is used for creatures that have no professions like haulers and peasants.

Position tokens are graphics used for appointed positions in the world, like queen, baron, general, but also slave and prisoner. When a creature does have a position and a graphic exists for that position, it takes precedence over the profession graphic.

In-game titles and position tags aren't necessarily the same. For example, female elven rulers are entitled *queen* and *princess*, but their positions tags are and , respectively. While the position is called in the raws, you can specify and in your graphic set. You can also have separate graphics for a ruler's spouse, for example . It is not clear from the raws which exact position names and genders are valid. In case of doubt, you can define them all, the game will just skip them if they don't exist.

[TABLE]

[TABLE]

### Creatures

`[CREATURE_GRAPHICS:`***`HUMAN`***`]`\
`       [DEFAULT:MYHUMANS:0:0:AS_IS:DEFAULT]    `\
`       [SWORDSMAN:MYHUMANS:0:1:AS_IS:DEFAULT]`\
`       [RECRUIT:MYHUMANS:0:2:AS_IS:ADVENTURER]`

Creatures that use a raw name you might not expect, such as a space instead of an underscore, birds without prefix, and "" instead of "", are highlighted orange. Be extra careful to spell these correctly.

| Raw name | Creature name | Vermin |
|----|----|----|
| creature_amphibians |  |  |
| TOAD | toad | VERMIN |
| TOAD_MAN | toad man |  |
| GIANT_TOAD | giant toad |  |
| creature_annelids |  |  |
| WORM | worm | VERMIN |
| WORM_MAN | worm man |  |
| creature_birds |  |  |
| BIRD_BLUEJAY | blue jay | VERMIN |
| BLUEJAY_MAN | bluejay man |  |
| GIANT_BLUEJAY | giant bluejay |  |
| BIRD_CARDINAL | cardinal | VERMIN |
| CARDINAL_MAN | cardinal man |  |
| GIANT_CARDINAL | giant cardinal |  |
| BIRD_GRACKLE | grackle | VERMIN |
| GRACKLE_MAN | grackle man |  |
| GIANT_GRACKLE | giant grackle |  |
| BIRD_ORIOLE | oriole | VERMIN |
| ORIOLE_MAN | oriole man |  |
| GIANT_ORIOLE | giant oriole |  |
| BIRD_RW_BLACKBIRD | red-winged blackbird | VERMIN |
| RW_BLACKBIRD_MAN | red-winged blackbird man |  |
| GIANT_RW_BLACKBIRD | giant red-winged blackbird |  |
| BIRD_PENGUIN | penguin |  |
| BIRD_PENGUIN_LITTLE | little penguin |  |
| BIRD_PENGUIN_EMPEROR | emperor penguin |  |
| PENGUIN MAN | penguin man |  |
| BIRD_PENGUIN_GIANT | giant penguin |  |
| BIRD_FALCON_PEREGRINE | peregrine falcon |  |
| PEREGRINE FALCON MAN | peregrine falcon man |  |
| GIANT PEREGRINE FALCON | giant peregrine falcon |  |
| BIRD_KIWI | kiwi |  |
| KIWI MAN | kiwi man |  |
| BIRD_KIWI_GIANT | giant kiwi |  |
| BIRD_OSTRICH | ostrich |  |
| OSTRICH MAN | ostrich man |  |
| BIRD_OSTRICH_GIANT | giant ostrich |  |
| creature_birds_new |  |  |
| BIRD_CROW | crow | VERMIN |
| CROW_MAN | crow man |  |
| GIANT_CROW | giant crow |  |
| BIRD_RAVEN | raven |  |
| RAVEN_MAN | raven man |  |
| GIANT_RAVEN | giant raven |  |
| BIRD_CASSOWARY | cassowary |  |
| CASSOWARY_MAN | cassowary man |  |
| GIANT_CASSOWARY | giant cassowary |  |
| BIRD_KEA | kea |  |
| KEA_MAN | kea man |  |
| GIANT_KEA | giant kea |  |
| BIRD_OWL_SNOWY | snowy owl |  |
| SNOWY_OWL_MAN | snowy owl man |  |
| GIANT_SNOWY_OWL | giant snowy owl |  |
| SPARROW | sparrow | VERMIN |
| SPARROW_MAN | sparrow man |  |
| GIANT_SPARROW | giant sparrow |  |
| BIRD_STORK_WHITE | white stork |  |
| WHITE_STORK_MAN | white stork man |  |
| GIANT_WHITE_STORK | giant white stork |  |
| BIRD_LOON | loon |  |
| LOON_MAN | loon man |  |
| GIANT_LOON | giant loon |  |
| BIRD_OWL_BARN | barn owl |  |
| BARN_OWL_MAN | barn owl man |  |
| GIANT_BARN_OWL | giant barn owl |  |
| BIRD_PARAKEET | parakeet | VERMIN |
| PARAKEET_MAN | parakeet man |  |
| GIANT_PARAKEET | giant parakeet |  |
| BIRD_KAKAPO | kakapo |  |
| KAKAPO_MAN | kakapo man |  |
| GIANT_KAKAPO | giant kakapo |  |
| BIRD_PARROT_GREY | grey parrot |  |
| GREY_PARROT_MAN | grey parrot man |  |
| GIANT_GREY_PARROT | giant grey parrot |  |
| BIRD_PUFFIN | puffin |  |
| PUFFIN_MAN | puffin man |  |
| GIANT_PUFFIN | giant puffin |  |
| BIRD_SWAN | swan |  |
| SWAN_MAN | swan man |  |
| GIANT_SWAN | giant swan |  |
| BIRD_LORIKEET | lorikeet | VERMIN |
| LORIKEET_MAN | lorikeet man |  |
| GIANT_LORIKEET | giant lorikeet |  |
| BIRD_WREN | wren | VERMIN |
| WREN_MAN | wren man |  |
| GIANT_WREN | giant wren |  |
| BIRD_OSPREY | osprey |  |
| OSPREY_MAN | osprey man |  |
| GIANT_OSPREY | giant osprey |  |
| BIRD_EMU | emu |  |
| EMU_MAN | emu man |  |
| GIANT_EMU | giant emu |  |
| BIRD_COCKATIEL | cockatiel | VERMIN |
| COCKATIEL_MAN | cockatiel man |  |
| GIANT_COCKATIEL | giant cockatiel |  |
| BIRD_LOVEBIRD_PEACH-FACED | peach-faced lovebird | VERMIN |
| PEACH-FACED_LOVEBIRD_MAN | peach-faced lovebird man |  |
| GIANT_PEACH-FACED_LOVEBIRD | giant peach-faced lovebird |  |
| BIRD_MAGPIE | magpie | VERMIN |
| MAGPIE_MAN | magpie man |  |
| GIANT_MAGPIE | giant magpie |  |
| BIRD_KESTREL | kestrel |  |
| KESTREL_MAN | kestrel man |  |
| GIANT_KESTREL | giant kestrel |  |
| BIRD_ALBATROSS | albatross |  |
| ALBATROSS_MAN | albatross man |  |
| GIANT_ALBATROSS | giant albatross |  |
| BIRD_OWL_GREAT_HORNED | great horned owl |  |
| GREAT_HORNED_OWL_MAN | great horned owl man |  |
| GIANT_GREAT_HORNED_OWL | giant great horned owl |  |
| BIRD_EAGLE | eagle |  |
| EAGLE_MAN | eagle man |  |
| GIANT_EAGLE | giant eagle |  |
| BIRD_HORNBILL | hornbill |  |
| HORNBILL_MAN | hornbill man |  |
| GIANT_HORNBILL | giant hornbill |  |
| BIRD_LOVEBIRD_MASKED | masked lovebird | VERMIN |
| MASKED_LOVEBIRD_MAN | masked lovebird man |  |
| GIANT_MASKED_LOVEBIRD | giant masked lovebird |  |
| BIRD_BUSHTIT | bushtit | VERMIN |
| BUSHTIT_MAN | bushtit man |  |
| GIANT_BUSHTIT | giant bushtit |  |
| creature_bug_slug_new |  |  |
| DAMSELFLY | damselfly | VERMIN |
| DAMSELFLY_MAN | damselfly man |  |
| GIANT_DAMSELFLY | giant damselfly |  |
| MOTH | moth | VERMIN |
| MOTH_MAN | moth man |  |
| GIANT_MOTH | giant moth |  |
| GRASSHOPPER | grasshopper | VERMIN |
| GRASSHOPPER_MAN | grasshopper man |  |
| GIANT_GRASSHOPPER | giant grasshopper |  |
| BARK_SCORPION | bark scorpion | VERMIN |
| BARK_SCORPION_MAN | bark scorpion man |  |
| GIANT_BARK_SCORPION | giant bark scorpion |  |
| MANTIS | mantis | VERMIN |
| MANTIS_MAN | mantis man |  |
| GIANT_MANTIS | giant mantis |  |
| TICK | tick | VERMIN |
| TICK_MAN | tick man |  |
| GIANT_TICK | giant tick |  |
| LOUSE | louse | VERMIN |
| LOUSE_MAN | louse man |  |
| GIANT_LOUSE | giant louse |  |
| THRIPS | thrips | VERMIN |
| THRIPS_MAN | thrips man |  |
| GIANT_THRIPS | giant thrips |  |
| SLUG | slug | VERMIN |
| SLUG_MAN | slug man |  |
| GIANT_SLUG | giant slug |  |
| MOSQUITO | mosquito | VERMIN |
| MOSQUITO_MAN | mosquito man |  |
| GIANT_MOSQUITO | giant mosquito |  |
| SPIDER_JUMPING | jumping spider | VERMIN |
| JUMPING_SPIDER_MAN | jumping spider man |  |
| GIANT_JUMPING_SPIDER | giant jumping spider |  |
| TERMITE | termite | VERMIN |
| MOON_SNAIL | moon snail | VERMIN |
| MOON_SNAIL_MAN | moon snail man |  |
| GIANT_MOON_SNAIL | giant moon snail |  |
| SPIDER_BROWN_RECLUSE | brown recluse spider | VERMIN |
| BROWN_RECLUSE_SPIDER_MAN | brown recluse spider man |  |
| GIANT_BROWN_RECLUSE_SPIDER | giant brown recluse spider |  |
| SNAIL | snail | VERMIN |
| SNAIL_MAN | snail man |  |
| GIANT_SNAIL | giant snail |  |
| creature_desert_new |  |  |
| GECKO_LEOPARD | leopard gecko | VERMIN |
| LEOPARD_GECKO_MAN | leopard gecko man |  |
| GIANT_LEOPARD_GECKO | giant leopard gecko |  |
| DESERT TORTOISE | desert tortoise |  |
| DESERT_TORTOISE_MAN | desert tortoise man |  |
| GIANT_DESERT_TORTOISE | giant desert tortoise |  |
| GILA_MONSTER | gila monster |  |
| GILA_MONSTER_MAN | gila monster man |  |
| GIANT_GILA_MONSTER | giant gila monster |  |
| creature_domestic |  |  |
| DOG | dog |  |
| CAT | cat |  |
| MULE | mule |  |
| DONKEY | donkey |  |
| HORSE | horse |  |
| COW | cow |  |
| SHEEP | sheep |  |
| PIG | pig |  |
| GOAT | goat |  |
| BIRD_CHICKEN | chicken |  |
| CAVY | cavy |  |
| BIRD_DUCK | duck |  |
| WATER_BUFFALO | water buffalo |  |
| REINDEER | reindeer |  |
| BIRD_GOOSE | goose |  |
| YAK | yak |  |
| LLAMA | llama |  |
| ALPACA | alpaca |  |
| BIRD_GUINEAFOWL | guineafowl |  |
| BIRD_PEAFOWL_BLUE | blue peafowl |  |
| BIRD_TURKEY | turkey |  |
| RABBIT | rabbit |  |
| creature_equipment |  |  |
| EQUIPMENT_WAGON | wagon |  |
| creature_fanciful |  |  |
| CHIMERA | chimera |  |
| CENTAUR | centaur |  |
| GRIFFON | griffon |  |
| creature_insects |  |  |
| FLY | fly | VERMIN |
| FLY_MAN | fly man |  |
| GIANT_FLY | giant fly |  |
| ROACH_LARGE | large roach | VERMIN |
| ROACH_MAN | roach man |  |
| GIANT_ROACH | giant roach |  |
| BEETLE | beetle | VERMIN |
| BEETLE_MAN | beetle man |  |
| GIANT_BEETLE | giant beetle |  |
| ANT | ant | VERMIN |
| BUTTERFLY_MONARCH | monarch butterfly | VERMIN |
| BUTTERFLY_MONARCH_MAN | monarch butterfly man |  |
| GIANT_BUTTERFLY_MONARCH | giant monarch butterfly |  |
| FIREFLY | firefly | VERMIN |
| FIREFLY_MAN | firefly man |  |
| GIANT_FIREFLY | giant firefly |  |
| DRAGONFLY | dragonfly | VERMIN |
| DRAGONFLY_MAN | dragonfly man |  |
| GIANT_DRAGONFLY | giant dragonfly |  |
| HONEY_BEE | honey bee | VERMIN |
| BUMBLEBEE | bumblebee |  |
| creature_large_mountain |  |  |
| GOAT_MOUNTAIN | mountain goat |  |
| GOAT_MOUNTAIN_MAN | mountain goat man |  |
| GIANT_GOAT_MOUNTAIN | giant mountain goat |  |
| MARMOT_HOARY | hoary marmot |  |
| MARMOT_HOARY_MAN | hoary marmot man |  |
| GIANT_MARMOT_HOARY | giant hoary marmot |  |
| GNOME_MOUNTAIN | mountain gnome |  |
| GNOME_DARK | dark gnome |  |
| creature_large_ocean |  |  |
| WALRUS | walrus |  |
| WALRUS_MAN | walrus man |  |
| GIANT_WALRUS | giant walrus |  |
| FISH_LAMPREY_SEA | sea lamprey |  |
| SHARK_GREAT_WHITE | great white shark |  |
| SHARK_FRILL | frill shark |  |
| SHARK_SPINY_DOGFISH | spiny dogfish |  |
| SHARK_WOBBEGONG_SPOTTED | spotted wobbegong |  |
| SHARK_WHALE | whale shark |  |
| SHARK_BASKING | basking shark |  |
| SHARK_NURSE | nurse shark |  |
| SHARK_MAKO_SHORTFIN | shortfin mako shark |  |
| SHARK_MAKO_LONGFIN | longfin mako shark |  |
| SHARK_TIGER | tiger shark |  |
| SHARK_BULL | bull shark |  |
| SHARK_REEF_BLACKTIP | blacktip reef shark |  |
| SHARK_REEF_WHITETIP | whitetip reef shark |  |
| SHARK_BLUE | blue shark |  |
| SHARK_HAMMERHEAD | hammerhead shark |  |
| SHARK_ANGEL | angelshark |  |
| FISH_SKATE_COMMON | common skate |  |
| FISH_RAY_MANTA | manta ray |  |
| FISH_STINGRAY | stingray |  |
| FISH_COELACANTH | coelacanth |  |
| FISH_STURGEON | sturgeon |  |
| FISH_CONGER_EEL | conger eel |  |
| FISH_MILKFISH | milkfish |  |
| FISH_COD | cod |  |
| FISH_OPAH | opah |  |
| FISH_GROUPER_GIANT | giant grouper |  |
| FISH_BLUEFISH | bluefish |  |
| FISH_SUNFISH_OCEAN | ocean sunfish |  |
| FISH_SWORDFISH | swordfish |  |
| FISH_MARLIN | marlin |  |
| FISH_HALIBUT | halibut |  |
| FISH_BARRACUDA_GREAT | great barracuda |  |
| FISH_TUNA_BLUEFIN | bluefin tuna |  |
| NARWHAL | narwhal |  |
| NARWHAL MAN | narwhal man |  |
| NARWHAL, GIANT | giant narwhal |  |
| creature_large_riverlake |  |  |
| HIPPO | hippo |  |
| HIPPO_MAN | hippo man |  |
| GIANT_HIPPO | giant hippo |  |
| FISH_GAR_LONGNOSE | longnose gar |  |
| FISH_CARP | carp |  |
| FISH_TIGERFISH | tigerfish |  |
| FISH_PIKE | pike |  |
| PLATYPUS | platypus |  |
| PLATYPUS MAN | platypus man |  |
| PLATYPUS, GIANT | giant platypus |  |
| creature_large_temperate |  |  |
| BEAR_GRIZZLY | grizzly bear |  |
| BEAR_GRIZZLY_MAN | grizzly bear man |  |
| GIANT_BEAR_GRIZZLY | giant grizzly bear |  |
| BEAR_BLACK | black bear |  |
| BEAR_BLACK_MAN | black bear man |  |
| GIANT_BEAR_BLACK | giant black bear |  |
| DEER | deer |  |
| DEER_MAN | deer man |  |
| GIANT_DEER | giant deer |  |
| FOX | fox |  |
| FOX_MAN | fox man |  |
| GIANT_FOX | giant fox |  |
| RACCOON | raccoon |  |
| RACCOON_MAN | raccoon man |  |
| GIANT_RACCOON | giant raccoon |  |
| MACAQUE_RHESUS | rhesus macaque |  |
| MACAQUE_RHESUS_MAN | rhesus macaque man |  |
| GIANT_MACAQUE_RHESUS | giant rhesus macaque |  |
| COUGAR | cougar |  |
| COUGAR_MAN | cougar man |  |
| GIANT_COUGAR | giant cougar |  |
| WOLF | wolf |  |
| WOLF_MAN | wolf man |  |
| GIANT_WOLF | giant wolf |  |
| GROUNDHOG | groundhog |  |
| GROUNDHOG_MAN | groundhog man |  |
| GIANT_GROUNDHOG | giant groundhog |  |
| ALLIGATOR | alligator |  |
| ALLIGATOR_MAN | alligator man |  |
| GIANT_ALLIGATOR | giant alligator |  |
| BIRD_BUZZARD | buzzard |  |
| BUZZARD_MAN | buzzard man |  |
| GIANT_BUZZARD | giant buzzard |  |
| PANDA | panda |  |
| PANDA, GIGANTIC | gigantic panda |  |
| PANDA MAN | panda man |  |
| CAPYBARA | capybara |  |
| CAPYBARA, GIANT | giant capybara |  |
| CAPYBARA MAN | capybara man |  |
| BADGER | badger |  |
| BADGER MAN | badger man |  |
| BADGER, GIANT | giant badger |  |
| MOOSE | moose |  |
| MOOSE MAN | moose man |  |
| MOOSE, GIANT | giant moose |  |
| RED PANDA | red panda |  |
| RED PANDA MAN | red panda man |  |
| RED PANDA, GIANT | giant red panda |  |
| creature_large_tropical |  |  |
| ELEPHANT | elephant |  |
| ELEPHANT_MAN | elephant man |  |
| GIANT_ELEPHANT | giant elephant |  |
| WARTHOG | warthog |  |
| WARTHOG_MAN | warthog man |  |
| GIANT_WARTHOG | giant warthog |  |
| LION | lion |  |
| LION_MAN | lion man |  |
| GIANT_LION | giant lion |  |
| LEOPARD | leopard |  |
| LEOPARD_MAN | leopard man |  |
| GIANT_LEOPARD | giant leopard |  |
| JAGUAR | jaguar |  |
| JAGUAR_MAN | jaguar man |  |
| GIANT_JAGUAR | giant jaguar |  |
| TIGER | tiger |  |
| TIGER_MAN | tiger man |  |
| GIANT_TIGER | giant tiger |  |
| CHEETAH | cheetah |  |
| CHEETAH_MAN | cheetah man |  |
| GIANT_CHEETAH | giant cheetah |  |
| GAZELLE | gazelle |  |
| GAZELLE_MAN | gazelle man |  |
| GIANT_GAZELLE | giant gazelle |  |
| MANDRILL | mandrill |  |
| MANDRILL_MAN | mandrill man |  |
| GIANT_MANDRILL | giant mandrill |  |
| CHIMPANZEE | chimpanzee |  |
| BONOBO | bonobo |  |
| GORILLA | gorilla |  |
| ORANGUTAN | orangutan |  |
| GIBBON_SIAMANG | siamang |  |
| GIBBON_WHITE_HANDED | white-handed gibbon |  |
| GIBBON_BLACK_HANDED | black-handed gibbon |  |
| GIBBON_GRAY | gray gibbon |  |
| GIBBON_SILVERY | silvery gibbon |  |
| GIBBON_PILEATED | pileated gibbon |  |
| GIBBON_BILOU | bilou |  |
| GIBBON_WHITE_BROWED | white-browed gibbon |  |
| GIBBON_BLACK_CRESTED | black-crested gibbon |  |
| CAMEL_1_HUMP | one-humped camel |  |
| CAMEL_1_HUMP_MAN | one-humped camel man |  |
| GIANT_CAMEL_1_HUMP | giant one-humped camel |  |
| CAMEL_2_HUMP | two-humped camel |  |
| CAMEL_2_HUMP_MAN | two-humped camel man |  |
| GIANT_CAMEL_2_HUMP | giant two-humped camel |  |
| CROCODILE_SALTWATER | saltwater crocodile |  |
| CROCODILE_SALTWATER_MAN | saltwater crocodile man |  |
| GIANT_CROCODILE_SALTWATER | giant saltwater crocodile |  |
| BIRD_VULTURE | vulture |  |
| VULTURE_MAN | vulture man |  |
| GIANT_VULTURE | giant vulture |  |
| RHINOCEROS | rhinoceros |  |
| RHINOCEROS_MAN | rhinoceros man |  |
| GIANT_RHINOCEROS | giant rhinoceros |  |
| GIRAFFE | giraffe |  |
| GIRAFFE_MAN | giraffe man |  |
| GIANT_GIRAFFE | giant giraffe |  |
| HONEY BADGER | honey badger |  |
| HONEY BADGER MAN | honey badger man |  |
| HONEY BADGER, GIANT | giant honey badger |  |
| GIANT TORTOISE | giant tortoise |  |
| GIANT TORTOISE MAN | giant tortoise man |  |
| GIGANTIC TORTOISE | gigantic tortoise |  |
| ARMADILLO | armadillo |  |
| ARMADILLO MAN | armadillo man |  |
| ARMADILLO, GIANT | giant armadillo |  |
| creature_large_tundra |  |  |
| MUSKOX | muskox |  |
| MUSKOX_MAN | muskox man |  |
| GIANT_MUSKOX | giant muskox |  |
| ELK | elk |  |
| ELK_MAN | elk man |  |
| GIANT_ELK | giant elk |  |
| BEAR_POLAR | polar bear |  |
| BEAR_POLAR_MAN | polar bear man |  |
| GIANT_BEAR_POLAR | giant polar bear |  |
| creature_mountain_new |  |  |
| WOLVERINE | wolverine |  |
| WOLVERINE_MAN | wolverine man |  |
| GIANT_WOLVERINE | giant wolverine |  |
| CHINCHILLA | chinchilla |  |
| CHINCHILLA_MAN | chinchilla man |  |
| GIANT_CHINCHILLA | giant chinchilla |  |
| creature_next_underground |  |  |
| FLOATING_GUTS | floating guts |  |
| DRUNIAN | drunian |  |
| CREEPING_EYE | creeping eye |  |
| VORACIOUS_CAVE_CRAWLER | voracious cave crawler |  |
| BLIND_CAVE_OGRE | blind cave ogre |  |
| CAP_HOPPER | cap hopper | VERMIN |
| MAGMA_CRAB | magma crab |  |
| CRUNDLE | crundle |  |
| HUNGRY_HEAD | hungry head |  |
| FLESH_BALL | flesh ball |  |
| ELK_BIRD | elk bird |  |
| HELMET_SNAKE | helmet snake |  |
| GREEN_DEVOURER | green devourer |  |
| RUTHERER | rutherer |  |
| CREEPY_CRAWLER | creepy crawler | VERMIN |
| DRALTHA | draltha |  |
| GIANT_EARTHWORM | giant earthworm |  |
| BLOOD_MAN | blood man |  |
| BUGBAT | bugbat |  |
| MANERA | manera |  |
| MOLEMARIAN | molemarian |  |
| JABBERER | jabberer |  |
| POND_GRABBER | pond grabber |  |
| BLIND_CAVE_BEAR | blind cave bear |  |
| CAVE_DRAGON | cave dragon |  |
| REACHER | reacher |  |
| ELEMENTMAN_GABBRO | gabbro man |  |
| GORLAK | gorlak |  |
| CAVE_FLOATER | cave floater |  |
| PLUMP_HELMET_MAN | plump helmet man |  |
| CAVE_BLOB | cave blob |  |
| ELEMENTMAN_AMETHYST | amethyst man |  |
| creature_ocean_new |  |  |
| OCTOPUS | octopus |  |
| OCTOPUS_MAN | octopus man |  |
| GIANT_OCTOPUS | giant octopus |  |
| CRAB | crab |  |
| CRAB_MAN | crab man |  |
| GIANT_CRAB | giant crab |  |
| LEOPARD_SEAL | leopard seal |  |
| LEOPARD_SEAL_MAN | leopard seal man |  |
| GIANT_LEOPARD_SEAL | giant leopard seal |  |
| CUTTLEFISH | cuttlefish | VERMIN |
| CUTTLEFISH_MAN | cuttlefish man |  |
| GIANT_CUTTLEFISH | giant cuttlefish |  |
| ORCA | orca |  |
| ORCA_MAN | orca man |  |
| GIANT_ORCA | giant orca |  |
| SPONGE | sponge |  |
| SPONGE_MAN | sponge man |  |
| GIANT_SPONGE | giant sponge |  |
| HORSESHOE_CRAB | horseshoe crab |  |
| HORSESHOE_CRAB_MAN | horseshoe crab man |  |
| GIANT_HORSESHOE_CRAB | giant horseshoe crab |  |
| SPERM_WHALE | sperm whale |  |
| SPERM_WHALE_MAN | sperm whale man |  |
| GIANT_SPERM_WHALE | giant sperm whale |  |
| ELEPHANT_SEAL | elephant seal |  |
| ELEPHANT_SEAL_MAN | elephant seal man |  |
| GIANT_ELEPHANT_SEAL | giant elephant seal |  |
| HARP_SEAL | harp seal |  |
| HARP_SEAL_MAN | harp seal man |  |
| GIANT_HARP_SEAL | giant harp seal |  |
| NAUTILUS | nautilus | VERMIN |
| NAUTILUS_MAN | nautilus man |  |
| GIANT_NAUTILUS | giant nautilus |  |
| creature_other |  |  |
| FOXSQUIRREL | fox squirrel | VERMIN |
| MOGHOPPER | moghopper | VERMIN |
| RAT_DEMON | demon rat | VERMIN |
| WAMBLER_FLUFFY | fluffy wambler | VERMIN |
| LIZARD_RHINO_TWO_LEGGED | two-legged rhino lizard | VERMIN |
| WORM_KNUCKLE | knuckle worm | VERMIN |
| SPIDER_PHANTOM | phantom spider | VERMIN |
| FLY_ACORN | acorn fly | VERMIN |
| GNAT_BLOOD | blood gnat |  |
| creature_reptiles |  |  |
| LIZARD | lizard | VERMIN |
| LIZARD_MAN | lizard man |  |
| GIANT_LIZARD | giant lizard |  |
| SKINK | skink | VERMIN |
| SKINK_MAN | skink man |  |
| GIANT_SKINK | giant skink |  |
| CHAMELEON | chameleon | VERMIN |
| CHAMELEON_MAN | chameleon man |  |
| GIANT_CHAMELEON | giant chameleon |  |
| ANOLE | anole | VERMIN |
| ANOLE_MAN | anole man |  |
| GIANT_ANOLE | giant anole |  |
| IGUANA | iguana |  |
| IGUANA_MAN | iguana man |  |
| GIANT_IGUANA | giant iguana |  |
| creature_riverlakepool_new |  |  |
| RIVER OTTER | river otter |  |
| SEA OTTER | sea otter |  |
| OTTER_MAN | otter man |  |
| GIANT_OTTER | giant otter |  |
| SNAPPING TURTLE | common snapping turtle |  |
| ALLIGATOR SNAPPING TURTLE | alligator snapping turtle |  |
| SNAPPING_TURTLE_MAN | snapping turtle man |  |
| GIANT_SNAPPING_TURTLE | giant snapping turtle |  |
| BEAVER | beaver |  |
| BEAVER_MAN | beaver man |  |
| GIANT_BEAVER | giant beaver |  |
| LEECH | leech | VERMIN |
| LEECH_MAN | leech man |  |
| GIANT_LEECH | giant leech |  |
| AXOLOTL | axolotl | VERMIN |
| AXOLOTL_MAN | axolotl man |  |
| GIANT_AXOLOTL | giant axolotl |  |
| MINK | mink |  |
| MINK_MAN | mink man |  |
| GIANT_MINK | giant mink |  |
| POND_TURTLE | pond turtle | VERMIN |
| POND_TURTLE_MAN | pond turtle man |  |
| GIANT_POND_TURTLE | giant pond turtle |  |
| creature_small_mammals |  |  |
| RAT | rat | VERMIN |
| RAT_MAN | rat man |  |
| SQUIRREL_GRAY | gray squirrel | VERMIN |
| SQUIRREL_GRAY_MAN | gray squirrel man |  |
| GIANT_SQUIRREL_GRAY | giant gray squirrel |  |
| SQUIRREL_RED | red squirrel | VERMIN |
| SQUIRREL_RED_MAN | red squirrel man |  |
| GIANT_SQUIRREL_RED | giant red squirrel |  |
| CHIPMUNK | chipmunk | VERMIN |
| CHIPMUNK_MAN | chipmunk man |  |
| GIANT_CHIPMUNK | giant chipmunk |  |
| creature_small_mammal_new |  |  |
| HAMSTER | hamster | VERMIN |
| HAMSTER_MAN | hamster man |  |
| GIANT_HAMSTER | giant hamster |  |
| HEDGEHOG | hedgehog | VERMIN |
| HEDGEHOG_MAN | hedgehog man |  |
| GIANT_HEDGEHOG | giant hedgehog |  |
| SQUIRREL_FLYING | flying squirrel | VERMIN |
| FLYING_SQUIRREL_MAN | flying squirrel man |  |
| GIANT_FLYING_SQUIRREL | giant flying squirrel |  |
| creature_small_ocean |  |  |
| MUSSEL | mussel | VERMIN |
| OYSTER | oyster | VERMIN |
| FISH_SALMON | salmon | VERMIN |
| FISH_CLOWNFISH | clownfish | VERMIN |
| FISH_HAGFISH | hagfish | VERMIN |
| FISH_LAMPREY_BROOK | brook lamprey | VERMIN |
| FISH_RAY_BAT | bat ray | VERMIN |
| FISH_RAY_THORNBACK | thornback ray | VERMIN |
| FISH_RATFISH_SPOTTED | spotted ratfish | VERMIN |
| FISH_HERRING | herring | VERMIN |
| FISH_SHAD | shad | VERMIN |
| FISH_ANCHOVY | anchovy | VERMIN |
| FISH_TROUT_STEELHEAD | steelhead trout | VERMIN |
| FISH_HAKE | hake | VERMIN |
| FISH_SEAHORSE | seahorse | VERMIN |
| FISH_GLASSEYE | glasseye | VERMIN |
| FISH_PUFFER_WHITE_SPOTTED | white-spotted puffer | VERMIN |
| FISH_SOLE | sole | VERMIN |
| FISH_FLOUNDER | flounder | VERMIN |
| FISH_MACKEREL | mackerel | VERMIN |
| JELLYFISH_SEA_NETTLE | sea nettle jellyfish | VERMIN |
| SQUID | squid | VERMIN |
| SQUID MAN | squid man |  |
| GIGANTIC SQUID | gigantic squid |  |
| creature_small_riverlake |  |  |
| FISH_LUNGFISH | lungfish | VERMIN |
| FISH_LOACH_CLOWN | clown loach | VERMIN |
| FISH_BULLHEAD_BROWN | brown bullhead | VERMIN |
| FISH_BULLHEAD_YELLOW | yellow bullhead | VERMIN |
| FISH_BULLHEAD_BLACK | black bullhead | VERMIN |
| FISH_KNIFEFISH_BANDED | banded knifefish | VERMIN |
| FISH_CHAR | char | VERMIN |
| FISH_TROUT_RAINBOW | rainbow trout | VERMIN |
| FISH_MOLLY_SAILFIN | sailfin molly | VERMIN |
| FISH_GUPPY | guppy | VERMIN |
| FISH_PERCH | perch |  |
| creature_standard |  |  |
| DWARF | dwarf |  |
| HUMAN | human |  |
| ELF | elf |  |
| GOBLIN | goblin |  |
| KOBOLD | kobold |  |
| GREMLIN | gremlin |  |
| TROLL | troll |  |
| OGRE | ogre |  |
| UNICORN | unicorn |  |
| DRAGON | dragon |  |
| SATYR | satyr |  |
| COLOSSUS_BRONZE | bronze colossus |  |
| GIANT | giant |  |
| CYCLOPS | cyclops |  |
| ETTIN | ettin |  |
| MINOTAUR | minotaur |  |
| YETI | yeti |  |
| SASQUATCH | sasquatch |  |
| BLIZZARD_MAN | blizzard man |  |
| WOLF_ICE | ice wolf |  |
| FAIRY | fairy | VERMIN |
| PIXIE | pixie | VERMIN |
| BEAK_DOG | beak dog |  |
| GRIMELING | grimeling |  |
| BLENDEC_FOUL | foul blendec |  |
| STRANGLER | strangler |  |
| NIGHTWING | nightwing |  |
| HARPY | harpy |  |
| HYDRA | hydra |  |
| MERPERSON | merperson |  |
| SEA_SERPENT | sea serpent |  |
| SEA_MONSTER | sea monster |  |
| BIRD_ROC | roc |  |
| creature_subterranean |  |  |
| CROCODILE_CAVE | cave crocodile |  |
| TOAD_GIANT_CAVE | giant cave toad |  |
| OLM_GIANT | giant olm |  |
| BAT_GIANT | giant bat |  |
| RAT_GIANT | giant rat |  |
| RAT_LARGE | large rat |  |
| MOLE_DOG_NAKED | naked mole dog |  |
| TROGLODYTE | troglodyte |  |
| MOLE_GIANT | giant mole |  |
| IMP_FIRE | fire imp |  |
| SPIDER_CAVE_GIANT | giant cave spider |  |
| SPIDER_CAVE | cave spider | VERMIN |
| FISH_CAVE | cave fish | VERMIN |
| CAVE_FISH_MAN | cave fish man |  |
| LOBSTER_CAVE | cave lobster | VERMIN |
| SNAKE_FIRE | fire snake | VERMIN |
| OLM | olm | VERMIN |
| OLM_MAN | olm man |  |
| BAT | bat | VERMIN |
| BAT_MAN | bat man |  |
| MAGGOT_PURRING | purring maggot | VERMIN |
| ELEMENTMAN_FIRE | fire man |  |
| ELEMENTMAN_MAGMA | magma man |  |
| ELEMENTMAN_IRON | iron man |  |
| ELEMENTMAN_MUD | mud man |  |
| BIRD_SWALLOW_CAVE | cave swallow | VERMIN |
| CAVE_SWALLOW_MAN | cave swallow man |  |
| BIRD_SWALLOW_CAVE_GIANT | giant cave swallow |  |
| AMPHIBIAN_MAN | amphibian man |  |
| REPTILE_MAN | reptile man |  |
| SERPENT_MAN | serpent man |  |
| ANT_MAN | antman |  |
| RODENT MAN | rodent man |  |
| creature_temperate_new |  |  |
| WILD_BOAR | wild boar |  |
| WILD_BOAR_MAN | wild boar man |  |
| GIANT_WILD_BOAR | giant wild boar |  |
| COYOTE | coyote |  |
| COYOTE_MAN | coyote man |  |
| GIANT_COYOTE | giant coyote |  |
| KANGAROO | kangaroo |  |
| KANGAROO_MAN | kangaroo man |  |
| GIANT_KANGAROO | giant kangaroo |  |
| KOALA | koala |  |
| KOALA_MAN | koala man |  |
| GIANT_KOALA | giant koala |  |
| ADDER | adder |  |
| ADDER_MAN | adder man |  |
| GIANT_ADDER | giant adder |  |
| ECHIDNA | echidna |  |
| ECHIDNA_MAN | echidna man |  |
| GIANT_ECHIDNA | giant echidna |  |
| PORCUPINE | porcupine |  |
| PORCUPINE_MAN | porcupine man |  |
| GIANT_PORCUPINE | giant porcupine |  |
| KINGSNAKE | kingsnake |  |
| KINGSNAKE_MAN | kingsnake man |  |
| GIANT_KINGSNAKE | giant kingsnake |  |
| GRAY_LANGUR | gray langur |  |
| GRAY_LANGUR_MAN | gray langur man |  |
| GIANT_GRAY_LANGUR | giant gray langur |  |
| BOBCAT | bobcat |  |
| BOBCAT_MAN | bobcat man |  |
| GIANT_BOBCAT | giant bobcat |  |
| SKUNK | skunk |  |
| SKUNK_MAN | skunk man |  |
| GIANT_SKUNK | giant skunk |  |
| GREEN_TREE_FROG | green tree frog | VERMIN |
| GREEN_TREE_FROG_MAN | green tree frog man |  |
| GIANT_GREEN_TREE_FROG | giant green tree frog |  |
| HARE | hare |  |
| HARE_MAN | hare man |  |
| GIANT_HARE | giant hare |  |
| RATTLESNAKE | rattlesnake |  |
| RATTLESNAKE_MAN | rattlesnake man |  |
| GIANT_RATTLESNAKE | giant rattlesnake |  |
| WEASEL | weasel |  |
| WEASEL_MAN | weasel man |  |
| GIANT_WEASEL | giant weasel |  |
| COPPERHEAD_SNAKE | copperhead snake |  |
| COPPERHEAD_SNAKE_MAN | copperhead snake man |  |
| GIANT_COPPERHEAD_SNAKE | giant copperhead snake |  |
| IBEX | ibex |  |
| IBEX_MAN | ibex man |  |
| GIANT_IBEX | giant ibex |  |
| WOMBAT | wombat |  |
| WOMBAT_MAN | wombat man |  |
| GIANT_WOMBAT | giant wombat |  |
| DINGO | dingo |  |
| DINGO_MAN | dingo man |  |
| GIANT_DINGO | giant dingo |  |
| COATI | coati |  |
| COATI_MAN | coati man |  |
| GIANT_COATI | giant coati |  |
| OPOSSUM | opossum |  |
| OPOSSUM_MAN | opossum man |  |
| GIANT_OPOSSUM | giant opossum |  |
| creature_tropical_new |  |  |
| MONGOOSE | mongoose |  |
| MONGOOSE_MAN | mongoose man |  |
| GIANT_MONGOOSE | giant mongoose |  |
| HYENA | hyena |  |
| HYENA_MAN | hyena man |  |
| GIANT_HYENA | giant hyena |  |
| ANACONDA | anaconda |  |
| ANACONDA_MAN | anaconda man |  |
| GIANT_ANACONDA | giant anaconda |  |
| MONITOR_LIZARD | monitor lizard |  |
| MONITOR_LIZARD_MAN | monitor lizard man |  |
| GIANT_MONITOR_LIZARD | giant monitor lizard |  |
| KING_COBRA | king cobra |  |
| KING_COBRA_MAN | king cobra man |  |
| GIANT_KING_COBRA | giant king cobra |  |
| OCELOT | ocelot |  |
| OCELOT_MAN | ocelot man |  |
| GIANT_OCELOT | giant ocelot |  |
| JACKAL | jackal |  |
| JACKAL_MAN | jackal man |  |
| GIANT_JACKAL | giant jackal |  |
| CAPUCHIN | capuchin |  |
| CAPUCHIN_MAN | capuchin man |  |
| GIANT_CAPUCHIN | giant capuchin |  |
| SLOTH | sloth |  |
| SLOTH_MAN | sloth man |  |
| GIANT_SLOTH | giant sloth |  |
| SPIDER_MONKEY | spider monkey |  |
| SPIDER_MONKEY_MAN | spider monkey man |  |
| GIANT_SPIDER_MONKEY | giant spider monkey |  |
| PANGOLIN | pangolin |  |
| PANGOLIN_MAN | pangolin man |  |
| GIANT_PANGOLIN | giant pangolin |  |
| BLACK_MAMBA | black mamba |  |
| BLACK_MAMBA_MAN | black mamba man |  |
| GIANT_BLACK_MAMBA | giant black mamba |  |
| BEAR_SLOTH | sloth bear |  |
| SLOTH_BEAR_MAN | sloth bear man |  |
| GIANT_SLOTH_BEAR | giant sloth bear |  |
| AYE-AYE | aye-aye |  |
| AYE-AYE_MAN | aye-aye man |  |
| GIANT_AYE-AYE | giant aye-aye |  |
| BUSHMASTER | bushmaster |  |
| BUSHMASTER_MAN | bushmaster man |  |
| GIANT_BUSHMASTER | giant bushmaster |  |
| PYTHON | python |  |
| PYTHON_MAN | python man |  |
| GIANT_PYTHON | giant python |  |
| TAPIR | tapir |  |
| TAPIR_MAN | tapir man |  |
| GIANT_TAPIR | giant tapir |  |
| IMPALA | impala |  |
| IMPALA_MAN | impala man |  |
| GIANT_IMPALA | giant impala |  |
| AARDVARK | aardvark |  |
| AARDVARK_MAN | aardvark man |  |
| GIANT_AARDVARK | giant aardvark |  |
| LION_TAMARIN | lion tamarin | VERMIN |
| LION_TAMARIN_MAN | lion tamarin man |  |
| GIANT_LION_TAMARIN | giant lion tamarin |  |
| creature_tundra_taiga_new |  |  |
| STOAT | stoat |  |
| STOAT_MAN | stoat man |  |
| GIANT_STOAT | giant stoat |  |
| LYNX | lynx |  |
| LYNX_MAN | lynx man |  |
| GIANT_LYNX | giant lynx |  |
