# Manager

> Fonte: [Manager](https://dwarffortresswiki.org/index.php/Manager) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Manager

Room requirements
 

Office
Meager Office

Quarters
None

Dining room
None

Tomb
None

Furniture requirements

Chests
None

Cabinets
None

Weapon racks
None

Armor stands
None

Other

Mandates
None

Demands
None

Arrival conditions

Appointed on the / nobles screen / .

Function

Allows large production orders.

The **manager** is a useful noble that allows players to create multiple Work orders, and also lets them set up profiles for workshops. This means that players can rapidly dispatch any number of jobs from a single screen, without having to add tasks to individual workshops.

## Manager skills

The only skill that is relevant for a manager is the organizer skill. There are soul attributes that affect the skills, and other skills that affect the same attributes' cross-training. The ones relevant for a manager are as follows:

- Analytical ability
- Creativity
- Social awareness

The better match-up with the skill and attributes in the table above, the better manager a dwarf will be.

## Office

A manager only performs their duties in their office, so it's absolutely necessary to assign them one, though they only require a meager office.

To set up a dwarf to be the manager and give them an office:

1.  Open the Nobles screen by pressing n or the crown button on the bottom left toolbar.
2.  Select the  button next to Manager which will bring up a list of valid candidates in your fort; those with applicable skills will be at the top of the list. Click on the candidate of your choosing; if nobody is particularly suited to the job, picking the Expedition Leader is a reasonable choice. You will see that the Study icon (the chair symbol) for the Manager position is red, meaning their requirement for an office is not met. Exit the Nobles screen.
3.  Use the Zones tool z to paint an  Office zone in a location and of a size you desire. Once the zone is placed, and while it is still selected, press the  Assign dwarf button and choose the dwarf you've assigned to the Manager position to make this their office.
4.  Build a chair inside the Office zone you've placed. Other furniture can also be included if you wish to increase the room value, but it must at least have a chair.
5.  Once this is done, if you return to the Nobles screen you will see that the Study icon for the Manager position is now green, their need for an office met. You should now be able to queue up work orders.

It is trivially easy for a manager to get experience in the organizer skill. Just queue a lot of jobs to produce 30 of something, such as Collect Webs, which appears first on the list. The manager will gain experience when validating the order, not when the order is finished. You can cancel the order after it's validated, if you wish.

## Work orders

Work orders are an advanced feature of Workshop Management that becomes available with a manager. It allows easier management, automation and/or fine control of the various activities needed to maintain a well-oiled fort. The manager screen lists all work orders in the fortress, shows their status and allows to modify them and place new general orders. It is accessed from the main screen through the o orders menu, or the clipboard icon in the bottom left of the screen.

Work orders can also be created that apply only to specific workshops, done using the  button on the Work orders tab of the individual workshop's interface. See Workshop for more information.

## Disadvantages

One disadvantage of the work order system is that once your fortress reaches 20 citizens, work orders will not be performed until they are validated by the manager. Work order validation appears to be fairly high priority, but it's best to ensure your manager has ample free time and isn't typically called far from the office for timely order validation.

A second disadvantage is that if there is more than one workshop which can fulfill a particular job set (such as several ordinary glass furnaces dedicated to sand collection, plus several magma glass furnaces for actual glass production) then the manager will distribute the jobs amongst all those workshops. While this can be an advantage (for example, if you want to speed up the work orders by having multiple workshops), this will make it difficult to dedicate different workshops to different tasks. This can be prevented by entering the interface of specific workshops and moving to the Work orders menu; setting "General work orders allowed" to 0 will prevent the manager from assigning tasks.

## Note

In older versions of *Dwarf Fortress*, options could be set to restrict the allowed tasks at any workshop using Workshop Profiles. This feature needed the manager, but has been removed.

## See also

- Work Orders
- Workshop

       [POSITION:MANAGER]
            [NAME:manager:managers]
            [SITE]
            [REQUIRES_MARKET]
            [NUMBER:1]
            [RESPONSIBILITY:MANAGE_PRODUCTION]
            [APPOINTED_BY:EXPEDITION_LEADER]
            [APPOINTED_BY:MAYOR]
            [PRECEDENCE:160]
            [DO_NOT_CULL]
            [COLOR:5:0:0]
            [DUTY_BOUND]
            [REQUIRED_OFFICE:1]
