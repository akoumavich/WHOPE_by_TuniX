# WHOpe

WHOpe est un projet destiné à détecter et faire des analyses sur des tweets pour détecter ceux qui sont potentiellement suicidaires afin d. Ce projet peut être exploité par des organisations humanitaires comme l'OMS (WHO en anglais) pour entreprendre les mesures necessaires et sauver des vies.

## Installation
D'abords, commencez par telecharger le zip du projet et l'extraire dans un dossier "main".

Utiliser ensuite le manager de paquet [pip](https://pip.pypa.io/en/stable/) pour installer les librairies necessaires pour le fonctionnement du projet.

```bash
pip install -r requirements.txt
```

## Prédiction des Tweets
Pour utiliser notre projet suivez les instructions suivantes : 
- Ouvrir le dossier "datasets". Vous trouverez un fichier "general_dataset.csv".Remplacez le par votre base de donnée en format csv tout en gardant le même nom.
- Assurez vous que les noms des colonnes de votre table verifient les conditions suivantes: 
    * La colonne contenant l'identifiant est appelée 'id'
    * La colonne contenant les tweets est appelée 'text'
    * La colonne contenant l'année est appelée 'year'
    * La colonne contenant le mois de l'année est appelée 'month'
    * La colonne contenant le jour de la semaine est appelée 'day'
    * La colonne contenant le nombre de Likes est appelée 'nlikes'
    * La colonne contenant le nombre de replies est appelée 'nreplies'
    * La colonne contenant le nombre de retweets est appelée 'nretweets'
```bash
python verify_dataframe.py
```
- Si tout est bien, vous aurez un message "Your DataSet is ready to be predicted"
- Ouvrir le terminal dans le dossier "main" Prédire ensuite votre base en éxecutant le fichier "save_predicted_dataframe.py"
```bash
python save_predicted_dataframe.py
```
Vous trouverez la base de donnée prédite dans le dossier "datasets" sous le nom "predicted_dataset.csv"
## Analyse des données
Pour obtenir les courbes et graphes nécessaires pour l'analyse des tweets prédites, veuillez suivre les instructions suivantes :
- Executez le fichier "get_plots.py" en écrivant la ligne de code suivante
```bash
python get_plots.py
```
- Tous les plots seront disponibles dans le dossier "plots".

Les differents plots générés sont :

- "boxplot_length_predicted.png" : comparaison de la longeur des tweets suicidaires et non suicidaires dans la base prédite.
- "boxplot_length_trained.png" : comparaison de la longeur des tweets suicidaires et non suicidaires dans la base d'entraînement.
- "heatmap_day_hour_non_suicidal.png" : répartition des tweets non suicidiares par jour et par heures.
- "heatmap_day_hour_suicidal.png" : répartition des tweets suicidiares par jour et par heures.
- "length_evolution.png" : évolution de la longeur des tweets
- "pie_predicted.png" : répartition des tweets suicidaires et non suicidaires de la base prédite
- "pie_trained.png" : répartition des tweets suicidaires et non suicidaires de la base d'entraînement
- un ensemble d'histogrammes qui representent l'évolution du nombre des tweets selon les heures, jours, mois et années
- "wordcloud_non_suicidal_hope.png" : génére un nuage de mots les plus utilisés par les tweets non suicidaires.
- "wordcloud_suicidal_sad.png" : génére un nuage de mots les plus utilisés par les tweets suicidaires.

## Tableau de bord / Dashboard
Pour ouvrir le tableau de bord sur votre navigateur et avoir une expérience intéractive, veuillez suivre les instructions suivantes :
- Executez le fichier "dashboard.py" du dossier "dash_visualization" ou bien en  écrivant la ligne de code suivante
```bash
python dash_visualization/dashboard.py
```

# Membres de l'équipe
### Houssem Guermazi
### Mohsen Akoum
### Myriam Gueddena
### Mohamed Bouhamed
### Maissen Ben Jemaa
