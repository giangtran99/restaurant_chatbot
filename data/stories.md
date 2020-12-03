## story 
* greet
  - utter_greet
* affirm  
  - utter_affirm
* deny
  - utter_deny
* mood_great
  - utter_mood_great
* happy
  - utter_happy
* unhappy
  - utter_unhappy
* cheer_up
  - utter_cheer_up
* goodbye
  - utter_goodbye

## fallback story
* out_of_scope
  - action_default_fallback

## ask_price_food
* ask_price_food
  - answer_price_food

## FAQ
* faq
   - respond_faq

## CHITCHAT
* chitchat
   - respond_chitchat

## ORDER 
* order
   - order_food

## REMOVE ORDER
* remove_food_in_order
   - action_remove_food_in_order

## ASK_FOOD_ORDER
* ask_food_in_order
   - answer_food_in_order
   - slot{"listOrder": "Cá basa phi lê \nThịt bò bông tuyết Mỹ"}

## ASK_TOTAL_ORDER
* ask_total_order
   - answer_total_order
   - slot{"totalOrder": 210}

## SEARCH_FOOD
* search_food
   - answer_search_food

