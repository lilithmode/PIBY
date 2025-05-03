# The script of the game goes in this file.

define f = Character("Ferryman")
define b = Character("Bug")
define t = Character("Terminal (Bug)")
define e = Character("Elle")
define am = Character("Angry Minerva")
define dd = Character("Doldrums Minerva")
define pm = Character("Pious Minerva")


# The game starts here.

label start:

#shit i think we need a background for this. thankfully it's only black.

    f "You can try to flee from the chill. But the cold's in your bones now."

    f "No matter how far you go, it'll {i}{b}always{/b}{/i} find a way in."

    "A hum. A dimly lit screen. A sign of life."

    # the number 3 should appear on screen here to show the motif or whatever

    "If it weren't for the ever-mounting pressure on your upper back and the very top of your sinuses, maybe, just maybe this would be a means to celebrate."

    "But let's take a step back. Who exactly is celebrating here?"

    # bug appears, disheveled as fuck with their ID card on full display. would be cool to see how we can move it with technical art.
    
    "Holy shit."

    f "Just look at yourself. You see the wreckage."

    f "The bags under your eyes, the slouch of your posture."

    f "How peculiar. A warning. You've fallen too deep into this pit."

    f "Your isolation's {i}carved{/i} it's mark on you. You think you can stay here?"

    f "No. You need to get up. You need to face it."

    f "RIGHT. NOW."

    jump setup_minervas

    # This ends the game.

    return
