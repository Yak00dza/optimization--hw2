MAX_ITER = 950

TABLE_HEAD = """
\\begin{table}[H]
	\centering
	\\begin{tabular}{c|c|c|c|c|}
		i & a & b & $x_k$ & $f(x_k)$ \\\\
		\hline
"""
class BracketingMethod:
	# iter_step takes an interval and a function and returns the next interval and x_k+1
	def __init__(self, iter_step):
		self.iter_step = iter_step
		self.history = []


	def solve(self, f, interval, epsilon, i=0):
		next_interval, x_k = self.iter_step(interval, f)
		self.history.append([interval[0], interval[1], x_k, f(x_k)])

		if abs(next_interval[1] - next_interval[0]) < epsilon:
			history_copy = self.history.copy()
			self.history = []
			return next_interval, history_copy

		if i > MAX_ITER:
			print(f'METHOD DID NOT CONVERGE IN {MAX_ITER} steps!!!')
			history_copy = self.history.copy()
			self.history = []
			return next_interval, history_copy

		return self.solve(f, next_interval, epsilon, i+1)

	def solve_and_analyze(self, f, interval, epsilon, task_n):
		result, history = self.solve(f, interval, epsilon)

		print(TABLE_HEAD)
		for i, line in enumerate(history[-5:]): 
			print(f'\t\t\t{len(history) - 5 + i + 1} & {" & ".join(map(str, line))} \\\\')
		TABLE_BOTTOM = f"""
		\\end{{tabular}}
		\\caption{{Last 5 iterations for task {task_n} }}
	\end{{table}}
		""" 
		print(TABLE_BOTTOM)

		return result, len(history)

