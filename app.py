import streamlit as st
import pandas as pd

def process_file(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, skiprows=4)  # La fila 5 es índice 4 en Python
        if set(["Tipo de Transacción", "Monto"]).issubset(df.columns):
            total_pago = df[df["Tipo de Transacción"] == "TE PAGÓ"]["Monto"].sum()
            st.write("### Total de Monto para 'TE PAGÓ':", total_pago)
        else:
            st.error("El archivo no contiene las columnas necesarias.")

st.title("Cargar Archivo Excel y Sumar Monto de 'TE PAGÓ'")

uploaded_file = st.file_uploader("Sube un archivo Excel", type=["xlsx"])
if uploaded_file:
    process_file(uploaded_file)
