import streamlit as st

# Inicializar el estado de sesión
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"
if "tipo" not in st.session_state:
    st.session_state.tipo = ""
if "documento" not in st.session_state:
    st.session_state.documento = ""
if "entrada" not in st.session_state:
    st.session_state.entrada = ""

st.title("🎓 Asistente para Trámite de Título")

def reiniciar():
    st.session_state.pantalla = "inicio"
    st.session_state.tipo = ""
    st.session_state.documento = ""
    st.session_state.entrada = ""

# Pantalla de inicio
if st.session_state.pantalla == "inicio":
    st.subheader("¿Qué tipo de título querés tramitar?")
    st.text("1 - Digital")
    st.text("2 - Decorativo")
    st.session_state.entrada = st.text_input("Ingresá el número de tu elección:", key="tipo_input")

    if st.button("Continuar"):
        if st.session_state.entrada == "1":
            st.session_state.tipo = "Digital"
            st.session_state.pantalla = "documentacion"
        elif st.session_state.entrada == "2":
            st.session_state.tipo = "Decorativo"
            st.session_state.pantalla = "documentacion"
        else:
            st.warning("❌ Opción no válida. Ingresá 1 o 2.")

# Pantalla de documentación
elif st.session_state.pantalla == "documentacion":
    if st.session_state.tipo == "Digital":
        st.success("✅ Elegiste título DIGITAL.")
        st.info("💸 Precio: $15.000")
    elif st.session_state.tipo == "Decorativo":
        st.success("✅ Elegiste título DECORATIVO.")
        st.info("💸 Precio: $30.000")

    st.subheader("📄 Documentación a presentar:")
    st.text("1 - DNI")
    st.text("2 - Libre deuda biblioteca UNNE")
    st.text("3 - Libre deuda biblioteca FACENA")
    st.text("4 - Formulario de cotejo de ficha académica")

    doc_input = st.text_input("Ingresá el número de la opción:", key="doc_input")

    if st.button("Ver información"):
        if doc_input == "1":
            st.session_state.documento = "DNI"
            st.session_state.pantalla = "info_documento"
        elif doc_input == "2":
            st.session_state.documento = "Libre deuda biblioteca UNNE"
            st.session_state.pantalla = "info_documento"
        elif doc_input == "3":
            st.session_state.documento = "Libre deuda biblioteca FACENA"
            st.session_state.pantalla = "info_documento"
        elif doc_input == "4":
            st.session_state.documento = "Formulario de cotejo de ficha académica"
            st.session_state.pantalla = "info_documento"
        else:
            st.warning("❌ Opción no válida. Ingresá un número del 1 al 4.")

# Pantalla de información sobre documentación
elif st.session_state.pantalla == "info_documento":
    st.subheader("ℹ️ Información sobre la documentación")

    doc = st.session_state.documento
    if doc == "DNI":
        st.write("🪪 DNI: Presentar frente y dorso del DNI en formato PDF.")
    elif doc == "Libre deuda biblioteca UNNE":
        st.write("📚 Libre Deuda UNNE: Se solicita en la biblioteca central de la UNNE.")
    elif doc == "Libre deuda biblioteca FACENA":
        st.write("📚 Libre Deuda FACENA: Solicitá en la biblioteca de la facultad.")
    elif doc == "Formulario de cotejo de ficha académica":
        st.write("📝 Formulario de Cotejo: Lo obtenés en la oficina académica o desde la web de la facultad.")

    st.subheader("¿Qué querés hacer ahora?")
    st.text("1 - Consultar otra documentación")
    st.text("2 - Volver al inicio")
    st.text("3 - Finalizar")

    siguiente = st.text_input("Ingresá una opción:", key="next_input")

    if st.button("Elegir acción"):
        if siguiente == "1":
            st.session_state.pantalla = "documentacion"
        elif siguiente == "2":
            reiniciar()
        elif siguiente == "3":
            st.session_state.pantalla = "fin"
        else:
            st.warning("❌ Opción no válida. Ingresá 1, 2 o 3.")

# Pantalla final
elif st.session_state.pantalla == "fin":
    st.balloons()
    st.success("🎓 ¡Gracias por usar el asistente de trámite de título! ¡Éxitos!")
    if st.button("Volver a empezar"):
        reiniciar()