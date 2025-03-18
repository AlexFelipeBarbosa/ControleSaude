# Alex Barbosa 18/03/2025

import streamlit as st

# Configuração da conexão com o banco de dados
conn = st.connection("neon", type="sql")

def autenticar_usuario(username, password):
    """Função para verificar se o usuário e senha são válidos no banco de dados."""
    try:
        query = "SELECT * FROM usuarios WHERE nome = %s AND senha = %s"
        user = conn.query(query, (username, password))

        return not user.empty  # Se houver resultado, o usuário é válido
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
            st.switch_page("passos")  # Redireciona para passos.py
        else:
            st.error("Usuário ou senha incorretos. Tente novamente.")

if __name__ == "__main__":
    main()
