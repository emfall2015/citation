# Importer la fonction get_citation de api_citation

from api_citations import get_citation

citation_data = get_citation()

# création du HTML dynamique
html = f"""
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Mes citations</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="card">
    <h1>Citation du jour</h1>
    <p>{citation_data["content"]}</p>
    <div class="author">
        {citation_data["author"]}
    </div>
    </div>
</body>
</html>
"""

# génération du page HTML
with open("citation.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Fichier HTML créé avec succès !")
