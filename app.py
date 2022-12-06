import streamlit as st
import functions

todos = functions.get_todos()
st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index_value, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=index_value)
    if checkbox:
        todos.pop(index_value)
        functions.write_todos(todos)
        del st.session_state[index_value]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
