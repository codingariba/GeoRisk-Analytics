import pandas as pd

fichier = r"2_Kit_de_donnees\P12_Seismes\centres_hebergement.xlsx"

df = pd.read_excel(fichier)

resultat = df.groupby("commune").agg(
    nombre_centres=("centre", "count"),
    capacite_totale=("capacite", "sum"),
    personnes_hebergees=("personnes_hebergees", "sum")
).reset_index()

print("=== REPARTITION DES CENTRES PAR COMMUNE ===")
print(resultat.to_string(index=False))

print("\n=== TOTAUX GENERAUX ===")
print("Nombre de centres :", df["centre"].count())
print("Capacité totale :", df["capacite"].sum())
print("Personnes hébergées :", df["personnes_hebergees"].sum())
