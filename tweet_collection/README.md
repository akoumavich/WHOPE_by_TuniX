# tweet_collection

Dans ce fichier vous trouverez les différentes fonctions utilisées dans les différents fichiers du paquet tweet_collection

## tweet_collection.py
#### Ce fichier permet de collecter les tweets

- get_training_dataframe : cette fonction prend la base de données qui sera utilisée pour l’apprentissage (.csv) et la transforme en une DataFrame. 
- get_general_dataframe : cette fonction prend la base de données de tweets qui sera utilisée pour la prédiction (.csv) et la transforme en une DataFrame.
- get_suicidal_dataframe : retourne la DataFrame contenant les tweets des personnes suicidaires.
- get_non_suicidal_dataframe : retourne la DataFrame contenant les tweets des personnes non suicidaires.
- get_dataframe_to_predict : importe la base de données à prédire et mettre sous forme de DataFrame
- get_predicted_dataframe : retourne la base de données prédite sous forme de DataFrame
## test_package.py
#### Ce fichier permet de tester les fonctions du paquet. Pensez à l'exécuter pou vérifier le bon fonctionnement du paquet
