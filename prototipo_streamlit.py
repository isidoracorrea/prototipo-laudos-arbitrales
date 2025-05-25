import streamlit as st
import pandas as pd

# Cargar el dataset
df = pd.read_csv("dataset_prototipo_streamlit.csv")

# Título de la app
st.title("Prototipo de Consulta de Causales - Recursos de Anulación")

# Descripción introductoria
st.markdown("""
Esta herramienta permite consultar de forma rápida los patrones identificados en los recursos de anulación de laudos arbitrales en Lima (2023).

Las causales que se muestran corresponden al **artículo 63 del Decreto Legislativo N.º 1071**, que regula las causales específicas por las que se puede solicitar la nulidad de un laudo arbitral en Perú.

Selecciona una causal para responder preguntas como:

- ¿Cuántas veces se ha invocado esta causal?
- ¿Con qué frecuencia ha sido acogida o rechazada?
- ¿Qué suele alegar el recurrente cuando la invoca?
- ¿Qué argumentos acepta el tribunal cuando acoge el recurso?
""")

# Selector de causal
causal_elegida = st.selectbox(
    "¿Qué causal quieres explorar?",
    df["letra_causal"] + ") " + df["descripcion"]
)

# Filtrar datos según la selección
causal_df = df[df["letra_causal"] == causal_elegida[0]].iloc[0]

# Sección 1: Frecuencia y resultado
st.subheader("🫣 ¿Con qué frecuencia se ha invocado esta causal y cuál ha sido el resultado?")
st.write(f"- Ha sido invocada **{causal_df['frecuencia']}** veces.")
st.write(f"- Fue **acogida** en {causal_df['acogida']} ocasiones.")
st.write(f"- Fue **rechazada** en {causal_df['rechazada']} ocasiones.")

# Sección 2: Argumentos del recurrente
st.subheader("🧠 ¿Qué suele alegar el recurrente cuando invoca esta causal?")
for arg in eval(causal_df["argumentos_recurrente"]):
    st.markdown(f"- {arg}")

# Sección 3: Fundamentos del tribunal
st.subheader("⚖️ ¿Qué ha dicho el tribunal cuando acoge el recurso por esta causal?")
for fund in eval(causal_df["fundamentos_tribunal"]):
    st.markdown(f"- {fund}")

