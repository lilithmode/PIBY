screen questionnaire_screen():

    tag menu  # So it behaves like a menu screen

    frame:
        style_prefix "pref"
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        background Frame("#00ffc088", 10, 10)  # glowing-ish border
        padding (10, 10)

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            yfill True
            xfill True

            vbox:
                spacing 20
                text "Social Rehabilitation Reflection Tool" size 30

                text "1. How did you feel about the experience?" size 20
                vbox:
                    textbutton "It was surreal." action SetDict(questionnaire_answers, "q1", "surreal")
                    textbutton "It made me uncomfortable." action SetDict(questionnaire_answers, "q1", "uncomfortable")
                    textbutton "I didn’t really get it." action SetDict(questionnaire_answers, "q1", "confused")

                text "2. What broke the immersion of the program?" size 20
                vbox:
                    textbutton "The Glitches." action SetDict(questionnaire_answers, "q2", "glitches")
                    textbutton "Behavior of the Minervas." action SetDict(questionnaire_answers, "q2", "behaviors")
                    textbutton "My Behavior." action SetDict(questionnaire_answers, "q2", "selfhate")

                text "3. Did the conversations prove useful to self-actualization?" size 20
                vbox:
                    textbutton "Absolutely." action SetDict(questionnaire_answers, "q3", "yes")
                    textbutton "Not sure yet." action SetDict(questionnaire_answers, "q3", "maybe")
                    textbutton "Probably not." action SetDict(questionnaire_answers, "q3", "no")

                text "4. Do you feel encouraged to retry this simulation?" size 20
                vbox:
                    textbutton "Absolutely." action SetDict(questionnaire_answers, "q4", "yes")
                    textbutton "Not sure yet." action SetDict(questionnaire_answers, "q4", "maybe")
                    textbutton "Probably not." action SetDict(questionnaire_answers, "q4", "no")

                text "5. Is this enough, yet, Bug?" size 20
                vbox:
                    textbutton "No." action SetDict(questionnaire_answers, "q5", "no")
                    textbutton "No." action SetDict(questionnaire_answers, "q5", "no")
                    textbutton "No." action SetDict(questionnaire_answers, "q5", "no")

                if all(questionnaire_answers.values()):
                    textbutton "Submit" action Return()
                else:
                    text "Please answer all questions to continue." size 15 color "#999"
