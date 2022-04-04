import sys
import inspect
from triangle import triangle

def get_code(function_code, lineno):
    source_lines, starting_line_no = inspect.getsourcelines(function_code)
    return source_lines[lineno - starting_line_no].rstrip()


def analyze(frame, event, arg):
    # get function code
    function_code = frame.f_code   
    # get function name
    function_name = function_code.co_name
    # get line number
    lineno = frame.f_lineno
    # prints them
    code_line = get_code(function_code, lineno)
    local_variables = frame.f_locals
    variable_values = ", ".join([f"{name} = {local_variables[name]}" for name in local_variables])
    print(f"{function_name}:{lineno} {code_line} ({variable_values})")

    # returns the function itself to track the new scope
    return analyze

def main():
    sys.settrace(analyze)
    triangle(2, 2, 1)
    sys.settrace(None)

if __name__ == '__main__':
    main()