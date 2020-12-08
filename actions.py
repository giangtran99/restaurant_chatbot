# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which uttecity "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import SlotSet,FollowupAction
from difflib import SequenceMatcher
from Food import Food
from Customer import Customer
from Table import Table
from Sale import Sale

import json
import MySQLdb


def ListSale():
    mylist = []
    s1 = Sale("Khuyến mãi Noel ăn lẩu thảo dược tặng 1 lẩu thảo dược")
    s2 = Sale("Khuyến mãi Lễ tạ ơn 13% khi ăn lẩu mala")
    mylist.append(s1)
    mylist.append(s2)

    return mylist

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
  "mười": 10,}
    return convert[number]

def ListTable():
    mylist = []
    t1 = Table("T1","View đẹp,cạnh cửa số, không gian thoáng mát ",1)
    t2 = Table("T2","Bàn trong phòng private không sợ bị làm phiền",0)
    t3 = Table("T3","Bàn phổ thông",0)
    t4 = Table("T4","Bàn phổ thông",0)
    t5 = Table("T5","View đẹp,cạnh cửa số, không gian thoáng mát ",0)

    mylist.append(t1)
    mylist.append(t2)
    mylist.append(t3)
    mylist.append(t4)
    mylist.append(t5)
    return mylist

def ListCustomer():
    mylist = []
    c1 = Customer("Giang","123456789",1)
    c2 = Customer("Tuấn Anh","777",0)
    c3 = Customer("Nam Trường","888",0)
    mylist.append(c1)
    mylist.append(c2)
    mylist.append(c3)
    return mylist

def Menu():

    mylist = []
    f1 = Food("Lẩu dầu cay không vụn", 200, "hotpot",0,"Lẩu dầu cay là hương vị truyền thống ở MTee Ay, tuy nhiên, nước lẩu này khá cay, nhiều dầu và gia vị, các bạn không quen ăn đồ Trung Quốc và ăn được ít cay thì nên cân nhắc ")
    f2 = Food("Lẩu cay mala", 250, "hotpot",0,"Dạ trong tiếng Trung, 'ma' là tê , 'la' là cay, Mala tức là cay đến tê người.Lẩu cay thơm từ hạt ngò, thảo quả, kỳ tử,… ")
    f3 = Food("Lẩu thảo dược", 230, "hotpot",0,"Lẩu thảo dược được nầu từ nguyên liệu là các thảo dược Trung Hoa rất tốt cho sức khỏe ạ")
    f4 = Food("Thịt bò bông tuyết Mỹ", 140, "beef",0,"Thịt bò bên em được nhập khẩu đạt chất lượng của Mỹ nha anh")
    f5 = Food("Thịt bò Nhật", 75, "beef",0,"Thịt bò bên em được nhập khẩu đạt chất lượng của Nhật nha anh")
    f6 = Food("Cá basa phi lê", 70, "food",0,"Dạ cá basa bên em nhập nguyên con từ vùng biển rất tươi và thơm ạ")
    f7 = Food("Múa mì", 20, "special",0,"")
    f8 = Food("Coca", 20, "drink",0,"")
    f9 = Food("Lavie", 10, "drink",0,"")
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

        db = MySQLdb.connect("localhost","root","root","quanlykhohang")
        cursor = db.cursor()
        q = "select * from users"
        cursor.execute(q)
        r = cursor.fetchall()
        for row in r:
            username = row[1]
            print("username : {}".format(username))
            password = row[2]
            print("password : {}".format(password))
        
        print("answer_price_food")
        food = str(tracker.get_slot('food'))
        if food is None:
            dispatcher.utter_message("Nhà hàng mình không có món kia bạn ạ") 

        Max = SequenceMatcher(a=food, b="Lẩu dầu cay không vụn").ratio()

        for item in Menu():
            temp = SequenceMatcher(a=food, b=item.name).ratio()
            if temp >= Max:
                Max = temp
                max_food = Food(item.name, item.price, item.type,item.quanity,item.info)

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

