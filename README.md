# 🚌 IDELIS — Impact des Transports sur l'Immobilier Palois

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-6.0+-blue?logo=plotly)

Projet d'analyse spatiale et d'évaluation hédonique de la valorisation foncière à Pau (64000) en fonction de l'accessibilité au réseau de transport en commun **IDELIS** et de sa ligne à haut niveau de service (**Fébus**).

---

## 📌 Présentation du Projet

Ce projet a été développé dans le cadre du cursus **MIASHS**. Il combine traitement de données géospatiales, modélisation économétrique hédonique et création d'un tableau de bord interactif sous Streamlit.

### Objectifs :
- **Quantifier l'impact** de la proximité du Fébus (BHNS) sur le prix au m² des logements palois.
- **Modéliser la dépréciation** marginale liée à l'éloignement d'un arrêt du réseau IDELIS.
- **Proposer un outil interactif** d'aide à la décision pour les acteurs de l'aménagement urbain et de l'immobilier.

---

## 📊 Modélisation Économétrique (Prix Hédonique)

La valeur estimée d'un bien au mètre carré est modélisée par l'équation hédonique suivante :

$$\text{Prix}_{m^2} = \beta_0 + \beta_1 \cdot \text{Fébus} + \beta_2 \cdot \text{Distance}_{\text{arrêt}} + \varepsilon$$

### Paramètres retenus :
| Variable | Coefficient | Signification |
| :--- | :--- | :--- |
| **$\beta_0$** (Constante) | `2 150 €/m²` | Prix médian de référence sur la commune de Pau |
| **$\beta_1$** (Effet Fébus) | `+350 €/m²` | Plus-value d'accessibilité directe au BHNS (< 300m) |
| **$\beta_2$** (Gradient) | `-0.50 €/m²` | Dépréciation par mètre d'éloignement d'un arrêt IDELIS |

---

## 🛠️ Structure du Dépôt

```text
├── app_1.py               # Application Streamlit principale
├── donnees_pau_idelis.csv # Jeu de données géolocalisé
├── requirements.txt       # Dépendances Python
└── README.md              # Documentation
