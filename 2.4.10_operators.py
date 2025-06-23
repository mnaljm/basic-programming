# Udtrykket 3x3 - 2x2 + 3x - 1 fra y
# 3 * x^3  (3 gange x i tredje potens)
# minus 2 * x^2  (minus 2 gange x i anden potens)
# plus 3 * x  (plus 3 gange x)
# minus 1  (minus 1)
# I Python skrives potens som **, så x^3 bliver x**3 og x^2 bliver x**2.

x =int(0)
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

x = int(1)
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

x =int(-1)
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)
