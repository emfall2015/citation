import requests


def get_citation():

    url = "http://api.quotable.io/random"

    response = requests.get(url)

    # transforme le JSON en dictionnaire Python
    data = response.json()

    return data


# récupération des données
citation_data = get_citation()

citation = citation_data["content"]
auteur = citation_data["author"]


# création du HTML dynamique
html = f"""
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Mes citations</title>

    <style>
        body {{
            font-family: Arial;
            background-color: #f4f4f4;
            text-align: center;
            padding-top: 100px;
        }}

        .card {{
            background: white;
            width: 500px;
            margin: auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }}

        h1 {{
            color: #6c2bd9;
        }}

        p {{
            font-size: 20px;
        }}

        .author {{
            margin-top: 20px;
            font-weight: bold;
        }}
    </style>

</head>

<body>

    <div class="card">

        <h1>Citation du jour</h1>

        <p>"{citation}"</p>

        <div class="author">
            - {auteur}
        </div>

    </div>

</body>

</html>
"""


# génération du fichier HTML
with open("Nos_Citation.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Fichier HTML créé avec succès !")


