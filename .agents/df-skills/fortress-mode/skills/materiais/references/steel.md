# Steel

> Fonte: [Steel](https://dwarffortresswiki.org/index.php/Steel) — Dwarf Fortress Wiki (GFDL/MIT)

**Steel** is an alloy of iron and carbon (refined coal), made at a smelter. It is the best common metal for smithing most weapons and armor. Steel also has the third highest value of all metals, tied with that of gold.

Steel can be created at a smelter by a dwarf with the furnace operator labor activated.

## Sedimentary layers

To smelt steel, you will need iron bars, flux stone, and fuel. Flux is used to remove impurities, including carbon, during the smelting process, while fuel (charcoal or coke) removes oxygen and puts back in a small amount of carbon. The end result is steel: iron with just the right amount of carbon in it. The three ores of iron (hematite, magnetite, and limonite) can only be found in sedimentary layers, with the exception of hematite, which can occasionally be found in igneous extrusive layers. Furthermore, four of the five flux stones (calcite, chalk, dolomite, and limestone) are found only in sedimentary layers, as well as both coal ores (bituminous coal and lignite).

If you have no sedimentary layers at your fortress site, your only hope to make steel is with:

- hematite from igneous extrusive layers, or iron ore imported from trade caravans, or melting iron items brought by siegers (goblinite) and caravans
- marble from metamorphic layers, or imported flux
- charcoal from wood, or coke from imported bituminous coal or lignite

If you embark in a forest biome, you can produce thousands of units of wood from the surface trees alone, without even tapping into the caverns. Charcoal requires more labor per unit than coke, but is often easier to acquire.

Note that bituminous coal and lignite, like most stones, cost only 3☼ at embark or from caravans. With a cunning-enough starting build, it is possible to embark with enough coal boulders to produce several hundred units of coke, but only if your parent civilization has access to coal; otherwise, it will not be available at all.

## Recipe

Steel production is fairly complex compared to the creation of other alloys, which only involves one step to combine bars of different pure metals to create the final product. Steelmaking from iron bars\* has 2 steps, and both steps require coke or charcoal *as part of the actual reaction*, combining that "fuel" with the other ingredients. This is required *in addition* to any heating source, if using a non-magma smelter (full details below).

*(\* If starting from iron*ore*, you will first need to create iron bars. Steel (or Pig Iron) cannot be created directly from ore. 1 ore creates 4 bars, but the recipe only requires 2 at a time.)*

**Recipe:**\
Necessary ingredients; produces **2 bars of steel**:

- 2 bars iron¹
- 2 units flux²
- 4 units of fuel (or only 2 if magma powered)³

Notes:

1.  Unless you are using a magma smelter, melting iron ore to create iron bars also requires +1 unit of fuel at a conventional (**non**-magma) smelter, producing a total of 4 bars of iron, twice what the recipe uses. This translates to also needing "half a unit" of additional fuel to the ingredients above for each recipe. Since you cannot use "half a unit", you will need a full unit up front, producing 4 iron bars to start, so add that in to any larger, long-term calculations for ore -\> steel.
2.  Calcite, Chalk, Dolomite, Limestone, and/or Marble
3.  For larger production runs, if using a **non**-magma smelter, you may also have to create more fuel. This means either burning wood at a wood furnace, or using 1 fuel to turn bituminous coal into +8 fuel each or lignite into +4 fuel each. Add this to any larger, long-term calculations for steel production. (Read: Don't get caught short, and don't consume your very last fuel without a way of producing more!)

**Step 1:** Use one iron bar to **create pig iron**:

- 1 bar of iron
- 1 flux stone
- 1 unit of fuel (as a source of carbon)
- 1 unit of fuel, or magma (to heat the forge)

**Produces**:

- 1 bar of pig iron

**Step 2:** Combine the pig iron bar with the second iron bar to **produce steel**:

- 1 bar of iron
- 1 bar of pig iron
- 1 flux stone
- 1 unit of fuel (as a source of carbon)
- 1 unit of fuel, or magma (to heat the forge)

**Produces**:

- **2 bars of steel**

To go from raw materials to finished products (assuming 1 bar per crafted item) at a conventional forge, a total of...

- 8 iron bearing ore (= 32 iron bars)
- 32 flux stone
- 13 bituminous coal (or 26 lignite or 104 logs)

... will have no leftover raw material and will yield **32** single-bar steel items. This is assuming, of course, that your dwarves can time-travel, and use the last remaining piece of coke to fire the furnace, to create the first fuel to get things rolling.

## Automated steel production

You can fully automate the production of steel via the use of a work order. The arrangement of these orders would be:

:\*Make 9 coke from bituminous coal (18 lignite, or 72 charcoal), then add the ondition to restart if completed, checked daily (press or until "Restart if completed, checked daily" is visible).

:\*Smelt 8 magnetite *(or hematite or limonite)* ore, then add the ondition to restart if completed, checked daily. then set the rder condition to "Make 9 coke from bituminous coal"

:\*Make 16 pig iron bars, then add the ondition to restart if completed, checked daily. then set the rder condition to "Smelt 8 magnetite *(or etc.)* ores"

:\*Make 16 steel bars, then add the ondition to restart if completed, checked daily. then set the rder condition to "Make 16 pig iron bars"

:\*Wait until the "Smelt 8 magnetite" order activates (once the coke or charcoal is done) to set its rder condition to "Make 16 steel bars"

This automated process would produce 32 steel bars every 4 days, assuming you have an adequate flow of ore, coke-producing stone, flux stone and labourers. You can also make multiple work order sets to increase production as much as necessary.

When using all magma furnaces, the ratio changes to 4 coke (from bituminous coal), 9 iron ore, 18 pig iron, and 18 steel bars. This process should produce 36 steel bars every 4 days with 0 extra products.

Alternatively, you can put together a pipeline:

- Make coal from your preferred fuel if there's less than 20 refined coal and more than 10 of your preferred fuel
- Make pig iron if there's less than 20 pig iron and more than 10 each of coal, iron, and flux
- Make steel if there's less than (however much) steel and more than 10 each of pig iron, iron, and flux

You will need stockpiles of the intermediate products, and there will be some sitting around, but this will make more steel whenever you use up some.

## Planned Steel Production

It is always recommended to have more iron bars than pig iron bars because, supposing you have an abundance of charcoal/coke and flux, you can always turn iron into pig iron, but not vice versa. In a fortress with only a limited number of iron bars and pig iron bars, you want to plan the two steps of steel production to maximize the steel bar yield:

- Step 1: Make pig iron bars, but also leave enough iron bars available for step 2 of the steel bar production
- Step 2: Have iron bars and pig iron bars in ratio 1:1, process them into steel bars

### Questions

- How many pig iron job orders should be issued to result in a 1:1 iron to pig iron ratio?
- How many steel bars can be optimally produced from all this?

### General formulas

Variables:

`   `*`i`*`: number of available iron bars`\
`   `*`p`*`: number of available pig iron bars`

Formula for stage 1, pig iron production plan:

`   `*`j`*`: job orders for pig iron production to be issued`\
`   `*`j`*` = (`*`i`*` – `*`p`*`)/2 (round down for iron surplus, or up for pig iron surplus)`

It is recommended to round down for iron surplus. Should need arise, an iron bar can be forged into a weapon, whereas a pig iron bar cannot.

Formula for the potential steel bar yield:

`   `*`s`*`: number of potential steel bars`\
`   `*`s`*` = 2 * (round_down(`*`j`*`) + p)`

### Example

**Question:**

If I have 32 iron bars and 8 pig iron bars, how many steel bars can I produce from this and how? (Presupposing an abundance of flux and fuel)

**Current stocks:**

- 32 iron bars
- 8 pig iron bars

`   `*`i`*` = 32`\
`   `*`p`*` = 8`

**Calculation:**

Formula for pig iron job orders, (where *i* \> *p*):

`   `*`j`*` = (`*`i`*` – `*`p`*`)/2`\
`   `*`j`*` = (32 – 8)/2`\
`   `*`j`*` = 24/2`

`   `*`j`*` = 12 (rounded down)`

Formula for expected steel bar yield:

`   `*`s`*` = 2 * (round_down(`*`j`*`) + p)`\
`   `*`s`*` = 2 * (12 + 8)`\
`   `*`s`*` = 2 * 20`

`   `*`s`*` = 40`

This can also be calculated from the initial amounts:

`   `*`s`*` = `*`i`*` + `*`p`*` rounded down to the closest even number`

**Answer:**

From 32 iron bars and 8 pig iron bars, 40 steel bars can be produced. Here is how:

**Plan:**

- Stage 1: Issue 12 job orders to make pig iron bars. This will turn 12 iron bars into 12 pig iron bars. 20 of our original 32 iron bars will remain. 12 new pig iron bars are produced, increasing pig iron bar stocks from 8 to 20.
- Stage 2: After stage 1 is completed, we will have 20 iron bars and 20 pig iron bars. We issue 20 job orders to make steel bars (each job order will produce two steel bars).
- Result: 40 new steel bars, 0 iron bars, 0 pig iron bars left unused.

Note: 10 metal bars can produce a full set of armor and a weapon for one soldier.

### Simplification, rule of thumb

If there are at least 20 iron bars more than pig iron bars, issue a job order to make 10 pig iron bars. If not, issue job orders to make steel bars, as many as there are pig iron bars.
