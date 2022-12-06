import streamlit as st
import functions

todos = functions.get_todos()

st.title("TO-DOz")
st.subheader("Never loose track again!")
st. write("Your todos:-")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter todo here...")
