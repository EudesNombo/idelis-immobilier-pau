# 🚌 IDELIS — Impact des Transports sur l'Immobilier Palois (Évaluation Hédonique & Dashboard Streamlit)

> 🚀 **Application interactive en ligne :** [Tester le Dashboard Streamlit](https://eudesnombo-idelis-immobilier-pau-app-1-hyukbr.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?logo=pandas)

Projet d'analyse spatiale et d'évaluation économétrique hédonique visant à mesurer l'impact de l'accessibilité au réseau de transports en commun **IDELIS** et de sa ligne à haut niveau de service (**Fébus**) sur la valorisation foncière résidentielle à Pau (64000).

---

## 🎯 Objectifs & But du Projet

- **Quantifier la plus-value foncière** liée à la proximité immédiate de la ligne BHNS Fébus (< 300 mètres).
- **Modéliser le gradient de dépréciation** marginale du prix de vente en fonction de l'éloignement physique d'un arrêt IDELIS (`dist_arret_bus_m`).
- **Visualiser la répartition spatiale** des transactions et des infrastructures de transport via une interface cartographique dynamique.
- **Proposer un outil interactif d'aide à la décision** pour les acteurs de l'aménagement urbain, de la mobilité et du marché immobilier palois.

---

## 🛠️ Étapes de Réalisation Détaillées (Workflow Data & Métier)

### 1. Prétraitement et Harmonisation Géospatiale (`donnees_pau_idelis.csv`)
- **Ingestion des données :** Chargement du jeu de données spatialisées comprenant les transactions immobilières paloises, la géolocalisation des biens (`latitude`, `longitude`), la surface (`surface_m2`), le nombre de pièces (`nb_pieces`) et le maillage du réseau IDELIS.
- **Nettoyage & Traitement des anomalies :** Filtrage des données aberrantes (*outliers*) sur les prix de vente et validation du périmètre géographique de la commune de Pau.
- **Calcul de métriques d'accessibilité :** Détermination de la distance géodésique à l'arrêt le plus proche (`dist_arret_bus_m`) et classification binaire de la proximité au BHNS Fébus (`proximite_febus`).

### 2. Spécification Econométrique : Modèle de Prix Hédonique
Pour décomposer la valeur d'un bien immobilier en fonction de ses caractéristiques intrinsèques et de son niveau de desserte par les transports, nous appliquons la modélisation hédonique suivante :

$$\text{Prix}_{\text{vente}} = \beta_0 + \beta_1 \cdot \text{Fébus} + \beta_2 \cdot \text{Distance}_{\text{arrêt}} + \varepsilon$$

#### Calibration et interprétation des paramètres :
| Variable dans le fichier | Paramètre Econométrique | Coefficient Retenu | Interprétation Économétrique |
| :--- | :--- | :--- | :--- |
| **`Intercept`** | $\beta_0$ (Constante) | `145 000 €` | Prix médian de référence sur la commune pour un logement standard. |
| **`proximite_febus`** | $\beta_1$ (Effet Fébus) | `+25 000 €` | Plus-value explicite liée à l'accès direct au tracé du Fébus (< 300m). |
| **`dist_arret_bus_m`** | $\beta_2$ (Gradient) | `-35 €/m` | Dépréciation marginale du prix de vente par mètre d'éloignement d'un arrêt IDELIS. |

### 3. Architecture & Développement du Dashboard Streamlit (`app_1.py`)
Le script de l'application s'articule autour d'une architecture simple, performante et totalement modulaire :
- **Filtre interactif par curseur (`st.slider`) :** Ajustement dynamique de la distance maximale acceptée (`dist_arret_bus_m`).
- **Filtrage conditionnel Pandas :** Sélection instantanée des lignes répondant au critère de distance (`df[df["dist_arret_bus_m"] <= dist_max]`).
- **Visualisation cartographique (`st.map`) :** Projection dynamique des biens filtrés selon leurs coordonnées GPS (`latitude`, `longitude`).
- **Analyse comparative (`st.bar_chart`) :** Diagramme comparatif des prix de vente selon la proximité au Fébus.

### 4. Déploiement Continu & Versioning (CI/CD)
- **Versioning :** Suivi de version et documentation sous Git et GitHub.
- **Contrainte Cloud :** Utilisation de chemins relatifs universels pour la lecture du fichier CSV.
- **Hébergement :** Déploiement en continu sur **Streamlit Cloud** s'appuyant sur le fichier de dépendances `requirements.txt`.

---

## 📊 Résultats & Enseignements Principaux

- **Effet structurant du BHNS Fébus :** Une survaleur significative est observée sur les biens situés à proximité directe de la ligne Fébus (particulièrement sur l'axe structurant Université - Centre-Ville - Hôpital).
- **Impact de l'accessibilité piétonne :** L'éloignement d'un arrêt IDELIS entraîne une décote progressive du prix de vente, confirmant que la centralité et la desserte en transports restent des critères prioritaires de la valorisation immobilière à Pau.

---

## 📂 Architecture du Dépôt

```text
├── 📄 app_1.py               # Code source principal du Dashboard Streamlit
├── 📄 donnees_pau_idelis.csv # Jeu de données spatiales et foncières paloises
├── 📄 requirements.txt       # Dépendances Python (pandas, streamlit)
└── 📄 README.md              # Documentation intégrale et détaillée du projet