class ActionAnswerInfoFood(Action):

    def name(self) -> Text:
        return "answer_info_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("answer_info_food")
        food = str(tracker.get_slot('food'))
        if food is None:
            dispatcher.utter_message("Nhà hàng mình không có món kia bạn ạ") 

        Max = SequenceMatcher(a=food, b="Lẩu dầu cay không vụn").ratio()
        for item in Menu():
            temp = SequenceMatcher(a=food, b=item.name).ratio()
            if temp >= Max:
                Max = temp
                max_food = Food(item.name, item.price, item.type,item.quanity,item.info)

        dispatcher.utter_message(max_food.info)
        return [SlotSet("food",None)]

class OrderFood(Action):

    def name(self) -> Text:
        return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action_order_food")
        

        table_for_orderfood = tracker.get_slot('order_table') 
        print(table_for_orderfood)
        food = tracker.get_slot('food') # Chứa các món trong cầu người dùng
        quanity = tracker.get_slot('quanity')
        jsonOrder = tracker.get_slot('listOrder') # Chứa các món trong order người dùng
        tOrder = tracker.get_slot('totalOrder')

        if food is None :
            dispatcher.utter_message("Bạn muốn đặt món gì ghi ra giúp mình nhé") 
            return []

        rs =""  
        for item in food:
            rs+=item + ","
            
        if quanity is None:
        ## Kiểm tra không có số lượng
            dispatcher.utter_message("Bạn lấy "+rs+" số lượng thế nào ạ ?")
            return []

                
        if table_for_orderfood is None:
            dispatcher.utter_message("Bàn đang ngồi ở bàn nào nhỉ ?!")
            return [SlotSet("sOrderFood",True)] 

        ck = False
        for table in ListTable():
            if table_for_orderfood == table.name:
                ck = True

        if ck is False:
            dispatcher.utter_message("Mình không thấy mã bàn kia bàn kiểm tra mã bàn đúng chưa ?")
            return []

        ## Nếu kiểm tra món ăn không tồn tại trong thực đơn
        
        
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
                    max_food= Food(item.name, item.price, item.type,item.quanity,item.info)   

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
        dispatcher.utter_message("Mình thêm vào order của bạn rồi nhé.")
        dispatcher.utter_message("Bạn có muốn xác nhận order này chưa ạ ? Có muốn đặt thêm gì không ?")

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

class AnswerToTalOrder(Action):
   
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

class RemoveFoodOrder(Action):
       
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
                max_food = Food(item.name, item.price, item.type,item.quanity,item.info)
        
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

class AnswerSale(Action):
       
    def name(self) -> Text:
        return "answer_sale"
    
    print("answer_sale")
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        rs =""
        dispatcher.utter_message("Dạ đây là danh sách khuyến mãi hiện tại bên em ạ !") 
        for item in ListSale():
            rs+="(*)"+item.name+"\n"

        dispatcher.utter_message(rs) 
        return []

class ConfirmOrder(Action):
    
       
    def name(self) -> Text:
        return "confirm_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("confirm_order")
        dispatcher.utter_message("Bạn vui lòng đợi một lát món ăn chuẩn bị thường trong vòng 10-15p ạ")
        return [SlotSet("listOrder",None),SlotSet("totalOrder",None),SlotSet("order_table",None),SlotSet("sOrderFood",None)]

