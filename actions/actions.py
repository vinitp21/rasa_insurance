# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import re
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from werkzeug.middleware import dispatcher

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'



class ActionHelloWorld(FormAction):

     def name(self) -> Text:
         return "insurance_form"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""


        print("required_slots(tracker: Tracker)")
        return ["name", "age", "1date", "state","email"]   

     def validate_email(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates the email provided by user to get an insurance."""
        email = tracker.get_slot("email")

        if(re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)):
            return {"email": value}  
            print("Valid Email")  

        else:
            dispatcher.utter_message(template="utter_wrong_email")
            return {"email": None}
            print("Invalid Email")


     def submit(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict]:

         dispatcher.utter_message(template="utter_submit")

         return []
         



