# Kitchen

> Fonte: [Kitchen](https://dwarffortresswiki.org/index.php/Kitchen) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Shortcut : b - o - f - k**
- **Icon**
- **Job Requirement**
- **Cooking**
- **Construction**
- **Materials:** Labors
- **Building material (non- economic ):** Cooking
- **Materials Used**
- **Alcohol Cheese Dwarven sugar Dwarven syrup Egg Fat Fish Flour Food Honey Meat Milk Plants Prepared organs Seeds Tallow**
- **Goods Created**
- **Prepared meals Tallow**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **kitchen** is operated by a dwarf with the cooking labor enabled. It is mainly used to cook prepared meals, but also to render fat from butchered animals into tallow.

Cooking meals applies a quality modifier to each ingredient, which can modestly increase the food's value (and a legendary cook can theoretically increase it by up to 34× in the case of cooking seeds). Cooked meals count as each of their ingredients for the purpose of satisfying your dwarves' preferences, increasing the likelihood of happy thoughts and fulfilling the "eat a good meal" need when eating. Cooking plants will not preserve the seeds: To retain seeds from plants, either brew them, process them, or simply encourage your dwarves to eat them raw.

## Types of meals

Prepared meals can be ordered in one of three categories:

- **Easy meals** require two ingredient stacks and are named "{last ingredient} **biscuit**" ().
- **Fine meals** require three ingredient stacks and are named "{last ingredient} **stew**" ().
- **Lavish meals** require four ingredient stacks and are named "{last ingredient} **roast**" ().

Lavish meals, with 4 ingredient stacks, result in larger stacks of food, and require less final hauling for the same amount of prepared food. They take a bit longer to produce (because the cook has to do more initial hauling, and because the workshop is more likely to become cluttered), and result in less experience gained for your cook per ingredient used. With a greater variety of materials in the prepared meal, there is a higher probability a dwarf will eat something they like, giving the eater a happy thought.

Easy meals, with only 2 ingredient stacks, will give more experience per ingredient and result in twice as much hauling *after* cooking, and fine meals, requiring 3 ingredient stacks, fall between the two.

There is no requirement or check that the ingredient stacks are not of the same ingredient, so it is possible to get meals with all the same ingredient.

## Using liquid ingredients

At least one stack going into a prepared meal must be a solid item - if you have only booze, milk, and syrup, your cooking jobs will get canceled. However, a single plump helmet can be cooked with ten dwarven wine, ten dwarven milk, and ten dwarven syrup, to make 31 +Plump Helmet Roast+ without issue.

## What to cook

You may want to adjust what your dwarves are allowed to cook. For example, your dwarves may happily cook away all the seeds you need for planting, or use all your booze as ingredients, a good way to create fun in the early stages of the fortress. Additionally, cooks seem to prefer some of the worst ingredients (single units of low-value materials like tallow). To suppress the cooking of certain items (such as booze, seeds or tallow) go to the y labor menu and then go to the *Kitchen* subtab. Every cookable and/or brewable item in your fortress will be listed. Once you allow or forbid the cooking or brewing of some kind of product, it will be used (or not) accordingly. Note that any cooking jobs in progress will be canceled if you disallow one of the cook's chosen ingredients.

Cooking with alcohol usually results in large stacks of prepared meals, because alcohol typically has large stack sizes. It is assumed that since all dwarves have a preference for at least one type of alcohol, cooking with alcohol improves the chance of happy thoughts from eating. Of course, you then need to ensure that you have enough alcohol left for your dwarves to drink; cooked alcohol does not count as drink.

Ideally, you want to combine four different ingredients in each meal to maximize the chance of a dwarf experiencing a happy thought due to a preference. Unfortunately, when left up to your cook, you'll likely end up with an endless string of tallow roasts. To enforce variety, you can create a series of single-tile, barrel-less "feeder" stockpiles, each of which allows a different type of (cookable) food, all set to "give" to your kitchen.

## Storage

Individual types of prepared meals are not listed in the middle column or right column of the stockpile menu for the Food category. The switch for allowing or banning prepared meals in a stockpile is displayed underneath the right column and toggled by clicking on "Prepared meals" in the mentioned category.

The size of a prepared food stack varies according to the sum of all ingredient stacks; with large input stacks your kitchen will create a stack of prepared meals that is too big to fit into a barrel or pot (capacity 60). If you want to designate a stockpile as the destination for your kitchen's output, be sure that the number of barrels allowed in the stockpile is lower than the number of squares in the stockpile. That way there will be a few non-barrel squares for your haulers to deposit overly large stacks of prepared meals. Given that food left in the open will attract flies, causing unhappiness in dwarves who encounter them, it may be best to store prepared meals in an area of less traffic than the rest of a food stockpile. You can also "break" large stacks into smaller stacks (for a fee) by trading them to a caravan and then purchasing them back in smaller stacks.\[Verify\]

Be aware that food that is not properly stored in a stockpile rots quite fast. Rotting is the worst possible fate for a masterfully prepared meal, and the chef would have every right to be angry about it, since all of their effort spent preparing the meal literally went to waste. Prepared meals can also trigger masterwork destruction if they are eaten by vermin.

## Trade

Prepared meals can be traded since they are renewable/sustainable, easily transported, easily sub-divided, and stack quality modifiers. Even a novice cook has a chance of increasing the value of raw ingredients somewhat; see item value for more information.

However, elven traders will be offended by meals that contain animal-derived ingredients.

## Bugs

Cooks will only cook fluid ingredients as a last resort, instead preferring to cook solid foods with solid foods. Bug:2393

To force the kitchen to cook with fluids like booze, milk, oil, or dwarven syrup, you can limit the possible ingredients used for cooking through stockpile linkage. If a kitchen is set to accept ingredients from a stockpile, it will not use any other ingredients unless they are already stored in the kitchen (which may be encountered if no one has yet hauled some recently-rendered tallow). Set up a tiny stockpile to only hold solid food ingredients, but no barrels. The size of this stockpile will determine how many solid ingredients the kitchen can easily use, so if it is 1x1, the cook will use just one solid ingredient before looking elsewhere. A speedy hauler might get another item into that space before the cook stops looking for ingredients, but this is uncommon. Set up another stockpile to hold the fluid ingredients. Set both of these stockpiles to give items to the kitchen. If there's nothing else left in the tiny stockpile when the cook is looking for ingredients, then the only other ingredients which can be used will be the fluid ingredients, and so they will be used even though they are not preferred by the cook.

Of course, the tiny solid ingredient stockpile will need to be refilled, so you will also need a larger stockpile that links to the tiny one. Unfortunately, once ingredients are in barrels, they will never be taken out of the barrels to be moved to the tiny stockpile, so the larger stockpile will also have to be limited to not use barrels. One way to get ingredients out of barrels is to set a barrel-using food stockpile to only accept from linked stockpiles, set the stockpile to give to the kitchen but not to take from anything, and queue up a lavish meal. Watch the kitchen, and once ingredients have been delivered so work can begin, cancel or pause the work. They will then need to empty the kitchen, and since your barrel-using stockpile is set to not accept from the kitchen, only your barrel-free stockpiles will be available. It might be quicker and less frustrating to dump ingredients from barrels into a barrel-free stockpile instead.

Artwork of a medieval kitchen.\
*(Art by Oksana)*
