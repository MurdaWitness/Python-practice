import random

x = random.randint(1, 10)
y = random.randint(1, 10)
z = random.randint(1, 10)
A = (abs(x+y**2+z))**(0.5)
print("A = ", A)
if A < 2:
    print("n = ", 1 - (y-z)/(y+z))
elif A == 2:
    print("n = ", y**3 - x**2)
else:
    print("n = ", x**2 - y**3 + 2*x*y)
