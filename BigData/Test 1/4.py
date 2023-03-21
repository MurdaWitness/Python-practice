list = []
S = 0
for i in range (10):
    x = int(input())
    list.append(x)
    s1 = (list[i]-2)**3
    s2 = list[i]**2
    S += s1+s2
print(S)
