# Adventurer mode gameplay

> Fonte: [Adventurer mode gameplay](https://dwarffortresswiki.org/index.php/Adventurer_mode_gameplay) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

*This is a detailed description of Adventurer mode gameplay. For a general overview of Adventurer mode, see Adventurer mode.*

## Common UI concepts

### About key symbols

This wiki uses symbols that look like t or t to indicate what keys or interface buttons are used for an operation. Note that keys are **case sensitive** and to save space, Shift+t is shown as T. So t means "press the 't' key without the shift key" and T means "hold down shift and press the 't' key". Lowercase and uppercase keys will often perform different functions, so it is important to use the correct key. Sequences of keys will be in separate boxes, so abC means "press 'a', then press 'b', then hold shift and press 'c'"; while bT means "press 'b', then hold shift and press 'T'. A plus sign '+' between the boxes means to press them all together, so Shift+Enter means to hold shift and press 'Enter'. Other separators, such as ',' or '-', might be used but mean the same as no separator: to press the keys in sequence.

Keybindings can be seen and changed on the Keybindings tab in the Settings menu.

### Menu navigation and selection

|  |  |
|----|----|
| Esc or right mouse | Go back to the previous screen/menu |
| Mouse wheel | Scroll menu one line |
| Shift+mouse wheel | Scroll menu one page |
| Left mouse | Select menu option |

Esc or right mouse will almost always return to the previous screen until you get to the top level of the UI, at which point Esc will display the options menu.

## Moving around

### Local movement

An image of normal travel mode. A list of the closest (but not necessarily close) sites is in the top-left corner. On the right side are minimaps of the next two levels down, relative to the player. Along the bottom is information about the player.

|  |  |
|----|----|
| 8 2 4 6 7 9 1 3 | Move |
| ↑ ↓ ← → | Move |
| Alt and a direction key | Move carefully / Deliberately enter dangerous terrain |
| Shift+\ or Shift+5 (num lock off) | Ascend |
| Shift+\> or Ctrl+5 (num lock off) | Descend |
| . | Wait for 10 instants |
| , | Wait for 1 instant |
| s | Stand or lie down |
| m | Open movement speed menu |

Unless your character is an outsider, (*and that your chosen race is even OUTSIDER_CONTROLLABLE to begin with, ie, that you perhaps did not mod such a thing into the creature tokens beforehand*), you will start out in a race-appropriate town or hamlet; in the standard tileset, the @ sign is your character. The directional keys allow movement, diagonal movement being particularly important, especially when chasing or running away from things. Use Alt+direction to enter water, jump off of cliffs, or otherwise attempt to enter anything that you can't enter using normal movement commands. Note that when entering water, it's best to enter the actual water, *not* the open space over the water, as in the latter case you will fall in, causing you to become stunned, which may lead to drowning (*if you are not at least an Adequate swimmer*). If you hit j, you can jump, being mostly useful for getting to the far sides of gorges and crevices. Occasionally, you can manage to jump onto an opponent and tackle them, which typically causes them to go flying a short distance. Note that not every creature is able to jump. Hitting . allows you to stay in one place and wait for other things to move. , does the same but with a tenth of the time it takes for ..

Use s to sit/lie down. Moving while laying down (crawling) will let you move past NPCs which are standing in your way. Also note that you will frequently get knocked to the ground in combat, and if you don't hit s to stand back up, then you will crawl slowly along the ground, giving your opponent a lot of opportunity to attack you.

You can press m to set gait and S to toggle sneak mode – it will allow you to move around invisibly, limited by your Ambusher skill and nearby creatures' Observer skill. Enemies will have sight cones indicating where they can detect a sneaking adventurer – the central zone of sight (red, violet, or cyan) is where they will see you immediately and begin chasing you; their peripheral vision (yellow) is where they might see you. Violet and cyan central zones indicate the enemy is on a different level than you, while red means they are on the same level. Staying out of sight will allow you to silently assassinate your foes, as they rarely seem to notice a knife in the back in time. Note that sneak mode is also affected by a variety of other factors detailed on the m movement screen, such as light level and weather.

If you press h to hold onto a wall or tree, you can climb the wall or tree by using the movement keys – in towns and tamer parts of the countryside, this isn't particularly useful; however, in a combat situation, climbing a tree or wall can give you a height advantage, possibly allowing you to dive-tackle your opponents. Sometimes, mountains will be too steep to walk up the edge, or you will find a deep drop into a ravine. In these cases, you will have to climb up to reach the top, or perhaps jump or climb down one face, and then climb up the other.

### Fast travel

Fast Travel screen. The player is in a hamlet, between the houses to the right and the mead hall in the top-left area of the map. The asterisk represents a group of creatures (in this case unfriendly goblins). The world map (in sepia) is on the far right.

|  |  |
|----|----|
| T | Fast Travel |
| d | Exit fast travel mode |
| K | Display detected tracks and odors |
| c | Toggle display of clouds on region map |
| S | Walk around in sneak mode. Exiting fast travel starts you in sneak mode. |
| m | Cycle through maps and significant structures |
| Q | View Quest Log |
| Z | Bring up sleep menu |
| h | Hide parts of the bottom bar |
| \> and \ | Enter/exit tunnel |

Entering Fast Travel mode will allow you to move large distances in a single keypress. Of course, the same amount of time will go by and you can also be interrupted (ambushed) while moving in fast travel mode. Along the top of the map is a line showing the sky, and position of the sun and/or moon from west to east – this primarily helps you determine how long you have before it gets dark, at which point you won't be able to see very far, will risk getting attacked by bogeymen if in a darkness or nightmare-aspected area, and will be more vulnerable to attack in general. If you are not near any sites, the m key will toggle a world map, colored in sepia tone (matching the map you see in the quest log). If you are near a site, then m cycles between a list of significant structures where your player is, a regional map (matching what you travel on when away from any site), and the aforementioned world map. The c key will only show clouds on the region map (the one you travel on outside of sites). Some clouds will be visible regardless of the state of this option.

The h key will cycle through various amounts of the bottom bar of content hidden. The effects of each press are:

- 1 press: hide key reference. Allows you to see status effects on your character if obscured by the key list.
- 2 presses: hide most local name, reducing the bar to one line of text.
- 3 presses: hide less local name, eliminating the bar entirely.
- 4 presses: shows all information

## Status and information

|  |  |
|----|----|
| l | Look around |
| Space | Advance/Clear Messages |
| a | View Announcements |
| z | Status |

### Looking around

If you're not sure what a tile is, the look command will tell you. In addition to being useful for identifying tiles and creatures, you can also view creatures' equipment and what items are sitting on the ground in a given tile. If in doubt, try the look command.

Move the cursor to the tile you want to look at using direction keys and Shift+direction. It's possible to look up and down z-levels (assuming you have line of sight) using the \ and \> keys. This, for example, allows you to find out if any flying creatures are above you. Hit Esc to exit look mode and go back to movement mode.

### Messages

The game makes frequent use of messages on the screen to tell you what is going on. If there are a lot of these you may need to use Space to display the rest of the messages that won't fit on the screen. You can always go back and view old announcements by pressing a.

### Status screen

The status screen z shows your skills, attributes, wounded body parts, health (along with more detailed descriptions of your wounds), lets you view your description, and change your nickname if you want.

### Saving the game

Hit the Esc key at any time and select Save Game to save your game. You can then come back to it later by using the Continue Playing option in the main menu.

## Searching and manipulating

|  |  |
|----|----|
| u | Interact with building, furniture, or mechanism |
| L | Search the nearby area very carefully |

The u key can be used to do stuff like pull levers in an abandoned fort. It is also used to lower and raise the bucket when standing right next to a well, so you can get water to refill your waterskin with. You can also access this through the context menu.

L will perform a thorough search of the area that you're standing in, possibly revealing some small creatures.

## Managing equipment

|  |  |
|----|----|
| i | Show Inventory |
| d | Drop an item |
| g | Get (pick up) an item off the ground |
| p | Put an item into a container |
| r | Remove an item you are wearing or from a container |
| w | Wear an item |
| I | Interact with an object in an advanced way (unstick a weapon, refill waterskin etc.). |
| q | Sheath your weapons and shield. (Frees your hands for tasks such as climbing or grabbing) |

### Inventory

Press i to display a list of what you are currently carrying. Press - +  \* / to scroll thru the list. This list will show you if items are being worn, held in hands, stuck on your body, or are inside a container. Detailed information about an object can be viewed by pressing the key associated with the item.

### Getting/dropping things

You can d drop items out of your inventory, as well as get items on the ground on the same tile that you are standing on. If there is more than one item a menu will be listed. Press - +  \* / to scroll the list if the list is too long to fit on the screen. Note that getting something makes your adventurer pick something up with his or her hands. This often means that you have to use q to sheathe whatever you have in your hands before you pick something up. If you do not have a backpack or some other way of storing the object, your adventurer will not pick the item up.

g will also allow you to ignite foliage/any flammable objects adjacent to you. Campfires aren't (yet) as devastating as one might imagine, but they will cause (most) enemies to path around them, making your crowd control techniques slightly more effective when taking on multiple enemies. As an added bonus, it will also surely piss off the elves.

### Containers/wearing

Items can be placed into containers with p and removed with r. Items can be worn using w and removed using r (the same command used for removing from containers). If an item you want to wear does not show up as an option, then it means you are already wearing too many items in the location used by that item. Try r removing items in that location and then wear them again in order of priority.

*Note that "large" or "small" clothing items are too big / small for your race* (e.g. a **large** giant cave spider silk sock). If you have that problem, try getting clothing from a different source. Looking at the article will reveal which race it has been fitted for.

After acquiring armor from one source or another, you'll most likely want to equip it. To do this, first make sure it is in your possession--not on the ground. You can then wear it, granted you don't already have too much on that equipment slot already. You can remove or drop inferior equipment as necessary.

See Armor for more information on wearing things. One thing to note in particular, items worn on the same location can stack in many situations, for example a copper mail shirt and a copper breastplate.

### Wielding

There is no command for wielding items such as weapons in specific hands. Instead, they are automatically equipped when you either g get them from the ground or r remove them from your backpack - provided the hand that would wield them is free. So in order to change weapons or shields you should drop items or place them into containers (such as your backpack) until your hands are free, then get items from the floor or remove them from containers which will place them in your hands. For example, put all items into backpack, remove sword from backpack, remove shield from backpack. The items will end up in the right and left hand. Simply remember the r remove command and the p put into container command.

While normally, one would only be able to equip one item in each hand, removing items from your inventory results in them being wielded regardless of whether one's hands are full.Bug:9817 This is especially useful with shields, as every shield will contribute a block chance to each incoming attack.

Once equipped, weapons and shields can be quickly drawn and sheathed with q, instantly preparing for attack or freeing your hands. Any number of weapons can be strapped, but only one for each hand will be drawn. Others can be manually r removed for use, and stowed again without occupying other inventory containers.

It should be noted that *Dwarf Fortress* does not enforce one particular hand as dominant for everyone (e.g. some characters may be left-handed), so do not be surprised if your character holds the weapon and shield in hands you yourself would not hold them in.

During advanced combat interactions, it's worth noting that the first item you picked up with empty hands shows up at the top of the interaction menu. This means picking up a shield first will mean pressing a will bash with the shield. Being consistent in the order you equip weapons will allow you to easily memorize attacks.

### Advanced interaction

The I key allows "complex interaction" with objects in your inventory, used for removing arrows and weapons stuck in wounds, which will appear in your inventory when they become stuck in you. Removing stuck arrows can cause bleeding, so it is not always a good idea mid-combat, but stuck objects will slow you down as you are encumbered by their weight. It's best to remove them as soon as possible when it is safe and you are not in danger of bleeding to death.

Advanced interaction can also be used to steal enemy equipment. Use wrestling to grab hold of a piece of enemy equipment, such as their weapon, or a helmet protecting their squishy brain, and it will appear in the advanced interaction menu. Simply grab the item with a free hand and pull away. If successful, you will now be holding that item in your hands.

This command is particularly useful for getting water. When standing next to a well you press the u key to lower, then raise the bucket, which gets 10 units of water in the bucket. Then you can press the I key to fill your waterskin from the full bucket (alternatively you can press the e key to drink directly from the bucket).

Advanced interactions can be used next to a campfire to heat things, such as any frozen liquids you have in your inventory (or snow lying on the ground) and need to drink. You can refill waterskins from a nearby liquid source as well

### Sheathing

The q key lets you strap your weapons to your back, useful because you can't climb or wrestle with your hands while holding weapons or other objects. People will also be less likely to be scared of you on first sight, if you don't appear to be ready to attack. Keep in mind that while strapping will put away *everything* you have in your hands, pressing it again will only cause you to put items into hands that are currently empty, meaning if you had multiple items in one hand, you'll have to r remove them manually to use them again.

## Time and weather

|  |  |
|----|----|
| D | Date |
| P | Temperature |
| W | Weather/Time |

The game has a day/night cycle, with time passing as various actions take place. When using fast travel mode, the top line of the screen will indicate the position of the sun in the sky with a yellow "☼"; Further to the right of the screen is earlier in the day, and further to the left is later. In local travel mode you'll have to use the W command to learn the position of the sun, when you're in a place where the sun is visible. At night you won't be able to see nearly as well, and you will be more vulnerable to ambush. The game also has weather and temperature. The most common weather you'll experience is rain, which is shown as blue moving dots on the local travel screen and will, unsurprisingly, cause everything outside to become wet. Temperature is important, because if it happens to drop below freezing while you're swimming through water, you'll instantly die from being encased in the ice. Therefore, you might want to keep an eye on the temperature while swimming, especially if it's getting cold. Also, unlike fortress mode, rivers/other bodies of water can be liquid during the day, and freeze at night. The cycles of freezing can also be erratic from day to day. Freezing weather can also freeze liquids in your inventory solid, making them undrinkable. If your water freezes and you are thirsty, make a campfire and Interact with your waterskin to heat it over the fire and melt the ice.

## Sleep

|  |  |
|----|----|
| Z | Sleep |

Eventually, your character will become Drowsy, and this will get worse until you get sufficient sleep.

Sleep does not necessarily have to coincide with night, but if you're traveling alone when night comes, you'll be in danger of being attacked by bogeymen. To avoid this while traveling solo you need to make it to shelter before nightfall and sleep the night away inside a building or abandoned lair. Enter a building, use k to talk to one of the speaking-peoples, and ask for permission to stay the night. Next, press Z to sleep, d to sleep until dawn, then Enter to confirm. (**NOTE**: If you stay the night in a castle, you have to sleep in the keep which houses the lord/lady of the castle. Sleeping inside the castle but outside the keep still leaves you vulnerable to attack.) Sleeping on an ocean beach also prevents bogeymen from attacking. (If you'd rather not deal with bogeymen, you can disable them by generating a world using advanced world generation and setting "Number of Bogeymen" to 0)

Though sleeping inside can be safe, it's also limiting: any quest site you want to go to has to be within a daytime's round-trip time of a safe habitation, and you have to make your way there by hopping from one habitation to the next, sleeping at each along the way. A way to avoid this is to travel with companions. If you have any companions with you, then bogeymen won't attack you. You'll still have to sleep at night, though, both to avoid sleep deprivation and because there's no visibility at night. You can still be ambushed at night by wildlife, but that's much less likely than being ambushed by bogeymen when traveling alone. If you find yourself alone at night with nowhere safe to sleep, the safest bet is to keep traveling until dawn, even if that means running around in circles. You will eventually feel unwell from sleep deprivation, but this can take a considerable amount of time. You can make up for lost sleep once you've found your way to safety. Note that sleeping in lairs, shrines, and labyrinths makes you safe from ambush, assuming that you or someone else has killed whatever was living there. If you have sufficient shrines/lairs/etc between you and your goal and they are either uninhabited or inhabited by things you are capable of killing, then you can travel from lair to lair, using each as a safe lodging. This is much safer than sleeping out in the open, day or night, even with companions.

If no other options are available, completely surrounding yourself with campfires will keep night marauders at bay as they cannot pass through the fires; the fires will go out after several hours and enable you to move on (you may also be able to jump over the fires). The bogeymen or other enemies may be outside your line of sight, which will prevent you from firing arrows or throwing things at them. In this case, you will have to ~~perform music, preferably playing guitar~~ stand up and lie down s or wait 10 ticks . repeatedly until the enemies wander into your range, the fires go out and the enemies can path to you, or dawn breaks. It should be noted that, as of DF2014, climbing trees and sleeping on them will sometimes prevent bogeyman attacks, as well. This is especially useful if you prefer to play solo, and do not wish to have an army of followers in your employ. This is also useful if you prefer to engage enemies at your own pace (such as via stealth), rather than having your entire following party immediately charge at anything that is hostile to you. Be wary though, as bogeymen may still be able to reach you by climbing or flying.

## Food and drink

|  |  |
|----|----|
| e | Eat or drink something |

To find water, you must find a river, stream, or well in a town and fill your waterskin (or any container) from it, or drink from it directly. Water that may be covering you or your items will not be able to satisfy your thirst. Note that drinking vampire blood will turn you into a vampire instantly. You can only eat and drink up to stomach capacity; after that you become increasingly nauseous and unable to retain your stomach contents (though if you needed a source for vomit, that's one way to acquire it.) You can reset stomach capacity by offloading the map (travel, rest, wait, etc.,) which can only be done in safe locations and circumstances. Over time, food contents are converted to stored fat, even if you remain active, and this will increase your fat layer mass and potentially reduce your speed. Fast traveling also resets food contents (as of v: 43.03) though the hunger and thirst timers are still satisfied by consumption. If you find yourself in need of both food and hydration, make sure to take care of the most urgent problem first, as if you are moderately hungry but severely dehydrated and eat three times, you may die before you have another chance to drink. If the temperature is low enough that you might have trouble finding liquid water, snow and ice can be heated into water by first making a campfire with g and then performing an advanced interaction with I on the ice or snow in your inventory to heat it. Advanced interactions with your waterskin (or any container) can also be used to gather water from water sources, or snow from the ground.

### Announcements when eating

When eating or drinking, the following announcements will be displayed:

- (nothing): You can eat or drink more no problem.
- You are starting to feel full: You can eat or drink *one* more time, but any more than that will cause problems.
- You feel really full: (Exactly what it says on the tin. This is as much as you can eat or drink at the moment.)
- It's too much! You might not be able to keep it down: You've eaten/drunk too much, and will likely vomit.

## Combat

*Main page: Combat*

## Talking

*Main page: Talking*

## Companions

|  |  |
|----|----|
| c | View companion interface |
| TAB | Change to another party member |
| E | Activate party tactical mode |
| k | Talk |

There are three main types of companions: party membersv0.47.01, hearthpeople and regular NPC companions. Mounts and pets are other types of companions.

Use the c key to open a list showing your companions and their position relative to you. That location is shown as a compass direction, the color of which indicates a rough distance with greens being closest. (\*\*\* means they are on the same tile as you.) A - or + after the direction indicates that they are on a z-level below or above you. This can be useful if one of them runs off and you want to find them. You can select a specific companion who is in visual range to view them, which is similar to selecting them with look, and useful to see their wounds or what they are carrying.

If a companion is too far away from you, they will no longer be shown on the list. You may be able to track them with K and looking at the displayed tracks. You can try waiting for an hour Z-(w-/-/-Enter) to see if they catch up to you. Or you can T fast travel to see if they show up as a \* near you. If you move towards the \* and it disappears, that may mean they are on the same region tile - stop traveling (d) and try to find them.

If you keep losing companions while crossing rivers, try finding a bridge or following the river upstream until it becomes crossable in fast travel mode.

### Party members

Party members are characters created before beginning the adventure. To add another member, press N on the last page of character creation (Mounts and pets). The limit on how many can be created is not known. Party members are limited to the ones you've created and NPCs can't be added to your party later in the game.

In game, you can switch control to the next member with TAB or pick a specific member to control with c then TAB. The name of the currently controlled member is shown on the status bar at the bottom of the screen (left side, top line). The screen will also center on the current character and when pressing l to look, the flashing X cursor will start on the current character.

You can activate party tactical mode with E. Normally, you control one member, and the others will act on their own; in tactical mode you can control all or some of the party members. You can set which ones you control with c then E. In tactical mode, after you select an action for the current member, control automatically passes to the next player–controlled member. Once all player–controlled members have actions selected, time will progress. Once one or more characters' actions have completed, control will pass to the first of those. Although most useful for combat, tactical mode can be used at any time. For example, having a conversation between two player-controlled party members in tactical mode allows you to control both sides. (Though this can be a bit confusing, since everything said will be labelled as being said by You: ….)

### Hearthpeople

Hearthpeople are NPCs who have sworn allegiance to you, as opposed to regular companions (who usually join your party as part of a mutual agreement) and party members (who you control). In order to gain hearthpeople, you should become a lord of some kind, which usually means claiming a site with no other competing claims. The easiest way to do this is to build and claim a camp; once you are a lord or lady of a site, you can recruit hearthpeople to your cause. Hearthpeople will not follow you around in your adventures, instead patrolling your site. They can also build for you,\[Verify\] and will side with you in case of conflict.

You may also gain hearthpeople if someone with a nobility title gives it up for you, which they can be made to through a common dialogue exploit.

### NPC companions

NPC companions are those who follow you around after they've accepted your offer for them to join you. Your character will have a limit on the maximum number of companions they can have at one time, based on their reputation level and the *Social Awareness* attribute. Companions that are not currently with you do not count towards that limit. With average social awareness and the maximum level of fame, the limit is 19 companions. Creatures with no military skills, or those with higher skills than you, are unlikely to agree to join you. However, the average soldier will join you "if you lead \[them\] to glory and death". Be careful, though, as joining you does not immediately mean they are loyal to you; if you turn around and start attacking their friends, they'll cancel the agreement. Companionship does seem to eventually rewrite old loyalties, although it takes some time.\[Verify\]

Companions keeping their loyalties has the unfortunate side-effect of them rarely respecting ceasefires, so yielding enemies are pretty much doomed. On the plus side, at least you are unlikely to be blamed if your companion murders people.

You can give or take equipment with an NPC companion by choosing to talk to them and selecting Exchange, give or take personal items. It is important to note that they prefer to store exchanged items in a personal container rather than to equip them. You must convince your companions to trade away any containers (pouches, quivers, backpacks, etc.) as well as the equipment that you are attempting to replace. Once you have given your companions almost no choice in the matter, they will equip the new items and a message like The Swordsman reorganizes his possessions will be displayed.

You can have NPCs join you as performers, after you convince them of your skills. This can be used to recruit those you normally couldn't recruit, such as civilians and stronger soldiers. What exactly is required to convince someone to join you is unclear, but reputation seems to factor into it. Even a totally unskilled performer can eventually convince eligible NPCs, simply by repeatedly spamming performances in front of them. (NPCs will not move away from performances, in fact, if they start moving while you're starting one, they'll take a step back to their previous location, once you begin. They may, however, fall asleep.) Enough performances, even if they never get a single reaction above "pretty good", should convince almost anyone. This method makes obtaining the maximum number of companions much easier, allowing you to have a mob of dancing companions.

#### Undead followers

If you have necromancer abilities, you may raise corpses as undead, who will then be listed in your companion list. Basic undead with no soul are not capable of talking, building, or indeed doing anything other than loosely following you around and attacking anything living on sight, including your other living companions. As your abilities give you the night creature status, undead followers will never attack you, even if you attack them - instead, they will all turn neutral. If you raise a corpse as intelligent undead, it will retain their pre-existing loyalty links from when they were living and not necessarily be loyal to you - this means that enemies you've slain in combat will attack you again if you resurrect them this way. To override this behavior, you should first raise them as basic undead, which destroys their souls (and associated links), 'kill' them again and re-raise them again.

### General information

The information in this section applies to all types of companions. If they survive long enough, companions are capable of levelling attributes and skills, and having a job title change; which also happens if they gain enough reputation.

Your companions will continue to follow you and fight hostile creatures around you, until they die (if you asked them to join you on an adventure) or get you to the proper location (if you asked them to guide you to some place). If you want to get rid of your companions at any time, the safe way is to talk to each one of them, ask them about their journey with you, and then cancel the agreement.

Companions can be instructed to stay where they are by talking to them and selecting Ask listener to wait here under the Ask favor, place request, make demand or issue order menu. Your companion will stop following you and wait where they are, until you talk to them again and select Ask listener to follow you. This can be useful if you need to leave a companion behind temporarily, such as when you are entering an area that you know will be too dangerous for your followers. Note that your petsv0.47.01 will also obey this instruction.

Companions can be assigned to zones in camps, with b-z-a. This is where they will spend their time when at the site and not travelling with you.

## Personal finance

### Trading (barter)

In human towns (not hamlets or castles), you can find shops; in elven trading-trees you can find markets; and at depots in dwarven fortresses, you can encounter brokers. Once you're inside of a shop and right next to any of the NPCs, you can use k to Trade with them. Use Enter to select which items to trade, left/right arrow keys to switch between the list of shop items and your items, and up/down arrow keys to scroll through the lists. You can also either ask for or offer currency as part of the process. Once done, press t to trade. The shopkeeper won't get angry if you're not offering enough in trade, so you can start offering just a few items, keep trying again with a little more until the trade is accepted. After trading, you will find the stuff you gave on the floor at your feet, and the stuff you got in your inventory.

### Theft

You may also pick up the item before buying it, but you should never walk out of a shop carrying an unbought item, as that is theft, punishable by death if you are caught, and exile if you are not. On any occasion when you have stolen goods from a store (indicated by dollar signs on either side of the item in your inventory), the game requires you to exit the site *and* move a considerable distance before allowing you to quick travel. This may make a getaway more difficult if your adventurer is not already faster than anyone else. This only applies to goods in stores; killing townsfolk and taking their personal things, including those of the shopkeep, still only requires exiting the site. The moment you are out of sight, you will be able to 'warp' out as usual. Theft and murder remain within entities; even depopulating one country and stealing all its things will not generate ill-repute in another country. In some cases, the shop will be abandoned. This will be made clear by the presence of unbought items and the lack of any merchants in the area. You will not be considered a thief by the relevant entity for taking stuff from an abandoned shop, but you will still be withheld the privilege of fast-travel until you leave the site. If the item name is not surrounded by dollar signs, it is never considered stealing, even in situations where it would be in real life.

### Managing coins

You will find that coins from one civilization are nearly worthless in any others (except for metal value, or so the presumption goes). This will typically result in adventurers carrying around lots of partially-useless coins. Coins can and will encumber your adventurer, eventually reducing their speed. To reduce that effect, you can try to exchange your copper and silver coins for gold ones, as well as sell all of your loot directly for gold coins. Remember, merchants will always try to pay you in higher-denomination currency first, but will resort to lower-value coins if they run out of anything higher. First, check the merchant's chest to see how much of each type of coins they have.

Standard coin values are as follows:

- Copper Coin == 1☼
- Silver Coin == 5☼
- Gold Coin == 15☼

To receive the maximum amount of gold coins from that merchant, make sure the amount **they owe you** during the trade is equal to (total amount of gold coins the shop has)\*15☼ . If you are selling loot, simply make sure you only trade this worth of goods, and move on to other merchants for the rest. If you wish to exchange copper and silver coins for gold, buy random goods from the merchant until their price is around this value, and then sell back all of the goods for their original value, but in gold. Alternatively, you can take your excess coinage and use it to purchase large gems at a trinket shop. Large gems make good investments because they are 1) light, 2) variably priced, and 3) equally valuable between different civilizations. A few goods are strictly superior to all forms of coinage as a store of value, most notably giant cave spider silk items. A suitably sneaky (or powerful) adventurer can murder a few dwarves or goblins for such items for trade and sale for human goods. Giant cave spider silk is a non-renewable resource in any given world - please harvest responsibly.

