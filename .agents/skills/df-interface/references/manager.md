# Manager

> Fonte: [Manager](https://dwarffortresswiki.org/index.php/Manager) — Dwarf Fortress Wiki (GFDL/MIT)

The **manager** is a noble that allows players to create multiple production orders, and also lets them set up profiles for workshops. This means that players can rapidly dispatch any number of jobs from a single screen, without having to add tasks to individual workshops.

## Relevant Skills

A certain set of skills are relevant for any manager. Furthermore, certain personality traits influence whether any experience is gained in the skill. There are soul attributes that affect the skills, and other skills that affect the same attributes' cross-training. The ones relevant for a manager are as follows:

| Skill (relevant for manager) |  | Personality Trait (needed to gain social skill) |  | Attribute (affected by social skill) |  |
|----|----|----|----|----|----|
| Body | Soul |  |  |  |  |
| Administrator | Organizer |  |  |  | Analytical ability |
|  |  |  |  |  | Creativity |
|  |  |  |  |  | Social awareness |
| Social - Other | Consoler | Straightforwardness (Honesty) | \> 39 |  | Linguistic ability |
|  |  |  |  |  | Empathy |
|  |  |  |  |  | Social awareness |
|  | Pacifier | Cooperation (Compromising) | \> 39 |  | Linguistic ability |
|  |  |  |  |  | Empathy |
|  |  |  |  |  | Social awareness |

The better match with the skills, traits and attributes in the table above, the better of a manager a dwarf will be. Try to avoid traits that halt experience gain for a relevant skill, otherwise time will be lost training a dwarf who will never get better at that skill.

## Office

A manager only performs their duties in their office, so it's absolutely necessary to assign them one - since only a meager office is required, a single chair in the dining room will suffice.

To set up a dwarf to be the manager and give them an office:

1.  Hit to enter the Nobles screen
2.  Select Manager and hit . Assign a dwarf to be the manager. If nobody is particularly suited to the job, picking the Expedition Leader is a reasonable choice.
3.  Build a chair somewhere, or locate an existing chair.
4.  Use the command and place the cursor on the chair. Select the option to make the area into an Office and assign your manager as the owner of the office. At this point, the red under "Manager" should have disappeared from the obles screen, and you should be able to queue up work orders.

It is trivially easy for a manager to get experience in the organizer skill. Just queue a lot of jobs to produce 30 of something, such as Collect Webs, which appears first on the list. The manager will gain experience when validating the order, not when the order is finished. You can cancel the order after it's validated, if you wish.

## Work orders

Work orders are an advanced feature of Workshop Management that becomes available with a manager. It allows easier management, automation and/or fine control of the various activities needed to maintain a well-oiled fort. The manager screen lists all work orders in the fortress, shows their status and allows to modify them and place new general orders. It is accessed from the main screen through the ob list and then the anager menu.

### Validating orders

A manager is required to coordinate work orders. The manager will need time to approve work orders before production begins. If there are at least 20 dwarves total, then the manager will need to go to their office to "validate" each work order before it is acted on. If they are somehow occupied with other things, then this might take a while, so in larger forts, you might want to make sure your manager is not overly-burdened with other labors (for example, disabling hauling and cleaning for the manager might be a good idea). The manager will also not perform their duties if socializing, drinking, eating, asleep or otherwise incapacitated (perhaps due to wounds). Managers don't require writing materials such as paper or scrolls to validate production orders.

After a production order is validated and Active, corresponding tasks will be automatically added to applicable workshops until the production quota has been met. An announcement appears when each order is completed. For repeating orders, the order then becomes inactive and the manager checks at the selected time interval for the conditions to become true again before restarting the order.

The status of orders can be checked in the manager screen — validated orders will have a green checkmark, while invalidated orders will have a red X. Job orders will remain enqueued until the manager is once again in his (or her) office. An order can have the prefix of 'Ready', 'Checking' or 'Active'. A 'Ready' order only needs to be validated by the manager to become 'Active'. A 'Checking' order is waiting for its conditions to be satisfied: it will then become 'Active'.

### Placing new orders

Work orders can be placed either as general orders through the Manager screen (and will be automatically tasked to any suitable workshops) or linked to a specific workshop through the Workshop Profile screen. To create a general order:

1.  Hit - or - to enter the Manager screen.
2.  Press to create a new work order
3.  Start typing (part of) the name of the item you want to produce. This will cause menu options that don't match the string you type to disappear from the menu.
4.  Use the directional keys to select the specific type of item you want.
5.  Enter the quantity of items you want to produce (0 for a perpetual order).
6.  Your work order will appear in the list.

On creation of that order, it can be further customized; changing the onditions for the order being fulfilled and repeated (see next sections) and adjusting the etails of an order specifying type of material used in the making of the item (if applicable). As well as emove it, raise its riority, make it max (op) priority, change its priority, or limit the amount of workshops the order can be tasked to.

Work orders are created as a one-time order. Unlike manual assignments in a workshop, these orders aren't limited to ten items, won't cancel until complete, will be automatically tasked to any available workshops, and will notify the player upon completion. Setting the max number of workshops that the order applies to can be especially useful to ensure that multiple orders for the same type of workshop (e.g. a Mason's Workshop) are worked on at the same time.

Repeating orders

An order can be set as a One-time order, or a Repeating order that will restart when completed (checked daily, monthly, seasonally or yearly). Use to adjust condition check frequency. Without conditions (see below) this is similar to making an infinite batch (quantity 0) job, though a yearly batch may be less likely to overwhelm stockpiles.

In repeating work orders, the quantity of items is treated as a batch size. The quantity is set when creating the work order, and cannot be changed without redoing the entire order. A repeating work order will not abort mid-batch due to job cancellation or failed conditions. It must wait until the end of the batch before stopping.

### Conditions

Work order conditions can be added by pressing ondition with relevant work order highlighted. This automatically sets the order to repeat (checked daily), set to activate based on the amount of an item in your fortress, or upon completion of other work orders. If multiple conditions exist, all must be satisfied for the job to start.

Be forewarned that perpetual (quantity 0) orders *only check their conditions the first time they become true*, since the (infinitely-sized) batch never completes. This can lead to confusion and frustration, as the order *will **never** stop, regardless of failed conditions*! To reiterate, quantity 0 orders start as soon as all conditions are met, and will only spam failures (but not stop) when Urist runs out of e.g. logs to turn into barrels. Any other orders at a given shop will be ignored after starting a perpetual order.

Specified item

Specified item conditions can be added using the eagents and roducts presets, which you can then tweak to your liking, or you can dd them manually. Reagents add input conditions (e.g. keep 10 wood logs before making beds), while products limit outputs (e.g. stop once 10 beds are made). For each item entry the following conditions can be changed:

- tem type - Items base type, such as: 'beds', 'bolts', 'bars', 'Plant'(used for wood), 'Boxes and Bags', or just 'item' for any type.

- aterial - Specific material such as 'obsidian', 'Acacia', 'Feather wood', 'steel' etc.

- raits - Such as food-storage items, nearby items, empty items, unrotten etc.

- umber - Change the number of items required. The number of the items (though this does not count items that are forbidden, built into something, or owned) and the ineuality, at least (\>=), less than(\), exactly(==), not(!=)).

Some useful item conditions are tricky to specify:

- "refined coal" is just simply item=bar, material=coal.
- a specific flour is item=powder, material=*required flour name* (not the *plant name*), trait=cookable.
- a specific alcohol is item=drink, material=*alcohol name* (not the *plant name*).
- "empty bags" cannot be chosen manually, but can be duplicated with item=boxes and bags, trait=empty, trait=sewn-imageless.
- trait=lye-containing item (not to be mistaken with trait=lye-bearing item which does nothing) is only available for the "make soap" job.
- item=liquid, material=lye ignores lye in buckets, but does correctly track lye in barrels.
- trait=unused cannot be chosen manually, only eagents/materials key sets it for "make clothing" type of jobs.
- trait=melt-designated does not work when chosen manually, only via eagents/materials key.

Order conditions

rder adds an entry that checks for a different order status. Set a job to only activate when another order is being completed, or another order is becoming active. For example, if you have one order to make barrels and another to brew drinks, you can add an order condition that first makes 10 barrels and then continues the brew order to brew 10 drinks. See also: Steel#Automated steel production.

Notes

- manager orders don't respect stockpile links, only workshop restrictions.
- A guide to setting up functional work orders may be found in this thread.

## Workshop profiles

The manager also allows players to change a workshop's "Profile". To access a workshop's Profile, uery a workshop, then look at the Workshop rofile. This gives you three tabs to go through: Permitted Workers, Work Orders, and Labor Restrictions. Press the arrow keys to go between the tabs.

- Permitted Workers tab allows to restrict the dwarves that can use it and the minimum and maximum skill level required to use the workshop. They can choose who specifically can use the workshop by pressing on their name to permit/forbid their use of the workshop.
- Work Orders tab allow place new orders specific to that workshop. Toggle whether or not the workshop will accept general work orders or adjust how many of them can be task to this workshop at a time. Additionally the Labor Restrictions tab allows to further restrict which general work orders the workshop can be tasked with.

Dwarves with strange moods seem to be able to claim a workshop, even if they do not meet the profile criteria.

A note of caution: workshop profiles persist^(v0.31.12) even if the manager is killed, which can lead to workshops becoming unusable if the manager is killed and the dwarves permitted into the workshop die or are reassigned. Furthermore, workshop profiles seem to be slightly buggy. Adequate (rusty) weaponsmiths have been seen using a forge with the skill min/max both set to "Dabbling". This may be somewhat irritating if peasants are undergoing training.

## Disadvantages

One disadvantage of the work order system is that no work will be performed until the manager finishes validating the order. Work order validation appears to be fairly high priority, but it's best to ensure your manager has ample free time and isn't typically called far from the office for timely order validation.

A second disadvantage is that if there is more than one workshop which can fulfill a particular job set (such as several ordinary glass furnaces dedicated to sand collection, plus several magma glass furnaces for actual glass production) then the manager will distribute the jobs amongst all those workshops. While this can be an advantage (for example, if you want to speed up the work orders by having multiple workshops), this will make it difficult to dedicate different workshops to different tasks. This can be prevented by entering the profile of specific workshops and moving to the Work Orders menu; setting "general work orders cannot task this shop" will prevent the manager from assigning tasks.
