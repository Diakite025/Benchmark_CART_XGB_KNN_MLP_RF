import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.markdown("# Graphe données physiques 📈")
st.sidebar.markdown("# Graphe données physiques 📈")

phys_norm_df = pd.read_csv("../dataset/Physical dataset/phy_norm.csv", encoding = 'UTF-16', sep="\t")
phys_att1_df = pd.read_csv("../dataset/Physical dataset/phy_att_1.csv", encoding = 'UTF-16', sep="\t")
phys_att2_df = pd.read_csv("../dataset/Physical dataset/phy_att_2.csv", encoding = 'UTF-16', sep="\t")
phys_att3_df = pd.read_csv("../dataset/Physical dataset/phy_att_3.csv", encoding = 'UTF-16', sep="\t")
phys_att4_df = pd.read_csv("../dataset/Physical dataset/phy_att_4.csv", sep=",")

#ATT 2 ERROR RENAME !
phys_att2_df.rename(columns={"Lable_n": "Label_n"}, inplace= True)
phys_att2_df['Label'].replace('nomal', 'normal', inplace=True)

def preprocess_data(df):
    df["Label_n"] = df["Label_n"].astype(bool)

    df = pd.get_dummies(df, columns=["Label"], prefix="Label", prefix_sep="_")

    df = df.astype({col: bool for col in df.columns if col.startswith("Label")})
    
    return df
    
phys_norm_df = preprocess_data(phys_norm_df)
phys_att1_df = preprocess_data(phys_att1_df)
phys_att2_df = preprocess_data(phys_att2_df)
phys_att3_df = preprocess_data(phys_att3_df)
phys_att4_df = preprocess_data(phys_att4_df)

# Créer un sélecteur pour choisir le dataframe à afficher
st.write("Sélectionnez le dataframe à afficher sur le graphique")
dataframe = st.selectbox("", ["dataframe normal", "dataframe attaque 1", "dataframe attaque 2", "dataframe attaque 3", "dataframe attaque 4"], index=0)

# Assigner le dataframe choisi à une variable
if dataframe == "dataframe normal":
    data = phys_norm_df
elif dataframe == "dataframe attaque 1":
    data = phys_att1_df
elif dataframe == "dataframe attaque 2":
    data = phys_att2_df
elif dataframe == "dataframe attaque 3":
    data = phys_att3_df
elif dataframe == "dataframe attaque 4":
    data = phys_att4_df

num_cols = data.select_dtypes(include="number").columns.tolist()

st.sidebar.write("Sélectionnez les colonnes numériques à afficher sur le graphique")

cols = st.sidebar.multiselect("", num_cols, default=num_cols)

bool_cols = data.select_dtypes(include="bool").columns.tolist()

st.sidebar.write("Sélectionnez les colonnes booléennes à afficher sur le graphique")

bools = []
for col in bool_cols:
    checked = st.sidebar.checkbox(col, value=False)
    if checked:
        bools.append(col)

fig = px.line(data, x="Time", y=cols)

for col in bools:
    state = False
    start_time = None
    for i, row in data.iterrows():
        if row[col] != state:
            # Si l'état passe à true, mettre à jour le temps de début
            if row[col]:
                start_time = row["Time"]
            # Si l'état passe à false, ajouter un rectangle qui va du temps de début au temps actuel
            else:
                fig.add_vrect(x0=start_time, x1=row["Time"], fillcolor="blue", opacity=0.2, line_width=0)
            # Mettre à jour l'état du booléen
            state = row[col]
    # Si le booléen reste à true jusqu'à la dernière ligne, ajouter un rectangle qui va du temps de début au temps final
    if state:
        fig.add_vrect(x0=start_time, x1=data["Time"].max(), fillcolor="blue", opacity=0.2, line_width=0)
        

st.plotly_chart(fig)