### Where to get items to sell

The best place to get items to sell is at bandit camps, after you've slaughtered all the bandits. You can loot the clothes and equipment off of the corpses of the bandits (and off your fallen companions, too), plus at the very center of camp there'll be a few scattered weapons and a few bags/chests containing various goods. The next best way to get items to sell is to kill a creature, butcher their corpse (see below for how), and pick up the edible bits. Butchered bits from the corpses of people (dwarves, elves, humans, etc.) can sometimes be found in monster lairs and these seem to be just as desired by shopkeepers as the products you gain from your own butchering. Remember that you can also carve the bones of animals to make them desirable trading items. Another good early source of income can be bags left in houses and shops, which usually contain plants and food. No one will complain, and the plants inside can be sold at about 2☼ each plus the value of the bag. At the bottom of the list comes L looking carefully and selling any small creatures you might find. However, shops will not accept live creatures unless they are in cages. Some rocks, piles of sand, and other things found on the ground nearly everywhere can also be sold for 1☼ each.

You can also try filling your backpack from a river - it can hold up to 100 units of water, which is worth 100☼ total. After you sell it, water will drop to the floor as a pool, and the backpack can be refilled instantly and for free from there. In fact, you can infinitely fill any container from any pool/pile of any liquid/powder, so if you happen to find some precious substance like sunshine or dwarven sugar, money won't be a problem for you anymore. This is of course an exploit, liable to be fixed at any time. It may be useful in a pinch, but don't rely on it. Another devious method is to go outside the shop, g grab handfuls of mud and throw it into your backpack, then sell them for 1☼ each. The merchants will gladly buy your rare and valuable mud, despite the unlimited free mud just outside their shop.

