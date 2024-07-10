import os.path
import os
import sqlite3
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# rajouter session/fouiller,modifier le panier, proposition en fonction du panier ou demande
#
class GetProductCharacteristics(Action):
    def name(self) -> Text:
        return "action_get_product_characteristics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produits = list(tracker.get_latest_entity_values('prod'))

        if produits:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_dir = os.path.join(BASE_DIR, 'veste.db')

            conn = sqlite3.connect(db_dir)
            cursor = conn.cursor()

            # Préparer une requête SQL dynamique pour chercher chacun des produits identifiés
            results = []
            for produit2 in produits:
                cursor.execute("SELECT * FROM produits WHERE nom=?", (produit2,))
                result = cursor.fetchone()
                results.append(result)

            conn.close()

            # Traiter les résultats obtenus
            for result in results:
                if result:
                    id_produit = result[0]
                    nom_produit = result[1]
                    description_produit = result[2]
                    prix_produit = result[3]
                    taille_dispo = result[4]
                    couleur = result[5]
                    stock = result[6]
                    dispatcher.utter_message(
                        text=f"Demande: {nom_produit}\nDescription: {description_produit}\nID produit: {id_produit}\nPrix: {prix_produit}\nTaille dispo: {taille_dispo}\nCouleur: {couleur}\nStock: {stock}"
                    )
                else:
                    dispatcher.utter_message(text=f"Demande: {produit2} - Je n'ai pas trouvé d'informations sur ce produit.")
        else:
            dispatcher.utter_message(text="Je n'ai pas trouvé le nom du produit dans votre demande.")

        return []



'''

class Produit(Action):

    def name(self) -> Text:
        return "action_produit_caracteristics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produit = next(tracker.get_latest_entity_values('prod'), None)
        if produit:
            dispatcher.utter_message(text=f"you are searching for {produit}.")
        else:
            dispatcher.utter_message(text=f"sorry, i could not not find {produit}.")
        return []

class ProduitCherche(Action):

    def name(self) -> Text:
        return "action_produit_caracteristics_cherche"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


class GiveName(Action):
    def name(self) -> Text:
        return "action_give_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        evt = BotUttered(
            text = "my name is bot? idk",
            metadata = {
                "nameGiven": "bot"
            }
        )

        return [evt]
'''