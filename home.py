# Alex Barbosa 18/03/2025

import streamlit as st
import psycopg2
import webbrowser
import os

st.set_page_config(page_title="Controle Diário de Saúde - Login", page_icon="🔑")

# Criando a conexão com o banco de dados
try:
    conn = st.connection("neon", type="sql")
    st.success("✅ Conexão com o banco estabelecida!")
except Exception as e:
    st.error(f"❌ Erro ao conectar ao banco: {e}")
    st.stop()

def autenticar_usuario(username, password):
    """Função para verificar se o usuário e senha são válidos no banco de dados."""
    try:
        query = f"SELECT * FROM usuarios WHERE nome = '{username}' AND senha = '{password}'"
        user = conn.query(query)  # 🔹 Forma correta de executar a query
        
        return not user.empty  # Se houver resultado, o usuário é válido
    except Exception as e:
        st.error(f"Erro ao buscar usuário no banco: {e}")
        return False

def main():
    st.title("🏥 Controle de Saúde - Login")

    username = st.text_input("Usuário", placeholder="Digite seu usuário")
    password = st.text_input("Senha", type="password", placeholder="Digite sua senha")

    if st.button("Entrar"):
        if autenticar_usuario(username, password):
            st.success(f"Bem-vindo, {username}!")
            
            # Redirecionamento para passos.py
            script_dir = os.path.dirname(__file__)
            rel_path = "passos.py"
            abs_file_path = os.path.join(script_dir, rel_path)
            
            # Verifica se o arquivo existe
            if os.path.exists(abs_file_path):
                st.rerun()
                webbrowser.open(f"streamlit run {abs_file_path}")
            else:
                st.error("Arquivo passos.py não encontrado!")
        else:
            st.error("Usuário ou senha incorretos. Tente novamente.")

if __name__ == "__main__":
    main()
