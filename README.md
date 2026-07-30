# 🚌 IDELIS — Impact des Transports sur l'Immobilier Palois (Évaluation Hédonique & Streamlit)

> 🚀 **Application interactive en ligne :** [Tester le Dashboard Streamlit](https://eudesnombo-idelis-immobilier-pau-app-1-hyukbr.streamlit.app)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-6.0+-blue?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?logo=pandas)

Projet d'analyse spatiale et d'évaluation économétrique hédonique visant à mesurer l'impact de l'accessibilité au réseau de transports en commun **IDELIS** et de sa ligne à haut niveau de service (**Fébus**) sur la valorisation foncière résidentielle à Pau (64000).

---

## 🎯 Objectifs & But du Projet

- **Quantifier la plus-value** liée à la proximité immédiate de la ligne BHNS Fébus (< 300 mètres).
- **Modéliser le gradient de dépréciation** marginale du prix au m² en fonction de l'éloignement physique d'un arrêt IDELIS.
- **Visualiser la répartition spatiale** des prix et des infrastructures de transport sur une carte dynamique.
- **Proposer un outil interactif d'aide à la décision** pour les acteurs de l'aménagement urbain, de la mobilité et de l'immobilier.

---

## 🛠️ Étapes de Réalisation Détaillées (Workflow Métier & Data)

### 1. Prétraitement et Harmonisation Géospatiale (`donnees_pau_idelis.csv`)
- **Chargement des données :** Ingestion du jeu de données spatialisées comprenant les transactions immobilières paloises, la géolocalisation des biens (latitude/longitude), ainsi que le maillage du réseau IDELIS.
- **Traitement des données manquantes & anomalies :** Nettoyage des valeurs aberrantes (*outliers*) sur les prix au m² et filtrage des coordonnées géographiques hors de la commune de Pau.
- **Calcul de métriques de distance :** Calcul de l'éloignement géodésique de chaque bien par rapport aux arrêts de bus classiques et au tracé spécifique du BHNS Fébus.

### 2. Spécification et Estimation du Modèle de Prix Hédonique
Pour décomposer la valeur d'un bien au mètre carré en fonction de ses caractéristiques intrinsèques et d'accessibilité aux transports, nous appliquons l'équation hédonique suivante :

$$\text{Prix}_{m^2} = \beta_0 + \beta_1 \cdot \text{Fébus} + \beta_2 \cdot \text{Distance}_{\text{arrêt}} + \varepsilon$$

#### Calibration des paramètres :
| Paramètre / Variable | Coefficient Retenu | Interprétation Économétrique |
| :--- | :--- | :--- |
| **$\beta_0$ (Constante)** | `2 150 €/m²` | Prix médian de référence sur la commune de Pau pour un bien standard. |
| **$\beta_1$ (Effet Fébus)** | `+350 €/m²` | Plus-value explicite liée à une accessibilité directe à la ligne Fébus (< 300m). |
| **$\beta_2$ (Gradient)** | `-0,50 €/m²` | Dépréciation marginale par mètre d'éloignement d'un arrêt du réseau IDELIS. |

### 3. Développement du Tableau de Bord Interactif (`app_1.py`)
- **Cartographie dynamique (Plotly Express) :** Représentation spatiale interactive des logements sous forme de carte thématique, avec encodage couleur selon la gamme de prix au m².
- **Moteur de filtres dynamiques :** Intégration de contrôles latéraux (sliders de distance aux transports, sélection par budget et par type de logement) recalculant instantanément les indicateurs clés.
- **Analyse statistique embarquée :** Graphiques de distribution des prix et histogrammes comparatifs entre zones connectées et zones éloignées.

### 4. Déploiement Continu (CI/CD & Cloud)
- **Gestion du code source :** Versioning du projet via Git/GitHub.
- **Contrainte de chemin relatif :** Adaptation de l'ingestion de données sous Pandas avec un chemin universel (`pd.read_csv("donnees_pau_idelis.csv")`) pour assurer la compatibilité Linux/Windows.
- **Hébergement Cloud :** Déploiement automatisé sur **Streamlit Cloud** via le fichier de dépendances `requirements.txt`.

---

## 📊 Résultats & Enseignements Principaux

- **Effet structurant du BHNS Fébus :** Une survaleur significative de **+350 €/m²** est observée sur les biens situés à moins de 300 mètres du tracé Fébus (notamment sur l'axe Université - Centre-Ville - Hôpital).
- **Impact de la marche à pied :** Un éloignement de 500 mètres d'un arrêt IDELIS entraîne une perte de valeur théorique de **250 €/m²**, soulignant l'importance de la centralité des transports dans les arbitrages immobiliers palois.

---

## 📂 Architecture du Dépôt

```text
├── 📄 app_1.py               # Code principal du Dashboard Streamlit
├── 📄 donnees_pau_idelis.csv # Jeu de données spatiales et foncières
├── 📄 requirements.txt       # Dépendances Python pour Streamlit Cloud
└── 📄 README.md              # Documentation intégrale et détaillée
