import sys
import inspect
from triangle import triangle
# Code from the Fuzzing Book
def traceit(frame, event, arg):
    function_code = frame.f_code
    function_name = function_code.co_name
    lineno = frame.f_lineno
    vars = frame.f_locals

    source_lines, starting_line_no = inspect.getsourcelines(frame.f_code)
    loc = f"{function_name}:{lineno} {source_lines[lineno - starting_line_no].rstrip()}"
    vars = ", ".join(f"{name} = {vars[name]}" for name in vars)

    print(f"{loc:50} ({vars})")

    return traceit

def main():
    sys.settrace(traceit)
    triangle(2, 2, 1)
    sys.settrace(None)

if __name__ == '__main__':
    main()