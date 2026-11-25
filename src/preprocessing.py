"""
preprocessing.py : préparer les données pour le réseau.
Étape 3 de la feuille de route (carnet, section « Les données »).

Ce fichier ne se lance pas tout seul : train.py et predict.py
importeront ses fonctions.

Ce qu'il devra faire :
  - lire un CSV et séparer X (les 30 mesures) et y (le diagnostic) ;
  - retirer la colonne identifiant ;
  - convertir M/B en 1/0, puis en one-hot de forme (n, 2) ;
  - standardiser X avec la moyenne et l'écart-type du TRAIN uniquement.
"""
