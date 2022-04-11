import inspect
import ast 
import z3
from twice import test

# from showast import showast
def main():
	test_source = inspect.getsource(test)
	test_ast = ast.parse(test_source)
	print(ast.dump(test_ast, indent=2))

# def main():
# 	tree = ast.parse("x+y", mode="eval")
# 	print(ast.dump(tree, indent=2))	

if __name__ == '__main__':
	main()