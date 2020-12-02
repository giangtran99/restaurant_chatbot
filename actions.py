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
import json



def Menu():
    mylist = []
    f1 = Food("Lẩu dầu cay không vụn", 200, "hotpot",0)
    f2 = Food("Lẩu cay mala", 250, "hotpot",0)
    f3 = Food("Lẩu thảo dược", 230, "hotpot",0)
    f4 = Food("Thịt bò bông tuyết Mỹ", 140, "beef",0)
    f5 = Food("Thịt bò Nhật", 75, "beef",0)
    f6 = Food("Cá basa phi lê", 70, "food",0)
    f7 = Food("Múa mì", 20, "special",0)
    f8 = Food("Coca", 230, "drink",0)
    f9 = Food("Lavie", 230, "drink",0)
    mylist.append(f1)
    mylist.append(f2)
    mylist.append(f3)
    mylist.append(f4)
    mylist.append(f5)
    mylist.append(f6)
    mylist.append(f7)
    mylist.append(f8)
    mylist.append(f9)
    return mylist


class ActionAnswerPriceFood(Action):

    def name(self) -> Text:
        return "answer_price_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = str(tracker.get_slot('food'))

        Max = SequenceMatcher(a=food, b="Lẩu dầu cay không vụn").ratio()

        for item in Menu():
            temp = SequenceMatcher(a=food, b=item.name).ratio()
            if temp >= Max:
                Max = temp
                max_food = Food(item.name, item.price, item.type,0)

        if max_food.type == "beef":
            dispatcher.utter_message(
                "Món "+max_food.name+" bên em đang bán có giá " + str(max_food.price)+"k/100g ạ")
        elif max_food.type == "special":
            dispatcher.utter_message("Tiết mục "+max_food.name+" bên em đang bán có giá " + str(
                max_food.price)+"k bao gồm cả phần mì và nhân viên ra múa mì luôn ạ")
        elif max_food.type == "drink":
            dispatcher.utter_message(
                "Dạ "+max_food.name+" bên em đang bán có giá " + str(max_food.price)+"k/chai ạ")
        else:
            dispatcher.utter_message(
                "Món "+max_food.name+" bên em đang bán có giá " + str(max_food.price)+"k/suất ạ")

        return []


class OrderFood(Action):


    
    def name(self) -> Text:
        return "order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = str(tracker.get_slot('food'))
        Max = SequenceMatcher(a=food, b="Lẩu dầu cay không vụn").ratio()
        food = tracker.get_slot('food')

        if food is None:
            dispatcher.utter_message("Dạ bên mình không có món này bạn ạ") 
            return
       
        for item in Menu():
            temp = SequenceMatcher(a=food, b=item.name).ratio()
            if temp >= Max:
                Max = temp
                max_food = Food(item.name, item.price, item.type,0)

        jsonOrder = tracker.get_slot('listOrder')
        print(jsonOrder)
        tOrder = tracker.get_slot('totalOrder')
        lOrder = [] 

        if tOrder is None or jsonOrder is None or lOrder is None:
            tOrder = 0
            lOrder = []
            jsonOrder = '[]'

        lOrder = json.loads(jsonOrder)
        tOrder+= max_food.price
        lOrder.append(max_food.__dict__)
        jsonOrder = json.dumps([item for item in lOrder])
        

        dispatcher.utter_message("Mình đã xác nhận đặt món cho bạn rồi nhé. Bạn muốn đặt gì thêm không ?")
        return [SlotSet("listOrder",jsonOrder),SlotSet("totalOrder", tOrder)]

class AnswerOrderFood(Action):
       
    def name(self) -> Text:
        return "answer_food_in_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        jsonOrder = tracker.get_slot('listOrder')
        lOrder = json.loads(jsonOrder)
        result = ""

        for item in lOrder:
            result+= "\n"+"(*) "+item["name"]+" - Số lượng: "+item["quanity"]
        dispatcher.utter_message("Danh sách món bạn đã đặt :") 
        dispatcher.utter_message(result)   
            
        return []

class AnswerOrderFoodv2(Action):
       
    def name(self) -> Text:
        return "answer_total_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        totalOrder = tracker.get_slot('totalOrder')

        if totalOrder is None:
            dispatcher.utter_message("Bạn chưa đặt món mà :D") 
        else:
            dispatcher.utter_message("Dạ tổng của anh hết: "+str(totalOrder)+ "k ạ !")  
        return []

class AnswerOrderFoodv3(Action):
       
    def name(self) -> Text:
        return "action_remove_food_in_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       
        return []

class SearchFood(Action):
       
    def name(self) -> Text:
        return "answer_search_food"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')

        if food is None:
            dispatcher.utter_message("Dạ bên mình không có bạn ạ") 
        else:
            dispatcher.utter_message("Bên mình có nhé !") 
        
        return []