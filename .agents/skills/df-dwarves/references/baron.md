# Baron

> Fonte: [Baron](https://dwarffortresswiki.org/index.php/Baron) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Baron

Room requirements
 

Office
Decent Office

Quarters
Decent Quarters

Dining room
Decent Dining Room

Tomb
Tomb

Furniture requirements

Chests
2

Cabinets
1

Weapon racks
1

Armor stands
1

Other

Mandates
1

Demands
2

Arrival conditions

20 Population / 100 000☼ Produced / wealth / 10 000☼ Exported / wealth

Function

Meet with / diplomats / Appoints a / Champion

When a fortress meets certain requirements, the liaison will offer to make it a barony. The player will then have the option to choose a citizen to promote to the rank of **baron**, which will take effect when the liaison leaves the map ("Do you have any dwarves to recommend for elevation?"). This offer can be temporarily rejected (by choosing the "we'd rather keep our distance" option or by canceling out of the selection screen after agreeing), deferring the choice until the liaison's next visit. Until the offer is accepted and a candidate nominated, the liaison(s) will not negotiate trade agreements. The promotion screen (see example below) displays only the names and titles of potential candidates. As of v0.50, it is possible to hit esc to close the diplomacy window, search for potential candidates in the u units menu and come back to the diplomacy window to appoint the new baron accordingly. A baron is required for your fortress to receive wagons in dwarven and human caravans. If baron gets killed, or lost on an off site mission, you will no longer get wagons (bug?).

It is also possible for a citizen to inherit a baron(ess) title, even from another site, immediately giving that citizen noble status. This can potentially result in the fortress becoming overrun with baron(esse)s that will never leave for the sites that they are the rulers of.

If the appointed baron(ess) is married, then the spouse will become the baron(ess) consort, and will be considered an unlisted noble (doesn't appear in the n noble menu, but is listed as a noble in the u units menu).

Once appointed, the local baron(ess) can issue mandates and demands, and these will be strongly influenced by his or her personal preferences. Of particular note, a baron(ess) with no item preferences will never issue any mandates (but may still make demands). If a non-mandater is appointed, it may be a good idea to supply additional happy thoughts for him/her to replace those that would have been experienced from having mandates met.

The selected baron(ess) may still perform useful labor from his/her normal life (as a miner, for example). However, as the baron is supposed to be a lazy noble, this seems to be an unintended, broken behaviour in all pre-0.50.xx versions (so far) and might be fixed in future releases.

If a baron dies, goes insane, or has an unfortunate accident, players will not be able to appoint a new baronBug:2960 and consequently cannot get other nobles which are upgraded from baron, i.e. count and duke. However, in at least some situations, the fortress can still eventually become the seat of the monarchy of its civilization, in which case a baron (or count/duke) for the fortress at least sometimes arrives as part of the monarch's entourage. You may find a DFhack workaround here.

A picture detailing how a baron is appointed. ASCII mode.

       [POSITION:BARON]
            [NAME_MALE:baron:barons]
            [NAME_FEMALE:baroness:baronesses]
            [SPOUSE_MALE:baron consort:barons consort]
            [SPOUSE_FEMALE:baroness consort:baronesses consort]
            [NUMBER:AS_NEEDED]
            [LAND_HOLDER:1]
            [LAND_NAME:a barony]
            [RESPONSIBILITY:LAW_MAKING]
            [RESPONSIBILITY:RECEIVE_DIPLOMATS]
            [SUCCESSION:BY_HEIR]
            [APPOINTED_BY:MONARCH]
            [REPLACED_BY:COUNT]
            [PRECEDENCE:40]
            [SPECIAL_BURIAL]
            [MENIAL_WORK_EXEMPTION]
            [MENIAL_WORK_EXEMPTION_SPOUSE]
            [SLEEP_PRETENSION]
            [PUNISHMENT_EXEMPTION]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [COLOR:5:0:0]
            [ACCOUNT_EXEMPT]
            [DUTY_BOUND]
            [DEMAND_MAX:2]
            [MANDATE_MAX:1]
            [REQUIRED_BOXES:2]
            [REQUIRED_CABINETS:1]
            [REQUIRED_RACKS:1]
            [REQUIRED_STANDS:1]
            [REQUIRED_OFFICE:500]
            [REQUIRED_BEDROOM:500]
            [REQUIRED_DINING:500]
            [REQUIRED_TOMB:500]
