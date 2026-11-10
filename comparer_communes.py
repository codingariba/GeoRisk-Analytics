import pandas as pd
import glob
import os

dossier = r"2_Kit_de_donnees\P12_Seismes"

print("=== COMMUNES DANS LES RAPPORTS CSV ===")
communes_csv = sorted([
    os.path.basename(f)
    .replace("rapport_terrain_", "")
    .replace(".csv", "")
    .replace("_", " ")
    for f in glob.glob(os.path.join(dossier, "rapport_terrain_*.csv"))
])

for c in communes_csv:
    print("-", c)

print("\n=== COMMUNES DANS LE FICHIER EXCEL ===")
df = pd.read_excel(os.path.join(dossier, "centres_hebergement.xlsx"))

for c in sorted(df["commune"].dropna().unique()):
    print("-", c)
