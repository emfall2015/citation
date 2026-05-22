# Importation de la bibliothéque requests pour envoyer des requetes HTTP
import requests

citations = []

def get_citation():
    url = "http://api.quotable.io/quotes/random?limit=6"

    response = requests.get(url)

    if response.status_code == 200:  # La requete a réussi
        datas = response.json()

        for data in datas:
            citations.append({
                "citation": data["content"],
                "auteur": data["author"]
            })

        return citations

    else:  # La requete a échoué
        print("Erreur :", response.status_code)
        return []
