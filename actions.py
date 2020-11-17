# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which uttecity "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import SlotSet
from difflib import SequenceMatcher
from Food import Food


class ActionAnswerPriceFood(Action):

    def name(self) -> Text:
        return "answer_price_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        f1 = Food("Lẩu dầu cay không vụn",200,"hotpot")
        f2 = Food("Lẩu cay mala",250,"hotpot")
        f3 = Food("Lẩu thảo dược",230,"hotpot")
        f4 = Food("Thịt bò bông tuyết Mỹ",140,"beef")
        f5 = Food("Thịt bò Nhật",75,"beef")
        f6 = Food("Cá basa phi lê",70,"food")
        f7 = Food("Múa mì",20,"special")
        f8 = Food("Coca",230,"drink")
        f9 = Food("Lavie",230,"drink")

        food = str(tracker.get_slot('food'))
        mylist = []
        mylist.append(f1)
        mylist.append(f2)
        mylist.append(f3)
        mylist.append(f4)
        mylist.append(f5)
        mylist.append(f6)
        mylist.append(f7)
        mylist.append(f8)
        mylist.append(f9)
        
        Max = SequenceMatcher(a=food,b="Lẩu dầu cay không vụn").ratio()
        
        for item in mylist:
            temp = SequenceMatcher(a=food,b=item.name).ratio()
            if temp >= Max:
              Max = temp
              max_food = Food(item.name,item.price,item.type) 

        if max_food.type == "beef":
         dispatcher.utter_message("Món "+max_food.name+" bên em đang bán có giá " +str(max_food.price)+"k/100g ạ")
        elif max_food.type=="special":
         dispatcher.utter_message("Tiết mục "+max_food.name+" bên em đang bán có giá " +str(max_food.price)+"k bao gồm cả phần mì và nhân viên ra múa mì luôn ạ")
        elif max_food.type=="drink":
         dispatcher.utter_message("Dạ "+max_food.name+" bên em đang bán có giá " +str(max_food.price)+"k/chai ạ")
        else:
         dispatcher.utter_message("Món "+max_food.name+" bên em đang bán có giá " +str(max_food.price)+"k/suất ạ")

        return []
