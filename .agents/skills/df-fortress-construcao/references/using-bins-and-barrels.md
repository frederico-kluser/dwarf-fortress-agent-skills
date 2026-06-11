# Using bins and barrels

> Fonte: [Using bins and barrels](https://dwarffortresswiki.org/index.php/Using_bins_and_barrels) — Dwarf Fortress Wiki (GFDL/MIT)

Ordinarily, each item or stack (e.g. ≡Dwarven Ale Stew \[12\]≡) of items occupies one space of stockpile room. You can consolidate stockpile space by making bins, barrels and pots that can hold many items at once. Barrels and pots store food and alcohol; bins can store many types of smaller items, such as finished goods, metal bars, ammo, and gems. Building a steady supply of containers helps reduce the space you need for storage. If resources permit, it's very easy to keep a nominal amount of bins and/or barrels available by using Manager work orders.

## Food storage

Food can be stored in barrels and pots. Each barrel or large pot can hold up to 60 total units. Each unit in a stack counts towards the total storage.

Foods will only be stored together if they're from the same category. For example, dwarves will never mix plants and meat in the same barrel.

One thing to note about storing seeds is that bags are required to put seeds in. These bags will then be placed inside the barrel or pot. Otherwise, the dwarves will end up with one seed per tile. Furthermore, as seeds will rot outside of a stockpile, you may find that your fortress is not getting seeds from the plants you're consuming when the food stockpile is full. Get your textile industry started early; you may want to avoid milling plants until it ramps up. 1

## Drink storage

Alcohol must be brewed into either a barrel or pot. Each container can hold a single stack of alcohol. Larger batches should be, but aren't, split across multiple containers automatically.

You can empty a container of alcohol by drinking, cooking, shotgunning it out of a minecart, trading or application of extreme cold that destroys the container.

## Goods storage

Most non-food items can be stored in bins; the quantity allowed depends upon the items stored. Each bin can store up to 10 bars or blocks, while 30 or more small crafts may fit into a single bin. This might have changed in newer versions of the game.

| Good           | Bin Capacity |
|----------------|--------------|
| Pig Tail Cloth | 300          |
| Stone Block    | 10           |
| Bone Bolts     | 400          |

## Managing stockpiles directly

It is possible to set whether bins can be used in a stockpile with → /. For barrels, and are used instead of C and V. By default, bins are used for Bar/Block, ammo, gems, finished goods, cloth and leather stockpiles, and barrels are used for food stockpiles. Also by default, the stockpiles that use barrels or bins to store other items will permit a barrel or bin on each of their spaces. You can override this by specifying the maximum number of barrels and bins that an individual stockpile is allowed to utilize, using → / and / to decrease and increase the limits.

## Reserving containers for other tasks

"Reserved Barrels/Bins" is a global setting that reserves a certain number of barrels or bins, preventing them from being claimed by a stockpile until they are filled by a Workshop that requires their use. This feature is most often used to ensure that a fortress has ample empty barrels for the production of alcohol, although empty barrels are also necessary for other jobs. You can change this setting in the stockpile menu . If there are 5 reserved barrels, no stockpile will claim an empty barrel until you have at least 6 lying around. In this way you can ensure that jobs like making alcohol always have free barrels available.

In the case of barrels necessary for producing alcohol and dwarven syrup, they do not have to be located on a furniture stockpile. This is because the "Store Item in \" task only looks at furniture stockpiles for available containers. Normal production tasks behave as mentioned earlier, they will just grab the nearest barrel. You can exert some limited control over this by setting a number of reserved barrels; however, you cannot set where these barrels will be.

Though it is possible to reserve bins, there is no advantage in doing so, as no workshop tasks require empty bins.

## Bin/Barrel reassignment

If you have a limited number of barrels and pots (possibly due to a lumber and stone shortage because you're playing in a Fun place like the tundra) and your food stockpile is using too many barrels and you need some for booze, or if for some reason the opposite is true, you can force the dwarves through a series of steps to have the barrels switch from one stockpile to another. Assume you have too much barrelled food and you need barrels for booze. First, designate a small garbage dump zone nearby. Then set the maximum barrel limit on the food stockpile way down--possibly to zero. Don't worry, the existing barrels won't be dumped as a result. Now view a barrel and then once inside, view each individual food item and set it to for dump (but do not dump the barrel itself). The dwarves will take the food from the barrel and throw it into the garbage zone, and once the barrel is empty they will immediately move it to a furniture stockpile because the food stockpile barrel limit is exceeded already. Now you have a free barrel with which to brew. You can reclaim the food from the garbage dump now, and the dwarves will do what they can to store it. Be warned that this might end up being on the floor in the stockpile which could attract flies. Remember to set the barrel limit on the food stockpile back up to some reasonable level if you get your hands on some new barrels.

A faster way to dump the contents of a barrel or bin is to use designations. , then select the barrels or bins you wish to dump. The container and all of its contents will be dumped separately. Then simply to reclaim the items once they are in the dump.

This trick does not work on artifacts as these cannot be dumped. One way to remove artifacts from a bin is to select them for display on a pedestal.

## Barrel and bin material

Heavy barrels and bins slow down hauling, so it is wise to make them from light materials when possible. Even the heaviest types of wood are lighter than any metal (excluding adamantine) - the wood of feather trees is the best of all. As an alternative, you can place small "feeder" stockpiles that disallow barrels/bins and link them to larger storage stockpiles nearby to greatly reduce the distance traveled while carrying a heavy container.

Metal barrels are supposedly better for food stockpiles because they resist vermin; unfortunately there is no good way to convince your dwarves to allocate metal barrels for food storage aside from using them exclusively.

The material of the container also determines whether the container is fire-safe and magma-safe.

## Bugs

- Hauling jobs block access to all the items in the destination containers until the hauling is complete. This often results in cancellation spam and work delays. One workaround is creating a "feeder stockpile" with containers disabled.

- Ammunition stored in bins may not appear available to marksdwarves, eventually causing them to head to battle without bolts. Disabling bins in ammo stockpiles is recommended.
- Items in bins are sometimes not found for tasks.

## See also

- Storage
