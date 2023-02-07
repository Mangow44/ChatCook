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

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import pandas as pd

recipe_list=[]

class ActionFeur(Action):
    def name(self) -> Text:
        return "action_feur"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Feur !")

        return []

class ActionSayRecipe(Action):
    def name(self) -> Text:
        return "action_say_recipe"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe = tracker.get_slot("recipe")

        if not recipe:
            dispatcher.utter_message(text="I don't know your recipe")
        else:
            dispatcher.utter_message(text=f"Your recipe is {recipe}")
        return []

class ActionResearchRecipe(Action):
    def name(self) -> Text:
        return "action_research_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe = tracker.get_slot('recipe')

        reader = pd.read_csv('./data/test_liste.csv')
        reader = reader[reader['Title'].str.contains(recipe, regex=False, na=False, case=False)]
        recipe_list = reader['Title'].tolist()

        if recipe_list:
            reply = "Which recipe do you want to cook ?"
            for i, item in enumerate(recipe_list):
                reply += f"\n{i + 1} - {item}"
            dispatcher.utter_message(text=reply)
        else:
            dispatcher.utter_message(text=f"I could not find recipes matching with {recipe}")

        return [SlotSet("recipe_list", recipe_list)]

class ActionSelectRecipe(Action):
    def name(self) -> Text:
        return "action_select_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe_choice = tracker.get_slot('recipe_choice')
        recipe_list = tracker.get_slot('recipe_list')

        reader = pd.read_csv('./data/test_liste.csv')

        recipe_name = recipe_list[(int(recipe_choice)-1)]

        #reader = pd.read_csv('./data/test_liste.csv')
        recipe = reader[reader['Title'].str.contains(recipe_name, regex=False, na=False, case=False)]

        if not(recipe.empty):
            reply = "Here is your recipe\n"

            reply += f"{recipe['Instructions'].values[0]}"

            dispatcher.utter_message(reply)
        else:
            dispatcher.utter_message(f"I could not find recipes matching with {recipe['Title']}")

        return []

class ActionSelectRecipe(Action):
    def name(self) -> Text:
        return "action_select_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe_choice = tracker.get_slot('recipe_choice')
        recipe_list = tracker.get_slot('recipe_list')

        reader = pd.read_csv('./data/test_liste.csv')

        recipe_name = recipe_list[(int(recipe_choice)-1)]

        #reader = pd.read_csv('./data/test_liste.csv')
        recipe = reader[reader['Title'].str.contains(recipe_name, regex=False, na=False, case=False)]

        if not(recipe.empty):
            reply = "Here is your recipe\n"

            reply += f"{recipe['Instructions'].values[0]}"

            dispatcher.utter_message(reply)
        else:
            dispatcher.utter_message(f"I could not find recipes matching with {recipe['Title']}")

        return []

class ActionHello(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bonjour ! Comment allez-vous ?")

        return []

class ActionByebye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ciao")

        return []

class ActionHappy(Action):
    def name(self) -> Text:
        return "utter_happy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I am so happy for youuuu :))")

        return []

class ActionCheerUp(Action):
    def name(self) -> Text:
        return "utter_cheer_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Courage ! Tout va bien se passer !")

        return []

class ActionHelp(Action):
    def name(self) -> Text:
        return "utter_did_that_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Did that help ?")

        return []