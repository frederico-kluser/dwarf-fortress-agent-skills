# Edge

> Fonte: [Edge](https://dwarffortresswiki.org/index.php/Edge) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Materials have a sharpness property, defined as `[``MAX_EDGE``:]`. In combat, this presumably defines how well the material works when used for slashing attacks.

Most materials draw this from their Material template, but placing a `[MAX_EDGE]` tag in the material's entry will override this and allow it to be sharper than other objects of its kind. For example, Obsidian has `[MAX_EDGE:20000]`, while the Stone Material Template has `[MAX_EDGE:1000]`. Incidentally, it seems that this is what allows Obsidian to be made into stone swords; a value of at least 10000 has been proven to also work.

Actual weapon sharpness depends on its quality: masterwork and artifact blades have the above-mentioned maximum material edge, while regular-quality items get only half as much.
