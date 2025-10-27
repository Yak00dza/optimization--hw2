# Bisection method assumes a and b have different signs
def bisection_method(interval, f):
	a, b = interval

	x_k = (a + b) / 2
	f_a, f_b, f_k = map(f, (a, b, x_k))

	if f_a < f_b: # f(a) < 0
		if f_k < 0:
			return (k_x, b), x_k
		return (a, x_k), x_k

	if f_k < 0:
		return (a, x_k), x_k
	return (x_k, b), x_k
