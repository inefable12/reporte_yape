import streamlit as st
import pandas as pd  

st.title("REPORTE YAPE")
uploaded_file = st.file_uploader("Sube un archivo Excel", type=["xlsx"])
df = pd.read_excel(uploaded_file, skiprows=4)
monto_te_pago = df[df["Tipo de Transacción"] == "TE PAGÓ"]["Monto"].sum()
st.write("### Total de Monto para 'TE PAGÓ':", monto_te_pago)
