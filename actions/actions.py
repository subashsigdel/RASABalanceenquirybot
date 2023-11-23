from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Mock database to store account balances
balance = {
    "123456": 1000,
    "789012": 500,
    # Add more entries as needed
}

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve account balance from the mock database
        account_number = tracker.get_slot("account_number")
        
        if account_number in balance:
            balance = balance[account_number]
            dispatcher.utter_message(
                f"Dear {tracker.get_slot('name')}, your balance is RS.{balance}."
            )
        else:
            dispatcher.utter_message("Account number not found. Please check and try again.")
        
        return []
