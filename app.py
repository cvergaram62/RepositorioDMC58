import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Cristhian Vergara Miranda")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"])

if sesion == "Sesión 1":
    st.write("Bienvenido a la sesión 1")
    st.image("python.png")


elif sesion == "Sesión 2":
    st.write("Bienvenido a la sesión 2")
    
    precio = st.number_input("Ingrese el precio del producto:")
    descuento = st.number_input("Ingrese el descuento del producto:")

    precio_final_producto = precio - (precio*descuento/100)

    st.write("El precio final del producto es: ",precio_final_producto)

elif sesion == "Sesión 3":
    st.write("Bienvenido a la sesión 3")

else:
    st.write("Bienvenido a la sesión 4")
