# Time

> Fonte: [Time](https://dwarffortresswiki.org/index.php/Time) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a discussion on the greater passage of time as measured in days/weeks/months/years/ages, see Calendar*

**Time**, in the lower-level "unit-based" sense, is an integral part of any simulation, nonetheleast in one as complex as *Dwarf Fortress*. Time is measured internally in units which the Adventurer key bindings menus call "instants", but are commonly dubbed "ticks" by the community. Each tick represents one step in the *Dwarf Fortress* program, requiring calculations related to unit movement, fluid movement, temperature transfer, various event checks, combat checks, pathing checks, job changes, experience ticks - basically everything required to run the program, broken up between individual lumps of time. These ticks are then bundled up into days, months, seasons, and then finally years under the dwarven calendar, which, eventually, add up to individual, context-sensitive ages.

## Basic mechanics

As explained above, in-game calendar time is amongst the many things that are processed over the course of a **tick**. The passage of ticks in fortress mode can easily be observed by pausing the game and pressing ., which causes exactly 1 tick to pass by. The adventurer mode equivalent is achieved simply by pressing , (as opposed to ., which results in the passage of 10 ticks).

Every tick causes the in-game clock to advance by a specific quantity of time that varies depending on the game mode. In adventurer mode, 1 tick moves time forward by 0.5 seconds, whereas in fortress mode this causes 72 seconds to pass by. Thus, the simulation of time runs 144 times faster in fortress mode on a per-tick basis [1]. This disparity is a game design choice, with the faster pacing enabling fortress mode players to more easily observe their fort over the years, witnessing events that'd take an immense amount of real-life time to unfold if the adventurer mode scale were to be used instead.

|  |  |  |
|----|----|----|
| 1 second | = 1⁄72 tick |  |
| 1 minute | = 60 seconds | = 5⁄6 tick |
| 1 hour | = 60 minutes | = 50 ticks |
| 1 day | = 24 hours | = 1200 ticks |
| 1 week | = 7 days | = 8400 ticks |
| 1 month | = 4 weeks | = 33600 ticks |
| 1 season | = 3 months | = 100800 ticks |
| 1 year | = 4 seasons | = 403200 ticks |

**Calendar time in fortress mode** {style="width:300px; float:left; border-right:1px dotted black;margin:0px 10px;"}

|          |              |                  |
|----------|--------------|------------------|
| 1 second | = 2 ticks    |                  |
| 1 minute | = 60 seconds | = 120 ticks      |
| 1 hour   | = 60 minutes | = 7200 ticks     |
| 1 day    | = 24 hours   | = 172800 ticks   |
| 1 week   | = 7 days     | = 1209600 ticks  |
| 1 month  | = 4 weeks    | = 4838400 ticks  |
| 1 season | = 3 months   | = 14515200 ticks |
| 1 year   | = 4 seasons  | = 58060800 ticks |

**Calendar time in adventurer mode** {style="width:300px; float:left;"}

#### Framerate

How quickly time *appears* to pass in your game, especially in fortress mode, has as much to do with your hardware as with the number of ticks in a year. The number of frames per second is a direct reflection of how many ticks a second your processor is working through. This should be distinguished from the frame *refresh* rate, which is how many frames appear on your *screen* per second. You can set your FPS to be visible by changing `[FPS:NO]` to `[FPS:YES]` in your Init.txt file, which will display two numbers in the top-right corner of your game window, the first being the frames per second and the second being the refresh rate (which is capped at a lower value by default). By default the framerate is capped at 100 FPS, but this setting can be changed or even removed: see here for a technical discussion. For tips on maximizing framerate, see the (topically named) Maximizing framerate article.

*Dwarf Fortress* is an *extremely* processor-intensive game, and so how many frames you actually get per second will depend on the strength of your machine, how far into the game and how much clutter there is in it, whether or not you are taking any FPS-saving measures, what mods or other programs you are running, and so on. Regardless of mode, there are 28 days in a month and 12 months in a year. Assuming an FPS of 100, not counting pauses an hour of fortress mode gameplay will translate into a year in-game.

- At 100 FPS:

1 day = 12 sec ; 1 month = 5 min 36 sec ; 1 year = 1 hour 7 minutes 12 seconds

- At 60 FPS:

1 day = 20 sec ; 1 month = 9 min 20 sec ; 1 year = 1 hour 52 min

- At 30 FPS:

1 day = 40 sec ; 1 month = 18 min 40 sec ; 1 year = 3 hour 44 min

In dwarf mode, the game starts with some announcement checks and considers autosaves, etc. A lot of the rest doesn't happen every tick. Every hundred ticks, for instance, it'll check job assignments and strange moods. Armies are moved on the world map. Every hundred ticks (staggered from the job check), it handles job applications by dwarves, a kind of invisible auction that it uses to manage the various competing priorities. Every ten ticks it advances the seasons, which actually does all kinds of things with the weather and map (both locally and in the world), and it also does a check for certain plot element advances (diplomats, sieges, etc.), and it checks whether your fort is still alive.

Then it hits some things that it does every tick. Fluids and other map tile information is advanced (though there are various optimizations here so that not every tile is necessarily checked every turn, and there are various flags so that entire sections of the map can be skipped if nothing has happened.) Vermin running around are updated. Other 'events' on the map, like active fires, are handled.

If a flag is set, wounded/thirsty/hungry dwarves that can't care for themselves get an update, and every so often, dead dwarves 'think' about their burial arrangements so that jobs can be set. Caged and chained creatures update their thoughts and situation periodically. Then, creatures leave the map (if they are set to) at the edges.

Every fifty ticks, staggered from other updates, all of the taverns, temples, libraries, etc. get their information updated. Stockpiles, staggered on a different tick, also work this way. Similarly with storage job creation, though that process is complicated with various optimizations and lengthening ping times and so forth, and it's still slow, since at some point, 50,000+ boulders will cause trouble.

Every thousand ticks, objects that have been marked for deletion and removed from the game are actually deleted and freed. This happens more often with items, every fifty ticks, along with a building use check (mostly updates for wells and some other flags that often need checking.)

We hit another every-tick update at this point. Projectiles are moved, and activities (ranging from dances, to martial training, to storytelling) get updated as needed. Dwarves and other creatures decide on and advance their immediate actions (movement to an adjacent tile, working at a workshop, etc.) -- the bulk of their AI (outside of job selection) is here.

Every hundred ticks, items are rotted. Every tick, vegetation is advanced (though there are various staggers and flags here). Building states are updated every tick as needed, and minecarts are moved. Hauling routes are advanced. Temperature is updated (there are various optimization flags here, but this is still an unfortunately slow process).

Finally, the camera is updated to follow the creature you are following, if any.

## Physics

For projectile physics, such as dwarves being thrown from a bridge, ticks use an assumed duration of 1/10 seconds, together with an assumed tile size of 2m wide by 2.8m tall. This is derived by monitoring the internal memory for thrown dwarves, which have a vertical speed that reduces by 0.035 tiles per second, and the fixed point math works in units that assume a tile to be 100,000 units wide by 140,000 tall. Using a gravity value of 9.8m/s2 and a tile size of 2x2x2.8m results in exactly 10 ticks per second with no rounding needed, so it's safe to assume that this is the unit value intended by Toady.

Using this value for ticks results in a day being a very short 2 minutes, and a year being 46 days and 16 hours.

## Applied mechanics

### Syndrome effects

Syndrome effects are defined by creature effect tokens, which use ticks as a basal unit. This value always operates at the same rate as fortress mode ticks, even when playing in adventure mode (meaning in the latter mode, 1 syndrome tick passes every 144 ticks). An example token would be `[CE_NECROSIS:SEV:300:PROB:100:LOCALIZED:VASCULAR_ONLY:RESISTABLE:START:50:PEAK:1000:END:2000]`, of which the `START:50:PEAK:1000:END:2000` end-line defines the timeline of the syndrome's effects. On a timer, `START` tells you how many ticks will pass before the poison starts to take effect, `PEAK` will tell you when it will peak, and `END` will tell you after how many ticks it will end. A syndrome that lists its effect as starting at "5" means that for all but the fastest characters, you will begin feeling the effects as soon as you take a step. "50" means 50 time units (or about five steps), and "500" reliably suggests that you'll be able to stagger all the way back to the hospital before your brain starts pouring out of your ears. Syndrome effects are stacked, and can cause short-term, medium-term, *and* long-term damage; for specifics see Syndrome.

### Plant growth

Plants use a `[GROWDUR:#]` plant token to constrain their growth times. Each `GROWDUR` unit (short for "grow duration) is equivalent to a hundred ticks. The default value is 300 and it is usually set to 300 or 500 (30,000 or 50,000 ticks) for crops; there are 1,008 `GROWDUR` units per season.

Additionally, plant growths such as leaves, flowers, and fruits express their time ranges in ticks - a flower that blooms on the first day of Summer would have a start tick value of 100,800.

### Hive harvesting time

Vermin in hives which produce items (currently only honey bees, which produce honeycombs and royal jelly) have the `[HIVE_PRODUCT:#:#:I]` creature token. The first variable is the number of the item produced, the second is the time in ticks that it takes for the item to be produced, and the third is an item token for the item produced. When multiple products are expected, multiple such tokens are used.

### Aging and lifespan

## Clocks

Based on the fact that pressure plates take 100 ticks to reset, some people have built various time-keeping devices to do various things around the fort, like flooding a trap once a month, or just for fun.

|  |
|----|
| "Time" in other / Languages / Dwarven / : / ashok / Elven / : / nela / Goblin / : / aspsa / Human / : / atir |
