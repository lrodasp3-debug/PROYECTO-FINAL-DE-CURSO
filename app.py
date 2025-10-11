import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora Gráfica", page_icon="📈", layout="centered")

st.title("📘 Calculadora Gráfica 📘")
st.markdown(
    """
    Esta aplicación permite:
    - Calcular **derivadas** e **integrales**
    - Obtener **áreas bajo la curva**
    - Calcular **volúmenes de revolución**
    - Visualizar los resultados de forma gráfica

    Ejemplos de funciones válidas: `x**2`, `x**3 - 2*x + 1`, `sin(x)`, `exp(x)`, `1/(x+1)`
    """
)

with st.expander("ℹ️ Cómo usar"):
    st.markdown(
        """
        1. Escribe la función en términos de `x`. Usa Python / SymPy syntax:
           - Potencias: `x**2`  (no usar ^)
           - Funciones: `sin(x)`, `cos(x)`, `tan(x)`, `exp(x)`, `log(x)`
        2. Elige la operación (Derivar, Integrar, Área definida, Volumen).
        3. Si la operación pide límites, ingrésalos en los campos `a` y `b`.
        """
    )

x = sp.Symbol('x')
funcion_str = st.text_input("✏️ Ingresa la función en términos de x:", "x**2 + 3*x - 2")

if funcion_str:
    try:
        f = sp.sympify(funcion_str)
        f = sp.simplify(f)
        st.latex(f"f(x) = {sp.latex(f)}")

        opcion = st.selectbox("Selecciona la operación:", [
            "Derivar",
            "Integrar (indefinida)",
            "Área bajo la curva (integral definida)",
            "Volumen de revolución (alrededor del eje X)"
        ])

        # 🎨 Fondos dinámicos con degradados
        background_gradients = {
            "Derivar": "linear-gradient(135deg, #e0f7fa, #80deea)",      # azul degradado
            "Integrar (indefinida)": "linear-gradient(135deg, #fff3e0, #ffcc80)", # naranja degradado
            "Área bajo la curva (integral definida)": "linear-gradient(135deg, #e8f5e9, #a5d6a7)", # verde degradado
            "Volumen de revolución (alrededor del eje X)": "linear-gradient(135deg, #f3e5f5, #ce93d8)" # violeta degradado
        }

        gradient = background_gradients.get(opcion, "linear-gradient(135deg, #ffffff, #f0f0f0)")

        # Aplica fondo degradado y letras negras
        st.markdown

