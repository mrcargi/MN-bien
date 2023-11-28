import sympy as sp
from prettytable import PrettyTable

x = sp.Symbol('x')

fx = sp.exp(x) + (2**(-1*x)) + (2*sp.cos(x)) - 6

table = PrettyTable(['x', 'f(x)'])

for val in range(0, 11, 1):
    result = fx.subs(x, val).evalf()
    table.add_row([val, result])

print(table)