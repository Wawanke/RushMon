import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import numpy as np

# Charger les données
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/PokemonDatabase.csv")
    df = df[~df["Alternate Form Name"].astype(str).str.contains("Mega|Gigantamax|Eternamax", na=False)]
    df = df.dropna(subset=["Primary Type"])
    return df

df = load_data()

# Colonnes utilisées comme features
feature_cols = [
    "Health Stat", "Attack Stat", "Defense Stat",
    "Special Attack Stat", "Special Defense Stat", "Speed Stat",
    "Pokemon Height", "Pokemon Weight"
]

target_col = "Primary Type"

# Filtrage et encodage
def prepare_data(df):
    X = df[feature_cols]
    y = df[target_col]
    
    # Pipeline de transformation
    numeric_transformer = StandardScaler()
    pipeline = Pipeline([
        ('scaler', numeric_transformer),
        ('classifier', RandomForestClassifier(class_weight="balanced", random_state=42))
    ])
    
    # Split et entraînement
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    pipeline.fit(X_train, y_train)

    return pipeline

# Entraîner le modèle
model = prepare_data(df)

# Application Streamlit
st.title("🔍 Prédiction du Type Principal d'un Pokémon")

# Liste des noms de Pokémon disponibles
pokemon_names = df["Pokemon Name"].dropna().str.replace('"', '').unique()
pokemon_name = st.selectbox("Choisissez un Pokémon :", sorted(pokemon_names))

if pokemon_name:
    poke_data = df[df["Pokemon Name"].str.replace('"', '') == pokemon_name]
    features = poke_data[feature_cols]
    if features.empty:
        st.warning("Aucune donnée trouvée pour ce Pokémon.")
    else:
        pred = model.predict(features)
        st.success(f"🎯 Le type principal prédit pour **{pokemon_name}** est : **{pred[0]}**")

        # (Optionnel) Afficher les caractéristiques utilisées
        if st.checkbox("Afficher les caractéristiques du Pokémon"):
            st.dataframe(features.reset_index(drop=True))

        # Bouton pour afficher le type réel
        if st.button("Afficher le véritable type"):
            true_type = poke_data.iloc[0]["Primary Type"]
            st.info(f"📘 Le type principal réel de **{pokemon_name}** est : **{true_type}**")

# (Optionnel) Afficher quelques métriques globales
if st.checkbox("Afficher la performance globale du modèle"):
    X = df[feature_cols]
    y_true = df[target_col]
    y_pred = model.predict(X)
    report = classification_report(y_true, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.dataframe(report_df.round(2))
