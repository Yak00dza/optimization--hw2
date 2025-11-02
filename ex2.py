from methods import fixed_point
import math

TABLE_HEAD = """
\\begin{table}[H]
\\centering
\\begin{tabular}{c|c|c}
	Task & Solution & Number of iterations \\\\
	\hline
"""

TABLE_BOTTOM = """
	\\end{tabular}
	\\caption{Solutions for the fixed point method}
\\end{table}
"""

LST_5_ITER_TH = """
\\begin{table}[H]
	\centering
	\\begin{tabular}{c|c|c}
		i & $x_k$ & $f(x_k)$ \\\\
		\hline
"""

tasks = [
	(lambda x: abs((1-x))**(1/3), [10, 15], 1e-12),
	(lambda x: abs(-(1-x))**(1/3), [10, 15], 1e-12),
	(lambda x: math.cos(x), [-1, 1], 1e-10),
	(lambda x: (math.exp(x) - 3)/2, [-5, 0], 1e-8),
	(lambda x: math.log(2*x+3), [0, 2], 1e-8),
]

results = []
for i, task in enumerate(tasks):
	f, interval, epsilon = task
	result, history = fixed_point(interval, f, epsilon) 
	results.append([i, result, len(history)])

	LST_5_ITER_TB = f"""
		\\end{{tabular}}
		\\caption{{Last 5 iterations for task {i+1} }}
	\\end{{table}}
	"""

	print(LST_5_ITER_TH)
	for j, line in enumerate(history[-5:]): 
		print(" & ".join(map(str, line)), '\\\\')
	print(LST_5_ITER_TB)	


print(TABLE_HEAD)
for line in results:
	print('\t\t'," & ".join(map(str, line)), '\\\\')

print(TABLE_BOTTOM)
