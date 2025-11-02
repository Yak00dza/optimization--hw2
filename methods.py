from math import sqrt
from bracketing_method import BracketingMethod

inv_phi = (sqrt(5) - 1) / 2

FIB = {0: 1, 1: 1}
print(len(FIB))
def F(n):
	if n in FIB:
		return FIB[n]
	FIB[n] = F(n-1) + F(n-2)
	return FIB[n]

def new_interval(a, b, x_k, f):
	f_a, f_b, f_k = map(f, (a, b, x_k))
	
	if f_k == 0:
		return (x_k, x_k), x_k

	if f_a < f_b: 
		if f_k < 0:
			return (x_k, b), x_k
		return (a, x_k), x_k

	if f_k < 0:
		return (a, x_k), x_k
	return (x_k, b), x_k

# Bisection method assumes a and b have different signs
def bisection_method(interval, f):
	a, b = interval
	x_k = (a + b) / 2
	return new_interval(a, b,x_k, f)

def regula_falsi(interval, f):
	a, b = interval
	c_k = (a * f(b) - b * f(a)) / (f(b) - f(a))
	return new_interval(a, b, c_k, f)

class RegulaFalsiModified(BracketingMethod):
	def __init__(self):
		super().__init__(None)

	def solve(self, f, interval, epsilon):
		history = []

		a, b = interval
		f_a, f_b = f(a), f(b)
		last = None
		while b-a >= epsilon:
			x_k = (a * f_b - b * f_a) / (f_b - f_a)
			f_k = f(x_k)
			history.append([a, b, x_k, f_k])
			if f_k == 0:
				return (x_k, x_k), history
			if f_a * f_k < 0:
				b = x_k
				f_b = f_k
				if last == "b":
					f_a /= 2
				last = "b"
			else:
				a = x_k
				f_a = f_k
				if last == "a": 
					f_b /= 2
				last = "a"
		return (a, b), history

def fixed_point(interval, f, epsilon):
	history = [] 
	x_k = interval[0]
	MAX_ITER = 950
	i = 1
	while abs(f(x_k) - x_k) >= epsilon:
		f_k = f(x_k)
		history.append([i, x_k, f_k])
		x_k = f_k
		i += 1
		if i >= MAX_ITER:
			break
	
	return x_k, history

def golden_search(interval, f):
	a, b = interval
	c = b - (b-a) * inv_phi
	d = a + (b - a) * inv_phi

	if f(c) < f(d):
		return (a, d), d
	return (c, b), c

class FibonacciSearch(BracketingMethod):
	def __init__(self):
		super().__init__(None)

	def find_n(self, a, b, epsilon):
		n = 2
		target = (b-a)/epsilon
		while F(n) <= target: 
			n += 1
		return n

	def solve(self, f, interval, epsilon):
		a, b = interval
		history = []

		n = self.find_n(a, b, epsilon) 
		
		c = a + (F(n - 2) / F(n)) * (b-a)
		d = a + (F(n-1)/F(n)) * (b - a)

		f_c = f(c)
		f_d = f(d)

		for k in range(1, n-1):
			if f_c > f(d):
				history.append([a, b, c, f(c)])
				a = c
			else:
				history.append([a, b, d, f(d)])
				b = d

			c = a + (F(n - k - 2) / F(n - k)) * (b-a)
			d = a + (F(n - k - 1)/F(n - k)) * (b - a)

			f_c = f(c)
			f_d = f(d)

		return (a, b), history

