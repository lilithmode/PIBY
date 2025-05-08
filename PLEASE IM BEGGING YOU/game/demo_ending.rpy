label demo_ending:

default questionnaire_answers = {
    "q1": None,
    "q2": None,
    "q3": None,
}
#the room goes dark. the minervas are nowhere to be found
t "hello?"
hide minervaroom with pixellate
t "..."

t "guys, hello?"

"I'm afraid they aren't here anymore."

t "where are you guys? guys??"

b "No... this can't be..."

"The plug to your computer malfunctioned."

b "..."

b "Damn it."

b "Test 3 is a failure."

b "I want to go to bed..."

b "I really thought this would be the batch..."

b "Back to the questionnaire."
play music ""
label end_of_demo:
    call screen questionnaire_screen
"Maybe you'll get it next time, Bug."

"Thanks for trying."

"You'll have to try again soon when it's more developed."

"More things work on. Implementation. Yay."

b "God damn it."
    # You can inspect the answers now


return