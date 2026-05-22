# Importer la fonction get_citation de api_citation

from api_citations import get_citation

citations = get_citation()


# création du HTML dynamique
html = """
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Mes citations</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>"""

# Ajout dynamique des citations
for i, citation in enumerate(citations, start=1):
    html += f"""
    <div class="card">
        <h1>Citation {i}</h1>
        <p>{citation["citation"]}</p>
        <div class="author">
            {citation["auteur"]}
        </div>
    </div> 
    <br>
    """
# Fermeture du HTML
html += """
</body>
</html>
"""

# génération du page HTML
with open("citation.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Fichier HTML créé avec succès !")
