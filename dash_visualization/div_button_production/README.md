# div_button_production
Dans ce fichier vous trouverez les différentes fonctions utilisées dans les différents fichiers du paquet suicide_training.

Ce paquet permet d'avoir les fonctionnalités des boutons import_csv et predict_tweet dans le tab "Want to predict?..."
## predict_csv.py
#### Ce fichier permet d'avoir la fonctionnalité du boutton import_csv
- predict_csv: cette fonction permet d'avoir la composante "Drag and Drop" et le bouton "Save File"
- parse_contents : permet de transformer le fichier (.csv) ou (.xls) téléversé en Dataframe

- update_output : cette fonction permet d'effectuer la prédiction sur la base de données téléversée et d'afficher son contenu après prédiction, et de sauvegarder le résultat obtenu dans un fichier (.csv) en cliquant sur le bouton "Save File"
## predict_tweet.py
#### Ce fichier permet d'avoir la fonctionnalité du bouton predict_tweet
- predict_tweet : ce fichier permet d'avoir une zone pour entrer un texte et un bouton "predict"
- predict_tweet_entered : ce fichier permet de prédire si l'auteur du texte entrée est suicidaire ou pas avec une probabilité et d'afficher le résultat
