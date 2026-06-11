# Millstone

> Fonte: [Millstone](https://dwarffortresswiki.org/index.php/Millstone) — Dwarf Fortress Wiki (GFDL/MIT)

A **millstone** is used to grind up certain plants to make sugar, flour, dye, and slurry. Each milling job requires an empty bag. To operate, it needs to be connected to a mechanical power source such as a water wheel or windmill that supplies it with 10 power units. If none is available, a quern can be used instead, although millstones process plants much faster than querns. Before they can be placed as a building, you must first construct the millstone at a Stoneworker's workshop.

If the power to the millstone is interrupted, any jobs must be requeued when power is returned. Therefore it is best to have uninterrupted power or at least the ability to run it for a long period of time.

A millstone can be placed in a hanging state, however, it will not actually be constructed as the builder needs to be able to stand on the square on which it is being built. Because of this, a millstone must be powered from above or from the side, not from below in order to be able to complete construction.

Ensuring the exclusive milling of certain plants (to, say, produce only dye, not flour) is quite cumbersome. It requires a stockpile that only allows these plants and setting it to give to the millstone, as it provides no menu to specify what to mill. If you don't set a custom stockpile, the miller will pick the closest random plant, with the usual, occasionally surprising, definition of closest. You also need something like a furniture stockpile that allows only bags, setting that to 'giving' to the millstone too. Deactivate wood, stone and metal as material to avoid it being cluttered with coffers. You still have to ensure somehow that the plants arrive at the right stockpile, for example by not allowing them on any other. Once you got this working repeat for every other plant you want to mill, either switching the 'give' orders every time or setting up a separate millstone for every plant/plant combination.

For general details read Giving to a Stockpile/Workshop.

Alternatively, to preserve what little sanity a DF player has left, just forbid all millable plants you don't want milled (for example from the stocks menu) and (re-)claim them once the milling job is done.

As another alternative, the utility DFHack provides a "job item-material" command that allows you to specify a plant to mill. For example, to set a quern to only mill dimple cups and ignore other plants, select a quern with a "Mill Plants" task, and issue command "job item-material 1 MUSHROOM_CUP_DIMPLE". This will set the material type of the plant item being milled in the selected quern.

(Selecting "job item-material 2" would select the material type of the bag the dye is stored in.)

This utility is also available as "gui/workshop-job", bound to by default.

## An Example Setup

As it is most efficient to set up workshops near their materials sources, usually by putting stockpiles next to them, it's common for millstones to be set up near farm plots. Putting a millstone just under the surface lets it be powered by a windmill on the surface, like so:

{\|style="border: 1px solid \#0b0; background: \#dfd"

\|+**Side view** \|- style="font-family: monospace; font-weight: bold; font-size: 135%" \|style="color: \#970; padding: 0; text-decoration: underline"\|- \|style="color: \#970; padding: 0; text-decoration: underline"\|= \|style="color: \#970; padding: 0; text-decoration: underline"\|- \|  \|style="color: \#970; padding: 0"\|- \|style="color: \#970; padding: 0"\|= \|style="color: \#970; padding: 0"\|- \|  \|- style="font-family: monospace; font-weight: bold; font-size: 135%" \|style="text-decoration: underline"\|  \|style="text-decoration: underline"\|\* \|style="text-decoration: underline"\|  \| \|style="text-decoration: underline"\|  \|style="text-decoration: underline"\|\* \|style="text-decoration: underline"\|  \|- style="font-family: monospace; font-weight: bold; font-size: 135%" \| \|1 \| \| \| \|2 \| \|} Note that version 1 only works if the windmill is built first, and version 2 only works if the millstone is built first.

When building a vertically powered millstone, build the components from the bottom up. First place the millstone, then place the vertical axles above the millstone, then place the windmill last.

*For a basic overview of how the different machine parts work and work together, see machinery.*

## Bugs

- Dwarves will occasionally combine two separate mill products in the same bag.
