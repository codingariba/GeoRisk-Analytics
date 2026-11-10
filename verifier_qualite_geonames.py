import pandas as pd

fichier = r"sources_brutes\geonames\MA.txt"

colonnes = [
    "geonameid", "name", "asciiname", "alternatenames",
    "latitude", "longitude", "feature_class", "feature_code",
    "country_code", "cc2", "admin1", "admin2", "admin3",
    "admin4", "population", "elevation", "dem",
    "timezone", "modification_date"
]

df = pd.read_csv(
    fichier,
    sep="\t",
    header=None,
    names=colonnes,
    dtype={"geonameid": "Int64"},
    low_memory=False
)

print("=== IDENTIFIANTS ===")
print("Identifiants manquants :", df["geonameid"].isna().sum())
print("Identifiants dupliqués :", df["geonameid"].duplicated().sum())

print("\n=== NOMS ET COORDONNEES ===")
for c in ["name", "latitude", "longitude"]:
    print(c, ":", df[c].isna().sum(), "valeur(s) manquante(s)")

print("\n=== COORDONNEES HORS LIMITES ===")
hors_limites = (
    ~df["latitude"].between(-90, 90)
    | ~df["longitude"].between(-180, 180)
)
print("Nombre :", hors_limites.sum())

print("\n=== POPULATION ===")
print("Populations manquantes :", df["population"].isna().sum())
print("Populations négatives :", (df["population"] < 0).sum())

print("\n=== LIEUX HABITES ===")
lieux = df[df["feature_class"] == "P"]
print("Nombre de lieux habités :", len(lieux))
print("Avec population > 0 :", (lieux["population"] > 0).sum())