## Quest log

|  |  |
|----|----|
| Q | Open quest log |
| Esc | Exit quest log |
| e p a s r b | Access various lists |
| m | Switch between the world map and additional info |
| z | Center cursor on location of selected list item, if known |
| c | Center cursor on your location |
| l | Toggle the visibility of the line between you and some other point on the map. |
| f | Filter the list |
| + -  \* / | Navigate the list |

The quest log contains everything you know about the world, such as various events going on, people you know, and various sites. The m key will alternate between a world map that you can navigate, and information on whatever item is highlighted in the list to the right.

There are various kinds of lists you can check on the quest log:

- **Events** — A list of events that are happening or have happened. Formatting of the list is (type)/(description). You can center on the location of the event if you know this. This list is the closest you'll get to some formal quest system.
- **People** — A list of people you know. At the start of the game, this list will contain people in your site.
- **Sites** — A list of various sites around the world.
- **Groups** — A list of groups you know of and your relation to them. Note that you have to press e when you're on the events list in order to reach this list, requiring you to press e at most twice.
- **Agreements** - Your various agreements; this includes tasks given to you by your lord, and why people are traveling with you and the history of your agreements.
- **Regions** — A list of regions. The additional information will list the biomes a region possesses.
- **Bestiary** — A list of creatures, their characteristics, and where you could find them.

