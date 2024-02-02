FILEPATH = "todos.txt"
def get_todos(file_path = FILEPATH):
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, file_path= FILEPATH):
    with open(file_path,'w') as file:
        file.writelines(todos_arg)
# no return for this one - its a procedure


# checking if running from the current module or caled elsewhere - if local = __main__
if __name__ == "__main__":
    print("Hello")