     import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora de Cálculo II", page_icon="📈", layout="centered")

st.title("📘 Calculadora Gráfica de Cálculo II")
st.markdown("""
Esta aplicación permite:
- Calcular **derivadas** e **integrales**
- Obtener **áreas bajo la curva**
- Calcular **volúmenes de revolución**
- Visualizar los resultados de forma gráfica
""")

# --- Entrada de función ---
x = sp.Symbol('x')
funcion_str = st.text_input("✏️ Ingresa la función en términos de x:", "x**2 + 3*x - 2")

if funcion_str:
    try:
        f = sp.sympify(funcion_str)

        st.latex(f"f(x) = {sp.latex(f)}")

        opcion = st.selectbox("Selecciona la operación:", [
            "Derivar", 
            "Integrar (indefinida)", 
            "Área bajo la curva (integral definida)",
            "Volumen de revolución (alrededor del eje X)"
        ])

        if opcion == "Derivar":
            derivada = sp.diff(f, x)
            st.latex(f"f'(x) = {sp.latex(derivada)}")

            # Gráfica
            xx = np.linspace(-10, 10, 400)
            f_num = sp.lambdify(x, f, "numpy")
            d_num = sp.lambdify(x, derivada, "numpy")
            plt.figure()
            plt.plot(xx, f_num(xx), label="f(x)")
            plt.plot(xx, d_num(xx), '--', label="f'(x)")
            plt.legend()
            plt.grid(True)
            st.pyplot(plt)

        elif opcion == "Integrar (indefinida)":
            integral = sp.integrate(f, x)
            st.latex(f"∫ f(x) dx = {sp.latex(integral + sp.Symbol('C'))}")

        elif opcion == "Área bajo la curva (integral definida)":
            a = st.number_input("Límite inferior (a):", value=0.0)
            b = st.number_input("Límite superior (b):", value=2.0)
            area = sp.integrate(f, (x, a, b))
            st.latex(f"Área = \\int_{{{a}}}^{{{b}}} f(x)\\,dx = {sp.N(area)}")

            # Gráfica del área
            f_num = sp.lambdify(x, f, "numpy")
            xx = np.linspace(a, b, 200)
            yy = f_num(xx)
            plt.figure()
            plt.fill_between(xx, yy, color='skyblue', alpha=0.5)
            plt.plot(xx, yy, color='blue')
            plt.title(f"Área bajo f(x) de {a} a {b}")
            plt.grid(True)
            st.pyplot(plt)

        elif opcion == "Volumen de revolución (alrededor del eje X)":
            a = st.number_input("Límite inferior (a):", value=0.0)
            b = st.number_input("Límite superior (b):", value=2.0)
            volumen = sp.integrate(sp.pi * f**2, (x, a, b))
            st.latex(f"V = \\pi \\int_{{{a}}}^{{{b}}} [f(x)]^2 dx = {sp.N(volumen)}")

            # Gráfica
            f_num = sp.lambdify(x, f, "numpy")
            xx = np.linspace(a, b, 200)
            yy = f_num(xx)
            plt.figure()
            plt.fill_between(xx, yy, color='lightcoral', alpha=0.4)
            plt.plot(xx, yy, color='red')
            plt.title("Volumen de revolución (visualización 2D)")
            plt.grid(True)
            st.pyplot(plt)

    except Exception as e:
        st.error(f"⚠️ Error al procesar la función: {e}")
