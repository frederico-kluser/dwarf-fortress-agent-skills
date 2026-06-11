# Memory (thought)

> Fonte: [Memory (thought)](https://dwarffortresswiki.org/index.php/Memory_(thought)) — Dwarf Fortress Wiki (GFDL/MIT)

**Memories** are recipients for a dwarf's thoughts. They are essentially an evolution of the old trauma system from previous versions.

Each dwarf has eight short-term memory slots and eight long-term memory slots. During a year-long period, the dwarf will "dwell upon/relive/remember" the eight events that evoked the strongest emotions (negative or positive) and receive an additional stress change. After a year in one of the short-term slots, a memory will then be moved to the long-term memory slots if it is stronger than the ones there, otherwise it is discarded. Long-term memory slots are retained forever and keep haunting the dwarf periodically (for better or for worse), until they are overwritten by even stronger memories or enter the dwarf's core memory. In order to avoid redundant and similar trauma that piles up and clogs your dwarf's slots (e.g. multiple instances of horror in battle when seeing many creatures die), memories are grouped into categories, and only the strongest emotion in each category will get a specific slot.

The emotion evoked by the memory may change in nature as time passes, and this may cause permanent personality changes in a dwarf's facets and values. When this happens, it will be indicated in the thoughts and preferences screen in bright magenta: which way the facet or value changed, what event caused the change and when.

## Mechanics

Dwarves have thoughts based on their experiences, which provoke emotions of varying degrees of strength, creating memories. Each type of memory falls into a group. Each dwarf has three memory storage systems: short-term, long term memory, and core memory. You can see what has recently been in a dwarf's memory by looking at their thoughts and preferences screen. If an experience is immediate: "" it has affected their short-term memory, but if an experience is recalled: "" it has affected their long-term memory. Core memories are shown in detail, alongside the year of the event and a personality change that came about as a result. ""

### Short-term memories

A dwarf has 8 short-term memory slots. When a dwarf has a thought, a check is made to see if a memory of that group already exists in a short-term memory slot. If the thought doesn't fall into an existing group, the new thought will fill an empty slot, or if no slots are empty, overwrite the weakest memory (the one with the weakest emotion) in the 8 short-term memory slots - even if the overwritten memory is stronger than the new one. If the thought already has one of its group in a memory slot the strongest memory of the two, the new thought and the existing memory, will be kept and the other discarded.

For example, a dwarf gets caught in the rain and is dejected (strength 1/4). If they haven't seen rain in the last year, this will be written to their memory, overwriting the weakest existing memory of a different group. If they have seen rain in the last year, it will overwrite the previously weaker emotion of being annoyed by the rain (strength 1/8), or ignore the new experience if the old emotion was the stronger being dismayed by the rain (strength 1/2).

This mostly leads to a constant cycling of the weakest of the 8 memory slots as new thoughts overwrite each other. An overwritten thought is a forgotten thought. You can see this in the dwarf's thoughts and preferences screen, they'll mention more than 8 things that they have recently experienced, but they are only being *affected* by 8 of those things. The list is not a reflection of what is in their current memory, but is a reflection of what has been in their memory recently. The consequence of this cycling is that short-term memories are mostly fleeting, with a maximum of 7 short-term memories having a lasting effect on a dwarf's mood.

### Long-term memories

Once a memory has remained in a short-term memory slot for one year it will attempt to be promoted to a long-term memory slot. There are 8 long-term memory slots, and the procedure works similarly to short-term memory allocations, with one important difference.

When the attempt to promote is made, a check is first made to see if there is an empty slot, if there is an empty slot the memory will be promoted to that slot even if a memory of that group already exists in another long-term memory slot. It is possible (but very rare) to have more than one memory of the same group in long term memory. This cannot happen in short term memory. If there are no empty slots a check is made to see if an existing memory of the same group exists. The promotion will fail if the existing long term memory is stronger, or will overwrite if the existing long term memory is weaker. If there are no empty slots and no existing memory of the same group, then the weakest of the other existing memories in long term will be overwritten.

When a short-term memory is promoted (or possibly fails to promote) to long term memory it leaves an empty slot in the dwarf's short-term memory. Due to the cycling of the weakest short-term memories, it tends to be the stronger emotions that cause memories to remain in short-term memory for long enough to be promoted. The effect of the promotion on the dwarf's short-term memory is that it 'purges' a slot, allowing for a relatively weaker emotion to stick around without being overwritten by the cycling.

Long-term memories are important and can be particularly impactful on a dwarf's mood because: 1) if a dwarf is frequently experiencing the same thing, good or bad, the same emotion can easily exist in both short term and long term, effectively doubling its impact; 2) long term memories are often revisited long after an experience has ceased to occur; and 3) long term memories can become clogged with thoughts that can't be promoted further - more on that below.

It's currently indeterminate what causes a dwarf to think about something in their long-term memory, whether it's random or predictable, but it seems to be frequent. (Across a sample size of 300 dwarves, all of whom had been in one of several 'happy' fortresses for more than 2 years, the median number of revisited memories was 9, with 83% of dwarves revisiting 8 or more long-term memories. This suggests that all of their long-term memories had been revisited at the point of sampling, with some cycling of long-term memories having occurred within the recent months.)

### Core memories

When a dwarf thinks about a long-term memory, it has a 1:3 chance of being promoted to core memory and causing one or more personality changes, if the memory is of a group that can be promoted to core memory. There is no limit on the number of core memory slots, and it is common to have several core memory slots populated by memories of the same group, for example, several experiences of seeing dead bodies in different years are common in core memory.

Core memories are less impactful than long-term memories, as they are rarely, if ever, revisited. However, the change that is made to the personality of the dwarf is permanent, and this can be for good or bad.

The majority of long-term memories that will be promoted to core memory are negative thoughts. The ones that have been found so far are: seeing a dead body, seeing somebody die, having a loved one die, being uncovered, experiencing trauma, experiencing miasma, rain, freakish weather or being made nauseous by the sun; and on the positive side: becoming a parent and gaining a sibling. A query to Toady about this tendency to promote only certain long-term memories to core memory confirmed that he thinks that there is an exclusion list, but couldn't recall what was on it at the time of the Q&A.

The effect of mostly negative memories being promoted to core means that the long-term memory slots of a dwarf can become clogged with relatively positive emotions, if care is taken. Only the weakest long-term memory will be cycled out by short-term memories being promoted, meaning that it is possible to maintain dwarves in an ecstatic state.

Long-term memories that are written to the core memory are removed from long-term memory, thereby leaving an empty slot.
