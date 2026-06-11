# Gem cutter

> Fonte: [Gem cutter](https://dwarffortresswiki.org/index.php/Gem_cutter) — Dwarf Fortress Wiki (GFDL/MIT)

A **gem cutter** is the profession of a dwarf whose highest skill is in gem cutting. Performed at a Jeweler's workshop, gem cutting is the basis of the gem industry, turning mildly valuable gem clusters you find as you mine away rock into valuable decorations for furniture and trade goods. It is the counterpart to gem setting; together, the two belong to the category profession of the Jeweler, and indeed if a dwarf has a relatively balanced skill level in both, they will be known as a Jeweler. (More often than not, migrants who are skilled in gem cutting will also be similarly skilled in gem setting.)

Large amounts of mining are bound to produce dozens of rough gems, so gem cutting is a method of developing wealth quickly, especially for new players. Cutting and encrusting with a gem more than triples the value of the rough gem, which is then multiplied by a quality modifier based on the gem setter's skill. A masterwork gem decoration is worth 40x the value of the original rough gem.

Cutting a gem can result in a cut gem, a large gem, or a gem craft. Cut gems are the most likely, and are used by a gem setter in creating gem windows and encrusting other objects. Large gems and gem crafts are only created occasionally, and are currently only useful for trade. The skill level of a gem cutter affects the cutting speed, and quality of large gems and gem crafts, but not the quantity of crafts produced^(1).

### Training

Gem cutters can cut not only gems proper, but regular stone, glass and clay as well. Although cut stone is next to worthless, it still provides experience points, and can be used to keep a jeweler busy while you mine out a fresh batch of gems. It is also the only way to decorate with stone, and an easy way to create windows without fuel or sand.

### Automation / Advanced Control

In the vanilla game, gem cutting can be quite tedious to manage: one Workshop job is required per type of gem, and can only be started when at least one rough gem of that type is in stock. A typical fortress will likely have dozens of available rough gem types, necessitating many separate jobs - spread across many separate Jeweler's workshops due to the 10-jobs-per-workshop limit. Even when low-value gems are excluded, this will still likely result in a regular stream of jobs suspending as stock of that gem is depleted, and much manual work re-enabling them: potentially to only cut a couple more gems before the job suspends again!

***DFHack: the content in the rest of this section requires the use of DFHack***

### Advanced control of gem cutting using DFHack

The utility DFHack can mostly resolve this problem, and its features can help facilitate an elegant, automated gem cutting-and-encrusting production line (see Gem Setting for more gem-related examples.)

- DFHack provides the plugin **Job material**, which can modify the materials used by a given Workshop job
  - In the default DFHack config, the UI for Job Material is accessible by pressing when looking at a Workshop with a job selected.
  - Job Material allows the user to edit the required components for a job.
  - In the case of gem cutting, this means the specific, one-per-type-of-gem Cut Gem jobs can be turned into a generic job that will cut any and all (available) rough gems.

To proceed, first ensure you have DFHack installed and are running with its default config file in place. PyLNP users can simply set DFHack to Yes on the DFHack tab, then relaunch the game (other launchers likely have a similar easy DFHack option.)

#### Using DFHack to create a single job that will cut any gem:

1.  At a Jeweller, create a Cut Gem job for any rough gem you have in stock.
2.  With the job selected, press .
3.  You will see the screen shown to the right (the gem type will likely differ of course):
4.  This screen is showing us the Input Items for the job. For a Cut Gem job, there is only one input material - the rough gem.
    - Input items have three parameters: input item, material, and flags. Using Job Material, we are able to edit the first two of these parameters.
5.  Press changes the input item, showing the valid options for this job. In the case of Cut Gem, *rough gem* is the only valid choice, so there is nothing to change here.
6.  Press to change the material, again showing all valid options. Here, we will see many options, in a categorised list. We could use this to change this Encrust job to use a different cut gem, but we can also do that through the normal UI. Instead we want to use the first option: *any material*.
7.  Once done, the UI will look as shown on the right.
8.  Now press to finish the edit. On the Workshop menu, you will see the job is now called ***Cut unknown material***.
9.  Set the job to Repeating and your Gem Cutter(s) will now happily cut any and all rough gem he/she can get their hands on, and the job will never Suspend unless you run out of *all* rough gems. One job to cut them all.
    - Rest assured that this job will only cut rough gems: not stone, glass, or anything else cuttable by a Gem Cutter. This was ensured by editing a rough gem job, ensuring *any material* applies only to rough gems.
10. For the final touch, provide a nearby Gem Stockpile with rules set to only allow Rough Gems that you care about: e.g. high value ones. Now set this stockpile to Give to your Jeweller's Workshop(s). This can be used to ensure that the generic Cut Any Gem job we just created won't waste time cutting Lapis Lazuli and other cheap stuff.
    - Remember that when a Stockpile Gives to a Workshop, that Workshop must then be able to get *all* its items from its stockpile links. That's no problem for the Cut Gem job, but it will become an issue if you also add Encrust With Gems jobs at this same jeweler. For more information, see Stockpile, Stockpile design and Gem setter.
11. You can of course mix and match the standard specific jobs with the general one: for example if you acquire some very high-value Black Diamonds or Star Rubies you can add specific job(s) for those alongside your Any Gem job and your gem cutter will alternate between the specific and general jobs.
    - You could control the distribution of your jeweller's time by adding multiple specific jobs to go along with one single generic job: for example if there are seven specific jobs and one All, the Any job will run 12.5% (one-eighth) of the time. That way, the highest-value gems are cut the majority of the time (stock permitting) but there's still a catch-all All Gems job to ensure your jeweller is always cutting *something*.

How one cuts gems without a chisel or any other tool is a source of much study. The predominant theory is that dwarven teeth, sharpened and conditioned by years of eating the tough flesh of plump helmets, function as a crude cutting tool hard enough to cut diamonds. This is followed by polishing the gem using the tough fibers of their beards, just as it's used to smooth surfaces.
