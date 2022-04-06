import inspect
import ast 
from twice import test

def collect_conditions(tree):
	conditions = []

	def traverse(node):
		if isinstance(node, ast.If):
			cond = ast.unparse(node.test).strip()
			conditions.append(cond)

		for child in ast.iter_child_nodes(node):
			traverse(child)

	traverse(tree)
	return conditions



def main():
	test_source = inspect.getsource(test)
	test_ast = ast.parse(test_source)
	print(collect_conditions(test_ast))


if __name__ == '__main__':
	main()