# suicide_analysis

ce paquet contiendra les différentes fonctions qui seront utilisées pour l’analyse de la base de données.
## temporal_analysis.py

#### Ce fichier contient les fonctions qui font un traitement temporel sur les tweets

-	get_tweet_per_day : retourne une dataframe contenant le nombre de tweet suicidaire par jour.
-	get_tweet_per_month : retourne une dataframe contenant le nombre de tweets suicidaires par mois.
-	get_tweet_per_year : retourne une dataframe contenant le nombre de tweets suicidaires par an.
-	get_tweet_per_hour : retourne une dataframe contenant le nombre de tweets suicidaires par heure.



## vocabulary_analysis.py
#### Ce fichier contient les fonctions nécessaires pour l'analyse de vocabulaire des tweets.
-	get_polarity_dataframe : retourne une data frame contenant la polarité de chaque tweet.
-	extract_features: prend une data frame et retourne les expressions de longueur n  les plus utilisés. 
-	get_polarity_dataframe : retourne une data frame contenant la polarité de chaque tweet.

## vocabulary_analysis.py

#### Ce fichier contient les fonctions nécessaires pour une analyse statistique sur le contenu des tweets.
-	get_tag_numbers : retourne le nombre de personnes  taguées par tweet.
-	get_keyWord_number : retourne le nombre d'utilisation d'un mot donné par tweet.
-	get_tweet_length: retourne l’intervalle des longueurs des tweets suicidaires et des tweets non suicidaires.

## test_analysis.py

#### Ce fichier contient les fonctions nécessaires pour une analyse statistique sur le contenu des tweets.

-	test_get_polarity_dataframe : teste la fonction get_tag_numbers 
-	test_extract_features: teste la fonction extract_features
-	test_get_polarity_dataframe : teste la fonction get_polarity_dataframe
-	test_get_tag_numbers : teste la fonction get_tag_numbers
-	test_get_keyWord_number : teste la fonction get_keyWord_number
-	test_get_tweet_length: teste la fonction get_tweet_length



