# Alex Barbosa 18/03/2025

import streamlit as st
import psycopg2
from psycopg2 import sql

# Recuperar as credenciais do banco de dados do arquivo secrets.toml
db_config = st.secrets["neon"]

# Função para conectar ao banco de dados
def get_connection():
    conn = psycopg2.connect(
        host=db_config["host"],
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        port=db_config["port"]
    )
    return conn


# Função para adicionar dados
def add_data(dia, passos):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Passos (dia, passos)
        VALUES (%s, %s);
    """, (dia, passos))
    conn.commit()
    cur.close()
    conn.close()

# Função para atualizar dados
def update_data(idpassos, dia, passos,):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE passos
        SET dia = %s, passos = %s
        WHERE idpassos = %s;
    """, (dia, passos,idpassos))
    conn.commit()
    cur.close()
    conn.close()

# Função para excluir dados
def delete_data(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM passos WHERE idpassos = %s;
    """, (user_id,))
    conn.commit()
    cur.close()
    conn.close()

# Função para ler dados
def get_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Passos order by idpassos desc;")
    records = cur.fetchall()
    cur.close()
    conn.close()
    return records

# Interface de usuário com Streamlit
st.title("Controle Diário de Passos! ")


# Exibir a tabela de dados
st.subheader("Controde Diário de Passos")
data = get_data()
if data:
    st.write(data)
else:
    st.write("Nenhum dado encontrado!")

# Formulário para adicionar dados
st.subheader("Adicionar um novo Registro de Passos!")
dia = st.date_input("Dia")
passos = st.number_input("Passos", min_value=0, max_value= 20000)


if st.button("Adicionar"):
    if dia and passos:
        add_data(dia, passos)
        st.success("Registro de Passos adicionado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos!")

# Formulário para atualizar dados
st.subheader("Atualizar o Registro de Passos")
idpassos = st.number_input("ID do Registro", min_value=1, max_value=1000000)
dia_atualizado = st.date_input("Novo Dia")
passos_atualizado = st.number_input("Novo Reigstro", min_value=0, max_value= 20000)


if st.button("Atualizar"):
    if dia_atualizado and passos_atualizado:
        update_data(idpassos, dia_atualizado, passos_atualizado)
        st.success("Registro Diário atualizado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos!")

# Formulário para excluir dados
st.subheader("Excluir Registro de Passos")
idpassos_deletar = st.number_input("ID do Registro a ser excluído", min_value=1, max_value=1000000)
if st.button("Excluir"):
    delete_data(idpassos_deletar)
    st.success("Registro de Passos excluído com sucesso!")