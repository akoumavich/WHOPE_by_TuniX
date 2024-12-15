# suicide_training

Dans ce fichier vous trouverez les différentes fonctions utilisées dans les différents fichiers du paquet suicide_training

## import_dataset.py
#### Ce fichier permet d'importer la base de données d'entraînement

- import_dataset : cette fonction importe la base de données d'entraînement retourne une liste contenant les tweets et un vecteur contenant les labels correspondant (0:non suicidaire, 1: suicidaire)
## pre_processing.py
#### Ce fichier permet d'effectuer l'opération de preprocessing
- text_preprocess : cette fonction prend une liste de tweets et transforme ses tweets en lemmatizant les mots, enlevant les caractères spéciaux et les caractères isolés.
## vectorize.py
#### Ce fichier permet de vectorizer une liste de tweets
- vectorize_data : cette fonction vectorize une liste de tweets en utilisant un TFIDF-Vectorizer
## training.py
#### Ce fichier permet d'entraîner nôtre modèle
- split_data : cette fonction diviser la base de données d'entraînement en 80 % pour l'apprentissage et 20 % pour le test
- trained_model : cette fonction retourne un RandomForestClassifier entraîné
## save_model.py
#### Ce fichier permet de sauvegarder le modèle entraîné
- optimum_classifier : retourne le modèle entraîné avec les paramètres optimaux
- save_as_model : sauvegarder le modèle dans le fichier suicide_classifier
## prediction.py
#### Ce fichier permet de faire la prédiction sur une base de données
- predicted_dataframe : prend une base de données et ajoute une colonne pour le label prédit et une colonne pour la probabilité de ce label
- save_predicted_dataframe : permet de sauvegarder la base de données prédite sous format (.csv)
## evaluate.py
#### Ce fichier permet d'évaluer la performance de nôtre modèle
- predict_data : cette fonction permet d'effectuer la prédiction sur la partie "test" de la base de données d'entraînement
- evaluate_model : cette fonction retourne la valeur de la précision de nôtre modèle
## test_file.py
#### Ce fichier permet de tester les fonctions du paquet. Pensez à l'exécuter pou vérifier le bon fonctionnement du paquet
