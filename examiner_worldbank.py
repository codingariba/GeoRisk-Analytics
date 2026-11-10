import json
import pandas as pd

fichier = r"sources_brutes\worldbank\population_rurale_maroc.json"

with open(fichier, "r", encoding="utf-8") as f:
    contenu = json.load(f)

observations = contenu[1]

df = pd.DataFrame([
    {
        "annee": int(obs["date"]),
        "population_rurale": obs["value"]
    }
    for obs in observations
])

df["population_rurale"] = pd.to_numeric(
    df["population_rurale"], errors="coerce"
)

df = df.sort_values("annee")

print("=== 10 OBSERVATIONS LES PLUS RECENTES ===")
print(df.tail(10).to_string(index=False))

print("\n=== PREMIERE ET DERNIERE OBSERVATION ===")
print(df.iloc[[0, -1]].to_string(index=False))

print("\n=== CONTROLES ===")
print("Nombre d'années distinctes :", df["annee"].nunique())
print("Années dupliquées :", df["annee"].duplicated().sum())
print("Valeurs négatives :", (df["population_rurale"] < 0).sum())
print("Valeurs manquantes :", df["population_rurale"].isna().sum())
