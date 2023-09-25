FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
     to do items from a local directory.
    """
    with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes a new version of the todos list
    text file to a local directory.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#print(__name__) # __name__ is a variable that equals __main__. It = the filename from another script
if __name__ == "__main__": #use if you only want it run here, not on import
     print("Hello") # python 3 course on codecademy on classes