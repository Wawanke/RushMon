# 🧠 Pokémon Rush Analyzer – Data & ML Project

&#x20;  &#x20;

---

## 📄 Description

Ce projet vise à explorer les statistiques et les rôles tactiques des Pokémon dans un contexte de **progression rapide vers la Ligue Pokémon**. Il combine **analyse de données**, **modélisation prédictive (ML)** et une **application interactive Streamlit** pour assister les choix stratégiques des joueurs.

---

## 📌 Fonctionnalités

- Analyse exploratoire visuelle des statistiques : par type, nombre d'évolutions, légendaires vs non-légendaires.
- Classification des Pokémon selon leur chaîne d'évolution.
- ✨ Modèle ML prédisant le type principal d'un Pokémon à partir de ses statistiques.
- Application **Streamlit** intuitive : prédiction de type, vérification du type réel, exploration des caractéristiques.
- Visualisations variées : scatter plots, bar charts, violin plots, donut charts, histogrammes.

---

## 🛠️ Installation

1. **Cloner le projet** :

```bash
git clone https://github.com/votre-utilisateur/RushMon.git
cd RushMon
```

2. **Installer les dépendances** :

```bash
pip install -r requirements.txt
```

3. **Lancer l'application Streamlit** :

```bash
streamlit run app/ML.py
```

---

## 📊 Structure du Projet

```
PokemonRushProject/
├── data/
│   └── PokemonDatabase.csv
├── app/
│   └── ML.py                 # Application Streamlit interactive
├── notebook/
│   └── Pokemon.ipynb         # Analyse exploratoire
├── requirements.txt          # Librairies Python
└── README.md
```

---

## 🤖 Machine Learning

- **Objectif** : Prédire le type principal (`Primary Type`) d’un Pokémon en fonction de ses statistiques.
- **Modèle utilisé** : `RandomForestClassifier` (scikit-learn)
- **Taux de réussite** : ✅ Satisfaisant dès les premières itérations (supérieur à 80% au minimum)

### 🔹 Justification du choix du ML :

Le fait de prédire de quel type est un certain Pokémon permet de montrer que, au-delà des statistiques et des talents, le type est certes très important via l'efficacité des attaques, mais il permet aussi de définir à quelle **catégorie tactique** le Pokémon appartient : défensif, offensif, soutien, temporisateur, échangeur, etc.

Étant donné le **taux de réussite élevé du modèle**, celui-ci permet de vérifier si un Pokémon est **cohérent dans sa relation type/rôle tactique**, et qu’il n’est pas “volatile” dans son comportement. Par exemple, on ne veut pas d’un Pokémon avec plein de capacités offensives mais dont le type est structurellement défensif.

C’est donc via cette idée que l’on peut organiser une équipe de manière globale lors d’un **rush**, et éviter de se retrouver avec une équipe qui, sur le papier, semble très bonne, mais qui est en réalité constituée uniquement de Pokémon défensifs, ce qui en combat réel serait un vrai problème pour le rush.

---

## 💻 Application Streamlit

L'application permet :

- de sélectionner un Pokémon existant
- d'en afficher les caractéristiques numériques
- de **prédire son type principal**
- d'afficher (en option) le **type réel** (pour vérifier la cohérence du rôle tactique)
- de consulter la performance globale du modèle
- analyse progressive des graphiques afin de comprendre leurs intérêts

---

## 📊 Explorations Graphiques

- Comparaison de stats entre légendaires / non-légendaires
- Répartition par chaîne d'évolution (aucune, une ou deux)
- Visualisations de moyennes, distributions et déviations
- Utilisation de `matplotlib`, `numpy`, `scipy`, `gaussian_kde` pour des plots personnalisés

---

## 🛠️ Technologies Utilisées

- Python 3.9+
- Pandas, Numpy, Scikit-learn
- Matplotlib, Seaborn
- Streamlit

---

## 👤 Auteurs

- Kervoelen Erwann
- Paillard Mathis

> Ce projet a été réalisé dans le cadre d'un projet de fin d'année (Bachelor 3 Ynov Campus).

