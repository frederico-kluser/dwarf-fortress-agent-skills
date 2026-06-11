# World History file

> Fonte: [World History file](https://dwarffortresswiki.org/index.php/World_History_file) — Dwarf Fortress Wiki (GFDL/MIT)

In Legends Mode, pressing the (Export Map/Gen information) will create three files in the root directory of DF, one of those files is the **World History file** named (save name)-world_history.txt.

## File Breakdown

Below, the history file will be explained in detail, using portions from an example file to show all of the possibilities.

### World Name

At the top of the file is your fortress name, followed by the world name.

    Mareecamo Ewè
    The Soul-Universe of Enchanting

### Unintelligent Civs

Following the world name is a series of names of different unintelligent civs which exist in the world; no further information can be gathered from these files about these civilizations.

    Mareecamo Ewè
    The Soul-Universe of Enchanting

    Cave fish men
    Serpent men
    Reptile men
    Bat men
    Antmen
    Cave swallow men
    Olm men
    ... (Multiple more lines)

### Civilizations

The majority of the useful information in the history file exists within the civilizations, which follow immediately after the unintelligent civs. A short example civ is shown below, but the components will be viewed in detail afterwards.

    Bat men
    Amphibian men
    Cave swallow men
    The Hammer of Seers, Dwarves
     Worship List
      Engig the Bright Pearls, deity: metals, jewels, wealth
      Onget the Fiery Oil, deity: mountains, volcanos
      Laltur, deity: fortresses
      Ral Minedirons, deity: minerals
      Mirstal, deity: music, festivals, song
      Kogan Coastalpaddled, deity: rivers
     king List
      [*] Logem Anvilentrance (b.??? d. 36, Reign Began: 1), *** Original Line, Married (d. 8)
          4 Children (out-lived 1 of them) -- Ages at death: 32 31 29 (d. 14)
          Worshipped Onget the Fiery Oil (61%)
      [*] Bomrek Championboulder (b.7 d. 51, Reign Began: 37), Inherited from mother, Never Married
          No Children
          Worshipped Onget the Fiery Oil (94%)
      [*] Cog Cloisteredrazors (b.???, Reign Began: 52), *** New Line, Married
          14 Children -- Ages: 62 61 60 59 54 51 36 31 24 18 16 15 12 4
          Worships Mirstal (32%)

#### Civ Name and Race

The Civ name is at the top of the section for each civ, along with the race of the civ.

    The Hammer of Seers, Dwarves

#### Worship List

If the civ has any deities or forces that they have ever worshipped, then this section will exist, beginning with the text:

     Worship List

Each individual line refers to a different force or deity. First the deity name, then whether they are a "deity" or "force", and finally a list of the spheres they belong to, or control.

      Istrath the Gravel of Oiling, deity: earth, wealth

#### Leader List

If the civ has had any leaders, they will be listed according to what type of leader they are (king/queen/law-giver/etc.):

     king List

Each individual leader begins with the text `[*]`, and has two or three lines. Those are:

      [*] Logem Anvilentrance (b.??? d. 36, Reign Began: 1), *** Original Line, Married (d. 8)
          4 Children (out-lived 1 of them) -- Ages at death: 32 31 29 (d. 14)
          Worshipped Onget the Fiery Oil (61%)

- **Leader Name and Life**: `Logem Anvilentrance (b.??? d. 36, Reign Began: 1), *** Original Line, Married (d. 8)`
- **Leader Children**: `4 Children (out-lived 1 of them) -- Ages at death: 32 31 29 (d. 14)`
- **Leader Worship**: `Worshipped Onget the Fiery Oil (61%)`

**Leader Name and Life** is made up of several pieces of information.

:\*The leader's name: `Logem Anvilentrance`

:\*The leader's birth year: `(b.???`

:\*\*This is represented as ??? if the leader was born before history (before year 1).

:\*\*If there is a year, there is no space between the "b." and the year. ex: `(b.66`

:\*The leader's death year: `d. 36`

:\*\*If the leader hasn't died, this won't be listed.

:\*\*There **is** a space between the "d." and the year.

:\*The year the leader's reign began: `, Reign Began: 1),`

:\*How the leader acquired power, either by being the original leader (`*** Original Line,`), starting a new line (`*** New Line,`), or by inheriting the position (`Inherited from`)

:\*If the position was inherited, it will list who they received it from. The possibilities:

:\*\*Father - `Inherited from father,`

:\*\*Mother - `Inherited from mother,`

:\*\*Paternal Grandfather - `Inherited from paternal grandfather,`

:\*\*Paternal Grandmother - `Inherited from paternal grandmother,`

:\*\*Maternal Grandfather - `Inherited from maternal grandfather,`

:\*\*Maternal Grandmother - `Inherited from maternal grandmother,`

:\*\*Unknown - `Inherited from,`

:\*The marriage of this leader. Either: `Never Married` or `Married`

:\*If the leader has married, and the spouse died, it'll list the year they died `Married (d. 8)`

**Leader Children** is made up of several pieces of information about a leader's children (if any)

:\*Number of children: `No Children`, `1 Child` or `x Children`, where "x" is the number of children \>1

:\*Number of outlived children, which is some number less than or equal to the number of children: `(out-lived 9 of them)`. If the leader outlived none, then this part won't be given.

:\*Ages (at death) of children. Listed with `-- Ages at death:` if the leader has died, otherwise with `-- Ages`

:\*\*It will list as "Ages" even if there was only one child.

:\*The ages at death will be listed as numbers separated by spaces: (`37 31 27 9`), or if the child was outlived, with the year they died: (`(d. 32) (d. 29) (d. 8)`)

:\*\*There aren't always the right number of items in this list, at times some children's ages might not be listed.

- **Leader Worship** gives information about the leader's deity/force of worship, if they did not worship, this line won't exist.

:\*Worship object name: `Worshipped Onget the Fiery Oil`

:\*Degree of worship: `(61%)`

:\*\*Between 1% and 100% inclusive.

## See Also

- Legends Mode
- World Sites file
- XML dump
