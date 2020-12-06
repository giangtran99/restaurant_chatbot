## happy path 1 (C:\Users\thg60\AppData\Local\Temp\tmp3vdylbtk\3abab82a60d94e28898c48e637500fa3_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: deny: amazing -->
    - utter_happy   <!-- predicted: action_default_fallback -->


## happy path 2 (C:\Users\thg60\AppData\Local\Temp\tmp3vdylbtk\3abab82a60d94e28898c48e637500fa3_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: deny: amazing -->
    - utter_happy   <!-- predicted: action_default_fallback -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\thg60\AppData\Local\Temp\tmp3vdylbtk\3abab82a60d94e28898c48e637500fa3_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: goodbye: not good -->
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: goodbye: yes -->
    - utter_happy   <!-- predicted: action_default_fallback -->


## sad path 2 (C:\Users\thg60\AppData\Local\Temp\tmp3vdylbtk\3abab82a60d94e28898c48e637500fa3_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: goodbye: not good -->
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: greet: not really -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 3 (C:\Users\thg60\AppData\Local\Temp\tmp3vdylbtk\3abab82a60d94e28898c48e637500fa3_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: goodbye: very terrible -->
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: action_default_fallback -->


