# Scheduling

> Fonte: [Scheduling](https://dwarffortresswiki.org/index.php/Scheduling) — Dwarf Fortress Wiki (GFDL/MIT)

No matter how much you micromanage your **military**, your **squads** won't be able to get stronger or protect you from ambushes without proper scheduling practices. With practice, you'll be able to set your **soldiers** to follow a complicated annual training regimen, patrol major trade routes, defend important areas, or any combination of these... all with a few clicks.

The military is now controlled entirely through the squad menu, which can be accessed with the key or with the banner icon in the bottom right of the main game screen. A squad must be selected by using the checkbox to the right of its name to edit its schedule, and the squad must be set to the desired routine by selecting it through the "Schedule" menu. From here, all schedulable training, defense, and patrol orders are configured within the "View monthly schedule" submenu by editing monthly orders.

## Passive defense

The scheduling system is a feature that is versatile but initially difficult to understand. Once you learn the system, though, you will find that you barely need to manage your military at all. Effectively, a schedule selectable routine for a squad to follow, broken up by month, and different routines can be quickly and easily swapped in order to apply different schedules of your choosing to different squads of your choosing.

It is possible to give your squads different monthly schedules, create different routines which will cause squads to follow new user-programmed instructions depending on circumstance, give direct orders to attack one or more specific targets or move to a specific location, or follow patrol routes and stations with greater accuracy. The entire system (including routine names) is completely configurable, and in time you will find yourself using complicated scheduling to rotate squads between training and defending/patrolling specified areas over the course of a year without any user input, or to start defending the fort entrance or trade route with a few easy clicks.

There is a clear distinction between *active* orders and *passive* orders — the former is used for making unexpected orders to deal with a threat, the latter is a typical schedule that a dwarf will follow year-round and acts more as a defense method. The main *squads* menu is predominantly used for active commands, and the *Schedule* menu is used for passive commands. This article will focus on the **passive** commands you can leave your squads to follow.

For more information on **active** commands, see **Squads**.

### Routines

The **routine** is a fundamental concept of passive military management. In each routine, you can program instructions for your military dwarves to follow. The game contains four routines by default — **Off Duty,** **Staggered Training,** **Constant Training,** and **Ready**. In **Off Duty**, a squad is assigned no orders and civilian equipment. In **Staggered Training**, a squad is assigned to train and wear military equipment in alternating blocks of 3 months each. In **Constant Training**, a squad is assigned to train the entire year. Finally, in **Ready**, a squad has no orders, but is assigned to wear military equipment the entire year. By default, your squads will all be set to **Off Duty** — in this state, they will tend to spend most of their idle time in the barracks doing individual combat drills, or in the case of some dwarves, only perform civilian work. You will need to add more routines if you want them to do anything more complicated than this.

Individual squads can be set to a certain routine by selecting the squad in the squad menu, clicking "Schedule," then clicking the appropriate routine. Squads can only be set to one routine at a time, so selecting one routine for a group removes them from the previous one.

Note that civilians can not currently be assigned to orders based on military routines and may need to be directed to safety using a burrow if your fortress is attacked.

#### Making Routines

Each squad can be given multiple routines to follow for an entire year, broken up by month. Each squad has a monthly schedule for each routine; it can be swapped between these routines with the procedure outlined in the previous section. Without monthly schedules, routines would do nothing; without routines monthly schedules would be inefficient to switch between; the two functions co-exist and rely on each other. The monthly schedule screen can be accessed from the **Schedule** menu by clicking the "View monthly schedule" button. Alternatively, all monthly orders for a routine can be edited at once directly from the Schedule menu by clicking "Clear" to remove any existing orders and "Edit" to begin bulk editing.

On the main monthly scheduling page you will see the name of the squad you are currently editing in the top left, a list of months down the left side and a list of routines for this squad the top edge. Scheduling is done separately for each month and routine; to begin editing click the "Edit" button on one of the months. If you have more routines than can be displayed along the top edge, a small yellow arrow button will appear next to the routine names to scroll between them. Scroll up and down to navigate the month list, and select any visible month to begin editing it. The orders for each month are displayed in green in the month's cell.

When you've decided which month to edit, click the "Edit" button to open the order menu. From here, you can use the four buttons at the bottom to quickly assign a new order. From left to right, these buttons create a **Station**, **Patrol Route**, **Defend Burrow**, or **Train** order. To create a **Defend Burrow** order, you will first need to set up the appropriate burrow, but **Patrol Route** allows you to create and save routes directly through a sub-menu by clicking on the map, and **Station** simply requires clicking the map to select a station location. Unlike the others, **Train** does not require a location to be set within the monthly orders menu, but rather a valid **barracks** zone must be defined and the squad must be assigned to train in it. Unneeded orders can be deleted by clicking the "cancel" (red circle with a line through it) button next to each assigned order. When you have finished editing the orders, click "Done editing" to save them.

Orders have soldier-based 'order criteria' that list how many soldiers in the squad the order will be assigned to at once. Using the '+' and '-' buttons next to "Minimum soldiers to follow new order" you can choose how many soldiers in the squad that the order will apply to at any one time. By default this number is ten. If you have it set to ten, the Squad will all follow it even if the squad does not have enough members, if you set it to one, only one soldier will be required to go at a time. You can also select specific positions within the squad by using the checkboxes next to each squad position to set those positions as 'preferred'. The order will then try to pick these dwarves to follow the orders if there are multiple off-duty dwarves to choose from. When you are done, click "Done editing" to save the order and return to the monthly schedule screen. If desired, multiple orders criteria can be set for each month. For example, a squad could be set to assign two soldiers to station in the tavern, four soldiers to patrol the entrance hallway, and three dwarves to train while leaving the other three dwarves idle.

Note that the text displayed on each cell (like "Train") can be completely customized text; it does **NOT** necessarily reflect the actual orders in the cell! When you are editing an order, you can click the text box or the next to it to edit the label and save it by pressing . If you do not change this name, or if you remove all orders for the month, the cell will automatically update with the current assigned orders. It is recommended to leave the name blank if you are only giving a single order, however, if you want to keep track of multiple orders per routine per month a descriptive name can be useful.

To eliminate some of the tedium in scheduling many months, you can copy-paste orders from one cell to another by clicking the "Copy" and "Paste" buttons. Press "Copy" button in the cell you want to copy from, then go to the cells you want to paste to and press "Paste" in each one.

### Orders

''If you were redirected here while looking for information on moving your squads to a certain point on command, you may be looking for the squad movement section on the squads page. Multiple orders can be given to a squad by while editing monthly orders by selecting a new order from one of the bottom four buttons; this can be useful if you want part of a squad on patrol duty and another part training, or part of a squad training, and the other half stood down. Unneeded orders can be deleted by clicking the 'cancel' (red circle with a line through it) button next to each assigned order.

The five types of scheduling orders are listed below:

#### Inactive / no order

When dwarves have an empty spot in their schedule, dwarves with good discipline skill will visit the barracks and train themselves in their spare time - if you see a dwarf doing "Individual training" when they're free, that's what's happening. Technically this is not an order applicable in the monthly orders menu - it is a *lack* of an order. Training jobs that are not specifically ordered will be colored green in the nits menu.

#### Train

For your dwarves to train, a **barracks** must be designated. This can be done through using to open the zone menu and the blue banner "Barracks" button to designate a barracks zone. To make use of the barracks zone, a squad must be assigned to it from the zones menu by clicking the 'banner with a plus' button then using the 'bed', 'axe', 'cabinet', and/or 'chest' button to define how exactly they this barracks. Many pieces of furniture are useful within a barracks, including beds, armor stands, weapon racks, and containers. Dwarves within the squad aren't assigned any furniture in particular, so they'll just use whatever they feel like, similar to a dormitory .

While being edited, barracks can be renamed with the button, used for sleeping with the 'bed' button, training with the 'axe' button, individual equipment storage with the 'cabinet' button, and/or squad equipment storage with the 'chest' button. You can choose if a squad trains in one place and sleeps in another, or in multiple, and so on. Multiple squads can overlap with one barracks. The tooltips indicate that the individual equipment storage option will make dwarves store their assigned weapons and armor in the selected barracks, while the squad equipment storage option will cause them to store equipment designated for that squad such as ammunition when not in use.

To get marksdwarves to train in any way other than bashing each other with their crossbows, they must have quivers, an archery range, and ammunition. Archers will not fire bolts without a quiver to store them in (i.e. they will not hold a single stack in their hand). The archery range is set up for the squad via building an archery target and creating an "Archery Range" zone around it. Marksdwarves are capable of training more than archery, so if they are assigned a barracks to train at they may train without an archery range (although since this training raises archery skills much more slowly, many players attempt to avoid it). If you are having trouble getting marksdwarves to train, see the appropriate section of the Military F.A.Q. for more information.

When dwarves are being ordered to train, squad members will set up training demonstrations for particular skills, or they will have dwarves spar. Any dwarves in the squad that don't qualify for these will default to individual training.

#### Defend burrows

After a burrow has been created in the menu, you can order your dwarves to defend it. If an enemy enters the burrow (and is not hiding) the assigned squads will be alerted and attack it. It is unknown if a soldier defending a burrow is limited to his line-of-sight or is simply aware that an enemy is present.

#### Station

Stations are defined from within the monthly order "Edit" menu. Simply adjust the number of soldiers you want following the order, click the 'Station' - green arrow button, and click a point on the map where you want a squad to stand to define the order.

#### Patrol Route

Routes are made similarly to stations. Click the 'Patrol' - three red X button to open the route selection submenu, then either choose an existing route or define a new one by choosing "Create new route" then clicking at least two spots on the map and hitting "Confirm". As you define the route, a preview of the path will appear to show which order the soldiers will through the points. This preview does not reflect the exact path they will take and only shows the shortest line between subsequent points. Existing routes can be viewed and edited from the select route menu by clicking the 'Inspect' magnifying glass button. Because patrol routes can be saved and used by multiple squads, it is highly recommended to name them as you define them by clicking the text box or , typing a descriptive name, and pressing .

Routes are very useful for Marksdwarves. They don't like to resupply their ammo when faced with an enemy. If you have a route with two waypoints in the firing platform, and two bracketing the ammo supply, the dwarves will be able to find their ammo when empty .

### Instructors and demonstrations

Members of a squad with relatively high experience in a combat skill will lead the group during a training session. This can be in the form of a demonstration. Instructors gain teaching experience, while students gain student and concentration experience. Higher levels of these skills make demonstrations more effective^(source). Observing demonstrations (with typically non-existent teacher/student/concentration skills) is not as effective as practicing and sparring. To encourage sparring, create at least half as many training orders each month as you have members in the squad with two soldiers minimum for each order (i.e. a squad of 10 hammerdwarves with 5 training orders requiring 2 soldiers each).

### Individual combat drill

Otherwise unoccupied soldiers often go to the barracks for individual combat drills regardless of the routine of their squad, if the squad to which the dwarf is assigned has any Training barracks available. Dwarves assigned to an inactive squad will remain civilians, although off-duty soldiers with high discipline tend to ignore all civilian labors if training is an option. Because of this, if you want your 'reserve' squad to actually do civilian work when not needed to defend the fort, it's preferable to disable their barracks assignment.

## Frequently asked questions

*See Military F.A.Q.*
