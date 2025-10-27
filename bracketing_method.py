class BracketingMethod:
	# iter_step takes an interval and a function and returns the next interval and x_k+1
	def __init__(self, iter_step):
		self.iter_step = iter_step
		self.history = []

	def solve(self, f, interval, epsilon):
		next_interval, x_k = self.iter_step(interval, f)
		self.history.append([interval[0], interval[1], x_k, f(x_k)])

		if abs(next_interval[1] - next_interval[0]) < epsilon:
			history_copy = self.history.copy()
			self.history = []
			return next_interval, history_copy

		return self.solve(f, next_interval, epsilon)

	def solve_and_analyze(self, f, interval, epsilon):
		print('Method results for', f)
		print(f'Interval: {interval}; epsilon: {epsilon}\n')

		result, history = self.solve(f, interval, epsilon)

		print(f'The method ran for {len(history)} iterations. The last five are:\n')
		print('a & b & x_k & f(x_k)')
		print('\hline')
		for line in history[-5:]: 
			print(' & '.join(map(str, line)))

		print('\nResulting interval:', result)
