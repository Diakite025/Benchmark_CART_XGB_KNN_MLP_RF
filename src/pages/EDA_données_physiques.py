import streamlit as st
import pandas as pd
import io
import plotly.express as px

st.markdown("# Analyse explloratoire des donénes physiques 🔎")
st.sidebar.markdown("# Analyse explloratoire des donénes physiques 🔎")

df_norm = pd.read_csv("../dataset/Physical dataset/phy_norm.csv", encoding = 'UTF-16', sep="\t")
df_att1 = pd.read_csv("../dataset/Physical dataset/phy_att_1.csv", encoding = 'UTF-16', sep="\t")
df_att2 = pd.read_csv("../dataset/Physical dataset/phy_att_2.csv", encoding = 'UTF-16', sep="\t")
df_att3 = pd.read_csv("../dataset/Physical dataset/phy_att_3.csv", encoding = 'UTF-16', sep="\t")
df_att4 = pd.read_csv("../dataset/Physical dataset/phy_att_4.csv", sep=",")

df_att2.rename(columns={"Lable_n": "Label_n"}, inplace= True)
df_att2['Label'].replace('nomal', 'normal', inplace=True)

df_concat = pd.concat([df_norm, df_att1, df_att2, df_att3, df_att4], axis=0)

df_all = [df_norm, df_att1, df_att2, df_att3, df_att4, df_concat]


df_norm["Label_n"] = df_norm["Label_n"].astype(bool)
df_att1["Label_n"] = df_att1["Label_n"].astype(bool)
df_att2["Label_n"] = df_att2["Label_n"].astype(bool)
df_att3["Label_n"] = df_att3["Label_n"].astype(bool)
df_att4["Label_n"] = df_att4["Label_n"].astype(bool)
df_concat["Label_n"] = df_concat["Label_n"].astype(bool)

    
phys_norm, phys_att_1, phys_att_2, phys_att_3, phys_att_4, phys_all = st.tabs([ "Phys norm", "Phys attack 1", "Phys attack 2", "Phys attack 3", "Phys attack 4", "Phys concat", ])

def info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()

with phys_norm:
    st.markdown("### Jeu de donnénes phys_norm")
    st.text(info(df_norm))
    st.write(df_norm.describe())
    st.sidebar.write("Sélectionnez les colonnes numériques à afficher sur le graphique")


with phys_att_1:
    st.markdown("### Jeu de donnénes phys_att_1")
    st.text(info(df_att1))
    st.write(df_att1.describe())
    st.sidebar.write("aaaa")

with phys_att_2:
    st.markdown("### Jeu de données phys_att_2")
    st.text(info(df_att2))
    st.write(df_att2.describe())
with phys_att_3:
    st.markdown("### Jeu de donnénes phys_att_3")
    st.text(info(df_att3))
    st.write(df_att3.describe())
with phys_att_4:
    st.markdown("### Jeu de donnénes phys_att_4")
    st.text(info(df_att4))
    st.write(df_att4.describe())
with phys_all:
    st.markdown("### Tous les jeux de données physiques concaténés")
    st.text(info(df_concat))
    st.write(df_concat.describe())
        