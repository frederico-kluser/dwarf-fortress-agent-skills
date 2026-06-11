# Library

> Fonte: [Library](https://dwarffortresswiki.org/index.php/Library) — Dwarf Fortress Wiki (GFDL/MIT)

**Libraries** are locations. At a library, scholars can write books (quires, which are bound into codices, and scrolls) and scribes can create copies. Any dwarves in your fortress will go to libraries to read books or idle around, giving them happy thoughts. You will need bookshelves to store books and chests to store writing materials. To attract visitors to your library, you can buy books from caravans or steal them using missions on the world map. Your dwarves will read books as a form of entertainment.

## Obtaining writing materials

There are several types of writing materials: scrolls, codex, quire, etc. Here is one setup.

To make paper, you need 'slurry' which is pressed into paper sheets, then rolled into scrolls or assembled into 'quires' (which are like books without covers.) You can also create a cover for a quire and then bind it, but it's not necessary for producing writing. Scrolls can also be produced for shorter works. There is mention of a bug that will lower the quality of your quires after binding.

### Making slurry

- Build stoneworker's workshop (Building \> Workshops \> Stoneworker)
- Produce stone quern using stoneworkers workshop (input: stone)
- Build quern (Building \> Workshop \> Farming \> Quern)
- Add plant stockpile near your quern
- Have your dwarves gather plants
- Set a work order for your quern to produce 'slurry' if fewer than 10 'globs' exist. Set "adj" to 'paper-slurry items'. (input: plants)

(Note: You need a dwarf with the 'Manager' role and an office assigned to use work orders. You can do that from Citizens \> Nobles and Administrators)

### Making paper sheets

- Build Mechanics workshop (Building \> Workshops \> Mechanics)
- Produce 2 mechanisms from Mechanics workshop
- Build screw press near your quern (Building \> Workshops \> Screw Press, input: 2 mechanisms)
- Set a work order on your screw press to produce paper if fewer than 10 exist (input: slurry)

### Making scrolls (used for shorter works)

- Build a crafts workshop (Building \> Workshops \> Crafts)
- Set a work order on your crafts workshop to produce 'scroll rollers' if fewer than 10 exist (input: stone or wood)
- Set a work order on your crafts workshop to produce scrolls if fewer than 10 exist (input: scroll rollers + paper sheets)(note: The purpose of setting all these work orders with the condition 'if fewer than 10' is so that your dwarves will keep a small stock of items and replace them as needed. You don't end up with overstock like you do if you set the condition to produce infinitely or every day/month.)

### Making quires (used for longer works)

- Build a crafts workshop (Building \> Workshops \> Crafts) if you haven't already
- Set a work order on your crafts workshop to produce 'quires' if fewer than 10 exist (input: paper sheet)

## Setting up a library

- Create a room and set it as a 'Meeting Area' zone (Zones \> Meeting Area)
- Click 'Zones' again and then click on your meeting area
- Click the + symbol and then 'New Library'
- Enjoy your randomly generated library name
- Click magnifying glass to change your library settings:
- Increase the desired number of writing materials to 20 (optional)
- Leave your library public so you can get visiting scholars (optional)
- Build bookcases to store written books, and containers to store writing material (blank quires and scrolls). (not paper sheets, they *must* be made into blank scrolls/books *before* writing).
- Build tables and chairs.
- Designate scholars and scribes as desired (via the Locations menu).

Libraries function best as a single activity zone - scholars in separate activity zones cannot discuss topics with each other, even if both zones belong to the same library. Scholars in the same activity zone can discuss topics together, regardless of distance, line of sight, or ability to path to each other. So, with the correct design, a scholar who must be separated from the general population for whatever reason can still contribute to the research effort.

## Designating scribes and scholars

### Scholars

- Click 'Zones' and then click on your library
- Click the magnifying glass
- On the library menu, click the + sign next to scholar
- Assign a dwarf as a scholar (bonus if they have good writing skills)
- If your library has desks + chairs + writing materials, your dwarves will eventually write... when they feel like it. Mostly they will chat, learn new topics, and read books until they have decided there's something they want to write about.
- Assign as many scholars as your fortress can spare to increase the chance of one of them writing
- After assigning a scholar, check their thoughts to see if they enjoy the role. Some dwarves feel anxious when they learn new things or debate/argue with other scholars. If they don't like the role, they will become unhappy over time.
- On the 'assign' menu, you can't see if your dwarf has knowledge to write about, but you can see this information on the dwarf's profile under SKILLS \> OTHER SKILLS

### Scribes

- Click 'Zones' and then click on your library
- Click the magnifying glass
- On the library menu, click the + sign next to scribe
- You probably won't need more than one or two scribes as they seem to copy a lot
- Set 'total number of each to scribe' to decide how many copies you would like of each original work
- You can sell copies to visiting traders and your scribes will produce more. (note: Finished scrolls are under 'tools' when you move goods to your trading depot.)
- Sell lots of copies of that book with a funny title to spread your culture across the world

## Obtaining scholars and books

If your library permits visitors, scholars from civilizations around the world will come to your fort to study, often bringing books of their own. These scholars will engage in various topics with your scholars and each other, and will sometimes write their own books while visiting (using your supplies of writing materials in the process). These books effectively become property of your fortress, as the author usually doesn't take their books away upon leaving, although they may take some of your own in return. Visiting scholars may petition to become a permanent part of your fortress for the purpose of studying. The rate at which they visit your library and apply for residency might be related to the number of books in your library.

If you retire your fort, scholars will continue to visit your library during retirement even if the library does not permit visitors. On unretirement, those scholars will be bugged and unable to behave normally in your fort, so it's best to delete your library activity zone before retirement.

Even with visitors, it takes a long, long time for your scholars to generate much knowledge or write many books in your fort. You can speed up this process by taking books from other libraries, with missions or adventurers. Legends mode can show you where the libraries are in your world.

## Getting your dwarves to write

Coaxing your dwarves into writing can take some time. While writing-related skills improve the quality of their work, they seem to have more to 'write about' if they have skills like medicine or mechanics. It's much easier to get them write guides about scientific topics than to write poetry or novels. (There's actually an entire technology tree in the background that your dwarves can progress by reading books, chatting, and having breakthroughs.)

## Urist's Lever

It was discovered that by putting an unlinked lever in the back of a library, assigning only the scholars and scribes to use it, then assigning them to pull the lever, with high priority on repeat... due to the vagaries of dwarven psychology, they will find themselves unable to resist reading, writing, or pondering something. This is a good way to increase the productivity of your fortresses' best and brightest.

## Library management

In vanilla DF, it's rather difficult to get information about the books you own: who wrote them, how many copies you own, what topics they cover, etc. Fortunately, there's a DFHack script that makes all that very clear.

Visiting scholars will sometimes steal the books they're carrying when they leave, even books they did not write. If you unassign the tables (but not the chairs) from your library, the visitors can produce books but cannot touch them, but your own dwarves can still interact with them normally. The tables should still physically be in the library, just not within the painted library zone. (To unassign a section of library, click 'Zone' and then 'library' and use the eraser icon.) You can also have separate libraries for your citizens and for visitors and using stockpiles to keep the books out of the public one.

Once your library is well-known enough, you'll start getting foreign scholars petitioning to join your fortress. A visiting necromancer may write a book that contains the 'secrets of life and death.' Any dwarf who reads this type of book will become a necromancer, which has... pretty serious consequences. You will need to find and forbid these books if you want to prevent this, or just sit back and wait for the Fun to happen.

## Adventure mode

In the rest of the world, libraries are generated structures that can be found in human towns and dwarven fortresses. Like the libraries in fortress mode, they will be frequented by scholars who spend their days discussing scholarly topics. The number of books and scholars in a given generated library depends on the history of the site. A library found in a town with a poor history may be almost empty of books and scholars alike.

The ground floor in a generated library is typically used as a study area, and furnished with chairs, tables and a container with usable writing materials. A ramp-staircase connects the ground floor to higher floors as well as a basement. Basements and higher floors are typically used to store the books, and contain several bookcases. Libraries found in fortresses only have two floors, while those found in towns can span many stories high.

Libraries have an effect in world gen, based on the original and copied books that are there. Every year, each library gets five turns to pick a book. If the book has a poetic/music/dance form, it has a chance to make that form well-known in the entire parent civ, as a form of cultural diffusion. If the book promotes a value at a certain level, it makes a roll against the author's skill roll when they wrote the book. The local site civ can have their values shifted by 1-2 points (it takes 10 or more to change the visible text for the value), and the parent civ can also be shifted a point, and all sites under the parent civ have a chance to be shifted a point as well.

See also:

Fr:Bibliothèque (library) "Fr:Bibliothèque (library)")
