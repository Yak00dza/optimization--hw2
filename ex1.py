from bracketing_method import BracketingMethod
from methods import RegulaFalsiModified
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

f_1 = lambda x: exp(x) - 4*x
f_2 = lambda x: -0.9 * x**2 + 1.7 * x + 2.5
f_3 = lambda x: 0.7*x**3 - 4*x**2 + 6.2*x - 2

tasks = [
	(f_1, [-1, 1], 1e-12),
	(f_2, [2.8, 3], 1e-8),
	(f_3, [1.5, 2.5], 1e-10),
	(f_3, [0.1, 1.09], 1e-10),
	(f_3, [1.09, 2.73], 1e-10),
	(f_3, [2.73, 3.8], 1e-10),
]

bisection_method = BracketingMethod(methods.bisection_method)
regula_falsi = BracketingMethod(methods.regula_falsi)
regula_falsi_modified = RegulaFalsiModified()

methods = (
	(bisection_method, 'Bisection'),
	(regula_falsi, 'Regula Falsi'),
    (regula_falsi_modified, 'Regula Falsi Modified')
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

