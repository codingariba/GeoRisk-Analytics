import pandas as pd

fichier = r"2_Kit_de_donnees\P12_Seismes\centres_hebergement.xlsx"
df = pd.read_excel(fichier)

print("=== GESTIONNAIRES DES CENTRES ===")
print(df["gestionnaire"].value_counts(dropna=False).to_string())

print("\nNombre de gestionnaires distincts :",
      df["gestionnaire"].nunique())
