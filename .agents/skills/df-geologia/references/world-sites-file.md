# World Sites file

> Fonte: [World Sites file](https://dwarffortresswiki.org/index.php/World_Sites_file) — Dwarf Fortress Wiki (GFDL/MIT)

In Legends Mode, pressing the (Export Map/Gen information) will create three files in the root directory of DF, one of those files is the **World Sites file** named (save name)-world_sites_and_pops.txt.

## File Breakdown

Below, the history file will be explained in detail, using portions from an example file to show all of the possibilities.

### Civilized World Population

At the top of the file, the text "Civilized World Population" appears with a listing of the total population of "civilized" beings:

    Civilized World Population

        20499 Dwarves
        11742 Humans
        14187 Elves
        150 Goblins
        575 Kobolds

        Total: 47153

### Sites

Following is a list of all of the sites in the world; they can appear in a few different varieties, some examples:

A site controlled by an entity belonging to a civilization:

    1: R lidsimo Gumsekemus, "Strangleechoes the Wretched Delight", cave
        Owner: Jibigiseekis, kobolds
        Parent Civ: Japlolbus, kobolds
        288 kobolds

A site controlled by an entity (which is referred to as a parent civ in other cases), and listing a leader located at that site.

    37: Karaboshkuc, "Heatedcruxes", fortress
        Owner: The Autonomous Confederacy, humans
        law-giver: Sabu Yawntusks, human
        1 tortoise demon prisoner

A site not controlled by any entity, simply listing various creatures living there.

    6: Ilasavuz, "The Absolute Mine", cave
        1 giant bat
        2 trolls
        312 bats
        395 cave swallows
        453 cave spiders

A site listed as an "important location" without a proper name, without any inhabitants

    2929: kobold, "Dashedstake", important location

### Outdoor/Underground Animal Populations

Following the site listing, there is a list of outdoor and underground animal populations:

    Outdoor Animal Populations (Including Undead)
        9060 merpeople
        28388 sperm whale men
        18120 giant orcas
        (many more lines)

    Underground Animal Populations (Including Undead)
        11284 gorlaks
        11270 trolls
        7123 giant cave spiders
        5001 giant rats
        (many more lines)

## See Also

- Legends Mode
- World History file
- XML dump
