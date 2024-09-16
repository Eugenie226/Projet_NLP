from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideEvents(Action):

    def name(self) -> Text:
        return "action_provide_events"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Exemple de récupération d'événements depuis une source de données
        events = "Les prochains événements sont le 100m, le marathon et le saut en longueur."
        dispatcher.utter_message(text=events)

        return []

class ActionProvideResults(Action):

    def name(self) -> Text:
        return "action_provide_results"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Exemple de récupération de résultats depuis une source de données
        results = "Usain Bolt a gagné la médaille d'or du 100m en 9.58 secondes."
        dispatcher.utter_message(text=results)

        return []

class ActionProvideAthleteInfo(Action):

    def name(self) -> Text:
        return "action_provide_athlete_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        athlete_name = tracker.get_slot('athlete_name')
        # Simuler la récupération d'informations sur un athlète
        if athlete_name:
            info = f"{athlete_name} est un athlète célèbre pour ses performances aux Jeux Olympiques."
        else:
            info = "Je n'ai pas d'informations sur cet athlète."
        
        dispatcher.utter_message(text=info)

        return []

