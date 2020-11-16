# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which uttecity "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_core_sdk.events import SlotSet

# class ActionAskAddress(Action):

#     def name(self) -> Text:
#         return "action_hoi_dia_chi"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         city = str(tracker.get_slot('city')).lower()
#         print(city)
#         if city is None:
#            return SlotSet('is_provided_city', False)
#         else:
#            if city == "hồ chí minh" or city == "sài gòn" or city == "hcm" or city == "tphcm":
#               dispatcher.utter_message(text="Dạ nhà hàng mình có ở tại Ngô Đức Kế, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh") 
#            elif city == "hà nội" or city == "hn":
#               dispatcher.utter_message(text="Dạ nhà hàng mình có ở tại Vincom Phạm Ngọc Thạch, 2 Phạm Ngọc Thạch, P. Trung Tự,  Quận Đống Đa, Hà Nội")
#         return []
