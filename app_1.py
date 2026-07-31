import pandas as pd
import streamlit as st

# 1. Titre
st.title("IMMOBILIER & TRANSPORTS À PAU")

# 2. Chargement des données
df = pd.read_csv("donnees_pau_idelis.csv")

# 3. Curseur (Slider) pour la distance max
dist_max = st.slider("Distance maximum à l'arrêt de bus (mètres)", min_value=50, max_value=700, value=300)

# 4. Filtrage des données
df_filtre = df[df["dist_arret_bus_m"] <= dist_max]

# 5. Affichage des résultats
st.write(f"Nombre de logements trouvés : **{len(df_filtre)}**")
st.dataframe(df_filtre)

# 6. Graphique explicite
st.write("### Prix de vente selon la proximité au Fébus (0 = Éloigné, 1 = Proche)")
st.bar_chart(data=df_filtre, x="proximite_febus", y="prix_vente")

# 7. Carte interactive
st.map(df_filtre)
