"""Exploration du dataset (étape 1). À lancer depuis la racine : python3 tools/explore.py"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data/data.csv", delimiter=",", dtype=str)
diag = data[:, 1]
X = data[:, 2:].astype(float)

features = ["radius", "texture", "perimeter", "area", "smoothness", "compactness",
            "concavity", "concave_points", "symmetry", "fractal_dimension"]
noms = []
for suffixe in ["mean", "se", "worst"]:
    for f in features:
        noms.append(f"{f}_{suffixe}")

print(f"{X.shape[0]} patients, {X.shape[1]} features\n")

# 1. Répartition M / B
for classe in ["M", "B"]:
    print(f"{classe} : {np.sum(diag == classe)} ({np.mean(diag == classe) * 100:.1f} %)")

# 2. Échelle de chaque feature
print("\nmin / max par feature :")
for i in range(30):
    print(f"{noms[i]:<24} {X[:, i].min():10.4f} {X[:, i].max():10.4f}")

# 3. Features qui séparent le mieux M et B
# score = écart entre la moyenne des M et celle des B, en nombre d'écarts-types
score = (X[diag == "M"].mean(axis=0) - X[diag == "B"].mean(axis=0)) / X.std(axis=0)
ordre = np.argsort(np.abs(score))[::-1]  # de la plus séparante à la moins séparante

print("\nles plus séparantes :")
for i in ordre[:5]:
    print(f"{noms[i]:<24} {score[i]:5.2f}")
print("\nles moins séparantes :")
for i in ordre[-5:]:
    print(f"{noms[i]:<24} {score[i]:5.2f}")

# 4. Histogrammes de la meilleure et de la pire feature
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# à gauche : la meilleure feature
i = ordre[0]
axes[0].hist(X[diag == "M", i], bins=30, alpha=0.5, label="M")
axes[0].hist(X[diag == "B", i], bins=30, alpha=0.5, label="B")
axes[0].set_title(noms[i])
axes[0].legend()

# à droite : la pire feature
i = ordre[-1]
axes[1].hist(X[diag == "M", i], bins=30, alpha=0.5, label="M")
axes[1].hist(X[diag == "B", i], bins=30, alpha=0.5, label="B")
axes[1].set_title(noms[i])
axes[1].legend()

plt.show()
