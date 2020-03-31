import os

def get_template_path(path):
    file_path = os.path.join(os.path.dirname("running_python_commands_and_arguments_in_terminal-27"), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path -> %s" %(file_path))
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()


def render_context(template_string, context):
    return template_string.format(**context)
    # if we pass the dictionary parameter to format as **parameter, it will become a keyworded,
    # variable lenght argument list (or you can see it as a tuple of key-value pairs)
    # (i.e name='Jose', date='29/05/1995', total=299). Double start (**) allows us to pass
    # key-value pair arguments (where you provide a name to the variable as you pass it into the function.)
    # for example information: https://www.geeksforgeeks.org/args-kwargs-python/
