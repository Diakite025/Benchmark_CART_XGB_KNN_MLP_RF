import pandas as pd
#keep this even marked unused
import ydata_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

st.markdown("# Analyse explloratoire des donénes physiques avec streamlit_pandas_profiling 🐼")
st.sidebar.markdown("# Analyse explloratoire des donénes physiques avec streamlit_pandas_profiling 🐼")

df_norm = pd.read_csv("../dataset/Physical dataset/phy_norm.csv", encoding = 'UTF-16', sep="\t")

df_att1 = pd.read_csv("../dataset/Physical dataset/phy_att_1.csv", encoding = 'UTF-16', sep="\t")
df_att2 = pd.read_csv("../dataset/Physical dataset/phy_att_2.csv", encoding = 'UTF-16', sep="\t")
df_att3 = pd.read_csv("../dataset/Physical dataset/phy_att_3.csv", encoding = 'UTF-16', sep="\t")
df_att4 = pd.read_csv("../dataset/Physical dataset/phy_att_4.csv", sep=",")

df_att2.rename(columns={"Lable_n": "Label_n"}, inplace= True)

df_concat = pd.concat([df_norm, df_att1, df_att2, df_att3, df_att4], axis=0) 

pr_norm = df_norm.profile_report()
pr_att1 = df_att1.profile_report()
pr_att2 = df_att2.profile_report()
pr_att3 = df_att3.profile_report()
pr_att4 = df_att4.profile_report()
pr_concat = df_concat.profile_report()

phys_att_1, phys_att_2, phys_att_3, phys_att_4, phys_norm, phys_all = st.tabs(["Phys attack 1", "Phys attack 2", "Phys attack 3", "Phys attack 4", "Phys norm", "Phys concat", ])

with phys_norm:
    st.markdown("### Jeu de donnénes phys_norm")
    st_profile_report(pr_norm)
with phys_att_1:
    st.markdown("### Jeu de donnénes phys_att_1")
    st_profile_report(pr_att1)
with phys_att_2:
    st.markdown("### Jeu de données phys_att_2")
    st_profile_report(pr_att2)
with phys_att_3:
    st.markdown("### Jeu de donnénes phys_att_3")
    st_profile_report(pr_att3)
with phys_att_4:
    st.markdown("### Jeu de donnénes phys_att_4")
    st_profile_report(pr_att4)
with phys_all:
    st.markdown("### Tous les jeux de ddonnées physiques concaténés")
    st_profile_report(pr_concat)

