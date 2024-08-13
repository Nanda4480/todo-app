import streamlit



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
todos = get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_todos(todos)



st.title("My Todo App")
st.subheader("This is a todo app")
st.write("this app will help you for the day's reminders")

cnt = 0
for index, todo in enumerate(get_todos()):
    cnt += 1
    #checkbox = st.checkbox(todo, key=cnt)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_fragment()


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
