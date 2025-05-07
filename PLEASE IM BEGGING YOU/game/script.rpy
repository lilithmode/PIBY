# The script of the game goes in this file.
init python:
    config.default_text_cps = 30  # adjust to your taste

    # This function is optional. Only include it if you want automatic pauses between punctuation
    def typography(what):
        replacements = [
                ('. ','. {w=.2}'), # Moderate pause after periods
                ('? ','? {w=.25}'), # Long pause after question marks
                ('! ','! {w=.25}'), # Long pause after exclamation marks
                (', ',', {w=.15}'), # Short pause after commas
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography # This ensures the text block has the same ID value, even after all the replacements are made

# wen testing soundfonts implementation for terminal (bug)
    def typing_sounds(event, interact=False, **kwargs):
        if event == "show":
            what = renpy.store._last_say_what
            if what:
                words = what.split()
                for i in range(len(words)):
                    randosound = renpy.random.randint(1, 5)
                    renpy.sound.queue(f"audio/sfx_typing_dirty/Bfxr_type_{randosound}.mp3", channel="sound", loop=False)
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")
            
define f = Character("Ferryman")
define b = Character("Bug", image = "bug")

image side bug = "images/side bug neutral.png"

define t = Character("Terminal (Bug)", callback=typing_sounds)
define e = Character("Elle")
define am = Character("Angry Minerva", image = "angry")
define dd = Character("Doldrums Minerva")
define pm = Character("Pious Minerva")

# The game starts here.

label start:

#shit i think we need a background for this. thankfully it's only black.

    f "You can try to flee from the chill. But the cold's in your bones now."

    b "hey i'm testing this still"

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

    f "Your isolation's {i}carved{/i} it's mark on you."

    f "You think you can stay here? No. You need to get up."

    f "You need to face it. RIGHT. NOW."

    jump setup_minervas

    # This ends the game.

    return
