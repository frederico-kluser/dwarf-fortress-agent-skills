# Profile

> Fonte: [Profile](https://dwarffortresswiki.org/index.php/Profile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*(For workshop profiles, see Manager.)*

The **profile** (or character sheet) is an important part of the interface, giving all information you can ever need (or better get by normal means)\* on a particular dwarf. The profile is accessible by clicking on a dwarf, and consists of several screens (or tabs): Relations, Groups, Military, Thoughts, Personality, Overview, Items, Health, Skills, Rooms, Labor.

After clicking the dwarf the overview screen (tab) is shown giving you an overview of their

- upper left box: gender, age, most important family relations and pets (if any)
- upper right box: notable characteristics
- second row box (left): (current) health status
- second row box (right): current positions (administrativ and noble)
- third row box (left): hauled (job) item, only one is shown, if multiple are hauled. Might be ie. wheelbarrow, if one is currently used by the dwarf.
- third row box (right): current assigned squad (if any) and highest combat related skills
- fourth row box (left): highest labor/job related skills
- last row box: a quote from the dwarf (ie. about their most recent activity or their general view on life or how they are feeling) and their most recent thoughts and memories. This can give an overview of some of the most recent activities of the dwarf.

Also on the top right side of the profile their are some buttons to view the dwarf's (recent) combat history, customize the dwarf's name and profession (ie. give the dwarf a nickname), set the camera to follow the dwarf around and a button to send the dwarf somewhere else (ie. send the dwarf to a linked site, if any, or outright expel the dwarf).

The other tabs of the profile can be accessed by clicking a tab (above the boxes) in the profile.

*Note:* \*): Some stats (ie. concrete current attribute values, raw skill level, amount of skill experience etc.) are either not acessible by normal means (except ie. using utilities like gui/gm-editor of dfhack) or only acessible (shown), if df is run with dfhack.

## Breakdown of (other) tabs

### Relations

This section is accesible by clicking the "Relations" tab. It lists the relations with other dwarves, worshipped deities (and/or religions), pets and bonded animals. Close family relations are listed first, then any worshipped deities, followed by pets and bonded animals and at last the non-kin relationships to other dwarves (and sentient beings) are listed. The more relationships, generally, the happier they are, but also the more impacted they will be by potential deaths.

### Groups

This lists the current and former groups (also known as entities) the dwarf does (and did) belong to, their ties to that group and the positions the dwarf holds (or did hold) in that group. Every entry gives the name of the group, the type of the group/entity (ie. civilization, site government or guild) and the tie the dwarf has to the group (ie. citizen, in case of a civilization). Groups, where the dwarf holds (or did held) a position, will be listed multiple times as each position is also a link/tie to a group. Also note for each unique position (like manager or mayor) of a group only one entry is added, ie. if a dwarf was previously a manager and is again serving as a manager, it is only mentioned that the dwarf is currently the manager (and not that the dwarf is also the ex-manager), but for each squad the dwarf was (or is) part of the list will have an entry, also for each different militia captain (squad leader) position the dwarf holds (or did hold) an entry is listed (as each squad has its own unique leader).

### Military

Has three sub-tabs: squads (opened after clicking on the military tab), uniform and kills. If the dwarf is in a squad the name of the squad and the current orders are listed (in the first tab, opened upon clicking the military tab). The second tab gives an overview of the assigned uniform (if any) and the third tab shows the kill list.

#### Kill list

A dwarf's kill list is a record of what creatures they have killed (slaughtering aside). Only dwarves that have actually killed things in hostile combat get kill lists. Some dwarves arrive at your fortress with a few kills already under their belt. Although vampires draining others of blood count as kills, in practice their true kill lists are hidden and usually empty as part of their disguise.

### Thoughts

*See also: Thought and Memory "Memory (thought)")*

This screen is accessible by clicking on the "Thoughts" tab. It has two sub-tabs: Recent thoughts and Memories.

The Recent thoughts (sub-)tab gives you a list of the recent thoughts of the dwarf (see thoughts), with the most recent thoughts (and remembered memories) listed first (in comparison to the list on the overview tab this list is much longer).

