import inspect
import ast 
import z3
from twice import test

def collect_path_conditions(tree):
	paths = []

	def traverse_if_children(children, context, cond):
		old_paths = len(paths)
		for child in children:
			traverse(child, context + [cond])
		if len(paths) == old_paths:
			paths.append(context + [cond])

	def traverse(node, context):
		if isinstance(node, ast.If):
			cond = ast.unparse(node.test).strip()
			not_cond = "z3.Not(" + cond + ")"

			traverse_if_children(node.body, context, cond)
			traverse_if_children(node.orelse, context, not_cond)

		else:
			for child in ast.iter_child_nodes(node):
				traverse(child, context)

	traverse(tree, [])

	return ["z3.And(" + ", ".join(path) + ")" for path in paths]

def main():
	test_source = inspect.getsource(test)
	test_ast = ast.parse(test_source)
	path_conditions = collect_path_conditions(test_ast)
	for condition in path_conditions:
		print(condition)
		s = z3.Solver()
		x = z3.Int("x")
		y = z3.Int("y")
		z = 2*y
		status = eval(f"s.check({condition})")
		if status == z3.sat:
			solution = s.model()
			input_x = solution[x]
			input_y = solution[y]
			print(f"test({input_x},{input_y})")


if __name__ == '__main__':
	main()