## Create

|  |  |
|----|----|
| x | Craft (butcher, create item...) |
| P | Compose or perform |

Adventurers can perform limited crafting, with access to butchery and moddable reactions. To access the crafting menu, press x. In addition to crafting, other actions can be performed.

### Crafting

- **Knapping** allows an adventurer to sharpen a rock. Knapping only works on stones on the ground or in your hands. When you select "Make sharp rock", you will be prompted to choose a rock to sharpen ("tool stone"), and then the rock that is to be the hammerstone. The tool stone will be replaced in your hand by a sharp version, which can serve well enough to make some...

- **Helves** (hafts)v0.43.01 which are carved from branches, which can be pulled from trees. Doing so requires a sharp item, which can be anything from a weapon or arrow, all the way to a sharpened rock (the product of your earlier Knapping usually works best in this case). Helves are currently only used to make...

- **Stone Axes**v0.43.01 - Assembling a stone axe requires a helve plus a sharp rock as components. Stone axes are inferior to battle axes weapon-wise, but are just as usable for cutting down trees.

- **Carve Bone** acts similarly to fortress mode's Bone carver by allowing the adventurer to carve bones into various objects and figurines. The bone carving options are contained in a subsection of the crafting menu, due to the number of options.

- **Carpentry**v0.43.01 is another crafting menu, but using it requires one to stand in a carpenter's workshop, either one found in a fortress, or constructed by the character. The menu includes various furniture (not all of which can be placed in the build menu) along with various containers, buckets, shields, and training weapons. All of these require a log and a sharp object.

