"""
train.py : programme 2 du sujet.
Étapes 7, 8 et 9 de la feuille de route (carnet, section « L'entraînement »).

Rôle :
  - lire les options en ligne de commande (couches, epochs, learning rate,
    taille de batch...) ;
  - charger data_train.csv et data_valid.csv, puis les prétraiter ;
  - entraîner le réseau et afficher loss et val_loss à chaque epoch ;
  - garder l'historique des métriques dans des listes ;
  - tracer les 2 courbes à la fin : loss et accuracy ;
  - sauvegarder le modèle : topologie, poids, et statistiques de standardisation.
"""
