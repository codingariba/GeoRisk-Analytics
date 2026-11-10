import pandas as pd
import glob
import os

fichiers = sorted(glob.glob("rapport_terrain_*.csv"))
total = 0

print("FICHIER".ljust(38), "LIGNES", "COLONNES")
print("-" * 60)

for f in fichiers:
    d = pd.read_csv(f, encoding="utf-8")
    total += len(d)
    print(os.path.basename(f).ljust(38), len(d), len(d.columns))

print("-" * 60)
print("Nombre de fichiers :", len(fichiers))
print("Total des lignes :", total)
