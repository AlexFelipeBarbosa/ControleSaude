# Alex Barbosa 18/03/2025


import streamlit as st
import psycopg2
import os


conn = st.connection("neon", type="sql")

def autenticar_usuario(username, password):
    try:
        conn = psycopg2.connect(**conn)
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user is not None
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return False

def main():
    st.set_page_config(page_title="Controle de Saúde - Login", page_icon="🔑")
    
    st.title("🏥 Controle de Saúde - Login")
    
    username = st.text_input("Usuário", placeholder="Digite seu usuário")
    password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
    
    if st.button("Entrar"):
        if autenticar_usuario(username, password):
            st.success(f"Bem-vindo, {username}!")
            st.experimental_set_query_params(page="passos")
        else:
            st.error("Usuário ou senha incorretos. Tente novamente.")

if __name__ == "__main__":
    main()
