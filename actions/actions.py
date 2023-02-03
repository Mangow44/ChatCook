# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionFeur(Action):
    def name(self) -> Text:
        return "action_feur"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Feur !")

        return []


recipe_list = []

class ActionResearchRecipe(Action):
    def name(self) -> Text:
        return "action_research_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipe = tracker.get_slot('recipe')
        with open('../data/recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            recipe_list.clear()
            recipe_list.append(row['Title'] for row in reader if recipe.lower() in row['Title'].lower())

        if recipe_list:
            reply = "Which recipe do you want to cook ?"
            for i, item in enumerate(recipe_list):
                reply += f"\n{i+1} - {item}"

            dispatcher.utter_message(reply)
        else:
            dispatcher.utter_message(f"I could not find recipes matching with {recipe}")

        return []


class ActionSelectRecipe(Action):
    def name(self) -> Text:
        return "action_select_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipe_choice = tracker.get_slot('recipe_choice')
        recipe_name = recipe_list[recipe_choice-1]
        with open('../data/recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Title'].lower() == recipe_name.lower():
                    recipe = row
                    break

        if recipe:
            # TODO
            reply = "Which recipe do you want to cook ?"
            for i, item in enumerate(recipe_list):
                reply += f"\n{i+1} - {item}"

            dispatcher.utter_message(reply)
        else:
            dispatcher.utter_message(f"I could not find recipes matching with {recipe}")

        return []



class ActionCook(Action):
    def name(self) -> Text:
        return "utter_cooking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Wow la recette !")

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