import math
n = int(input("Number of students:"))
list1=[]
list2=[]
for i in range(n):
    p=int(input())
    list1.append(p)
    x=(math.floor((p/2.2046) * 100 ) )/ 100;
    list2.append(x)
print(list2)