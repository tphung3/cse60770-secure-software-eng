# coding=utf8
import sys
import inspect
from shell_example import execute_cmd

import re

SINK_REGEX = re.compile(r"[ \t]+os\.system\((.*)\)")

def get_code(function_code, lineno):
	source_lines, starting_line_no = inspect.getsourcelines(function_code)
	return source_lines[lineno - starting_line_no].rstrip()

# checks whether a tainted variable reached a sink
def taint_check(frame, event, arg, codeline):
	
	if event == "return":
		m = SINK_REGEX.match(codeline)
		var_name = m.group(1)
		var_id = id(frame.f_locals[var_name])
		if var_id in tainted_variables:
			print("❌ Vulnerable!!")


def taint_analyzer(frame, event, arg):
	function_code = frame.f_code   			
	function_name = function_code.co_name 
	lineno = frame.f_lineno
	codeline = get_code(function_code, lineno)
	variable_values = ", ".join([f"{name}={frame.f_locals[name]}" for name in frame.f_locals])
	print(f"{function_name}:{lineno} {codeline} ({variable_values})")
	taint_check(frame,event,arg,codeline)


	return taint_analyzer

# this is a dummy function that for now hardcodes one input
def generate_inputs():
	global tainted_variables
	tainted_variables = set()
	
	# hardcode inputs
	inputs = []
	tainted_input1 = "ls"
	tainted_input2 = "echo 'Executed Tainted Input'"
	inputs.append(tainted_input1)
	inputs.append(tainted_input2)
	
	# mark all generated inputs as tainted
	tainted_variables.add(id(tainted_input1))
	tainted_variables.add(id(tainted_input2))

	# returns the generated inputs
	return inputs



	


def main():
	inputs = generate_inputs()
	
	for tainted_input in inputs:
		sys.settrace(taint_analyzer)
		t = execute_cmd(tainted_input)
		sys.settrace(None)


if __name__ == '__main__':
	main()