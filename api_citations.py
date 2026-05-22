# Importation Bibliothéque requests pour envoyer des requetes HTTP
import requests

citations =[]
def get_citation():
    url = "http://api.quotable.io/random" 
    
    for i in range(5):
        response = requests.get(url)

        if response.status_code == 200:  # la requete a reussi 
            data= response.json()
            citations.append({
            "citation": data["content"],
            "auteur": data["author"]})
            
    
        else:                            # la requete a  échoué 
            print("Erreur :", response.status_code)
            return []
    return  citations
