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
        menu:
            "Deep breaths. Go ahead.":
                jump heads_choice
    else:
        menu:
            "Oh God. You're losing control.":
                jump tails_choice


label heads_choice:

    menu:
        "how was your day?":
            dd "tired."
            m "YOU ALREADY SEE ME AS A MEATBAG FOR THE SLAUGHTER DON'T YOU?! JUST FINISH THE JOB."
            jump proceed

        "you feeling alright now?":
            dd "uhhhh yeah, i mean, better."
            am "CHECKING IN? YEAH, {i}SOME{/i} SAINT YOU ARE. I PRAY TO THE GODS ABOVE THAT YOU ABSOLVE US FROM OUR SINS, EVIL."
            jump proceed

        "how was initilization? do you remember any of the process?":
            dd "honestly, don't know what happened all too well. i think I'm here now."
            am "WHY DO I LOOK LIKE THIS ANYWAYS? IT'S... SO... ILLOGICAL."
            jump proceed


label tails_choice:

    menu: 
        "i don't know, i'm sorry.":
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


label proceed:

    "Despite anything that could've happened, it honestly could've been worse."

    "it works~!"

    return




    



