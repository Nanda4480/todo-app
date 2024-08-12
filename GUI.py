import todo_function
from todo_function import get_todos, write_todos
import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme('DarkAmber')

clocks = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")#sg.Button(size=10, key="Add", mouseover_colors="LightBlue2", tooltip="Add a todo")
list_box = sg.Listbox(values=todo_function.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clocks],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H : %M : %S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = todo_function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            todo_function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = todo_function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                todo_function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select todo list", font=('Helvetica', 16))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = todo_function.get_todos()
                todos.remove(todo_to_complete)
                todo_function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select todo list", font=('Helvetica', 16))
        case "Exit":
            break
        case 'todo':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()