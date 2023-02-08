# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

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

        reader = pd.read_csv('./csv/recipes.csv')
        reader = reader[reader['Title'].str.contains(recipe, regex=False, na=False, case=False)]
        recipe_list = reader['Title'].tolist()

        if recipe_list:
            reply = "Which recipe do you want to cook ?"
            for i, item in enumerate(recipe_list):
                if i<30:
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

        reader = pd.read_csv('./csv/recipes.csv')

        recipe_name = recipe_list[(int(recipe_choice)-1)]

        recipe = reader[reader['Title'].str.contains(recipe_name, regex=False, na=False, case=False)]

        if not(recipe.empty):
            reply = "Here is your recipe\n"

            reply += f"{recipe['Instructions'].values[0]}"

            dispatcher.utter_message(reply)
        else:
            dispatcher.utter_message(f"I could not find recipes matching with {recipe['Title']}")

        return []

class ActionDisplayIngredients(Action):
    def name(self) -> Text:
        return "action_display_ingredients"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe_choice = tracker.get_slot('recipe_choice')
        recipe_list = tracker.get_slot('recipe_list')

        reader = pd.read_csv('./csv/recipes.csv')

        recipe_name = recipe_list[(int(recipe_choice)-1)]

        recipe = reader[reader['Title'].str.contains(recipe_name, regex=False, na=False, case=False)]

        if not(recipe.empty):
            reply = "Here are the ingredients you will need :\n"

            list_ingredients = recipe['Ingredients'].values[0]
            list_ingredients = list_ingredients[2:]
            list_ingredients = list_ingredients[:-2]
            list_ingredients = list_ingredients.split("', '")

            for i in list_ingredients:
                reply += "- " + i + "\n"

            reply += "\nDo you want to see the full recipe ?"

            dispatcher.utter_message(reply)
        else:
            dispatcher.utter_message(f"I could not find recipes matching with {recipe['Title']}")

        return []