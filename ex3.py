from bracketing_method import BracketingMethod
from math import exp
import methods

TABLE_HEAD = """
\\begin{table}[H]
\\centering
\\begin{tabular}{c|c|c}
	Task & Solution segment & Number of iterations \\\\
	\hline
"""

TABLE_BOTTOM = """
	\\end{tabular}
	\\caption{Solution segments for the {name} Method}
\\end{table}
"""

tasks = [
	(lambda x: (x-1.7)**4 + (x-1.7)**2 + 0.5, [0, 4], 1e-5),
	(lambda x: exp(0.5 * (x - 2)) + (x-2)**6 + 0.1 * (x-2)**2, [-1, 5], 1e-6)
]


methods = (
	(BracketingMethod(methods.golden_search), 'Golden Search'),
	(methods.FibonacciSearch(), 'Fibonacci Search')
)

for method, name in methods:
	results = []
	print('Method:', name)
	i = 1
	for f, S, epsilon in tasks:
		result, num_iters = method.solve_and_analyze(f, S, epsilon, i)
		results.append([i, result, num_iters])
		i += 1
		print()

	print(TABLE_HEAD)
	for line in results:
		print('\t\t'," & ".join(map(str, line)), '\\\\')

	print(TABLE_BOTTOM)
	print('----')

