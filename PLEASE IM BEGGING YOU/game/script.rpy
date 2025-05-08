# The script of the game goes in this file.
init python:
    config.default_text_cps = 30  # adjust to your taste

    config.auto_voice = "audio/{id}.mp3"

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
                    renpy.sound.queue(f"audio/_sfx_typing_dirty/Bfxr_type_{randosound}.mp3", channel="sound", loop=False)
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")
            
define f = Character("Ferryman")
define b = Character("Bug", image = "side bug")
define t = Character("Terminal (Bug)", callback=typing_sounds, image = "side bug")
define e = Character("Elle")
define am = Character("Angry Minerva", image = "angry")
define dd = Character("Doldrums Minerva")
define pm = Character("Pious Minerva")

# The game starts here.

label start:

#shit i think we need a background for this. thankfully it's only black.

    f "You can try to flee from the chill.{w=2.0} But{w=0.35} the cold's in your bones now." id start_dfa79694

    f "No matter {w=0.1}how {w=0.1}far {w=0.2}you go,{w=1.5} it'll {i}{b}always{/b}{/i} {w=0.5}find a way in." id start_c5d441f2

    play sound "audio/_sfx_gen/SFX_ElectricityHum.mp3"
    "A hum. A dimly lit screen. A sign of life." 

    # the number 3 should appear on screen here to show the motif or whatever

    "If it weren't for the ever-mounting pressure on your upper back and the very top of your sinuses, maybe, just maybe this would be a means to celebrate."
 
    "But let's take a step back. Who exactly is celebrating here?"

    # bug appears, disheveled as fuck with their ID card on full display. would be cool to see how we can move it with technical art.
    show bug wtf at center, small_sprite, Position(xpos=0.5, ypos=0.7)
    with pixellate
    "Holy shit."

    f "Just look at yourself. {w=2.0}You see the wreckage." id start_b483d9bc
    
    f "The bags under your eyes, {w=1.9}the slouch of your posture." id start_55d92647

    f "How peculiar. {w=1.7}A warning. {w=1.1}You've fallen {w=0.3}too{w=0.2} deep {w=0.2}into this pit." id start_7b44d2ed

    f "Your isolation's {w=0.5}{i}carved{/i} {w=0.8}it's mark {w=0.2}on you." id start_e1c82833

    f "You think {w=0.2}you can {w=0.1}stay {w=0.2}here? {w=1.2}No. {w=1.0}You need to get up." id start_b418d00d

    f "You need {w=0.3}to {w=0.2}face {w=0.1}it. {w=0.5}RIGHT. {w=0.15}NOW." id start_a8ba575d
    hide bug wtf with dissolve
    jump setup_minervas

    # This ends the game.

    return