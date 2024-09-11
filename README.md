# Benchmark_CART_XGB_KNN_MLP_RF

Ce projet propose un benchmark des modèles de machine learning, notamment CART, XGBoost, KNN, MLP et Random Forest, sur des données numériques. Il comprend des scripts pour l'entraînement des modèles, des évaluations de performance et des visualisations de résultats à l'aide de Streamlit.

## Installation

### Dépendances

Assurez-vous d'avoir Python installé sur votre machine, puis installez les dépendances nécessaires en utilisant pip :

```bash
pip install -r requirements.txt
```

## Jeu de données

Téléchargez le jeu de données depuis le lien suivant : https://drive.google.com/file/d/1S-1VCrzPPcy14Ez3qXK36GdgnIuIdV3X/view?usp=sharing 
Décompressez l'archive à la racine du projet. Le jeu de données doit être stocké directement à cet emplacement pour que les notebooks et scripts puissent y accéder.

## Entraînement des Modèles

Les notebooks Jupyter pour l'entraînement des modèles se trouvent dans le répertoire /src. Vous pouvez ouvrir et exécuter chacun des fichiers suivants pour entraîner les modèles sur les différents sous-ensembles de données :

concat.ipynb
network.ipynb
physical.ipynb
Chaque notebook contient les étapes nécessaires pour prétraiter les données, entraîner les modèles, et évaluer leurs performances.

## Résultats
Les résultats de l'entraînement des modèles sont enregistrés dans le dossier results situé dans /src. L'arborescence des résultats est structurée comme suit :

```lua
results/
│
├── jeu_de_données/
│   ├── sous-jeu/
│   │   ├── taille_du_jeu/
│   │   │   └── modèle/
│   │   │       └── résultats.csv

```
## Utilisation de Streamlit

L'application Streamlit est utilisée pour visualiser les résultats et effectuer des comparaisons interactives entre les modèles.

Pour lancer l'application, exécutez les commandes suivantes dans le terminal :

````bash

cd src
streamlit run home.py
````

## Pages Streamlit

Graphe données physiques : Cette page affiche un graphique montrant les niveaux des cuves en fonction du temps et des attaques. Les attaques sont sélectionnables depuis la sidebar.

Résultats : La page "Résultats" permet de comparer les résultats de deux modèles différents en fonction de divers paramètres.