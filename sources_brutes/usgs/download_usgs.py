
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

DOSSIER = Path(__file__).parent
URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

parametres = {
    "format": "geojson",
    "minlatitude": 27,
    "maxlatitude": 36,
    "minlongitude": -13,
    "maxlongitude": -1,
    "minmagnitude": 0
}

tous_les_seismes = []

for annee in range(1970, 2027):
    debut = f"{annee}-01-01"
    fin = "2026-11-10" if annee == 2026 else f"{annee + 1}-01-01"

    params = parametres.copy()
    params["starttime"] = debut
    params["endtime"] = fin

    url = URL + "?" + urllib.parse.urlencode(params)

    print(f"Telechargement : {annee}...")

    try:
        requete = urllib.request.Request(
            url,
            headers={"User-Agent": "P12-Risque-Sismique/1.0"}
        )

        with urllib.request.urlopen(requete, timeout=120) as reponse:
            donnees = json.loads(reponse.read().decode("utf-8"))

        evenements = donnees.get("features", [])
        nombre_annonce = donnees.get("metadata", {}).get("count", 0)

        if len(evenements) != nombre_annonce:
            raise RuntimeError(
                f"Collecte incomplete pour {annee} : "
                f"{len(evenements)} recuperes sur {nombre_annonce} annonces."
            )
        tous_les_seismes.extend(evenements)

        print(f"  {len(evenements)} seismes recuperes.")

    except Exception as erreur:
        print(f"  ERREUR pour {annee} : {erreur}")
        raise

    time.sleep(0.5)

resultat = {
    "type": "FeatureCollection",
    "metadata": {
        "source": "USGS Earthquake Catalog",
        "periode": "1970-01-01 au 2026-11-10",
        "minmagnitude": 0,
        "nombre_seismes": len(tous_les_seismes)
    },
    "features": tous_les_seismes
}

fichier = DOSSIER / "seismes_usgs_1970_2026.geojson"

with open(fichier, "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False)

print("\nTelechargement termine.")
print(f"Nombre total de seismes : {len(tous_les_seismes)}")
print(f"Fichier cree : {fichier}")