The Memories tab gives a lists of seasons and the memories the dwarf has gained in that season (see memories "Memory (thought)")), if a listed memory (upon becoming a core memory) did change a personality facet (and/or value) it is mentioned here (but is not generally mentioned, whether a listed memory has become a core memory or not).

### Personality

A miner's mind.

This tab consists of four sub-tabs (Traits, Values, Preferences, Needs) and gives an overview over the personality of the dwarf. When the personality tab is clicked by default the Traits tab is shown.

#### Traits

This tab gives a detailed description of the dwarf's (or character's) traits.

If any of the mental attributes (see mental attributes) are above or below the racial average attribute range, then all of these attributes are listed in the first paragraph (the paragraph is missing if all mental attributes are within the average mental attribute ranges). Instead of just listing the name of the attribute and the concrete value of the attribute a verbose description of the attribute (and the corresponding value range the attribute's value belongs to) is given instead. All attributes above the average attribute range are listed first and in green (with the attributes more tiers above the average listed before attributes with less tiers above the average) and all attributes below are listed (afterwards and) in red (with the attributes with more tiers below the average listed after the attributes with less tiers below the average, so that the worst mental attributes are listed last).

Afterwards the personality facets of the creature, which are not in the default range, are listed. As usually every creature will have a personality facet, which is not in the default range, this paragraph will usually not be empty. Again the facets, with the higher deviation from the default range are listed first. If any of the personality facets were changed due to the memory of an event becoming a core memory, for each personality facet changed, the last such event with the change is also mentioned here. Also not that temporary personality facet changes (eg. due to recent alcohol consumption) are also mentioned (and highlighted by using yellow text color).

In the next paragraph the mannerisms of the character are mentioned, which might be empty (if the character does not have any).

And afterwards the alcohol addiction of dwarves is mentioned and it is also mentioned if the character likes working outdoors - it is not mentioned, if a character does not like working outdoors.

#### Values

This subtab lists first (in one very long sentence) the general personality values shared by all members of that civilization. The personality values are ordered by the higher tier differences from the middle personality value tier listed before personality value with lower tier deviation. Any personality values, which belong to the middle tier, are omitted. Also all personality values, which differ from the normal personality value of that civilization are not mentioned in the first sentence. Afterwards in light blue (?) text color the personality values, which differ from the cultural values (of that civilization) are mentioned. And lastly, if the character has personality goals, these are listed afterwards (in vanilla, without adding any more personality goals ie. via dfhack, a character will have at most one personality goal).

#### Preferences

This sub-tab lists the preferences of the dwarf as well as the hateable vermin, the creature hates (or dislikes) the most.

#### Needs

This sub-tab lists gives an (detailed) overview of the characters needs and to which degree the need is currently met.

### Items

This tab lists the items the character is currently wearing or hauling. Any (worn) items, which are part of the regular clothing (which includes any crafts or even large gems), are marked as such (with the letter 'c' before the button at the right side of the entry) and are considered to be owned by that dwarf. Any item worn (and not hauled), which is not considered part of the regular clothing, is not considered to be owned by that dwarf. All items (ie. to view, dump or forbid the item) can be accessed via a button on the right side of the entry.

### Health

This tab has five sub-tabs, which are status, wounds, treatment, history and description. Upon clicking on the Health tab the status sub-tab is shown. If the character has any health problems, they are listed here. If the character has any (evaluated) wounds, they are listed in the wounds sub-tab. Any treatments are listed in the treatment sub-tab. The medical history (if any) of the character are given in the history sub-tab. The Description sub-tab gives a description of the dwarf (and an overview of the dwarfs physical attributes).

#### Description

This tab gives a detailed description of the creatures (appearance and physical capabilities).

First (in grey text color) a short description of the race (or species) the character belongs to is given.

If there are any physical attributes, which deviate from the average value range of that attribute for that creature, another paragraph is added listing all physical attributes, which deviate from the average value range. The ordering of the attributes is the same as the ordering for the mental attributes (and again the attributes above the default/average value range are listed in green text and the attributes below the default/average value range are listed in red text).

Afterwards a detailed description of the characters appearance is given. Also any missing or deformed extremeties (and organs) are listed (if there are any).

\

### Skills

This tab has five sub-tabs, which are Labor, Combat, Social, Other skills and knowledge. Upon clicking on the Skills tab the Labor sub-tab is opened. In all sub-tabs (except the Knowledge sub-tab) different skills the character has are listed. In each category the skills with the higher skill levels are listed above the skills with lower skill levels. For skills with the legendary rank, the skills with higher raw skill level are listed above other legendary skills with lower raw skill level. If a skill is considered to be rusty (or very rusty) it is mentioned here.

The Labor sub-tab lists all skills (with at least 1 experience point), which are associated with any labor (including organizer, for administrative jobs, and appraiser, for the broker position, but not ie. ambusher). For each skill the color associated with the corresponding profession is used as text color.

The Combat sub-tab lists all combat related skills (including Observer and Discipline, but not ie. Mining, allthough that skill is used for characters using a pick-axe as a weapon, or ambusher).

The Social sub-tab lists all social skills of the character (including ie. leader, speaker and teacher, but not student).

In the Other skills sub-tab all remaining skills are listed, which ie. includes all skills (except speaker), which are associated with any performance, Concentration, Student, Ambusher, Swimmer and Climber.

The Knowledge sub-tab lists all knowledge of ie. art forms, with known poetic forms listed before known musical forms, which in turn are listed before known dance forms.

### Rooms

This tab lists all rooms (Study, Quarters, Dining Room and Tomb) which are assigned to the dwarf. If no room of a type is assigned to the character (or the character's spouse) then this is also mentioned, ie. by saying "No Study" or "No Dining Room". If multiple rooms of a type are assigned to a character (including rooms assigned to the character's spouse) each such room is listed. Each entry has first an icon, donating the type of room, then the name of the room (or default name of that room, if the room was not named) and the type of the room (including quality) is mentioned. If any of the character's positions (noble or administrative) need a room of a certain quality, then the entry also mentions for any assigned room of that type, whether that room satisfies the requirement (and also the icon color is then changed from ie. grey, no requirement, to either green or yellow, depending on whether the room meets the requirement) - and in general all rooms, which do not satisfy the needed room quality should be removed (as the character might use the sub-standard room and thus get a bad thought from that). Also each room entry has a button on the right side to directly go to the location of that room (but this does not open the corresponding zone menu).

### Labor

This tab has four sub-tabs, which are work details (shown, after clicking the labor tab), workshops, locations and work animals. At the top of each sub-tab it is mentioned, whether the character is specialized or not (and can be changed by clicking the corresponding button).

#### Work details

If the character's profession is not a baby (nor a child), then an overview of the character's work details is given here, with the possiblity to reassign the characters work details.

#### Workshops

Lists the name of the workshop (if any name was given) the character is assigned to. Each list entry also has three buttons on the right side, allowing to navigate to the location of the workshop, to view the workshop's screen (and thereby exiting the character sheet) and to remove character from an assigned workshop. All build levers are considered workshops, too, so if the character is assigned to a lever (or multiple levers), the levers are also listed here.

If the character's profession is either baby or child, then it is only stated: "No dedicated workshop assignments".

#### Locations

Lists the name of the location with the type of occupation and the name of the location. The entry also has the possibility to open the corresponding location menu (or more precise to the zone assigned to a location with the lowest id) via a button or to remove the character from the assignment via a button.

If the character's profession is either baby or child, then it is only stated: "No dedicated location assignments".

#### Work animals

Lists all work animals, which are all animals trained for either hunting or war (including work animals currently assigned to other characters), and gives the possibility to assign or remove an assigned work animal from that character (note: the first time a work animal is assigned to a character the work animal is given a name) - it should also be noted that an assigned work animal cannot be removed via the list entry in the Pet/livestock tab of the unit list. It is also possible for all listed work animals to either view the current location of the work animal or to view the corresponding character sheet (profile) of that work animal.

It should also be noted, that it is possible to assign work animals to children and babies(!) via the Pets/Lifestock tab of the unit list, but it is not possible to remove these assigned animals (before the character did come of age), because, if the character's profession is either baby or child, then it is only stated: "Cannot assign work animals" (eventhough the assignment of work animals is clearly possible, via the Pets/Lifestock tab of the unit list).
