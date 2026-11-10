import pandas as pd
import glob
import os

fichiers = glob.glob("rapport_terrain_*.csv")
liste = []

for f in fichiers:
    d = pd.read_csv(f, encoding="utf-8")
    d["commune"] = os.path.basename(f).replace(
        "rapport_terrain_", ""
    ).replace(".csv", "")
    liste.append(d)

df = pd.concat(liste, ignore_index=True)

print("=== TOTAUX NUMERIQUES ===")
for col in ["menages", "maisons_detruites", "maisons_endommagees"]:
    print(col, ":", df[col].sum())

print("\n=== VALEURS ETAT_ROUTE ===")
print(df["etat_route"].value_counts(dropna=False).to_string())

print("\n=== VALEURS ACCES ===")
print(df["acces"].value_counts(dropna=False).to_string())

print("\n=== BESOINS PRIORITAIRES ===")
print(df["besoin_prioritaire"].value_counts(dropna=False).to_string())

print("\n=== QUALITE GENERALE ===")
print("Valeurs manquantes :", df.isna().sum().sum())
print("Lignes dupliquees :", df.duplicated().sum())
print("Nombre de douars distincts :", df["douar"].nunique())
print("Couples commune-douar distincts :", df[["commune", "douar"]].drop_duplicates().shape[0])
