import streamlit as st
import pandas as pd  
import pip
pip.main(["install", "openpyxl"])

st.title("REPORTE YAPE")
uploaded_file = st.file_uploader("Sube un archivo Excel", type=["xlsx"])
df = pd.read_excel(uploaded_file)
df = df.iloc[4:]
new_column_names = {
    df.columns[0]: "Tipo de Transacción",
    df.columns[1]: "Origen",
    df.columns[2]: "Destino",
    df.columns[3]: "Monto",
    df.columns[4]: "Mensaje",
    df.columns[5]: "Fecha de operación"
}
df = df.rename(columns=new_column_names)
df["Monto"] = pd.to_numeric(df["Monto"], errors='coerce')
df["Monto"] = df["Monto"].astype(float)
monto_te_pago = df[df["Tipo de Transacción"] == "TE PAGÓ"]["Monto"].sum()
st.write("### Total de Monto para 'TE PAGÓ':", monto_te_pago)
