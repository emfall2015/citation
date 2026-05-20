# Importation Bibliothéque requests pour envoyer des requetes HTTP
import requests


def get_citation():
    url = "http://api.quotable.io/random" 
    response = requests.get(url)

    if response.status_code == 200:  # la requete a reussi 
        return response.json()
    else:                            # la requete a  échoué 
        print("Erreur :", response.status_code)
        return []
