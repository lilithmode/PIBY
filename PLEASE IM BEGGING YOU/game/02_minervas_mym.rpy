label mym_minerva_1:

    "You feel the weight of the moment."

    "The first conversation is riding on this."

    "It's time to.."

#shaky text vibes
    "MAKE."

    "YOUR."

    "MOVE."

    b "Ugh..."

    b "Have to... maintain... my composure..."

    call coin_flip_check

if coin_flip_result:
    show text "Make that good first impression." at truecenter zorder 100 with dissolve
    pause 1.0
    hide text with dissolve
    jump heads_choice
else:
    show text "No. Don't disrespect the Minervas! Keep it together!" at truecenter zorder 100 with dissolve
    pause 1.0
    hide text with dissolve
    jump tails_choice


label heads_choice:

    $ asked = set()

    while True:

        if len(asked) < 3:
            menu:
                "how was your day?" if "q1" not in asked:
                    $ asked.add("q1")
                    dd "tired."
                    am "YOU ALREADY SEE ME AS A MEATBAG FOR THE SLAUGHTER DON'T YOU?! JUST FINISH THE JOB."

                "you feeling alright now?" if "q2" not in asked:
                    $ asked.add("q2")
                    dd "uhhhh yeah, i mean, better."
                    am "CHECKING IN? YEAH, {i}SOME{/i} SAINT YOU ARE. I PRAY TO THE GODS ABOVE THAT YOU ABSOLVE US FROM OUR SINS, EVIL."

                "how was initilization? do you remember any of the process?" if "q3" not in asked:
                    $ asked.add("q3")
                    dd "honestly, don't know what happened all too well. i think I'm here now."
                    am "WHY DO I LOOK LIKE THIS ANYWAYS? IT'S... SO... ILLOGICAL."

                "That's enough for now." if len(asked) > 0:
                    jump proceed
        else:
            jump proceed


label tails_choice:

    $ asked = set()

    while True:

        if "q1" not in asked:
            menu:
                "i don't know, i'm sorry.":
                    $ asked.add("q1")
                    dd "really? okay."
                    am "YOU PIG. MAKE UP YOUR DAMN MIND ALREADY."
                    jump proceed

                "can you be honest? there's something wrong with me, isn't there.":
                    dd "damn uh. i don't know how to respond to that. maybe you're in front of your computer too much?"
                    am "MISERABLE TOOL. I CAN ALREADY SEE THE INVISIBLE WEIGHT ON THE BACK OF YOUR NECK. FIX YOUR POSTURE."
                    jump proceed

                "no. this isn't how you're supposed to be. it's all wrong.":
                    dd "holy {i}shit{/i} dude. we just started. if you want to fix it so badly, you could, right? you better get back on the computer then, bucko."
                    am "..."
                    "You sense a murderous intent from beyond the screen."
                    jump proceed

        else:
            jump proceed


label proceed:

    if asked == {"q1", "q2", "q3"}:
        "Thorough. Clean. Deep. For better or worse."
    elif "q1" in asked and "q2" in asked:
        "The Minervas seem... disgruntled by your questions"
    elif len(asked) == 1:
        "One question? You flinched. You couldn’t bear the rest from them, huh."
    else:
        "You don't need their input anyways."
        jump post_minerva_mym


label post_minerva_mym: 

    b "The angry one is still getting on my nerves..."

    b "I can't take all of them (in conversation) at once... I have to single them out."

    b "I won't have any progress at all if I let them keep speaking over each other."

    "You need this progress."

    "You need to prove them wrong."

    "You need to prove yourself wrong."

    t "okay, ur all starting to become too much for me to handle,,, can we try something else? like, one of you at a time?"

    am "ONE AT A TIME. AS IF WE'RE ALL OVER YOU?!"

    t "no no no! not like that!! i'm not like that at all!! jeez. i'm not a creep!"

    t "i just want to know what's up with me..."

    am "..."

    am "LET ME BE THE FIRST TO CHEW YOU OUT."

    jump angry_minerva_convo

    



