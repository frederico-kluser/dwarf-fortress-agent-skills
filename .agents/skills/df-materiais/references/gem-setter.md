# Gem setter

> Fonte: [Gem setter](https://dwarffortresswiki.org/index.php/Gem_setter) — Dwarf Fortress Wiki (GFDL/MIT)

**Gem setter** is the skill associated with the **gem setting** labor. Gem setters encrust furniture, finished goods (excluding tools), and ammo (including siege ammo) with cut gems. It is not currently possible to decorate weapons and armor with gems, unless the armor is made of cloth. A high level of gem setting allows a dwarf to set gems faster and with better quality, making the decorated items more valuable.

Rough gems, which are found by miners, have to be converted to cut gems by a gem cutter before a gem setter can use them. Gizzard stones are a type of cut gem and can also be used by gem setters. Large gems, which are sometimes created instead of a cut gem, cannot be used for gem setting, as they are finished goods. (You might be lucky enough to be the proud owner of a magnificent \\> (This is a masterful quality large *(Insert rare gem name here)*.) This object is adorned with hanging rings of *(Insert worthless gem name here)*.)

Because there are a very wide variety of gems in most regions, and some types of gems have pretty high material value, adding decorations of different types of gems is a good way to create items with very high value for trade or nobles.

## Training

As with gem cutters, gem setters can be easily trained by ordering them to set common stone such as basalt, mudstone, diorite, and schist.

## Control

In the base game, it is not possible to directly specify which item will be encrusted, however control over the process can be exerted by creating an intermediary stockpile linked to take from your main stockpile and give to the workshop, then adjusting its settings to match whatever item(s) you wish to decorate (for instance, a masterwork gold throne for your monarch, or low-quality clothing if you're training a novice gem setter). Your gem setter will refuse to use any item that is not stored in a linked stockpile; you can then selectively forbid items in the stockpile to control exactly which item will be decorated. (If you do this, remember you will also need a stockpile link that provides gems to the jeweler, as workshops that have any Give links must get *all* their items from links. The same intermediary stockpile could be used if you don't mind mixing your gems with the items being encrusted.)

Another problem in the base game is the number of Encrust Gems jobs required: one per type of gem. Gem cutting and gem setting can be quite tedious to manage, as one workshop job is required per type of gem, and can only be started when at least one cut gem of that type is in stock. A typical fortress will likely have dozens of available rough gem types, necessitating many separate jobs - spread across many separate Jeweler%27s workshops due to the 10-jobs-per-workshop limit. Even when low value gems are avoided, this will still likely result in a regular stream of jobs suspending as stock of that gem is depleted, and much manual work re-enabling them: potentially to only set a couple more gems before the job suspends again!

In summary: Gem Setting jobs suffer from two inconveniences that are in effect the opposite of each other:

- The type of item to encrust is general - *too* general: providing no control over which items are encrusted without the use of (potentially multiple) intermediary stockpiles and often manual forbidding.
- The type of gems to use is specific - *too* specific: requiring one job for each type of cut gem, and resulting in lots of cancellation spam and manual resuming of jobs.

Both of these can be fixed with the use of DFHack.

***DFHack: the content in the following section requires the use of DFHack***

### Advanced Control Using DFHack

The utility DFHack can largely resolve both of the problems described above, and in doing so facilitate an elegant, automated gem cutting and encrusting production line.

- DFHack provides the plugin **Job material**, which can modify the materials used by a given workshop job
  - In the default DFHack config, the UI for Job Material is accessible by pressing when looking at a workshop with a job selected.
  - Job Material allows the user to edit the required components for a job.
  - In the case of gem setting, this means:
    - the specific, one-per-type-of-gem Encrust jobs can be turned into a generic job that will encrust with *any* cut gem;
    - the non-specific, "Encrust Furniture/Finished Goods/Ammo" jobs can be made specific, to encrust only specified items of that type;
    - both of these changes can be combined: for example, to create a job to Encrust Gold Statues with any Gem.

To proceed, first ensure you have DFHack installed and are running with its default config enabled. PyLNP users can simply set DFHack to Yes on the DFHack tab, then relaunch the game (other launchers likely have a similar, easy DFHack option.)

#### Using DFHack to create a single job that will Encrust with any cut gem:

1.  At a Jeweler's workshop, create an Encrust With Gems job for any cut gem you have in stock, choosing the type of job you want, e.g. Furniture or Finished Goods.
2.  With the job selected, press .
3.  You will see the screen shown to the right (probably using a different type of gem).
4.  This screen is showing us the *input* Items for the job. For an Encrust With Gems job, there are two input items: the cut gems to encrust with, and the item to encrust.
    1.  Input items have three parameters: input item, material, and flags.
    2.  Using Job Material, we are able to edit the first two of these parameters. In the case of this task, we only want to edit the *material*, to specify that the gem can be of any type. In the next task, we will look at changing both type and material when editing the second Input Item.
    3.  The third parameter, Flags, is visible here as well - we can see that the type of object to Encrust, e.g. Furniture, is specified as a Flag (*improvable, **furniture**, not_bin*). Unfortunately it is not (yet) possible to edit Flags through DFHack Job Material, so we can't make a job that Encrusts anything at all!
5.  For this task we only care about the first input item, item 1, which is the cut gem. So with this highlighted (as it will be by default):
    1.  Press to change the input item, and see all valid options for this job: in the case of Encrust With Gems, *cut gem* is the only valid choice, so there is nothing to change here.
    2.  Press to change the material, again showing all valid options. Here, we will see many options, in a categorised list. We could use this to change this Encrust job to use a different cut gem, but we can also do that through the normal UI. Instead we want to use the first option: *any material*.
6.  Once done the UI should look as shown on the right.
7.  Now press to finish the edit. On the workshop menu you will see the job is now called *Encrust furniture with unknown material*.
8.  Set the job to Repeating and your Gem Setter(s) will now happily encrust furniture with any cut gems they can get their hands on; and the job will never Suspend unless you run out of *all* cut gems. One job to encrust them all.
9.  To provide some control over which Cut Gems are used - and thus avoid encrusting high-value furniture with lapis lazuli and other cheap stuff, if that's been cut in your fortress - provide a nearby Gem Stockpile with rules set to only allow Cut Gems that you care about, i.e. high value ones. Now set this stockpile to Give to your jeweller's workshop(s).
    1.  Alternatively, control this at the \|gem cutting stage: if you only cut higher value rough gems, you won't have any cheap Cut Gems to avoid in the first place.
    2.  If you do make a stockpile link for Cut Gems, remember that you must then also provide a stockpile that Gives the furniture to encrust - as once a workshop has one stockpile set to Give, it must be able to get *all* its items from stockpile links. See Stockpile and Stockpile design.

#### Using DFHack to specify the items encrusted by an Encrust With Gems job:

1.  As per the above steps, create or select an Encrust With Gems job of the desired type, then press on it.
    1.  If you want this job to cut Any Gem, choose the job you edited in the first task
2.  This time we want to edit the second Input Item - Item 2 - which is the item to Encrust.
    1.  Scroll down to Item 2, using your standard secondary scroll key.
3.  There are two things we can edit: The *type* of the item, and its *material*
    1.  The type could be, for example, statue, table, or chair; the material could be gold, platinum, iron, etc.
    2.  Or you can specify a type only, leaving material at 'any'
    3.  Unfortunately, due to a limitation in the game, it is not possible to have type:'any' and then pick a material (eg to encrust any item made of gold.) Doing so would cause the job to fail, and therefore if you try to change the material when the type is *any item*, Job Material will stop you and print a message indicating the problem.
4.  To edit the type:
    1.  Press to see the list of valid Input Items
        1.  You will now see a long list of possible items. Some of these have category headings, such as "any instrument", but most do not.
            1.  Be aware that the item type you select needs to match the overall type of Encrust job you chose - for example Furniture or Finished Goods. Don't select Any Instrument or Figurine if you chose the Furniture Type; don't select Statue if you chose Finished Goods.
            2.  Job Material will not stop you doing so, but the job will cancel and suspend due to lack of usable items.
        2.  You can scroll up/down with the primary scroll keys, or you can type to search
        3.  For this example let's choose Statue. Press Enter to confirm the selection.
5.  To edit the material:
    1.  Press to see the list of valid Materials. As mentioned above, you will only be able to proceed if you have given a specific item type.
    2.  Now you can scroll through the long list of materials.
        1.  This list is categorised; the first page you see contains some specific materials - of which the only useful one is likely to be rock - and three categories, *inorganic*, *creature* and *plant*.
        2.  The categories are labelled with a letter - for example **I** for Inorganic; press the letter to open that category
        3.  For the purpose of Encrust With Gems, you are almost certainly going to want something under Inorganic
    3.  So let's press for Inorganic, and then choose a suitable material - like gold.
6.  If you made all those changes, the UI should appear as shown on the right.
7.  If necessary we can create multiple jobs that encrust only that furniture we want - for example, only gold statues, tables and chairs. And we can do it without an intermediary, feeder stockpile (you may want to have a linked stockpile anyway, but it can now also contain other items; you don't need to set its rules only according to what you want to encrust.)
8.  We can use another DFHack feature to make it quicker to create multiple jobs: with a job selected, press : this maps to DFHack's `job-duplicate`, and does exactly what it sounds like.
    1.  It's therefore very quick to create multiple jobs: create one, copy it (perhaps a few times), then edit the new job(s), just changing the variable parameter.
    2.  For example, set up one job to Encrust Gold Statues with Any Gem, copy it four times, and edit the copies to change Statue to Chairs, Tables, Cabinet and Chests in each job respectively. A Royal Bedroom factory!
9.  One minor UI downside: on the job list (both in workshop and the master job lister) these jobs will appear as *Encrust Furniture With Unknown Material*; you will only be able to see that they're Gold Statues or whatever else by pressing on them.

### Putting it all together: using DFHack to create a high-value gem cutting/encrusting production line

Combining the above steps with jobs to Cut Any Gems (see Gem cutting), can create a (nearly) fully automatic, high value Encrusted Furniture Production Line.

This annotated screenshot shows an example:

**Explanation:**

1.  Four Jewelers are permanently cutting any/all gems that are available
    1.  Four Jewelers have DFHack-modified "Cut Any Gem" jobs: JC1 - JC4 (top left.)
    2.  Stockpile 2 (*Gems All*) gives rough gems to JC1-JC4
        1.  This stockpile can have rules only accepting rough gems of suitably high value, ensuring only valuable gems are later encrusted.
    3.  Stockpile 4 (*Gems Out*) takes from JC1-JC4
    4.  Stockpile 4 (*Gems Out*) gives to Stockpile 2 (*Gems All*).
        1.  *Gems Out* is an intermediary stockpile, necessary because a stockpile cannot both Give and Take from a workshop - its only purpose is to route the newly cut gems back to the master *Gems All* stockpile, from where they will be used for encrusting.
        2.  Or one could simply have the Jewelers performing Encrust Gem jobs (JE1-JE4) take directly from *Gems Out*, but the layout shown gives the closest proximity of stockpiles to the workshops using them; we want our peasants hauling things about, not our legendary gem cutters/setters!
2.  Four Jewelers are permanently encrusting furniture with gems
    1.  Four Jewelers have DFHack-modified "Encrust Any Furniture with Any Gem" jobs: JE1-JE4 (bottom right.)
    2.  Stockpile 1 (*Furniture In*) gives furniture to JE1-JE4
        1.  This stockpile can take from a source of furniture, such as Metal Forges. It can have rules specifying the type, material and quality of eligible furniture.
    3.  Stockpile 2 (*Gems All*) gives cut gems to JE1-JE4
    4.  Stockpile 3 (*Furniture Out*) takes encrusted furniture from JE1-JE4
    5.  Stockpile 3 (*Furniture Out*) gives to Stockpile 1 (*Furniture In*) - or at least, ideally it does; this is shown as disabled, as explained below.
3.  This creates an endless loop of encrusting. The same furniture will be encrusted repeatedly, with multiple types of different gems, ever increasing in value until the player chooses to Build some of it somewhere. (Furniture can't be encrusted with the same gem type twice, but it can be encrusted with many different gems.)
    1.  This loop can be run for perpetuity with no player input at all, creating fabulously valuable furniture.
    2.  Except there is one issue with total automation:
        1.  As shown in the screenshot, the link from *Furniture Out* giving to *Furniture In* is disabled: this is because it has been found to often result in the same small set of furniture being encrusted again and again, and any new furniture being added to *Furniture In* (eg from Metal Forges) not usually being encrusted at all.
        2.  The problem is that the haulers moving the encrusted furniture from *Furniture Out* to *Furniture In* will put it in the closest available tile of *In*; then the Gem Setters picking up from *In* will usually also collect the nearest furniture. Furniture further away in the stockpile tends not to be picked up by the jobs.
        3.  You might end up with 5 or 10 items of furniture encrusted 10 times each, and 40 other items encrusted only once, or not at all.
        4.  Given long enough it would eventually all be encrusted because no item can be encrusted with the same gem twice. But if you have a lot of gem types, this is likely to take unacceptably long.
        5.  A simple workaround for this is to remove the link from *Furniture Out* to *Furniture In*, so it will not automatically loop. Once all furniture is encrusted once, simply swap the links (*Furniture Out* becomes a Give to workshop; *Furniture In* becomes a Take from workshop) and all the furniture will go around for its second encrust.
        6.  If you prefer to keep the links unchanged, (re-)add the Give link from *Furniture Out* to *Furniture In* so that all finished furniture is hauled over, then remove the link once everything has been moved over.
        7.  This prevents total, hands-off automation, however the amount of work involved is very minor and with enough furniture (240 items are present in the screenshot example), you won't have to do this very often.
4.  In this example, we have not edited the Encrust Furniture jobs to specify the types to use; it is left at the default of "any furniture", because the feeder stockpile has rules allowing only high value furniture and we want to encrust it all.
    1.  It would be very simple to modify the jobs at JE1-JE4 such that only certain furniture - perhaps just the Statues and Doors - are encrusted.
    2.  We might thus create two or more jobs at each of JE1-JE4 instead of the one currently shown, for example: *Encrust Any Statues with Any Gems* and *Encrust Any Doors with Any Gems*.
5.  One more DFHack feature is demonstrated in the screenshot: the eight jeweler's workshops have each been given suitable names according to their intended function:
    1.  Shown in the screenshot are the UIs for workshop JC3 (named *Jewel Cut3*) and JE4 (named *Jewel Encrust4*).
    2.  This is done by selecting the workshop then pressing . A dialogue will appear into which you can type the desired name for the workshop.
    3.  The same works for stockpiles and most other buildings. It is especially useful to name both workshops and stockpiles because these names are used when you view stockpile links.
