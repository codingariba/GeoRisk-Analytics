import pandas as pd

fichier = r"2_Kit_de_donnees\P12_Seismes\centres_hebergement.xlsx"
df = pd.read_excel(fichier)

print("=== 1. VALEURS MANQUANTES ===")
print(df.isnull().sum())

print("\n=== 2. LIGNES DUPLIQUEES ===")
print("Nombre :", df.duplicated().sum())

print("\n=== 3. VALEURS NUMERIQUES ===")
for colonne in ["capacite", "personnes_hebergees"]:
    print("\n", colonne)
    print("Valeurs négatives :", (df[colonne] < 0).sum())
    print("Valeurs nulles :", (df[colonne] == 0).sum())
    print("Valeurs non numériques :", df[colonne].isna().sum())

print("\n=== 4. CENTRES AVEC DEPASSEMENT DE CAPACITE ===")
depassements = df[df["personnes_hebergees"] > df["capacite"]]
print(depassements[["centre", "commune", "capacite",
                    "personnes_hebergees"]].to_string(index=False))
print("\nNombre de centres concernés :", len(depassements))
