import random

list = []
N = 0
for i in range (8):
    x = random.randint(1, 10)
    list.append(x)
    print("x[",i+1 ,"] = ", x)
    
for i in range (8):
    check = max(list)/2
    if (list[i]<list[0] and list[i]<check and i%2==1):
        N+=1
        
print("N = ", N)
