# Body detail plan token

> Fonte: [Body detail plan token](https://dwarffortresswiki.org/index.php/Body_detail_plan_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

## Tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  BODY_DETAIL_PLAN | identifier | Create a new body detail plan with the specified identifier. The rest of the tokens in this table are then used to define this body detail plan's properties. |
|  ADD_MATERIAL | identifier / material template | Adds a new material to the creature based on the specified template and assigned to the specified identifier. |
|  ADD_TISSUE | identifier / tissue template | Adds a new tissue to the creature based on the specified template and assigned to the specified identifier. |
|  BP_LAYERS | BY_CATEGORY / or / BY_TYPE / or / BY_TOKEN / body part / tissue name or tissue ARG# for innermost tissue / tissue thickness / tissue name or tissue ARG# for second innermost tissue / tissue thickness / tissue name or tissue ARG# for third innermost tissue / tissue thickness / etc... | Defines a series of tissue layers. Alternatively to specifying a tissue, variable arguments can be entered (numbered arbitrarily to a max of 5) to be filled with tissues when the plan is called in the creature entry. The SELECT_TISSUE creature token with TL_RELATIVE_THICKNESS can change tissue thickness, but tissue *layering* is hard to do without a new detail plan. |
|  BP_LAYERS_OVER |  | Works like BP_LAYERS, but defines layers over existing layers. |
|  BP_LAYERS_UNDER |  | Works like BP_LAYERS, but defines layers under existing layers. |
|  BP_POSITION | BY_CATEGORY or BY_TYPE or BY_TOKEN / body part / position token | Defines a position for the specified body part relative to its parent part (the nose is assigned the position FRONT, as it's on the front of the face). This has some effects on combat, attacks and the like. Valid position tokens are FRONT, BACK, LEFT, RIGHT, TOP and BOTTOM. The position token SIDES is of unverified validity. |
|  BP_RELATION | BY_CATEGORY or BY_TYPE or BY_TOKEN / body part to be affected / relation token / BY_CATEGORY or BY_TYPE or BY_TOKEN / parent body part / coverage | Defines a positional relationship between one body part and another (the right eyelid is AROUND the right eye with coverage 50, as it only partially covers the eye). This has some effects on combat, attacks and the like. Valid relation tokens are AROUND, SURROUNDED_BY, ABOVE, BELOW, IN_FRONT, BEHIND, CLEANS, and CLEANED_BY. The lattermost two tokens are used when specifying parts that clean each other (such as eyelids to eyes). |
|  BP_RELSIZE | BY_CATEGORY (or, presumably, BY_TYPE or BY_TOKEN) / body part / relsize | Defines a relsize for the selected body part for the current body detail plan |
