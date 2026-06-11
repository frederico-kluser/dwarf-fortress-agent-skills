# Speech mods

> Fonte: [Speech mods](https://dwarffortresswiki.org/index.php/Speech_mods) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\
Dwarf Fortress' Speech files determine the exact dialog (mostly in adventurer mode) between two characters, such as the threats an important enemy will make to you before attacking, or the response when you ask a child his or her profession. The files may be found in the Dwarf Fortress folder, in the directory "data/speech". These files are easily modified by adding additional lines of text, one entry per line. Take for instance, the file "positive.txt":

    fantastic!
    wonderful!
    I'm thrilled to hear that.
    I'm pleased to hear that.
    that is good news.
    that is wonderful news.
    this is encouraging.
    very good.
    I'm proud of you.
    that is a good turn of affairs.

A file may also contain a variable in brackets. Instead of displaying the variable, Dwarf Fortress will display its contents (often the age of the speaker, their profession, or someone they killed.) For instance, the file "hist_fig_slayer.txt":

    It is I that felled [CONTEXT:HIST_FIG:TRANS_NAME] the [CONTEXT:HIST_FIG:RACE].

This can be thought of as the speaker saying "It is I that felled (translated name of a historical figure) the (race)". The result may look like:

    It is I that felled Urist Skyseal the dwarf.

To figure out the exact meaning of the variable(s) involved, it is usually sufficient to see how they are used in the actual game. In other cases, their meaning is obvious by the name of the file and the dialog before or after their usage.

\

## The Usage of this Page

The contents of speech files are to be placed here with the intention of any user adding new possible replies to them as they see fit. Another user may then copy the new dialog to their appropriate files and enrich their Dwarf Fortress experience. They may also neglect to include entries they do not like, if they should choose.

### How do I add a new entry?

Simply place it at the *bottom* of the appropriate table. Be sure to check that your entry isn't already in the table to avoid duplicates. If an entire file is missing from the page, feel free to create the table for it yourself, but please include the default entry or entries along with any you add. Please do not *remove* an entry from a file unless it is obviously vandalism. When in doubt, leave a message on the talk page expressing your concern.

It is also worth noting that these entries should *not* break the fourth wall. As an example, the character speaking should not be aware that they are in a computer game.

# Mods

## wandering_profession

    I wander [CONTEXT:PLACE:TRANS_NAME].
    I roam the lands. My travels have taken me all around [CONTEXT:PLACE:TRANS_NAME].
    I live the life of a nomad in [CONTEXT:PLACE:TRANS_NAME].
    I am a vagabond. I have wandered [CONTEXT:PLACE:TRANS_NAME].
    I wander [CONTEXT:PLACE:TRANS_NAME], do you not also believe it beautiful?
    I just wander about really, I'm not really good at staying put.
    I just wander about really, I guess that makes me a wanderer.
    Oh, I'm not from around here, I wander from place to place. Nowhere ever really feels like home.

## wandering_profession_year

    I have wandered [CONTEXT:PLACE:TRANS_NAME] for [CONTEXT:NUMBER] of my years.
    I am a wanderer. I have roamed [CONTEXT:PLACE:TRANS_NAME] for around [CONTEXT:NUMBER] years.
    I have roamed the land alone for [CONTEXT:NUMBER] years.
    I have lived a nomadic life in [CONTEXT:PLACE:TRANS_NAME] for [CONTEXT:NUMBER] years. Where I lay my head is home.
    I have gone where the wind has taken me for [CONTEXT:NUMBER] years.

## thief_profession

    I seek treasures and bring them back to [CONTEXT:PLACE:TRANS_NAME].
    I am a treasure hunter and what I find goes to [CONTEXT:PLACE:TRANS_NAME].
    I do a little of this, a little of that.
    What I do isn't important.
    I acquire things that have been lost and bring them back to [CONTEXT:PLACE:TRANS_NAME].
    I retrieve trinkets from lost ages.
    I help circulate wealth, keeping it from standing still and stagnating
    What's it to ya?
    Some call me a bandit, but I prefer to think of myself as a businessman
    I'm a farmer, don't mind me. Just a poor little farmer minding my own business. Nothing to see here.
    Me? Oh, I'm nothing special.
    I do what I have to. I'm not always proud of it, but we all have to eat.

## thief_profession_year

    I seek treasures and bring them back to [CONTEXT:PLACE:TRANS_NAME] and have done so for [CONTEXT:NUMBER] of the years of my life.
    I am a treasure hunter and what I find goes to [CONTEXT:PLACE:TRANS_NAME]. I've been doing this for about [CONTEXT:NUMBER] years.
    I do a little of this, a little of that.
    What I do isn't important.
    For [CONTEXT:NUMBER] years I have acquired things that have been lost for [CONTEXT:PLACE:TRANS_NAME].

## scouting_profession

    It is my duty to scout the area around [CONTEXT:PLACE:TRANS_NAME].
    I find danger before it finds us at [CONTEXT:PLACE:TRANS_NAME].
    I scout the land around [CONTEXT:PLACE:TRANS_NAME].
    I know this area like the back of my hand.
    I watch for the enemy.

## scouting_profession_year

    I have been scouting the area around [CONTEXT:PLACE:TRANS_NAME] for [CONTEXT:NUMBER] of my years.
    For [CONTEXT:NUMBER] years I have found danger before it has found us at [CONTEXT:PLACE:TRANS_NAME].
    I have scouted the land around [CONTEXT:PLACE:TRANS_NAME] for [CONTEXT:NUMBER] years.

## past_snatcher_profession

    Once it was my calling to rescue lost children.
    For [CONTEXT:NUMBER] of my years, I rescued lost children.
    I'm ashamed of my past. Please do not ask.
    ...I wonder what happened to them... Hm? My job? Oh, it was nothing.
    Let's just say I helped poor children find new homes.
    I prefer not to talk of my child-snatching days.

## soldier_profession

    I am a soldier.
    I live by the sword.
    My profession is war.
    I bring death to those who would see [CONTEXT:PLACE:TRANS_NAME] fall to ruin.
    I simply do as I am told.
    I am a strong man among strong men, fighting for the weak.
    I'm a soldier.
    I live by the sword, I'll die by the sword.
    I follow the way of the sword.
    My sword should speak for itself.
    I am a writer, my sword is my pen, my enemies are my paper.
    I do as I am told.
    I simply do as I am told to.
    I do as I am ordered.
    I follow orders.
    I simply do as I am told.
    I do as I am commanded.
    I do as commanded.
    I fight for the weak.
    I protect the weak.
    My life is battle.
    My heart belongs to the sword.
    I am a dealer of death.
    I am the muscle of [CONTEXT:PLACE:TRANS_NAME]'s might.
    I am a guard.
    I am a warrior.
    I am an enforcer.
    I'm a dealer of death.
    I'm the muscle of [CONTEXT:PLACE:TRANS_NAME]'s might.
    I'm a guard.
    I'm a warrior.
    I'm an enforcer.
    I eliminate problems.
    You can call me "sir".

## general

    whose bones you now stand on
    who wore [PRO_POS] entrails around [PRO_POS] neck
    who tried to fight, but was scattered before my strikes like wheat to a scythe
    who tried to change things that were not meant to be changed
    who lost all in [PRO_POS] attempt at battle
    who couldn't fight on a real battlefield
    whose skill in fighting couldn't match [PRO_POS] tormentor's
    whose passion was only a candle compared to my forest fire
    who tried to fly, only to find that [PRO_SUB] lacked wings
    who wished upon a star, only to have it shoot [PRO_OBJ] down
    whose questionable parentage shamed [PRO_POS] name
    who had no spouse nor child to seek vengeance
    who has been forever silenced
    who was lost
    who was an unfortunate discoverer of concealed recreational things
    for whom the bell now tolls
    who walks with the gods now
    whose voice cried out and was suddenly silenced
    whose story is ended
    who recently became a martyr for mediocrity
    who will never know another day
    who tried to fight [PRO_POS] fate
    who was made to swallow [PRO_POS] own weapon
    whose face met my foot at high velocity
    whose name shall be buried by the sands of time, forgotten by all
    who has gone to where all men and beasts one day go
    who I barely remember
    whose ghost I laugh at
    whose grave I piss on
    enjoys the taste of worm
    whose bones have made a fine back scratcher
    who knows the taste of death

## threat

    Your blood shall be spilled this day!
    I shall delight in your torture!
    I shall feast on your entrails!
    I damn you to oblivion!
    Pray while you still can!
    Ding fries are done! Ding fries are done!
    Pray to your maker!
    Submit to the cold embrace of death!
    I am going to split you like a ripe melon!
    ohhh! ohhhhh! OHHHH! and I'm done.
    Your head will hang on my wall!
    Give in to darkness and despair!
    Your life belongs to me!
    I shall couple with your skull upon your death!
    You will beg for death before I am done!
    Die! Die! DIE!
    Your phallus shall shrivel in agony!
    You will be proud to die at my hands!
    Perhaps you will be a worthy prey!
    There is no escape!
    Are you yet afraid? If not, you will be!
    You will know nothing but terror when I am through!
    Your body will fall like a limp bag!
    Scream now, for you will soon be unable to speak!
    Imma wear you like a coat! LIKE A COAT!
    I shall flatten you!
    It is already over; stand still and embrace death!
    Please do not hurt me!
    I am destined to be your last foe.
    Embrace the end that awaits you!
    You DARE challenge me?!
    Fool! Perish at my hand!
    It tis hammer time!
    Cower before my might and I might just crush you quickly.
    Do you not see? You are dead already.
    It's time to suffer!
    I shall strike you down!
    You have already made your final mistake!
    You have not felt suffering yet!
    N'wah!
    You may pry your weapon out of your own face!
    Gwowowowowowowowowowow!
    Your bones will be my dinner!
    Die, fetcher!
    You dare bring light to my lair? YOU MUST DIE!
    I, [SPEAKER:TRANS_NAME], shall knock you all down!
    I have fury!
    Now I have to kill you.
    Excuse me while I kill you.
    Do you like stew? You'll make a fine stew.
    One day they'll say [SPEAKER:TRANS_NAME] struck you down.
    One day they'll say [SPEAKER:TRANS_NAME] killed you.
    One day they'll say [SPEAKER:TRANS_NAME] made light work of you.
    One day they'll say [SPEAKER:TRANS_NAME] fed you to the underworld.
    One day they'll say [SPEAKER:TRANS_NAME] wiped the floor with you.
    One day they'll say [SPEAKER:TRANS_NAME] uses your skull as a cup.
    One day they'll say [SPEAKER:TRANS_NAME] uses your bones as a back scratcher.
    One day they'll say [SPEAKER:TRANS_NAME] played with your heart like a toy.
    One day they'll say [SPEAKER:TRANS_NAME] enjoyed killing you.
    One day they'll say [SPEAKER:TRANS_NAME] uses your head as a lantern.
    Pick a god and pray!

## greet

    Greetings.  My name is [SPEAKER:TRANS_NAME].
    Hello.  My name is [SPEAKER:TRANS_NAME].
    Howdy.  My name is [SPEAKER:TRANS_NAME].
    Ah, finally, someone sentient!   My name is [SPEAKER:TRANS_NAME].
    I am grateful for your attention.   My name is [SPEAKER:TRANS_NAME].
    What a nice shirt! I'm [SPEAKER:TRANS_NAME].
    Looking into your eyes, I can see a depth that I have not witnessed since I last glanced in the well. Pray, come speak with me.  My name is [SPEAKER:TRANS_NAME].
    Yo!  My name is [SPEAKER:TRANS_NAME].
    Greetings!  My name is [SPEAKER:TRANS_NAME].
    Hello!  My name is [SPEAKER:TRANS_NAME].
    [SPEAKER:TRANS_NAME], at your service!
    Local hunk, [SPEAKER:TRANS_NAME], gracing you with their attention!
    Please. Shut up. If you must talk, call me [SPEAKER:TRANS_NAME].
    I must say, I have never seen someone bearing boots of such an intriguing color before. My name is [SPEAKER:TRANS_NAME].
    Oh! Sorry! I didn't see you there.  My name is [SPEAKER:TRANS_NAME].
    Well!  My name is [SPEAKER:TRANS_NAME]. And it is nice to see you!
    The grass is green today, eh? I'm [SPEAKER:TRANS_NAME].

## greet_worship

    Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Praise [SPEAKER:HF_LINK:DEITY:RANDOM_DEF_SPHERE].
    Life is, in a word, [SPEAKER:HF_LINK:DEITY:RANDOM_DEF_SPHERE].
    This servant of [SPEAKER:HF_LINK:DEITY:TRANS_NAME] greets you.
    This servant of [SPEAKER:HF_LINK:DEITY:RANDOM_DEF_SPHERE] greets you.
    Greetings. Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Hello.  Praise [SPEAKER:HF_LINK:DEITY:RANDOM_DEF_SPHERE].
    Howdy.  Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Ah, finally, someone sentient!   Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    I am grateful for your attention.   Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    What a nice shirt! Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]. They love nice shirts, I'm sure!
    Looking into your eyes, I can see a depth that I have not witnessed since I last glanced in the well. Pray, come speak with me.  My name is [SPEAKER:TRANS_NAME]. Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Yo!  Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Greetings!  Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Hello!  Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    [SPEAKER:TRANS_NAME], at your service! Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]!
    Local hunk, [SPEAKER:TRANS_NAME], gracing you with their attention! Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Please. Shut up. If you must talk, praise [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    I must say, I have never seen someone bearing boots of such an intriguing color before. Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Oh! Sorry! I didn't see you there.  Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    Well!  My name is [SPEAKER:TRANS_NAME]. And praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]!
    The grass is green today, eh? Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME].
    I'm sorry, if you hate [SPEAKER:HF_LINK:DEITY:TRANS_NAME], we can't be friends. Otherwise, hello!
    Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]! Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]! Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]! Praise be to [SPEAKER:HF_LINK:DEITY:TRANS_NAME]!
    May I tell you of our Lord and Savior, [SPEAKER:HF_LINK:DEITY:TRANS_NAME]?
