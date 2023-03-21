import random

s = 0
x = 1
A = random.randint(1, 10)
for n in range(1, 7):
    s = ((-1)**n) * (A**(n+1)) / (4*n)
    x = x + s
print("x = ", x)