### Butchery

**Butcher** acts similarly to fortress mode's butchery by converting a corpse into edible products, bones, and skin. A corpse must be on the ground or in your hand. With a sharp object (such as a large dagger or knapped stone or even a bolt/arrow) in your hand, or on the same tile as the corpse, press x for the crafting menu, then select the butcher option, and then you can select the corpse and the sharp tool to butcher with. The corpse will be replaced by its butchering returns.

### Composing

The P performance menu allows you to create **musical compositions**, **poetry**, **choreography**, or **writing**. You will then be able to select from one of the art forms already known to the adventurer, which the specific song, poem, or dance will be an example of.

Writing allows the adventurer to write books and scrolls, allowing one to create various types of literature. Writing requires reading or writing skill as a prerequisite, along with a blank scroll or quire available. Each option produces different results.

- **Guide** - General writing about a specific site, generally described as "concerning" that town, dark pit, etc. without going into detail.

- **Essay** - Writing about individual historical events, generally of personal relevance to the adventurer. E.G: the ascension of that adventurer to lordship, companions joining the party, and other such events.

- **Manual** - This will write down a randomly-selected form of knowledge the adventurer is aware of, to be learned by future readers. Most commonly this will be musical, poetic, and dance forms the adventurer knows or composed. This can also include scientific research the adventurer has learned, and necromancer adventurers can spread the secrets of life and death by writing manuals about them.

