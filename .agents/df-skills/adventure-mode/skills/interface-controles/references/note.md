# Note

> Fonte: [Note](https://dwarffortresswiki.org/index.php/Note) — Dwarf Fortress Wiki (GFDL/MIT)

**Notes** are comments that you can leave around your fortress, each attached to a single tile. They are both placed and read using the key, the Notes showing up as custom symbols on the map, with the full text in the Notes menu, much the same way that zones and their information are visible only when you enter the zone function (). They are also used to predefine stations and patrol routes.

Activating the menu also allows one to find the closest Note, including across z-levels, by +/- x,y,z coordinates. By navigating the cursor nearest a particular symbol, you can read or edit the text of that particular note. The currently active note will flash when selected - if you move the cursor, you'll see the nearest note symbol flashing on the tile where it was placed. The flashing indicates that it is the currently displayed note, and you can see distance and direction with the x,y,z coordinates at the top of the notes screen. The coordinates and menu always display the *closest* note, even if it's off-screen or on a different level.

## The Notes menu

Press to bring up the notes screen.

The default selection determines the single symbol that will mark that note. One note is attached to one tile - one note per tile max. There are 3 parts to the sub-menu - at the top is the list of available symbols to mark your note, and below are (in order) 8 possible background colors and 8 more (16 total) possible font colors. One and only one symbol will mark your note in each selected tile.

## Adding a Note

When you first open the Note function\*, you will notice 3 flashing X's - one bright and two greyed out. You will be changing between these sub-menus using the hange key. The contrast is not great, and the flashing doesn't help - look closely to make sure you've selected the desired sub-menu.

*(\* If you already have Notes in place anywhere on the map, the text of the nearest Note will be visible at the top along with the symbol for that Note - see Finding/Reading, below.)*

In order, the steps are 1) select a symbol, 2) select the location tile, and 3) type the note itself.

#### Symbol selection

The first step is to select what symbol you want to use to mark the tile you will select. This only a single-character "marker" - the text will be chosen in a moment. This selection is made on the top line, the long list of symbols. Hit hange to get that X bright, and then use the / (or and ) keys to scroll across and choose your symbol - you have 256 symbols to choose from.

To change the text color, hit hange again and use the same selector keys to choose your desired color. The X will go all across all 16 colors.

Then select the background color, by hitting hange again and doing likewise. For background, you only have the 8 thicker colors on the left to choose from.

If you change your mind, cycle through symbols and colors until you're happy with the combination. Later, this symbol will flash when you are close to it with the Note reader, or be solid if you are closer to another that is also visible on the map screen.

Depending on your selection of symbol, color and text, your symbol could be invisible to view (by blending in with the chosen tile location), but you can still find it if you remember the general area and other Notes are not surrounding it.

#### Placement

The next step is to select where the Note will be placed. Move the cursor using the standard navigation keys (the , , , & keys) to the tile you want to label with this Note. Once you have the symbol, colors, and location you want, press to place it. This changes the menus, disabling 'place' until you move to a new location (only one note per tile).

The symbol you selected will be flashing in that location - unfortunately, if the cursor is over it, you will not be able to see this - trust that it's there, or look in the upper left corner of the Note screen for the symbol you chose, and that there is a distance/direction of 0,0,0.

*(If no other Notes are nearby, you can move the cursor to see the note you have just placed - if they are, you will still see it, but another might be flashing, indicating that now that one is selected.)*

#### Typing the Note itself

Once you have placed the symbol you can type the note itself. Hit the "Enter ote text" key, and type your message. You have 100 characters to work with, 4 lines (on that screen) -hardly limitless, but should be ample for most purposes. Press when done typing.

Then move the cursor and place another Note (with a new or the same symbol), or hit to exit.

##### Second thoughts

To change the selected note symbol or colors (now or later) when in the Notes menu, first select a new symbol (as above when selecting the original symbol), and press the key to "Adopt selected symbol". The flashing symbol will change to your new selection.

