init python:
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