- **Chronicle** - In-depth writing about a particular site, group, or civilization. This will be presented as a multiple-chapter work, each chapter relating to a historical event related to the writing's subject.

- **Letters**, **short stories**, **novels**, and **plays** will write generic prose, typically described as having no particular subject. In addition, letters will normally generate untitled.

- **Composition** - Writes new songs. This functions similarly to composing new songs, with the added benefit of writing it down for others to learn. However, unlike normal composition you do not get to select which musical form to base the song on.

- **Choreography** - As with compositions above, this writes down a new dance based on a randomly-selected dance form the adventurer knows.

- You can also unlock even more types of writing by going to a library and reading books of different genres, such as **biographies**.

Additionally, at the bottom of the writing menu, you have the option of writing down specific songs and dances known to the adventurer.

## Natural abilities and acquired powers

|  |  |
|----|----|
| X | Use ability |

- **Spitting** lets you spit (if you are a creature that can), which can be aimed at someone in much the same way as any projectile. To get this, choose natural ability and then spit in the interactions menu. Other natural abilities exist (such as breathing fire), but only some are usable, since some belong to creatures that are not playable.

You may also gain acquired abilities when you become a creature of the night, such as a necromancer or intelligent undead.

## Woodcutting, building and site management

|  |  |
|----|----|
| b | Found a site and build |

