import sys
import inspect
from triangle import triangle

def analyze(frame, event, arg):
	# get function code
    function_code = frame.f_code   
    # get function name
    function_name = function_code.co_name
    # get line number
    lineno = frame.f_lineno
    # prints them
    print(f"{function_name}:{lineno}")

    # returns the function itself to track the new scope
    return analyze

def main():
    sys.settrace(analyze)
    triangle(2, 2, 1)
    sys.settrace(None)

if __name__ == '__main__':
    main()