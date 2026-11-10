
import csv

total = 0
habitees = 0
pop = 0

with open("MA.txt", encoding="utf-8") as f:
    lecteur = csv.reader(f, delimiter="\t")

    for row in lecteur:
        latitude = float(row[4])
        longitude = float(row[5])

        if 27 <= latitude <= 36 and -13 <= longitude <= -1:
            total += 1

            if row[6] == "P":
                habitees += 1

                if row[14].isdigit() and int(row[14]) > 0:
                    pop += 1

print("Localités dans la zone :", total)
print("Lieux habités (classe P) :", habitees)
print("Lieux habités avec population > 0 :", pop)

from collections import Counter

classes = Counter()

with open("MA.txt", encoding="utf-8") as f:
    lecteur = csv.reader(f, delimiter="\t")

    for row in lecteur:
        latitude = float(row[4])
        longitude = float(row[5])

        if 27 <= latitude <= 36 and -13 <= longitude <= -1:
            classes[row[6]] += 1

print("\nRépartition des classes :")
for classe, nombre in classes.most_common():
    print(classe, ":", nombre)
