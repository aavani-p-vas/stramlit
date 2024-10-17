import streamlit as st
st.title ('Geostoria')
x = st.slider('x')  # 👈 this is a widget

y = st.slider('y')  # 👈 this is a widget
z= x+y
st.write( 'sum is', z)

