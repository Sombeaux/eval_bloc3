
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import chardet

# détecte l'encodage du fichier
with open('C:\\Users\\c.noel1\\OneDrive - STUDI\\Bureau\\evalutation\\eval_3_data\\database\\goldenline_client.csv', 'rb') as f:
    result1 = chardet.detect(f.read())
    

with open('C:\\Users\c.noel1\OneDrive - STUDI\\Bureau\\evalutation\\eval_3_data\\database\\goldenline_collecte.csv', 'rb') as f:
    result2 = chardet.detect(f.read())


df = pd.read_csv('C:\\Users\\c.noel1\\OneDrive - STUDI\\Bureau\\evalutation\\eval_3_data\\database\\goldenline_client.csv',encoding=result1['encoding'],sep =';|,')
df_collecte = pd.read_csv('C:\\Users\c.noel1\OneDrive - STUDI\\Bureau\\evalutation\\eval_3_data\\database\\goldenline_collecte.csv',encoding = result2 ['encoding'],sep=';|,')

df_final=df
df_final['jacket'] = df_collecte['jacket']
df_final['sweater'] = df_collecte['sweater']
df_final['pant'] = df_collecte['pant']
df_final['t_shirt'] = df_collecte['t_shirt']
df_final['underwear'] = df_collecte['underwear']



# Dictionnaire de noms d'utilisateur et mots de passe correspondants
#user_credentials = {
    "Marketing1": "zhgéoih",
    "Marketing2": "pefjnhga",
    "admin": "gzojgh"
}

# Dictionnaire pour stocker les autorisations
#authorized_users = {}


# Affichage de la page d'authentification
#if 'username' not in st.session_state:
    st.write("Veuillez vous identifier pour accéder à cette page.")
    username = st.text_input("Nom d'utilisateur :")
    
    if st.button("Se connecter"):
        if username in user_credentials and password == user_credentials[username]:
            st.success("Connecté en tant que " + username)
            st.session_state.username = username
            if username == "admin":
                st.write("Vous êtes connecté en tant qu'administrateur.")
                st.write("Utilisateurs autorisés : ", authorized_users)
                # Champ de texte pour entrer le nom d'un utilisateur à autoriser
                authorized_username = st.text_input("Nom de l'utilisateur à autoriser :")
                # Bouton pour autoriser l'utilisateur
                if st.button("Autoriser"):
                    if authorized_username in user_credentials and authorized_username not in authorized_users:
                        authorized_users[authorized_username] = True
                        st.success("L'utilisateur a été autorisé à accéder aux données.")
                    elif authorized_username in authorized_users:
                        st.warning("L'utilisateur est déjà autorisé à accéder aux données.")
                    else:
                        st.warning("Nom d'utilisateur non valide ou utilisateur déjà autorisé.")
            elif username in authorized_users:
                st.write("Vous êtes déjà autorisé à accéder aux données.")
            else:
                st.warning("Vous n'êtes pas encore autorisé à accéder aux données.")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    st.write("Vous êtes connecté en tant que " + st.session_state.username)
    if st.session_state.username == "admin":
        st.write("Vous êtes connecté en tant qu'administrateur.")
        st.write("Utilisateurs autorisés : ", authorized_users)
        # Champ de texte pour entrer le nom d'un utilisateur à autoriser
        authorized_username = st.text_input("Nom de l'utilisateur à autoriser :")
        # Bouton pour autoriser l'utilisateur
        authorized_password = st.text_input("mot de passe à l'utilisateur")
        if st.button("Autoriser"):
            if authorized_username in user_credentials and authorized_username not in authorized_users:
                authorized_users[authorized_username] = True
                st.success("L'utilisateur a été autorisé à accéder aux données.")
            elif authorized_username in authorized_users:
                st.warning("L'utilisateur est déjà autorisé à accéder aux données.")
            else:
                st.warning("Nom d'utilisateur non valide ou utilisateur déjà autorisé.")
        
        st.set_option('deprecation.showPyplotGlobalUse', False)
        moyenne_sp_price = df_final.groupby("social_categorie")['total_price'].mean().reset_index()
        dépense_catégorie = df_final.groupby(["social_categorie"])[["jacket", "sweater", "pant", "t_shirt", "underwear"]].sum()

        
    

    # Afficher le graphique de distribution de la catégorie sociale
        st.write('**Distribution de la catégorie sociale**')
        sns.countplot(df_final['social_categorie'])
        plt.xticks(rotation=75)
        plt.xlabel('')
        plt.ylabel('nombre de personne')
        plt.title('')
        st.pyplot()

    # Afficher le graphique de la dépense moyenne du panier par catégorie sociale
        st.write('**Dépense moyenne du panier par catégorie sociale**')
        sns.barplot(x='social_categorie', y='total_price', data=moyenne_sp_price)
        plt.xticks(rotation=75)
        plt.xlabel('')
        plt.ylabel('dépense moyenne en euros')
        plt.title('')
        st.pyplot()

    # Afficher le graphique de la somme de la dépense du panier par catégorie sociale
        st.write('**Dépenses par catégorie et par catégorie socio-professionnelle**')
        # tracer un graphique à barres empilées pour chaque catégorie socio-professionnelle
        ax = dépense_catégorie.plot(kind="bar", stacked=True, figsize=(10, 8))
        # ajouter une légende, des titres et des étiquettes aux axes
        ax.set_xlabel("Catégorie socio-professionnelle")
        ax.set_ylabel("Dépenses en euros")
        ax.legend(title="Catégorie", loc="upper right")
        st.pyplot()

    
        #export de donnée 
    
        n_rows_to_export = st.number_input("Nombre de lignes à exporter", min_value=1, max_value=len(df_collecte))
        export_button = st.download_button(
        label="Exporter les données",
        data=df_collecte.head(n_rows_to_export).to_csv(index=False),
        file_name='collecte_export.csv')
        
        
    else:
        st.warning("Vous n'êtes pas autorisé à accéder aux données.")

    
    if st.button("Se déconnecter"):
        if st.session_state.username == "admin":
            if authorized_username in user_credentials and authorized_username not in authorized_users:
                authorized_users[authorized_username] = True
                st.success("L'utilisateur a été autorisé à accéder aux données.")
            elif authorized_username in authorized_users:
                st.warning("L'utilisateur est déjà autorisé à accéder aux données.")
            else:
                st.warning("Nom d'utilisateur non valide ou utilisateur déjà autorisé.")
        elif st.session_state.username in authorized_users:
        # Suppression de l'autorisation d'accès de l'utilisateur déconnecté
            del authorized_users[st.session_state.username]
    del st.session_state.username