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

        print("answer_price_food")
        food = str(tracker.get_slot('food'))
        if food is None:
            dispatcher.utter_message("Nhà hàng mình không có món kia bạn ạ") 

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

        return [SlotSet("food",None)]


def ConvertNumber(number):
    convert = {
  "một": 1,
  "hai": 2,
  "ba": 3,
  "bốn": 4,
  "năm": 5,
  "sáu": 6,
  "bảy": 7,
  "tám": 8,
  "chín": 9,
  "mười": 10,

}
    return convert[number]


class OrderFood(Action):

    def name(self) -> Text:
        return "order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("order_food")
        food = tracker.get_slot('food') # Chứa các món trong cầu người dùng
        quanity = tracker.get_slot('quanity')
        jsonOrder = tracker.get_slot('listOrder') # Chứa các món trong order người dùng
        tOrder = tracker.get_slot('totalOrder')

        ## Nếu kiểm tra món ăn không tồn tại trong thực đơn
        if food is None :
            dispatcher.utter_message("Dạ bên mình không có món này bạn ạ") 
            return []
        
        rs =""  
        for item in food:
            rs+=item + ","
        if quanity is None:
        ## Kiểm tra không có số lượng
            dispatcher.utter_message("Bạn lấy "+rs+" số lượng thế nào ạ ?")
            return []

        
        print(food)
        print(quanity)
    
        if len(food) > len(quanity):
        ## Kiểm trả có số lượng nhưng thiếu
            dispatcher.utter_message("Bạn kiểm tra lại các món ăn đã kèm số lượng tương ứng chưa ạ ?") 
            return []
       

        ## Đổi chứ sáng số
        nQuanity = []
        for item in quanity:
            if item.isnumeric() is False:
                nQuanity.append(ConvertNumber(item.lower()))
            else:
                nQuanity.append(int(item))
         
        Max = SequenceMatcher(a=food[0], b="Lẩu dầu cay không vụn").ratio()
        list_max_food = []
        for element in food:
             for item in Menu():     
                temp = SequenceMatcher(a=element, b=item.name).ratio()
                if temp >= Max:
                    Max = temp
                    max_food= Food(item.name, item.price, item.type,item.quanity)   

             Max = SequenceMatcher(a="a", b="b").ratio()
             list_max_food.append(max_food)   
         
        lOrder = [] 

        if tOrder is None or jsonOrder is None or lOrder is None:
            tOrder = 0
            lOrder = []
            jsonOrder = '[]'

        lOrder = json.loads(jsonOrder)
        count =0
        for element in list_max_food:
            tOrder+= (element.price*nQuanity[count])
            element.quanity = nQuanity[count]
            count+=1
            lOrder.append(element.__dict__)
      
        jsonOrder = json.dumps([item for item in lOrder])
        dispatcher.utter_message("Mình đã xác nhận đặt món cho bạn rồi nhé. Bạn muốn đặt gì thêm không ?")
        return [SlotSet("listOrder",jsonOrder),SlotSet("totalOrder", tOrder),SlotSet("food",None),SlotSet("quanity",None)]

class AnswerOrderFood(Action):
       
    def name(self) -> Text:
        return "answer_food_in_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("answer_food_in_order")
        jsonOrder = tracker.get_slot('listOrder')

        if jsonOrder is None:
            dispatcher.utter_message("Bạn chưa đặt món nào cả !")  
            return [] 

        lOrder = json.loads(jsonOrder)
        result = ""
       

        for item in lOrder:
            result+= "\n"+"(*) "+item["name"]+" - Số lượng: "+str(item["quanity"])
        dispatcher.utter_message("Danh sách món bạn đã đặt :") 
        dispatcher.utter_message(result)   
            
        return []

class AnswerOrderFoodv2(Action):
   
    def name(self) -> Text:
        return "answer_total_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("answer_total_order")
        totalOrder = tracker.get_slot('totalOrder')

        if totalOrder is None:
            dispatcher.utter_message("Bạn chưa đặt món mà :D") 
        else:
            dispatcher.utter_message("Dạ tổng hóa đơn hiện tại của bạn hết: "+str(totalOrder)+ "k ạ !")  
        return []

class AnswerOrderFoodv3(Action):
       
    def name(self) -> Text:
        return "action_remove_food_in_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_remove_food_in_order")
        food = str(tracker.get_slot('food'))
        jsonOrder = tracker.get_slot('listOrder')
        tOrder = tracker.get_slot('totalOrder')

        if jsonOrder is None or tOrder is None:
            dispatcher.utter_message("Bạn chưa đặt món nào cả :D") 
            return

        if food is None:
            dispatcher.utter_message("Nhà hàng mình làm gì có món kia bạn ơi") 
            return

        Max = SequenceMatcher(a=food, b="Lẩu dầu cay không vụn").ratio()

        for item in Menu():
            temp = SequenceMatcher(a=food, b=item.name).ratio()
            if temp >= Max:
                Max = temp
                max_food = Food(item.name, item.price, item.type,item.quanity)
        
        lOrder = json.loads(jsonOrder)
        print(len(lOrder))
        print(max_food.name)
        for element in lOrder:
            tOrder-=(element["price"]*element["quanity"])
        ## Thuật toán xóa
        i=0

        for item in lOrder:
            if item["name"]==max_food.name:
                i+=1

        k = len(lOrder)-1
        for x in range(i,k+1):
            if lOrder[x]["name"]==max_food.name:
                for y in range(0,i):
                     if lOrder[y]["name"]!=max_food.name:
                        lOrder[x],lOrder[y]=lOrder[y],lOrder[x]
            
        print(lOrder)
        for x in range(i):
         lOrder.pop(0)

                      
        jsonOrder = json.dumps([item for item in lOrder]) 
        dispatcher.utter_message("Mình đã bỏ "+max_food.name+" cho bạn rồi nhé !") 

        return [SlotSet("listOrder",jsonOrder),SlotSet("totalOrder", tOrder),SlotSet("food",None)]

class SearchFood(Action):
       
    def name(self) -> Text:
        return "answer_search_food"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("answer_search_food")
        food = tracker.get_slot('food')
        print(food)

        
        if food is None:
            dispatcher.utter_message("Dạ bên mình không có bạn ạ") 
            return []

        Max = SequenceMatcher(a=food[0], b="Lẩu dầu cay không vụn").ratio()
        for item in Menu():
            temp = SequenceMatcher(a=food[0], b=item.name).ratio()
            if temp >= Max:
                Max = temp

        print(Max)
        if Max < 0.7:
            dispatcher.utter_message("Dạ bên mình không có bạn ạ") 
        else:
            dispatcher.utter_message("Bên mình có nhé !") 
        return [SlotSet("food",None)]