class AnswerProvidedInFoTable(Action):

       
    def name(self) -> Text:
        return "answer_provided_info_table"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Vào ngữ cảnh order food
        check = tracker.get_slot('sOrderTable') 
        check2 = tracker.get_slot('sOrderFood')

        if check is None and check2 is None:
            return[SlotSet("sOrderFood",True),FollowupAction("action_order_food")]

        # Nếu ngữ cảnh order table thì cho về order_table
        if check is True:
            return [FollowupAction("action_order_table")]

        print("answer_provided_info_table")
        table_for_orderfood = tracker.get_slot('order_table') 

        print(table_for_orderfood)
        if table_for_orderfood is None:
            dispatcher.utter_message("Bạn ngồi bàn nào thế ?")
            return []

        
        ck = False
        for table in ListTable():
            if table_for_orderfood == table.name:
                ck = True

        if ck is False:
            dispatcher.utter_message("Mã bàn không đúng nhé bạn kiểm tra lại giúp mình ")
            return []
        
        dispatcher.utter_message("Ok bạn mình đã xác nhận được bàn bạn muốn")
        return [FollowupAction("action_order_food")]

class OrderTable(Action):

       
    def name(self) -> Text:
        return "action_order_table"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_order_table")
        cusName = tracker.get_slot('cusName') 
        cusPhone = tracker.get_slot('cusPhone') 
        quanity = tracker.get_slot('quanity') 
        table_for_orderfood = tracker.get_slot('order_table')        
        check = tracker.get_slot('sOrderFood')
        check2 = tracker.get_slot('sOrderTable')

        if check is None and check2 is None:
            return[SlotSet("sOrderTable",True),FollowupAction("action_order_table")]

        # Nếu trong ngữ cảnh order_food thì trả về order_food
        if check is True:
            return[FollowupAction("action_order_food")]  

        if table_for_orderfood is None:

            dispatcher.utter_message("Chọn mã bàn bạn muốn đặt giúp mình nhé")
            return[SlotSet("sOrderTable",True)]   
        
        # kiểm tra trạng thái mã bàn có trống không
        deny = False
        for t in ListTable():
            if t.name == table_for_orderfood and t.status == 1:
                deny = True

    
        if deny is True:
            dispatcher.utter_message("Bàn này đã có người đặt anh chọn bàn khác giúp em với ạ !")
            return[SlotSet("order_table",None)]   

        if cusName is None:
            dispatcher.utter_message("Bạn cho mình xin tên bạn với")
            return []

        if cusPhone is None:
            dispatcher.utter_message("Bạn cho mình xin Số điện thoại bạn với")
            return[]

        if quanity is None:
            dispatcher.utter_message("Cho mình hỏi bạn đi mấy người nhỉ ?")
            return[]
         
        rs = ""

        dispatcher.utter_message("Bạn có chắc chắn muốn đặt bàn này không ?")
        
        return []

class AnswerProvidedInFoCustomer(Action):

       
    def name(self) -> Text:
        return "answer_provided_info_customer"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("provided_info_customer")
        cusName = tracker.get_slot('cusName') 
        cusPhone = tracker.get_slot('cusPhone') 
        quanity = tracker.get_slot('quanity') 
        table_for_orderfood = tracker.get_slot('order_table') 
         
        if cusName is None:
            dispatcher.utter_message("Bạn cho mình xin lại tên bạn với")
            return []

        if cusPhone is None:
            dispatcher.utter_message("Bạn cho mình xin Số điện thoại bạn với")
            return[]

        if quanity is None:
            dispatcher.utter_message("Cho Mình hỏi bạn đi mấy người nhỉ ?")
            return[]

        if table_for_orderfood is None:

            dispatcher.utter_message("Chọn mã bàn bạn muốn đặt giúp mình nhé")
            return[SlotSet("sOrderTable",True)]   
        

        dispatcher.utter_message("Ok bạn mình đã xác nhận thông tin của bạn")
        return [FollowupAction("action_order_table")]

class ConfirmOrderTable(Action):
     
    def name(self) -> Text:
        return "confirm_order_table"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cusName = tracker.get_slot('cusName') 
        cusPhone = tracker.get_slot('cusPhone') 
        quanity = tracker.get_slot('quanity') 
        table_for_order= tracker.get_slot('order_table') 

        print("confirm_order_table")
        dispatcher.utter_message("Dạ mình đặt bàn thành công cho bạn rồi nhé")
        dispatcher.utter_message("Anh/Chị : "+cusName+"\nSố Điện Thoại: "+cusPhone+"\nSố Người: "+quanity[0]+"\nMã bàn : "+table_for_order)

        return [SlotSet("order_table",None),SlotSet("quanity",None),SlotSet("sOrderTable",None),SlotSet("cusName",None),SlotSet("cusPhone",None)]

