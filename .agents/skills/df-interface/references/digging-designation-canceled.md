# Digging designation canceled

> Fonte: [Digging designation canceled](https://dwarffortresswiki.org/index.php/Digging_designation_canceled) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Error Messages FAQ**
- **Dwarf cancels task: Hunting vermin for food**
- **Dwarf cancels Store Item: Job item misplaced**
- **Dwarf cancels Store Item: Item inaccessible**
- **Dwarf cancels Construct Building: Item blocking site**
- **Dwarf cancels task: Dropoff inaccessible**
- **Dwarf cancels task: Dangerous terrain**
- **Dwarf cancels task: Could not find path**
- **Dwarf cancels task: Forbidden area**
- **Dwarf cancels task: Job item lost or destroyed**
- **Dwarf cancels Pickup Equipment: Equipment mismatch**
- **Dwarf cancels task: Interrupted**
- **Dwarf cancels task: Handling dangerous creature**
- **Diplomacy Stymied - A diplomat has left unhappy**
- **Dwarf cancels construct "Rock object": Needs non-economic rock**
- **Cat cancels Store Item in Stockpile: Too injured**
- **Digging designation canceled: Warm / Damp stone located**
- **Miner cancels dig: Inappropriate dig square**
- **Dwarf cancels fill pond: Inappropriate building**
- **Their wagons have bypassed your inaccessible site**
- **Dwarf cancels Construct Building: cannot reach site**
- **Dwarf cancels construct "Rock short sword": Needs sharpenable rock**
- **Dwarf cancels construction of Wall: Creature occupying site**
- **Needs butcherable unrotten nearby item.**
- **Add a question to this FAQ**
- **Back to the Main FAQ**

## Dados (infobox)

- **Water FAQ**
- **How do I move water up levels?**
- **How do I stop water moving up levels?**
- **Can dwarves swim to the surface for air?**
- **How long does it take for a dwarf/goblin/creature to drown?**
- **How deep is the water?**
- **Is it possible to melt ice?**
- **How do I build a well?**
- **How do I channel a path for water?**
- **Will water push items around?**
- **Can I build a dam to stop the water?**
- **Digging designation canceled: Damp stone located**
- **What is the best way to proceed on a map with no rivers? Will my dwarves die of thirst?**
- **How can I divert a river to allow safe(ish) indoor fishing?**
- **How can I dig through an aquifer?**
- **How do I purify my water?**
- **Add a question to this FAQ**
- **Back to the Main FAQ**

## Dados (infobox)

- **Magma FAQ**
- **Practically everything Magma related**
- **What can I use to make magma-proof items?**
- **How do I channel magma?**
- **Digging designation canceled: Warm stone located**
- **Where can I find magma?**
- **Can magma cremate dead dwarves instead of burying them?**
- **Add a question to this FAQ**
- **Back to the Main FAQ**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

This error message pauses the game and zooms to the location where the warm or damp stone was located.

Warm or damp stone can be very dangerous, as it indicates the presence of nearby magma or water, respectively. However, the stone could be warm/damp because the magma/water is beside the tile, directly above the tile, or directly below the tile - and, most of the time, *you don't know which*. You will only know if you are near the surface and find the damp stone below a known murky pool or river.

In this case, digging the room around the butcher was cancelled due to the last, bottom right tile being below the pool floor. The pool is known since it is on the surface. Note that it was possible to dig below the upper level's damp tiles of clay.

The safest thing to do is back off several tiles, mine up a z-level then approach the location again. Rinse and repeat until you emerge above the surface of the magma/water. Note that you will not receive warnings when digging staircases upward. If you plan on digging a staircase to a higher z-level, make sure there are no heavy aquifers or magma in your way!

    Side Profile:

       Below tile   Beside tile  Above tile            Key

         #######     #######      #######          # Unmined stone
     ↑   __o####     #######      #######          # Warm stone
     z   ###~~##     _o#~~##      ###~~##          # Square that was just canceled
    axis ###~~##     ###~~##      ###~~##          ~ Magma
     ↓   #######     #######      __o####          _ Floor of the tunnel
         #######     #######      #######          o Miner

Only in the middle case would it be unsafe to mine out the square that had just been canceled: In the first and last cases, there would be a floor between your miner and the fluid.

If the damp stone is due to an aquifer, empty tiles next to damp stone will fill with water, either slowly with a light aquifer, or quickly.

The announcements can be changed to add recentering and pausing, either in the settings, or by editing announcements.txt.

If you have DFHack installed, you will have the option to enable "Damp dig" or "Warm dig" mode. If you do not want to have your digging designations canceled, for example when digging minerals out of a light aquifer, you can enable the appropriate mode when you designate the tiles for digging. Click on the toolbar icon to set your desired mode.

Digging toolbar with DFHack damp dig enabled

In this screenshot, the upper row is designated without any special mode. The second row is designated with damp dig enabled. The third row is designated with warm dig enabled. The fourth row is designated with both damp and warm dig modes enabled.

In ASCII mode, tiles designated in warm and/or damp dig mode will flash in an appropriate color.

There are also options to retroactively enable damp or warm dig mode for existing designations on a z-level.

\

\

\
