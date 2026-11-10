import pandas as pd

fichier = r"sources_brutes\geonames\MA.txt"

df = pd.read_csv(
    fichier,
    sep="\t",
    header=None,
    usecols=[6],
    names=["feature_class"]
)

print("=== REPARTITION DES CATEGORIES GEONAMES ===")
print(df["feature_class"].value_counts().to_string())

print("\nNombre de catégories distinctes :",
      df["feature_class"].nunique())
