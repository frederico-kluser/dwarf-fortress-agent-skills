# Mod

> Fonte: [Mod](https://dwarffortresswiki.org/index.php/Mod) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

*For information on making mods, see Modding.*

A **mod** (short for modification) is an alteration of the game and the objective of modding. Modifications can range from small tweaks to complete overhauls.

## Downloading mods

Mods can be acquired using the Steam Workshop (if using the Steam version), a manual download from Bay 12 Forums or third party websites (like DFFD), or by creating one yourself.

Users of the Steam version can subscribe to mods on the Steam Workshop, once the download is complete they will be available when creating a new world automatically. Otherwise, manually download the mod, then place the mod zip file or the unzipped mod folder into the *Dwarf Fortress* mod folder (if this folder doesn't exist, you can create it.) You can have more than one mod in the mod folder, including different versions of the same mod. The game will detect all mods that are properly made in this folder and let the user select which mods to play (see below.)

## Enabling/installing mods

world generation mod menu

Mods are enabled per world. When creating a world and choosing its initial parameters, if you have a mod available, there should be a **Mods** button at the bottom of the screen. Pressing this will let you select which mods you'd like to enable and what the load order should be. You should put mods at the end of the mod list after the vanilla objects if you don't have any further information, so that they can reference vanilla objects after those are loaded.

Some mods might depend on other mods which have to be loaded before, refer to the mod description for information about that.

- Mods are enabled per world, and cannot be disabled afterwards, however, it is possibly to manually modify the game file, as we did in previous versions, by applying the mods directly to `/data/vanilla`. Be aware, this method has the disadvantage of being a permanent change for all worlds, and may break your game.

- Unlike the previous versions of *Dwarf Fortress*, mods no longer live inside save and must be installed on every computer where saves using those mods are going to be loaded. Once a world is created that uses mods, the game will copy the relevant mods to the `/data/installed_mods` folder. That is the version that the game actually uses. Installed mods will now show in the main menu-\>mods screen as 'installed'.

## Updating/missing mods

possible update message

If a save is using a mod that's been updated, and is currently using an older version of that mod, the player will be prompted about this when a save is loading. When this happens, you have the choice of simply updating the mod, updating *all* mods at once, continuing to use the older version of the mod in question without updating, selecting the previous task but not updating *any* possibly outdated mods or simply returning to the title screen.

If a save is using a mod that is missing, the player will be prompted about this when a save is loading. When this happens, try to reinstall the mods, either by manually downloading them again, or in the case of Steam Workshop, making sure you are subscribed and if you are, by unsubscribing and subscribing again.

## Modding

*Dwarf Fortress* supports mods in the form of new objects and tiles. Each mod is a zip file or unzipped folder with the required format (see below.)

### Mod format

Mods contain an info.txt file and either an "objects" folder or a "graphics" folder (or both.) All of the vanilla objects in the game use this format too. Your mod folder should look something like this:

     Mod Name
     ├  info.txt
     ├  preview.png
     ├  objects
     └  graphics

### Mod info

Each mod must have an `info.txt` at the root of your mod folder. It has a few fields defining basic metadata information about the mod and can be edited using any text editor (like notepad++). See Example:

    [ID:wiki_example]
    [NAME:Wiki Example Mod]
    [NUMERIC_VERSION:5001]
    [DISPLAYED_VERSION:50.01]
    [EARLIEST_COMPATIBLE_NUMERIC_VERSION:5001]
    [EARLIEST_COMPATIBLE_DISPLAYED_VERSION:50.01]
    [AUTHOR:Dwarf Fortress Wiki]
    [DESCRIPTION:This is an example mod. This text shows up in-game.]

    [STEAM_TITLE:Wiki Example Mod]
    [STEAM_DESCRIPTION:This text shows up on Steam Workshop.]
    [STEAM_TAG:mod]
    [STEAM_KEY_VALUE_TAG:test:stuff]
    [STEAM_METADATA:metadata test]
    [STEAM_CHANGELOG:Made some changes. Shown in 'Change Notes' tab.]

    [STEAM_FILE_ID:#########]

Only `ID` and `NAME` are required to appear in the in-game mod menu.

STEAM tags are only used by Steam.

- The `STEAM_FILE_ID` used to identify the mod in the Workshop. This is automatically managed when uploading to Steam the first time, and required if you wish to update an existing Steam Workshop mod.
- The `STEAM_TAG` and `STEAM_KEY_VALUE_TAG` are used by Steam's search engine for categorization. You can use as many entries as you want, use a separate tag for each one.
- You can also create a thumbnail for your mod, by creating an image called `preview.png` in the same level as your info.txt file. This image will become the thumbnail when the mod is uploaded to Steam Workshop. The image should be less than 1MB in size.

### Objects and graphics folder

A mod folder can contain an `objects` and `graphics` folder. These are where all the raw files or graphics for the mod go (exactly the same as objects from previous versions of Dwarf Fortress) allowing you to tweak or add new content for the game. It's beyond the scope of this short guide to go into what specific tags do, but the vanilla objects and previous mods by members of the community will give you plenty of examples to work with. See modding for more information.

The graphics filenames are not important; furthermore, they can be arbitrarily nested into other sub-folders to help you organize your mod content.

## Publishing mods

There are two official platforms for publishing *Dwarf Fortress* mods, recommended because it's easy for people to find them there. These are the Steam Workshop and the Dwarf Fortress File Depot (DFFD).

### Publishing on Steam Workshop

To upload a mod to Steam Workshop, you need to add STEAM tags to the `info.txt` file (see above.) Afterward, you put the unzipped mod folder in the "`mods/mod_upload`" folder. Then select Mods from the title menu, and upload your mods using the button you'll see there. Other Steam users will be able to subscribe to your mod immediately once it is uploaded.

Once the upload process is completed successfully, you'll find a `[STEAM_FILE_ID:#########]` appended to your info.txt. Make sure this entry is included for future uploads if you want to make changes to your mod and have it overwrite the existing entry on the workshop. Otherwise you'll create a new entry every time you upload.

If you have problems with blank or empty mods uploading, adding a preview.png file (as detailed above) may fix this problem.

### Publishing on DFFD

In addition to Steam Workshop, it is recommended you upload your mod to DFFD. This allows people who play *Dwarf Fortress Classic*, or *Premium* via Itch.io, to also download and play your mod. To publish/upload a file to DFFD you first need to create an account.

For legal reasons, mods that contain graphics derived from the *Premium* graphics should not be uploaded outside Steam Workshop. For this reason, you might want to separate your mod into two parts: the first without graphics, which is uploaded to both DFFD and Steam Workshop, and the second with *only* the graphics, uploaded only to Workshop. Of course, this is not an issue if your graphics are not based off the *Premium* ones.
