import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Cristhian Vergara Miranda")

sesion = st.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 1"])
