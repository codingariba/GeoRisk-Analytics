import json
import pandas as pd

fichier = r"sources_brutes\usgs\seismes_usgs_2000_2026.geojson"

with open(fichier, "r", encoding="utf-8") as f:
    data = json.load(f)

evenements = []

for feature in data["features"]:
    prop = feature["properties"]
    coord = feature["geometry"]["coordinates"]

    evenements.append({
        "id": feature["id"],
        "magnitude": prop.get("mag"),
        "date": prop.get("time"),
        "profondeur": coord[2] if len(coord) > 2 else None,
        "longitude": coord[0],
        "latitude": coord[1]
    })

df = pd.DataFrame(evenements)

print("=== VALEURS MANQUANTES ===")
print(df.isna().sum())

print("\n=== IDENTIFIANTS ===")
print("Identifiants dupliqués :", df["id"].duplicated().sum())

print("\n=== MAGNITUDE ===")
print("Magnitude minimale :", df["magnitude"].min())
print("Magnitude maximale :", df["magnitude"].max())
print("Magnitudes négatives :", (df["magnitude"] < 0).sum())

print("\n=== PROFONDEUR ===")
print("Profondeurs négatives :", (df["profondeur"] < 0).sum())

print("\n=== COORDONNEES ===")
hors_limites = (
    ~df["latitude"].between(-90, 90)
    | ~df["longitude"].between(-180, 180)
)
print("Coordonnées hors limites :", hors_limites.sum())

print("\n=== PERIODE DES EVENEMENTS ===")
dates = pd.to_datetime(df["date"], unit="ms", utc=True)
print("Date la plus ancienne :", dates.min())
print("Date la plus récente :", dates.max())
