import streamlit as st
import os
import json

# CSS pour enlever la marge
st.markdown("""
<style>
    .block-container {
        max-width: none
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# Comparer les résultats 📊")
st.sidebar.markdown("# Comparer les résultats 📊")


# Déclarer les variables globales
folder1 = None
folder2 = None
folder3 = None
folder4 = None

def select_folder(path, level, col_name, folder1=None, folder2=None, folder3=None, folder4=None):
    folders = os.listdir(path)

    folders = [f for f in folders if os.path.isdir(os.path.join(path, f))]

    if folders:
        if level == 1:
            phrase = "Jeu de données:"
        elif level == 2:
            phrase = "Sous-jeu de données:"
        elif level == 3:
            phrase = "Nombre de lignes:"
        elif level == 4:
            phrase = "Modèle:"
        else:
            phrase = "Choisissez un dossier au niveau " + str(level) + ":"
              
        folder = st.selectbox(phrase, folders, key=(str(level) + col_name) if level else ("nope" + col_name))

        new_path = os.path.join(path, folder)

        if level == 1:
            folder1 = folder
        elif level == 2:
            folder2 = folder
        elif level == 3:
            folder3 = folder
        elif level == 4:
            folder4 = folder

        return select_folder(new_path, level + 1, col_name, folder1, folder2, folder3, folder4)
    else:
        return folder1, folder2, folder3, folder4


# Créer deux colonnes
col1, col2 = st.columns(2)

# Assigner les valeurs retournées par la fonction à la première colonne
with col1:
    root = "results"
    folder1, folder2, folder3, folder4 = select_folder(root, 1, "col1")

    if (folder1 and folder2 and folder3 and folder4):

        path4 = os.path.join(root, folder1, folder2, folder3, folder4)

        files = os.listdir(path4)

        images = [f for f in files if f.endswith((".png", ".jpg", ".jpeg"))]

        for image in images:
            image_path = os.path.join(path4, image)
            st.image(image_path)

        time_file = os.path.join(path4, "time.json")

        with open(time_file, "r") as f:
            time_dict = json.load(f)

        st.write("Temps de fit: " + str(time_dict["fit_time"]))
        st.write("Temps de prédiction: " + str(time_dict["pred_time"]))

# Assigner les valeurs retournées par la fonction à la deuxième colonne
with col2:
    # Vous pouvez répéter le même processus que pour la première colonne
    # ou choisir un autre dossier à afficher
    # Par exemple, vous pouvez appeler à nouveau la fonction select_folder
    # avec un autre chemin racine
    root2 = "results"
    folder1, folder2, folder3, folder4 = select_folder(root2, 1, "col2")

    if (folder1 and folder2 and folder3 and folder4):

        path4 = os.path.join(root2, folder1, folder2, folder3, folder4)

        files = os.listdir(path4)

        images = [f for f in files if f.endswith((".png", ".jpg", ".jpeg"))]

        for image in images:
            image_path = os.path.join(path4, image)
            st.image(image_path)

        time_file = os.path.join(path4, "time.json")

        with open(time_file, "r") as f:
            time_dict = json.load(f)

        st.write("Temps de fit: " + str(time_dict["fit_time"]))
        st.write("Temps de prédiction: " + str(time_dict["pred_time"]))