class Affirm(Action):
    
       
    def name(self) -> Text:
        return "action_affirm"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        context_1 = tracker.get_slot('sOrderFood')
        context_2 = tracker.get_slot('sOrderTable')

        if context_1 is True:
            return[FollowupAction("confirm_order")]
        if context_2 is True:
            return[FollowupAction("confirm_order_table")]

        dispatcher.utter_message("Có chuyện gì không ạ ?")
        return []

class AnswerProvidedInFoOrder(Action):

       
    def name(self) -> Text:
        return "answer_provided_info_order"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("answer_provided_info_order")
        food = tracker.get_slot('food') # Chứa các món trong cầu người dùng
        quanity = tracker.get_slot('quanity')

        if food is None :
            dispatcher.utter_message("Bạn muốn đặt món gì ghi chính xác giúp mình nhé") 
            return []

        rs =""  
        for item in food:
            rs+=item + ","
            
        if quanity is None:
        ## Kiểm tra không có số lượng
            dispatcher.utter_message("Bạn lấy "+rs+" số lượng thế nào ạ ?")
            return []

        return [FollowupAction("action_order_food")]

class SugestOrderFood(Action):
    
       
    def name(self) -> Text:
        return "action_suggest_order_food"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        context_1 = tracker.get_slot('sOrderFood')
        context_2 = tracker.get_slot('sOrderTable')

        if context_1 is None and context_2 is None:
            return[SlotSet("sOrderFood",True),FollowupAction("action_order_food")]

        if context_2 is True:
            return[FollowupAction("action_order_table")]  

        dispatcher.utter_message("Có chuyện gì không ạ ?")
        return []

class SugestOrderTable(Action):
     
    def name(self) -> Text:
        return "action_suggest_order_table"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        context_1 = tracker.get_slot('sOrderFood')
        context_2 = tracker.get_slot('sOrderTable')

        if context_1 is None and context_2 is None:
            return[SlotSet("sOrderTable",True),FollowupAction("action_order_table")]

        if context_1 is True:
            return[FollowupAction("action_order_food")]  


        dispatcher.utter_message("Có chuyện gì không ạ ?")
        return []  

class SearchTable(Action):
     
    def name(self) -> Text:
        return "action_search_table"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("search_table")
        table = tracker.get_slot('table')

        if table is None:
            dispatcher.utter_message("Bên mình hết bàn này rồi bạn nhé") 
            return []

        Max = SequenceMatcher(a=table, b="T1").ratio()
        status = 0

        for item in ListTable():
            temp = SequenceMatcher(a=table, b=item.name).ratio()
            if temp >= Max:
                Max = temp
                status = item.status

        if Max < 0.7:
            dispatcher.utter_message("Bên mình hết bàn này rồi bạn nhé. Bạn thông cảm giúp mình :(") 
        elif Max >= 0.7 and status == 1:
            dispatcher.utter_message("Bên mình hết bàn này rồi bạn nhé. Bạn thông cảm giúp mình :(") 
        else :
            dispatcher.utter_message("Bên mình còn bàn này bạn nhé :D") 
        return [SlotSet("table",None)]

class AnswerTableEmpty(Action):
     
    def name(self) -> Text:
        return "answer_table_empty"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("answer_table_empty")
        answer = ""
        for item in ListTable():
            if item.status == 0 :
                answer += " {}".format(item.name)
        if(answer == ""):
            dispatcher.utter_message("Bên mình hiện tại không còn bàn nào trống bạn nhé :(")
        else :
            dispatcher.utter_message("Hiện tại bên mình còn có bàn{} trống nhé :D".format(answer))  
        return[]