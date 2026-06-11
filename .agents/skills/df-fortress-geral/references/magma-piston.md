# Magma piston

> Fonte: [Magma piston](https://dwarffortresswiki.org/index.php/Magma_piston) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Magma pistons** are used to move magma near the surface. This approach was developed by players as an alternative to pump stacks. Magma pistons are used because they require less time and fewer precious materials to construct than pump stacks. However, magma pistons are a bit more complicated than pump stacks, so it takes more time to understand how to operate and build them.

## The concept

The piston method is based on a clever abuse of cave-in physics. The basic principle involves channeling out an area around a huge stone pillar, hundreds of z-levels tall, which will become the "piston" that drives magma to the top. Rest the piston on a single support, then carve out a tank at its base which will be filled with magma pumped from the magma sea. (**Beware:** building the piston directly over the magma sea will **NOT** work. The piston must be made entirely of *natural* (non-constructed) walls.) Once the tank has been filled, drop the piston by removing its support. Liquids displaced by a cave-in will "teleport" straight up to the nearest available space; here, the nearest available space will be the catchment area you thoughtfully prepared earlier atop the piston.

A simple magma piston works as shown in the following diagram:

    Key:

      #    = Wall
      ~    = Magma
      S    = Support
      _    = Floor hatch or bridge (your choice)

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | \_  | \#  | \#  | \#  | \_  | \#  |
| \#  |     | \#  | \#  | \#  |     | \#  |
| \#  |     | \#  | \#  | \#  |     | \#  |
| \#  | ~   | ~   | S   | ~   | ~   | \#  |
| \#  | \#  | \#  | \#  | \#  | \#  | \#  |

**Basic magma piston design (side view)** {style="border: 1px solid #0b0; background: #dfd"}

When the support is destroyed, the wall sections in the middle will fall down into the magma. The magma will teleport to the top of the piston, as shown in the following diagram:

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | \_  | ~   | ~   | ~   | \_  | \#  |
| \#  |     | \#  | \#  | \#  |     | \#  |
| \#  |     | \#  | \#  | \#  |     | \#  |
| \#  | ~   | \#  | \#  | \#  | ~   | \#  |
| \#  | \#  | \#  | \#  | \#  | \#  | \#  |

## Construction

A magma piston is composed of 4-5 parts: the catchment area, the magma reservoir, the support, the piston, and the obsidian caster (optional).

### Catchment area

The **catchment area** is located at the top of the piston. After the piston is dropped, the magma will spread out around the catchment area. In a repeating magma piston, some of the magma is used to cast obsidian on top of the piston, in order to reuse it. The volume and size of the catchment area must be carefully calculated to ensure that you won't have too much or too little magma above the piston for casting. Ideally, you want the depth of the magma above the piston to be 2. If the depth is 1, then the magma might evaporate and you won't be able to repair your piston. If the depth is greater than 2, then you're wasting magma if you cast it into obsidian. You can also make the catchment area multiple z-levels deep. If you need a catchment area smaller than possible with bridges or floodgates, you may use a floor-less floodgate to prevent the magma entering that square, while keeping the piston free to fall.

### Magma reservoir

The **magma reservoir** is dug out near the magma sea. You can't actually drop the piston directly into the magma sea because the bottom of the magma sea is semi-molten rock, and it will completely destroy any piston dropped into it. The magma reservoir is artificial, so it won't have a floor made of semi-molten rock. This will allow the piston to rest on the floor of your reservoir. The magma reservoir needs three parts: a magma inlet, a magma drain, and an access corridor. After letting magma in, and dropping the piston, you'll want to dig out the bottom of the piston so you can drop it again. To do that, you need to drain any excess magma and let your workers in through the access corridor.

### Support

The **support** is what prevents your piston from dropping until you decide to pull the firing lever. The support can be located either at the bottom of the piston, as shown in the simplified diagram, or at the side of the piston (shown in the following diagram). If the support is at the bottom of the piston, then the support and the mechanism it uses must both be magma-safe. If it's at the side, then neither need to be magma-safe. Here's an example of a side-mounted support:

**Key:**

      #    = Wall
      P    = Piston
      X    = Up/Down stairs
      S    = Support
      _    = Floor hatch or bridge (your choice)
      =    = Constructed floor

|     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| X   | \#  | \#  | \_  | P   | P   | P   | \_  | \#  |
| X   | \#  | \#  |     | P   | P   | P   |     | \#  |
| X   | \_  | =   | =   | P   | P   | P   |     | \#  |
| X   |     | S   |     | P   | P   | P   |     | \#  |
| X   | \#  | \#  |     | P   | P   | P   |     | \#  |

**Side-mounted support** {style="border: 1px solid #0b0; background: #dfd"}

In this diagram, you can see the catchment area at the top, and the piston in the middle of the shaft. The support structure is to the left. When the support element collapses, the two constructed floors will become unsupported, and then the piston will collapse. The stairs and hatch to the left of the constructed floors allows for convenient reconstruction of the support.

### Piston

The **piston** is the heart of the scheme. It may be 100-200 z-levels long, so it will take quite a while for your miners to dig it out. You may encounter trouble with caverns. Ideally, you should scout out the caverns and find a clear path straight down. If you can't find such a path, you can fix the problem as follows:

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | X   | P   | P   | P   | X   | \#  |
| \#  | X   | P   | P   | P   | X   | \#  |
| \#  | X   | P   | P   | .   | .   | .   |
| \#  | X   | P   | .   | .   | .   | .   |
| .   | .   | .   | .   | .   | .   | .   |
| .   | \#  | \#  | \#  | .   | .   | .   |
| \#  | \#  | \#  | \#  | \#  | \#  | \#  |

**Cavern problem** {style="border: 1px solid #0b0; background: #dfd"}

First, smooth the top and bottom, like so:

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | X   | P   | P   | P   | X   | \#  |
| \#  | X   | P   | P   | P   | X   | \#  |
| .   | .   | .   | .   | .   | .   | .   |
| .   | .   | .   | .   | .   | .   | .   |
| .   | .   | .   | .   | .   | .   | .   |
| .   | .   | .   | .   | .   | .   | .   |
| \#  | \#  | \#  | \#  | \#  | \#  | \#  |

Now drop the top of the piston on to the floor of the cavern. You can use a cave-in to destroy the stairs quickly, if you remove all up-stairs first.

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  |     | P   | P   | P   |     | \#  |
| \#  |     | P   | P   | P   |     | \#  |
| .   | .   | P   | P   | P   | .   | .   |
| .   | .   | P   | P   | P   | .   | .   |
| .   | .   | P   | P   | P   | .   | .   |
| .   | .   | P   | P   | P   | .   | .   |
| \#  | \#  | \#  | \#  | \#  | \#  | \#  |

### Obsidian caster

The **obsidian caster** is what allows you to rebuild your piston and get more magma. It's an application of techniques drawn from obsidian farming. The caster just needs to precisely dump water into the catchment area in order to form obsidian. A caster is composed of two parts: a water inlet, and a retracting bridge. Here's a sample design:

**Key:**

      #    = Wall
      P    = Piston
      F    = Closed floodgate
      ±    = Retracting bridge with water
      ±    = Retracting bridge with magma
      ~    = Magma
      ~    = Water

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | ~   | ~   | ~   | ~   | ~   | \#  |
| \#  | \#  | \#  | F   | \#  | \#  | \#  |
| \#  | \#  | ±   | ±   | ±   | \#  | \#  |
| \#  |     |     |     |     |     | \#  |
| \#  | ±   | ~   | ~   | ~   | ±   | \#  |
| \#  |     | P   | P   | P   |     | \#  |

**Obsidian caster** {style="border: 1px solid #0b0; background: #dfd"}

When you retract the bridge at the top, the water will fall straight down, and you'll get the following result:

|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
| \#  | ~   | ~   | ~   | ~   | ~   | \#  |
| \#  | \#  | \#  | F   | \#  | \#  | \#  |
| \#  | \#  |     |     |     | \#  | \#  |
| \#  |     |     |     |     |     | \#  |
| \#  | ±   | P   | P   | P   | ±   | \#  |
| \#  |     | P   | P   | P   |     | \#  |

## Operation

The general procedure for operating a repeatable magma piston is as follows:

1.  Pull your firing lever to collapse the side support, thus dropping the piston into the magma.
2.  In the magma reservoir, close the inlet and open the drain to empty the magma and allow workers in later.
3.  Retract the bridge of the obsidian caster to drop water onto magma and rebuild the piston.
4.  Extend the bridge of the obsidian caster and open the inlet floodgate, to refill your caster's water supply.
5.  Reconstruct the side support and re-link it to your firing lever.
6.  Pump/drain any magma you want to use out of the catchment area.
7.  Allow workers into the magma reservoir when it's safe and empty, and dig out the bottom of the piston.
8.  Get the workers out of the reservoir and lock the door.
9.  In the magma reservoir, close the drain and open the inlet to fill it with magma.
10. Remember to close the inlet floodgate of your obsidian caster.
11. Make sure that your side-support is clear.
12. When the magma reservoir is full, use your firing lever to restart the process.

## More information

The original discussion of this trick, including how to make the piston reusable, can be found in this forum thread.

That being said, I will link this here so that those who attempt this concept in the premium version have access to this guide. https://steamcommunity.com/sharedfiles/filedetails/?id=2924657714

## Magma Piston - Updated 9th December 2023

So here I will begin the editing of a new chapter in magma pistons after the premium version has been released. The work that Fenwah and others on bay12forums began is still going on. This page teaches you to:

- Finding the right spot using Dwarven Sonar
- Induce multi floor cave-in (to channel multiple floors very fast)
- Magma Tapping (breaking into the magma sea to get a source of magma for magma reservoir)
- Using portable drain ( For draining magma )
- Using Supports to drop the piston ( massive pillar of rock, 120 blocks high )
- Using water to reload the piston

## Dwarven Sonar

Now, how to do it? it is mentioned as follows :

- Go to build -\> farming -\> farm plot
- Drag and drop a square at any plot that is suitable for farming, but make sure to only select the starter tile and not the placement click.
- Now drag a big square, do not end the placement, max size plot, now scroll to lower tiles
- When you drag the mouse wheel and go below, the places where farm plot is place-able is visible
- Underground in undiscovered regions, where there is farm plot, there is a cavern
- I have shown a gif of how to do it below, it shows what is written here applied, in full.
- We have discovered 3 caverns in the mentioned manner.
- Where ever there is a cavern, it is visible by a different manner in placement pop-up
- Now when you discover the caverns, note the levels where you discover them and dig carefully.
- Cancel the placement option

Here is the big Gif, I have cropped the empty frames in the GIf. The relevant frames are kept in here.

|                     |
|---------------------|
| 1                   |
| The Sonar in action |

## Detailed Video

- 5th April 2023:
- Youtube video:

Magma Piston Video

## Making a Portable Drain

A portable drain is a mine-cart dumping infinite amounts of water in a wall . A quick TL;DR

- Make a track stop dumping into wall
- Place (Magma-safe material for magma) mine-cart on it with empty conditions/give or take stockpiles/
- Make sure the set-up is made one floor below the region to be drained
- one can place a pump, pumping fluid in to the mine-cart but then that needs automation

1\. What you need is:

- A mine-cart -\> Material depends on what you intend it for.
- A proper track stop - that - dumps - in to - a - wall, (maximum friction )

2\. This is my portable magma drain design:

|                               |
|-------------------------------|
| 1                             |
| Portable Drain Layout example |

- Water -\> Any mine-cart
- Magma -\> Magma-safe material for cart
- The location of the drain is important.
- I usually channel a room and make it 1-Z level low, so the entire magma goes to the cart and drainsup, leaving the upper floor totally empty when needed.
- This will clear it up.

|                      |
|----------------------|
| 2                    |
| Portable Drain Logic |

3\. Now we set the IRON drain dump stop:

|                        |
|------------------------|
| 3                      |
| Drain Dump designation |

4\. Now we set the drain dump mine-cart

- Go to set mine-cart hauling routes, add a new route, then look at the index described below:

|                          |
|--------------------------|
| 4                        |
| Minecart icons explained |

5\. Now we do this:

- Set track stop to the Iron track stop we made
- Set an IRON mine-cart to the stop
- delete every single conditions and leave it empty
- We do not want any conditions in it, we do not want it to take or give from any stockpile, nor do we want it to take any specific item. So we leave the below tab empty, except for the names

So I will re-cap this : 1. Add new track stop. 2. Click on iron track stop and name it. 3. Click on add mine-cart and add iron mine-cart. 4. Name the track-stop if you will. 5. Remove all conditions. 6. Let the items to be placed in be empty. 7. That should do it. 6. Now if the dumping into a wall and mine-cart with all empty and normal placement is there then it will work absolutely fine. There is only one way to test, fill it up with water or magma, it will drain the floors above its current floors, it will drain up to only 6/7 of the floor it is placed on. So the reason for its one floor lower placement. It is very important that you don't place the dump on the same floor as your desired draining floor.

## Magma Tapping

Magma Tapping has various methods, I will try to depict a very simple method:

- But before hand, there is a section in-game:
- Under Labour Tab
- Go to Stone use

This list gives you the list of magma safe materials, so in my case, I had a lot of dolomite, so I selected ( Allow dolomite to be used in normal stone jobs ). So I could make some magma safe grates and stuff. Another good idea is to use iron for all these magma operations.

So this is an approximate list of materials you'd want ready before going for magma pump

- Iron Pipe Section X 1
- Iron Blocks X 4 or 8
- Enormous Iron Cork-Screw X 1
- Iron Flood Gate X 2
- Iron Grates X 1
- Iron Mechanisms X as per need, because later on, we are going to need these a lot
- Iron Mine-cart
- A Portable Drain ( I will teach this )
- This is what you are looking forward to

|                               |
|-------------------------------|
| 1                             |
| Portable Drain Layout example |

- This is my Pump :

|            |
|------------|
| 2          |
| Magma Pump |

- This is magma below the Pump, the tile of magma has been channelled.

|                                 |
|---------------------------------|
| 3                               |
| View below the pump shown above |

\
Place the pump such that it is one tile ahead of the tile it is sucking from and place the direction of pumping carefully. We place the iron bars so that creatures don't come from underneath the magma into the fortress. The materials are made of iron so that the pump doesn't burn. The Door is placed as a precaution in case things don't work out as intended.

|                     |
|---------------------|
| 4                   |
| Pumps working logic |

\
This is how it is intended to work, don't mind the burning trash, it just shows how non-fire proof materials melt to magma, whereas the pump, operator, grate, door and bars are safe, even the floodgate is safe and sound.

|                             |
|-----------------------------|
| 5                           |
| Magma being pumped Gif File |

\
Now you know how to do it hopefully, good luck with the tapping. Some tips, when you hit warm rock, be exceptionally careful with it. Dig little little upwards and sideways to discover from what z level the warm rocks start, above that layer will be the pump. Also, better to have all materials ready before a magma man pays a visit through the hole you made in the magma sea. Yes, that will be the best I can explain it to you my dear reader. This is the concept of the pump with things mentioned.

## Cave-in organising and executing

This is how a multi-floor cave-in is organised. This is the youtube video describing what is to be explained below now :

- Planned Mass Cave-in
- This image explains the concept of the video as to how to do it, and all.

|               |
|---------------|
| Image         |
| Cave in logic |

We dig out the piston but the floors... 100 or perhaps 120.. 120 floor channelling? nah dude... This is a better alternative, a 100 or 120 floor digging itself takes an in-game year or so. So what we do is, above all these floors, make a support. on this support is a 5x5 square floor. This 5x5 square has a 3x3 hole in the centre. Attach the support to a lever, when all 100 or 120 floors are dug out, you just make sure all dwarves and creatures are away from these floors or it is instant death. So when you pull the lever, this 5x5 drops exactly on similar 5x5 floors supporting the piston. Every single floor below is destroyed. But the oiston is intact. Why? because it is supported by a support. So all that is left here is the piston alone, clean and beautiful. Now in our case, why is a piston shown? Why is this example describing a piston? Why a piston in a cave in? Because, that video shows the magma piston that is to be used in our guide and that video is a great example of how to clean multiple floors. Yes, even TwistedLogicgaming destroyed an entire island with a floor collapse. So now enough chit chat, lets go to a small summary.

## What have we learnt so far and why?

We have learnt

- To find the caverns to suitably dig for the piston.
- To cause a massive cave-in to dig the circumference of the magma piston.
- To carefully pump magma in a designated place.
- And then to drain it very effectively.

##  ***Magma Piston***

Video is right here :

- Firing a Magma Piston

- Let us get into this, this below image is just for reference: a general understanding of the entire process:

|                                      |
|--------------------------------------|
| 1                                    |
| Artistic Depiction of a Magma Piston |

- **This is the top level : The Obsidian Regenerator**
- An obsidian Regenerator servers one purpose,to recreate the blocks we dig at the base at the piston. The way this works is, we have a retracting bridge on exactly top of the magma piston head. This retractable bridge will have water on top of it 7/7. This draw bridge is covered on all sides. Water inlet and outlet is floodgate controlled. When we retract, the water 7/7 exactly falls down on the piston head creating 2/7 (minimum magma to be present) magma to obsidian. This completes the regeneration.

|                                       |
|---------------------------------------|
| 2                                     |
| A ready position obsidian regenerator |

- **This is the level where magma forges will be build:**
- When magma is pumped here, there needs to be micro-management else this magma that is being pumped will freely flow and become cold. If this magma entirely becomes cold, then the obsidian regenerator won't work. This causes the entire project to be fu(k3d because the absence of magma makes the entire repeatability of the project to fail. So a save before first pump is always advised.
- In this image, there are series of channels and slots dug out for the Forge placement. There are several levers controlling draw-bridges below.

|             |
|-------------|
| 3           |
| Piston Head |

- **This is where the magma floods in:**
- The bridges control the magma flow. Every single draw bridge is retracted before the first pump. The floodgate is a critical part and a grate installation is highly advised. Sequential opening and repeating of pumping further opening the bridges to allow more and more magma flow to make it minimum 4/4. In the first three piston drops, one magma forge will be running. Took me 3 pumps and mirco-management to get it running honestly

|                     |
|---------------------|
| 4                   |
| Magma Control Slots |

- **This is how it looks post piston drop:**
- The support has been pulled by the lever, the entire pillar/piston falls down. Upon falling down the area occupied by magma which is replaced by the piston is instantly teleported on top of it, hence the name " Magma Piston " also depicted in the fan-art posted before.

|                                       |
|---------------------------------------|
| 5                                     |
| The top of the piston post activation |

- **This is how the bottom design is:**

|                       |
|-----------------------|
| 6                     |
| Piston Bottom Support |

- **This is how it looks when flooded with magma and piston drops down:**

|                        |
|------------------------|
| 7                      |
| Activated magma piston |

- **Magma Piston types -**
- magma pistons are of two types specifically :
- Re-usable:-
- one such as ours with only a single z-level dropping into magma. This single z-level can be easily regenerated with water drop on magma at the piston top surface as shown in video
- Non-re-usable:-
- the one which is made for a single time use, use like a magma moat... what happens in this is, the piston literally drops in a massive tank full of magma, multiple z-levels deep. Such as 10 Length x 10 Breadth x 5 Levels, so 3,500 units of magma to be transferred. The upper surface must be prepared well to hold this magma as well to use else it can flood the fort leading massive Fun.

multiple z-level regeneration is not possible so this is a single use massive piston. Does the trick though.

## Cavern between piston

The Problem of Cavern occurring in between the piston parts. Firstly, for a project like this, exploration of caverns is primarily advised. Radar isn't sufficient to pull off the direct exploration. The problem occurs when there is a small cavern and there ain't no perfect spot without cavern occurring in between the piston. So this is the method to solve that problem.

1\. Make the top and bottom piston. The bottom piston is held by a support. The top piston is to be dropped but not directly. keep top and bottom ready.

2\. Every single thing in between the top and bottom of pistons to be dug clean. Nothing but air between the top and bottom.

3\. Now the top side piston column may have un-even bottom and the top-surface of the bottom piston can be un-even. We make it smooth 3x3 on top and bottom so that the mating surfaces are clean and 3x3 with nothing in between.

4\. Drop top piston on bottom piston.

5\. Now the part where the piston top is there , 1z level below is your magma pumping chamber and obsidian retainer tank is to be on its top and so on...

6\. Now during your pumping process, somehow using the retainer and a very well thought out process you can increase the piston length but it is tedious.

7\. So TLDR; clean the area between top and bottom surfaces between piston. Make mating faces clean 3x3 / 10 x 10 or whatever. drop topside and make the surfaces connect. Make arrangements and start pumping.

## The Significance of retracting bridge

In the room where magma is teleported above the piston when it drops is because the magma doesn't drip below. What is the use of teleporting massive amounts of magma and it legit drips down to where it was pumped from... One more factor is, if water were to fall in alone the pillar and connect to a piece of magma, it will attach the piston with the channel around leading to process disruption. Floor grates, flood gates didn't work in my case. Magma safe retractable bridges work excellently.

## Mega Piston Regnerator

|        |
|--------|
| 1      |
| Page 1 |

|        |
|--------|
| 2      |
| Page 2 |

## Compound Magma Piston

Very advanced stuff, basically, you make pump stack in between and place a gigantic piston at the top. If there is a huge gap in between two caverns, the design can be implemented in between them. You can use reducer pistons or something like that as well.

|        |
|--------|
| 1      |
| Page 3 |
