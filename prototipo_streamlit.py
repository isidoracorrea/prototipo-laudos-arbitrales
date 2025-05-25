import streamlit as st
import pandas as pd

# Cargar el dataset
df = pd.read_csv("dataset_prototipo_streamlit.csv")

# Título de la app
st.title("Prototipo de Consulta de Causales - Recursos de Anulación")

# Descripción breve
st.markdown("""Esta herramienta permite consultar de forma rápida los patrones identificados en los recursos de anulación de laudos arbitrales en Lima (2023).
Las causales que se muestran corresponden al **artículo 63 del Decreto Legislativo Nro. 1071**, que regula las causales específicas por las que se puede solicitar la nulidad de un laudo arbitral en Perú.
Selecciona una causal para ver su frecuencia, probabilidad de acogida o rechazo, argumentos comunes y fundamentos del tribunal.
""")

# Selector de causal
causal_elegida = st.selectbox(
    "Selecciona una causal:",
    df["letra_causal"] + ") " + df["descripcion"]
)

# Filtrar datos según la selección
causal_df = df[df["letra_causal"] == causal_elegida[0]].iloc[0]

# Mostrar resultados
st.subheader("📊 Frecuencia y Resultado")
st.write(f"- Frecuencia: {causal_df['frecuencia']}")
st.write(f"- Recursos acogidos: {causal_df['acogida']}")
st.write(f"- Recursos rechazados: {causal_df['rechazada']}")

st.subheader("🧠 Argumentos del recurrente")
for arg in eval(causal_df["argumentos_recurrente"]):
    st.markdown(f"- {arg}")

st.subheader("⚖️ Fundamentos del tribunal (si acoge)")
for fund in eval(causal_df["fundamentos_tribunal"]):
    st.markdown(f"- {fund}")
