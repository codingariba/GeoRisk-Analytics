import pandas as pd
import glob

liste = []

for f in glob.glob("rapport_terrain_*.csv"):
    d = pd.read_csv(f, encoding="utf-8")
    liste.append(d)

df = pd.concat(liste, ignore_index=True)

print("=== FORMATS DES DATES ===")
dates = df["date_visite"].astype(str).str.strip()
print("Format AAAA-MM-JJ :", dates.str.match(r"^\d{4}-\d{2}-\d{2}$").sum())
print("Format JJ/MM/AAAA :", dates.str.match(r"^\d{2}/\d{2}/\d{4}$").sum())
print("Autres formats :", (~dates.str.match(r"^(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})$")).sum())

print("\n=== COHERENCE ROUTE / ACCES ===")
route = df["etat_route"].astype(str).str.strip().str.lower()
acces = df["acces"].astype(str).str.strip().str.lower()

print("Route praticable et accès non :", ((route == "praticable") & (acces == "non")).sum())
print("Route coupée et accès oui :", (route.isin(["coupée", "coupee"]) & (acces == "oui")).sum())

print("\n=== CONTROLE DES QUANTITES ===")
print("Maisons détruites + endommagées supérieures aux ménages :",
      ((df["maisons_detruites"] + df["maisons_endommagees"]) > df["menages"]).sum())
