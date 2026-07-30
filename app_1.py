import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="IDELIS - Immobilier & Transports Pau",
    page_icon="🚌",
    layout="wide",
)


# Chargement des données
@st.cache_data
def load_data():
  df = pd.read_csv(r"C:\Users\PC\Documents\projet\donnees_pau_idelis.csv")
  df["prix_m2"] = df["prix_vente"] / df["surface_m2"]
  return df


df = load_data()

# En-tête
st.title("🚌 IDELIS — Impact des Transports sur l'Immobilier Palois")
st.markdown(
    "Analyse de l'accessibilité au réseau de transport et simulation de la"
    " valorisation foncière à Pau."
)
st.divider()

# Sidebar - Filtres
st.sidebar.header("🔍 Filtres d'analyse")
surface_min, surface_max = int(df["surface_m2"].min()), int(
    df["surface_m2"].max()
)
surf_filter = st.sidebar.slider(
    "Surface (m²)", surface_min, surface_max, (30, 100)
)

febus_filter = st.sidebar.radio(
    "Axe Fébus (BHNS)", ["Tous", "Proche Fébus uniquement", "Hors Fébus"]
)

# Application des filtres
df_filtered = df[
    (df["surface_m2"] >= surf_filter[0]) & (df["surface_m2"] <= surf_filter[1])
]

if febus_filter == "Proche Fébus uniquement":
  df_filtered = df_filtered[df_filtered["proximite_febus"] == 1]
elif febus_filter == "Hors Fébus":
  df_filtered = df_filtered[df_filtered["proximite_febus"] == 0]

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Biens analysés", len(df_filtered))
col2.metric("Prix moyen", f"{int(df_filtered['prix_vente'].mean()):,} €")
col3.metric("Prix moyen / m²", f"{int(df_filtered['prix_m2'].mean())} €/m²")

# Calcul de l'effet Fébus
prix_febus = df[df["proximite_febus"] == 1]["prix_m2"].mean()
prix_hors_febus = df[df["proximite_febus"] == 0]["prix_m2"].mean()
diff_pct = ((prix_febus - prix_hors_febus) / prix_hors_febus) * 100
col4.metric(
    "Plus-value ligne Fébus", f"+{diff_pct:.1f} %", delta_color="normal"
)

st.divider()

# Section 1 : Carte interactive
st.subheader("📍 Cartographie des ventes et proximité réseau IDELIS")
fig_map = px.scatter_mapbox(
    df_filtered,
    lat="latitude",
    lon="longitude",
    color="prix_m2",
    size="surface_m2",
    color_continuous_scale="Viridis",
    zoom=12,
    mapbox_style="carto-positron",
    hover_data=[
        "prix_vente",
        "surface_m2",
        "nb_pieces",
        "dist_arret_bus_m",
        "proximite_febus",
    ],
    labels={
        "prix_m2": "Prix/m² (€)",
        "dist_arret_bus_m": "Distance bus (m)",
        "proximite_febus": "Accès Fébus",
    },
)
fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=450)
st.plotly_chart(fig_map, use_container_width=True)

# Section 2 : Simulateur pour IDELIS
st.divider()
st.subheader("🧮 Simulateur de valorisation par le transport")

col_sim1, col_sim2 = st.columns(2)

with col_sim1:
  surf_sim = st.number_input("Surface du bien (m²)", min_value=15, max_value=250, value=65)
  dist_bus_sim = st.slider("Distance au prochain arrêt IDELIS (mètres)", 10, 800, 150)
  acces_febus_sim = st.checkbox("Proche de la ligne Fébus (BHNS)", value=True)

with col_sim2:
  # Calcul de la valeur estimée
  base_m2 = 2150
  bonus_febus = 350 if acces_febus_sim else 0
  malus_dist = -0.5 * dist_bus_sim
  
  prix_m2_estime = base_m2 + bonus_febus + malus_dist
  valeur_totale = surf_sim * prix_m2_estime
  
  st.markdown("### Estimation du bien")
  st.metric("Prix/m² estimé", f"{int(prix_m2_estime)} €/m²")
  st.metric("Valeur totale estimée", f"{int(valeur_totale):,} €".replace(",", " "))
  
  if acces_febus_sim:
    gain_febus = surf_sim * 350
    st.success(f"💡 L'accès au Fébus apporte une valorisation estimée à **+{int(gain_febus):,} €** sur ce bien.")