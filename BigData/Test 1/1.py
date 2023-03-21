import random

N = random.randint(1, 10)
M = random.randint(1, 10)
P = (2.5*N + M)/(N**2 + M**2) - (N*M)/((N-M)**2)
L = (P - (N+M)**2 - M/10)
print("P = ", P)
print("L = ", L)
