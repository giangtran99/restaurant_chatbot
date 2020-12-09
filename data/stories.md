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
   - slot{"sOrderFood": "True"}


## provided_info_customer
* provided_info_customer
   - answer_provided_info_customer
   - slot{"sOrderTable":"True"}

## order_table

* want_order_table
   - action_order_table
   - slot{"sOrderTable": "True"}
   - slot{"order_table": "None"}

## search_table
* search_table
   - action_search_table
   - slot{"table":"T1"}

## table_empty
* table_empty
   - answer_table_empty

## ORDER 
* order_food
   - action_order_food
   - slot{"sOrderFood":"True"}
   - slot{"food": "None"}
   - slot{"quanity": "None"}
   - slot{"listOrder": "None"}
   - slot{"totalOrder": "None"}
  
## ASK_FOOD_ORDER
* ask_food_in_order
   - answer_food_in_order

## ASK_TOTAL_ORDER
* ask_total_order
   - answer_total_order

## SEARCH_FOOD
* search_food
   - answer_search_food
   - slot{"food": "coca"}

## REMOVE_ORDER
* remove_food_in_order
   - action_remove_food_in_order
   - slot{"food": "coca"}
   - slot{"listOrder": "None"}
   - slot{"totalOrder": "None"}
## PROVIDED_INFO_ORDER
* provided_info_order
   - answer_provided_info_order

## story 3
* greet
   - utter_greet
* ask_sale
   - answer_sale
* order_food
   - action_order_food
   - slot{"sOrderFood":"True"}
   - slot{"food": "None"}
   - slot{"quanity": "None"}
   - slot{"listOrder": "None"}
   - slot{"totalOrder": "None"}
* remove_food_in_order
   - action_remove_food_in_order
   - slot{"food": "coca"}
   - slot{"listOrder": "None"}
   - slot{"totalOrder": "None"}
* goodbye
   - utter_goodbye

## confirm
* confirm
   - action_affirm

## suggest 1
* suggest_order_food
   - action_suggest_order_food
   - slot{"sOrderFood":"True"}
## suggest 2
* suggest_order_table
   - action_suggest_order_table
   - slot{"sOrderTable":"True"}

