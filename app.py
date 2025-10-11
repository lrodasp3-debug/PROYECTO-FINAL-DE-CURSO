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
funcion_str = st.text_input(" Ingresa la función en términos de x:", "x**2 + 3*x - 2")

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
              "Derivar": "#00897B",  # verde azulado
    "Integrar (indefinida)": "#43A047",  # verde
    "Área bajo la curva (integral definida)": "#C0CA33",  # verde lima
    "Volumen de revolución (alrededor del eje X)": "#E64A19"  # naranja quemado
        }

        gradient = background_gradients.get(opcion, "linear-gradient(135deg, #ffffff, #f0f0f0)")

        # Aplica fondo degradado y letras negras
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: {gradient};
                transition: background 1s ease;
                color: black;
            }}
            .stMarkdown, .css-10trblm, .css-1d391kg {{
                color: black !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        def to_numeric(func):
            try:
                return sp.lambdify(x, func, "numpy")
            except Exception:
                return None

        if opcion == "Derivar":
            derivada = sp.diff(f, x)
            derivada_s = sp.simplify(derivada)
            st.markdown("**Derivada simbólica:**")
            st.latex(f"f'(x) = {sp.latex(derivada_s)}")

            f_num = to_numeric(f)
            d_num = to_numeric(derivada_s)
            if f_num and d_num:
                xx = np.linspace(-10, 10, 400)
                plt.figure(figsize=(6, 3.5))
                plt.plot(xx, f_num(xx), label="f(x)", color="blue")
                plt.plot(xx, d_num(xx), '--', label="f'(x)", color="red")
                plt.legend()
                plt.grid(True)
                st.pyplot(plt)
                plt.close()
            else:
                st.info("No se pudo generar la gráfica numérica (función no numérica en algunos puntos).")

        elif opcion == "Integrar (indefinida)":
            integral = sp.integrate(f, x)
            st.markdown("**Integral indefinida:**")
            st.latex(f"\\int f(x)\\,dx = {sp.latex(integral)} + C")

        elif opcion == "Área bajo la curva (integral definida)":
            a = st.number_input("Límite inferior (a):", value=0.0, format="%.6f")
            b = st.number_input("Límite superior (b):", value=2.0, format="%.6f")
            if b <= a:
                st.warning("⚠️ El límite superior b debe ser mayor que a.")
            else:
                area = sp.integrate(f, (x, a, b))
                st.markdown("**Área definida:**")
                st.latex(f"\\mathrm{{Área}} = \\int_{{{a}}}^{{{b}}} f(x)\\,dx = {sp.N(area)}")

                f_num = to_numeric(f)
                if f_num:
                    xx = np.linspace(a, b, 300)
                    yy = f_num(xx)
                    plt.figure(figsize=(6, 3.5))
                    plt.fill_between(xx, yy, where=~np.isnan(yy), alpha=0.5, color="orange")
                    plt.plot(xx, yy, color="black")
                    plt.title(f"Área bajo f(x) de {a} a {b}")
                    plt.grid(True)
                    st.pyplot(plt)
                    plt.close()
                else:
                    st.info("No se pudo graficar la función numéricamente.")

        elif opcion == "Volumen de revolución (alrededor del eje X)":
            a = st.number_input("Límite inferior (a):", value=0.0, format="%.6f", key="vol_a")
            b = st.number_input("Límite superior (b):", value=2.0, format="%.6f", key="vol_b")
            if b <= a:
                st.warning("⚠️ El límite superior b debe ser mayor que a.")
            else:
                volumen = sp.integrate(sp.pi * f**2, (x, a, b))
                st.markdown("**Volumen de revolución (eje X):**")
                st.latex(f"V = \\pi \\int_{{{a}}}^{{{b}}} [f(x)]^2 dx = {sp.N(volumen)}")

                f_num = to_numeric(f)
                if f_num:
                    xx = np.linspace(a, b, 300)
                    yy = f_num(xx)
                    plt.figure(figsize=(6, 3.5))
                    plt.plot(xx, yy, color="purple")
                    plt.fill_between(xx, yy, alpha=0.3, color="violet")
                    plt.title("Visualización 2D del perfil (revolución alrededor del eje X)")
                    plt.grid(True)
                    st.pyplot(plt)
                    plt.close()
                else:
                    st.info("No se pudo graficar la función numéricamente.")

    except Exception as e:
        st.error(f"⚠️ Error al procesar la función: {e}")
