# Druid

> Fonte: [Druid](https://dwarffortresswiki.org/index.php/Druid) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Skill: Druid

Association
 

Profession
N/A

Job Title
Druid

Labor
None

Tasks

None

Workshop

None

Attributes

Endurance / Agility / Toughness / Empathy / Willpower / Focus

Druid refers to both an unused skill and a noble position.

## Skill

**Nature** is a skill that does not normally appear in *Dwarf Fortress*. It only exists in the raws as the [`[MAGIC_NATURE]`](/index.php/Skill_token#MAGIC_NATURE "Skill token") token, implying use in magic. As such, it is sometimes used as an extra skill by modders. However, it has no associated labors so it cannot be switched off.

Though a unit's character sheet lists creatures as being a "Dabbling Druid" (and so on), there is no associated unit type and this name cannot be changed by [`[PROFESSION_NAME]`](/index.php/Creature_token#PROFESSION_NAME "Creature token").

## Noble

**Druids** are also a position of nobility among the elves, responsible for religion and the worship of forces. Despite sharing a name, they do not possess the Druid skill. Because they are foreign rulers, druids will not normally visit and cannot be appointed in an unmodded game of Fortress mode.

Druids have the highest precedence in the elven civilization, the same as the dwarven monarch. The game treats them as the *de jure* ruler - in Legends, or if modded to be playable, on the embark screen and for "mountainhome" purposes. However, they are not directly responsible for government affairs. Instead, they select both the queen, the *de facto* leader, and the princess, who functions as a general. They are succeeded by the acolyte position, which they appoint. This allows druids to choose their intended successor.

If all the acolytes are killed, and then the druid is also killed, before he had the chance to appoint a new acolyte, they remain extinct. The elven civilisation is then doomed, because there is no druid to appoint a new queen when she dies. And thus any other positions can also no longer be filled with new candidates.\[Verify\]

       [POSITION:DRUID]
            [NAME:druid:druids]
            [NUMBER:1]
            [RESPONSIBILITY:RELIGION]
            [SUCCESSION:BY_POSITION:ACOLYTE]
            [MENIAL_WORK_EXEMPTION]
            [PUNISHMENT_EXEMPTION]
            [ELECTED]
            [DETERMINES_COIN_DESIGN]
            [PRECEDENCE:1]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [EXPORTED_IN_LEGENDS]
            [COLOR:2:0:1]
            [DUTY_BOUND]
