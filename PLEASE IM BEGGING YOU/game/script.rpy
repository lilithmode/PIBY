# The script of the game goes in this file.

define f = Character("Ferryman")
define b = Character("Bug")

# The game starts here.

label start:

#shit i think we need a background for this. thankfully it's only black.

    f "You can try to flee from the chill. But the cold's in your bones now."

    f "No matter how far you go, it'll {i}{b}always{/b}{/i} find a way in."

    # This ends the game.

    return
