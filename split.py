"""
split.py : programme 1 du sujet.
Étape 2 de la feuille de route.

Rôle : couper data/data.csv en deux fichiers, data/data_train.csv (environ 80 %)
et data/data_valid.csv (environ 20 %), après avoir mélangé les lignes.

Utilisation (depuis la racine du projet) :
  python3 split.py              -> seed 42 par défaut
  python3 split.py --seed 7     -> autre mélange, lui aussi reproductible

À retenir :
  - une même seed redonne exactement les mêmes fichiers (le sujet l'autorise) ;
  - les deux fichiers font 569 lignes au total.
"""

import argparse
import random

parser = argparse.ArgumentParser(description="Split data.csv into a training set and a validation set.")
parser.add_argument("--seed", type=int, default=42, help="seed used to shuffle the lines (default: 42)")
args = parser.parse_args()

with open("data/data.csv") as file:
    lines = file.read().splitlines()

random.seed(args.seed)
random.shuffle(lines)

split_index = int(len(lines) * 0.8)
train = lines[:split_index]
valid = lines[split_index:]

with open("data/data_train.csv", "w") as file:
    file.write("\n".join(train) + "\n")

with open("data/data_valid.csv", "w") as file:
    file.write("\n".join(valid) + "\n")

print(f"seed: {args.seed}")
print(f"data/data_train.csv: {len(train)} lines")
print(f"data/data_valid.csv: {len(valid)} lines")
