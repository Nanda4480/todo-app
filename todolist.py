

'''
numbers = input("enter numbers")
def find_duplicates(input_list):
 count_dict = {}
 duplicates = []

 for item in input_list:
     if item in count_dict:
         count_dict[item] += 1
 else:
        count_dict[item] = 1

for key, value in count_dict.items():
    if value > 1:
        duplicates.append(key)



duplicates = find_duplicates(numbers)
print(f"the multiple integers aare : {duplicates}")
'''
'''
def count_occurrences(numbers):
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    return count_dict
numbers_list = [1, 2, 3, 4, 5, 2, 3 ,4, 6, 7, 7, 6]
occurrences = count_occurrences(numbers_list)
print(occurrences)
'''
'''
user_pompt = "enter a todo"
todo1 = input(user_pompt)
todo2 = input(user_pompt)
todo3 = input(user_pompt)

todos = [todo1, todo2, todo3]
print(todos)
print(type(todo1))

#bonus1
text = input("enter a title: ")
length = len(text)
print(length)
'''
'''
x = 2
while x <= 6:
    print(x)
    x+=1

name = input("enter your name: ")
while len(name) >= 5:
    print(name.capitalize())
'''
'''
user_pompt = "enter a todo"
todos = []
while True:
    todo = input(user_pompt)
    todos.append(todo)
    print(todo.capitalize())
    print(todos)
'''

'''
todos = []
while True:
    user_action = input("type add or show or exit")

    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("list completed")
'''
'''
todos = []
while True:
    user_action = input("type add or show or exit")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show": #case "show" | "display": (add additonal input | == or)

            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("wrong input")
print("list completed")
'''
'''
food = ["idly", "vada", "sambar"]
for food in food:
    print(food.capitalize())
'''

'''
todos = []
while True:
    user_action = input("type add or show or edit or exit")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("number of todo to edit: "))
            number = number - 1
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("wrong input")
print("list completed")

'''
'''
#add the number for the list
todos = []
while True:
    user_action = input("type add or show or edit or complete or exit")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

            print(f"lastone: {index, item}")

            print(len(todos))
                
        case "edit":
            number = int(input("number of todo to edit: "))
            number = number - 1
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("number of todo to complete: "))
            todos.pop(number - 1)

        case "exit":
            break
        case _:
            print("wrong input")
print("list completed")

'''

'''
#saving the variables or inputs in a file

#todos = []
while True:
    user_action = input("type add or show or edit or complete or exit")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"

            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)


        case "edit":
            number = int(input("number of todo to edit: "))
            number = number - 1
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo

        case "complete":
            number = int(input("number of todo to complete: "))
            todos.pop(number - 1)

        case "exit":
            break
        case _:
            print("wrong input")
print("list completed")

'''


'''


files = open("./files/reports.txt", 'r')
content = files.read()
length = len(content)
print(length)
'''

'''
while True:
    user_action = input("type add or show or edit or complete or exit")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"

            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n')for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)

        case "edit":
            number = int(input("number of todo to edit: "))
            number = number - 1
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo

        case "complete":
            number = int(input("number of todo to complete: "))
            todos.pop(number - 1)

        case "exit":
            break
        case _:
            print("wrong input")
print("list completed")

'''
# Optimizing the code

'''
while True:
    user_action = input("type add or show or edit or complete or exit")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"


            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n')for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)

        case "edit":
            number = int(input("number of todo to edit: "))
            number = number - 1
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()


            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n'
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)


        case "complete":
            number = int(input("number of todo to complete: "))
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"the todo {todo_to_remove} has been removed"
            print(message)

        case "exit":
            break
        case _:
            print("wrong input")
print("bye bye")

'''

'''
while True:
    user_action = input("type add/new or show or edit or complete or exit")
    user_action = user_action.strip()

    if "add" in user_action or 'new' in user_action:
        todo = user_action[4:]


        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n')for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        print(number)
        number = number - 1
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()


        new_todo = input("enter a new todo: ")
        todos[number] = new_todo + '\n'
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)


    elif "complete" in user_action:

        number = int(user_action[9:])
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

        message = f"the todo {todo_to_remove} has been removed"
        print(message)

    elif "exit" in user_action:
        break

    else:
            print(" the wrong input")
print("bye bye")
'''

'''
# Use the "Try and except" method
while True:
    user_action = input("type add/new or show or edit or complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]


        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

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
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()


            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n'
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("your input is incorrect")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

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

'''

'''
# Use custom functions
def get_todos():
    with open("files/todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("type add/new or show or edit or complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]


        todos = get_todos()

        todos.append(todo + '\n')

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

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
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
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

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

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
'''
'''
# Use advance custom functions - include arguments

def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("type add/new or show or edit or complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos(filepath="files/todos.txt")

        todos.append(todo + '\n')

        write_todos(filepath="files/todos.txt", todos_arg=todos)

    elif user_action.startswith("show"):

        todos = get_todos("files/todos.txt")

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

            todos = get_todos("files/todos.txt")


            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(filepath="files/todos.txt", todos_arg=todos)

        except ValueError:
            print("your input is incorrect")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("files/todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(filepath="files/todos.txt", todos_arg=todos)

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
'''

'''
# Use advance custom functions - default arguments
def get_todos(filepath="files/todos.txt"):
    """ Read a text file and return the lis of todo items""" # documentation strings
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("type add/new or show or edit or complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

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
'''

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



