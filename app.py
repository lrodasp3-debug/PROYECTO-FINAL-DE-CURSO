import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora Gráfica ", page_icon="📈", layout="centered")

st.title("📘Calculadora Gráfica📘")
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

with st.expander("Cómo usar"):
    st.markdown(
        """
        1. Escribe la función en términos de `x`. 
           - Potencias: `x**2`  (no utilizar ^)
           - Funciones: `sin(x)`, `cos(x)`, `exp(x)`, `e^(x)`
        2. Elige la operación (Derivar, Integrar, Área definida, Volumen).
        3. Si la operación pide límites, ingrésalos en los campos `a` y `b`.
    )

x = sp.Symbol('x')
funcion_str = st.text_input("✏️ Ingresa la función en términos de x:", "x**2 + 3*x - 2")

if funcion_str:
    try:
        # Parsear y simplificar
        f = sp.sympify(funcion_str)
        f = sp.simplify(f)
        st.latex(f"f(x) = {sp.latex(f)}")

        opcion = st.selectbox("Selecciona la operación:", [
            "Derivar",
            "Integrar (indefinida)",
            "Área bajo la curva (integral definida)",
            "Volumen de revolución (alrededor del eje X)"
        ])

        # Helper: lambdify safely
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

            # Gráfica de f y f'
            f_num = to_numeric(f)
            d_num = to_numeric(derivada_s)
            if f_num and d_num:
                xx = np.linspace(-10, 10, 400)
                plt.figure(figsize=(6,3.5))
                plt.plot(xx, f_num(xx), label="f(x)")
                plt.plot(xx, d_num(xx), '--', label="f'(x)")
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
                st.warning("El límite superior b debe ser mayor que a.")
            else:
                area = sp.integrate(f, (x, a, b))
                st.markdown("**Área definida:**")
                st.latex(f"\\mathrm{{Área}} = \\int_{{{a}}}^{{{b}}} f(x)\\,dx = {sp.N(area)}")

                # Gráfica del área
                f_num = to_numeric(f)
                if f_num:
                    xx = np.linspace(a, b, 300)
                    yy = f_num(xx)
                    plt.figure(figsize=(6,3.5))
                    plt.fill_between(xx, yy, where=~np.isnan(yy), alpha=0.5)
                    plt.plot(xx, yy)
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
                st.warning("El límite superior b debe ser mayor que a.")
            else:
                volumen = sp.integrate(sp.pi * f**2, (x, a, b))
                st.markdown("**Volumen de revolución (eje X):**")
                st.latex(f"V = \\pi \\int_{{{a}}}^{{{b}}} [f(x)]^2 dx = {sp.N(volumen)}")

                # Visualización 2D
                f_num = to_numeric(f)
                if f_num:
                    xx = np.linspace(a, b, 300)
                    yy = f_num(xx)
                    plt.figure(figsize=(6,3.5))
                    plt.plot(xx, yy)
                    plt.fill_between(xx, yy, alpha=0.3)
                    plt.title("Visualización 2D del perfil (revolución alrededor del eje X)")
                    plt.grid(True)
                    st.pyplot(plt)
                    plt.close()
                else:
                    st.info("No se pudo graficar la función numéricamente.")

    except Exception as e:
        st.error(f"⚠️ Error al procesar la función: {e}")
