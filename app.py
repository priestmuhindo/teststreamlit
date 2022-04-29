import pandas as pd
import streamlit as st
import sqlite3
# Création de la base de données et sa gestion
conn=sqlite3.connect("data.db")
c=conn.cursor()
# création de la table d'utilisateurs
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
# Insertion des utilisateirs
def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()
### vérification si l'utilisateur existe
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
## Selectionnez tous les éléments de la base de données
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
def main():
    """Simple connexion"""
    st.title("Application de connexion")
    menu=["Accueil","Connexion","Inscription"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Accueil":
        st.subheader("Bienvenue sur notre site")
    elif choice=="Connexion":
        st.subheader("Connectez-vous")
        username=st.sidebar.text_input("Nom d'utilisateur")
        pwd=st.sidebar.text_input("Mot de passe",type="password")
        if st.sidebar.checkbox("connexion"):
            create_usertable()
            result=login_user(username,pwd)
            #if pwd=="1234":
            if result:
                st.success("Vous êtes connecté en tant que {}".format(username))
                task=st.selectbox("action",["Faire un blog","Data-analyse","profile"])
                if task=="Faire un blog":
                    st.subheader("Faire un post")
                elif task=="Data-analyse":
                    st.subheader("Analyse de Données")
                elif task=="profile":
                    st.subheader("Votre profil:bar_chart:")
                    view_all_users()
                    user_result=view_all_users()
                    clean_db=pd.DataFrame(user_result,columns=["nom_utilisateur","mot__pass"])
                    st.dataframe(clean_db)

            else:
                st.warning("Mot de passe Incorrect")
    elif choice=="Inscription":
        st.sidebar.subheader("Inscrivez-vous")
        newusername=st.sidebar.text_input("Définir votre mot d'utilisateur")
        newpassword=st.sidebar.text_input("Définir le mot de passe",type="password")
        if st.sidebar.button("s'inscrire"):
            create_usertable()
            add_userdata(newusername,newpassword)
            st.sidebar.success("Vous avez réussi à créer un compte ")
            st.sidebar.info("Veuillez vous connectez afin de parcourir les ménus que nous vous proposons")

    










if __name__ == '__main__':
    main()