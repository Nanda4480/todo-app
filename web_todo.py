import streamlit as st
import functions
FILEPATH = "files/todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the lis of todo items""" # documentation strings
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("this app will help you for the day's reminders")


#for todo in get_todos():
    #st.checkbox(todo)


st.text_input(label="", placeholder="Add new todo...")
