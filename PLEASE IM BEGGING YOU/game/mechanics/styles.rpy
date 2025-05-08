init python:
    style.unsent_text = Style(style.default)
    style.unsent_text.color = "#FFFFFF80"
    style.unsent_text.italic = True
    style.unsent_text.size = 26
    style.unsent_text.font = "DejaVuSans.ttf" 

transform hop:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform upclose:
    xpos 0.25 yalign 0.5

transform small_sprite:
    xzoom 0.5
    yzoom 0.5

## mostly for side images
image side_bug_neutral = "images/sprites/side_bug_neutral.png"
image side_bug_huh = "images/sprites/side_bug_huh.png"
image side_bug_nervous = "images/sprites/side_bug_nervous.png"
image side_bug_wtf = "images/sprites/side_bug_wtf.png"
