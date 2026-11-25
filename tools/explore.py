"""
explore.py : comprendre data.csv avant de coder le réseau.
Étape 1 de la feuille de route (carnet, section « Les données »).

Ce script n'est pas demandé par le sujet. Il sert à t'approprier les données.
Il se lance depuis la racine du repo : python3 tools/explore.py
Le fichier à lire est donc data/data.csv.

À faire, dans l'ordre :
  1. Charger data.csv et afficher la forme du tableau, la première ligne
     et le diagnostic des 10 premiers patients.
  2. Compter les M et les B.
  3. Convertir les 30 mesures en nombres.
  4. Tracer l'histogramme de 2 ou 3 features, en séparant M et B.
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data/data.csv", delimiter=",", dtype=str)
print(f"Le dataset contient {data.shape[0]} patients et {data.shape[1]} colonnes.")

diag = data[:, 1]

for classe in ["M", "B"]:
    nb = np.sum(diag == classe)
    pct = np.mean(diag == classe) * 100
    print(f"Nombre de patients {classe} : {nb} ({pct:.2f} %)")


X = data[:, 2:].astype(float)
print(X.shape)
for i in range(30):
    colonne = X[:, i]
    print(f"colonne {i + 2} : min={colonne.min():.4f}, max={colonne.max():.4f}")

rayons_m = X[diag == "M", 0]
plt.hist(rayons_m, bins=30, alpha=0.5, label="M")
plt.show()