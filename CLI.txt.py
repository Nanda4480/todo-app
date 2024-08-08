from todo_function import get_todos, write_todos #local module
#import todo_function

import time
date_time = time.strftime("%b %d, %Y %H : %M : %S")
print("It is: " + date_time)

while True:
    user_action = input("type add/new or show or edit or complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        #todos = todo_function.get_todos() - if we use import function

        todos.append(todo + '\n')

        write_todos(todos_arg=todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        # new_todos = [item.strip('\n')for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()


            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos_arg=todos)

        except ValueError:
            print("your input is incorrect")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos_arg=todos, filepath="files/todos.txt")

            message = f"the todo {todo_to_remove} has been removed"
            print(message)
        except IndexError:
            print("No item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
            print(" the wrong input")
print("bye bye")