### Editing/Deleting

First, always remember that the function edits the *closest* note, which will be flashing when it's automatically selected as such. You cannot see the symbol flash when the cursor is directly on the symbol, but the Note's symbol and distance will appear at the top of the Notes menu.

To select an existing Note, just open the Note menu, and move the cursor to the Note you want - the nearest one will flash and be seen in the upper left corner of the Note menu, and that is close enough. The numbers at the top of the screen show the distance in the x, y and z direction to that nearest note. Distance 0,0,0 means your cursor is directly over the Note.

To edit, just hit again - it's a painfully simple program, so you can either add or erase and retype, no proper text editing.

To edit a symbol, use and the / keys to select the symbol, then use to adopt the new symbol to the note.

To delete that Note, just hit . CAUTION - each time you hit , you will delete the *nearest* Note on that z-level - use with care, or other nearby Notes will get deleted. You cannot recover a deleted Note.

## Finding/Reading existing Notes

Just as in Editing, above, open the otes menu and all Notes on the map will become visible. Navigate close to the Note you want to read (or edit) - it will begin to flash, and the text will be visible in the sub-menu, along with the symbol and exact distance and direction (in terms of x,y,z) at the top. Once you are closer to your desired Note than any others, it will flash and you can read, edit or delete it.

## Patrol Routes

Once you've defined at least two Notes, you can define patrol routes between them. In the Notes menu, press and you'll be able to manage routes and waypoints within a route.

### Managing Routes

Here, you can dd new routes, elete unnecessary routes, ame them, enter the view on the currently-highlighted waypoint, switch to diting waypoints, or back out by pressing .

You can also switch the currently-visible route by pressing .

### Managing Waypoints

As with the route manager, you can dd new waypoints, elete waypoints from the route, ame the route, enter the view on the chosen waypoint, switch back to diting routes, or leave the manager by pressing .

You can also change the currently-selected waypoint by pressing .

### Creating a Route

So you've got a bunch of notes, and you want to create a patrol route between some of them:

1.  Go to the route screen by pressing -\>.

2.  Switch to editing routes (if necessary) by pressing .

3.  dd a new route. Your newly created route will be selected automatically.

4.  Give it an informative ame.

5.  Switch to editing waypoints by pressing .

6.  Add the starting waypoint by navigating the cursor on the map until the desired note is shown in top-right of screen and then press .

7.  Continue adding waypoints in the order you want them visited.

8.  To delete a waypoint, use the keys to highlight the waypoint and press .

9.  Complete the patrol by pressing .

### Using a Route

Once created, your military dwarves can be scheduled to patrol a route. Go into the military scheduler (-\>), choose a squad and month, give an rder, then rotate through the rders until it says "Patrol route". The screen will display a list of your routes, allowing you to choose one.

## Suggested Uses

It's recommended that all important levers are labeled, and possibly anything they are connected to, to remind you which lever activates exactly which items, and how, and what the result will be, and anything else that might possibly be of concern. The more complex the fortress, the more important this can be. You never know when you'll walk away from a fortress for a few weeks, come back and not know how to do anything - or, worse, only *think* you do.

Consider color coding your notes (and levers), to know approximately what they do - maybe red can injure dwarves, dark red controls magma, dark blue controls water at the source, light blue at the function - whatever works for you.

This becomes even more important in a succession game, where the next player has no idea what the previous one(s) built. Also for comments on future plans, ongoing projects, or perceived trouble spots.

### Squad Movement

Notes can act as predefined destinations for squad movement. Within the quad manager, select a squad, and start giving it a ove order. The next screen will show a list of your notes, allowing you to easily boss your squad without having to move the viewing cursor.

### Scheduled Movement

Notes can also be used to position military dwarves on a scheduled basis. Within the military scheduler (-\>), choose a squad and month, give an rder, then rotate through the rders until it says "Station". The screen will display a list of your notes, allowing you to choose one for a destination.
