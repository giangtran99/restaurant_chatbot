## happy path 1 (C:\Users\thg60\AppData\Local\Temp\tmp_r9roskg\e66047a17255487f8b5efa74cb172f79_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: affirm: amazing -->
    - utter_happy


## happy path 2 (C:\Users\thg60\AppData\Local\Temp\tmp_r9roskg\e66047a17255487f8b5efa74cb172f79_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: affirm: amazing -->
    - utter_happy
* goodbye: bye-bye!   <!-- predicted: greet: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## sad path 1 (C:\Users\thg60\AppData\Local\Temp\tmp_r9roskg\e66047a17255487f8b5efa74cb172f79_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: mood_great: not good -->
    - utter_cheer_up   <!-- predicted: utter_happy -->
    - utter_did_that_help
* affirm: yes
    - utter_happy


## sad path 2 (C:\Users\thg60\AppData\Local\Temp\tmp_r9roskg\e66047a17255487f8b5efa74cb172f79_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: mood_great: not good -->
    - utter_cheer_up   <!-- predicted: utter_happy -->
    - utter_did_that_help
* deny: not really   <!-- predicted: mood_great: not really -->
    - utter_goodbye   <!-- predicted: utter_happy -->


## sad path 3 (C:\Users\thg60\AppData\Local\Temp\tmp_r9roskg\e66047a17255487f8b5efa74cb172f79_conversation_tests.md)
* greet: hi   <!-- predicted: affirm: hi -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: very terrible   <!-- predicted: mood_great: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_happy -->
    - utter_did_that_help
* deny: no   <!-- predicted: affirm: no -->
    - utter_goodbye   <!-- predicted: utter_happy -->


## say goodbye (C:\Users\thg60\AppData\Local\Temp\tmp_r9roskg\e66047a17255487f8b5efa74cb172f79_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: greet: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_greet -->