Adventurers can chop down trees for resources—this requires a *non-wooden* axe. By pressing g while next to a tree, you can chop it down and collect logs. However building is no longer functional.

### Faction management

While building personal sites and construction mechanics are no longer available in adventure mode, faction management remains functional. After claiming a meadhall or other similar structure (And disappearing all previous nobles) you will get a text popup telling you that you are in control now, and your title will change to lord; at this point you can take control of a site and manage it as its leader. This includes hiring guards by Invite listener to become a hearthperson. The guards will automatically patrol your site if they are not your companions, or will hang out in the zones you assign them. Additionally, as the site's lord, you can force the leaders of nearby villages to pay you tribute, via the submit and pay tribute demand. However, they are unlikely to submit under non-strenuous circumstances.

## Sites

*Main article: Site*

More information on each type of site can be found in the site's specific article.

At these sites you can trade, take quests, or talk with people:

|  |  |  |
|----|----|----|
| **Tile** | **Name** | **Inhabitated by** |
| Ω | Mountain halls | Dwarves |
| Ω | Hillocks | Dwarves |
| Ω | Fortress | Dwarves |
| ○ | Castlev0.47.01 | Humans |
| î ¶ ₧ | Forest retreat | Elves |
| = ≡ æ Æ | Hamlet | Humans |
| + \* \# ☼ | Town | Humans |
| ○ | Monasteryv0.47.01 | ? |

These sites are populated with goblins, monsters or undead. You may want to go there to accomplish a quest, or just for fun:

|  |  |  |
|----|----|----|
| **Tile** | **Name** | **Inhabitated by** |
| ☼ | Camp | Bandits |
| ○ | Fortv0.47.01 | Bandits |
| º | Dark pits | Goblins |
| Π Π | Dark fortress | Goblins |
| • | Cave | Monsters |
| \# | Labyrinth | Monsters |
| • • | Lair | Monsters |
| μ μ μ μ μ | Ruins | Monsters? |
| Å | Shrine | Monsters |
| 0 | Tomb | Undead |
| I | Tower "Tower (necromancy)") | Undead |

## FAQ

*Main page: Adventurer mode F.A.Q.*
