from math import exp
from methods import bisection_method
from bracketing_method import BracketingMethod


f = lambda x: exp(x) - 4*x
interval = (-1, 1)
epsilon = 1e-6

solve_and_analyze(f, interval, epsilon, bisection_method)
