
filepath = "files/todos.txt"
def get_todos(filepath=filepath):
    """ Read a text file and return the lis of todo items""" # documentation strings
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=filepath):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__": #this will stop the below print command in the main todolist file
    print(get_todos())