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

* ask_view_restaurant
   - utter_ask_view_restaurant


## confirm_order
* want_confirm_order
   - confirm_order

## confirm_table

* want_confirm_order_table
   - confirm_order_table
   - slot{"cusName":"Giang"}
   - slot{"cusPhone":"1234567891"}
   - slot{"quanity":"1"}
   - slot{"order_table":"T1"}
   
## fallback story
* out_of_scope
   - action_default_fallback

## FAQ
* faq
   - respond_faq

## CHITCHAT
* chitchat
   - respond_chitchat

## ask_price_food
* ask_price_food
   - answer_price_food
   - slot{"food": "coca"}

## ask_info_food
* ask_info_food
   - answer_info_food
   - slot{"food": "coca"}

## ask_sale
* ask_sale
   - answer_sale

## provided_table
* provided_info_table
   - answer_provided_info_table
   - slot{"order_table":"T2"}

## provided_info_customer
* provided_info_customer
   - answer_provided_info_customer
   - slot{"cusName":"Giang"}
   - slot{"cusPhone":"1234567891"}
   - slot{"quanity":"1"}

## order_table

* want_order_table
   - action_order_table
   - slot{"cusName":"Giang"}
   - slot{"cusPhone":"1234567891"}
   - slot{"quanity":"1"}
   - slot{"order_table":"T1"}

## ORDER 
* order_food
   - action_order_food
   - slot{"order_table":"T1"}
   - slot{"food": "coca"}
   - slot{"quanity": "một"}
  
## ASK_FOOD_ORDER
* ask_food_in_order
   - answer_food_in_order
   - slot{"listOrder": "[]"}

## ASK_TOTAL_ORDER
* ask_total_order
   - answer_total_order
   - slot{"totalOrder": 210}

## SEARCH_FOOD
* search_food
   - answer_search_food
   - slot{"food": "coca"}

## REMOVE_ORDER
* remove_food_in_order
   - action_remove_food_in_order
   - slot{"food": "coca"}

## story 3
* greet
   - utter_greet
* ask_sale
   - answer_sale
* order_food
   - action_order_food
   - slot{"order_table":"T1"}
   - slot{"food": "coca"}
   - slot{"quanity": "một"}
* remove_food_in_order
   - action_remove_food_in_order
   - slot{"food": "coca"}
* goodbye
   - utter_goodbye