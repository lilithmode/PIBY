label coin_flip_check:

    play sound ""

    show text "Keep your composure." at truecenter zorder 100 with dissolve
    pause 1.0
    hide text with dissolve

    $ result = renpy.random.choice(["heads", "tails"])

    # variations for the homies <3
    $ heads_lines = [
        "Nice work.", 
        "Steady, now. Breathe in.", 
        "Will you keep this up even further?",
        "The words bend to your will. This was inevitable."
    ]

    $ tails_lines = [
        "Uh oh.",
        "This can't be good.",
        "Dude. You're already acting weird as fuck.",
        "Holy shit man. You can't just say that...",
    ]

    if result == "heads":
        $ coin_flip_result = True
        $ flip_text = renpy.random.choice(heads_lines)
    else:
        $ coin_flip_result = False 
        $ flip_text = renpy.random.choice(tails_lines)

    hide screen say  # temporarily hide dialogue box
    show text "[flip_text]" at truecenter zorder 100 with dissolve
    pause 1.5
    hide text with dissolve

    return