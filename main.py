import random

F = []
k = int(input("Enter value array k: "))
i = int(0)
while (i < k):
    F.append(random.randint(0, 100))
    i+=1
print(F)

q   =   int(input("Enter 1 for create array with board: "))
if (q == 1):
    print("Enter array numbers from 1 to 100")
    F.clear()
    i = int(0)
    while (i < k):
        x = int(input("Enter array number: "))
        F.append(x)
        i+=1
print(F)

#EX 2
#Powered by Kolyas for Vika:)

a = int(0) #number of repetitions
b = int(0) #final element
c = int(1) #final number of repetitions
d = int(0) #flag max rep
r = int(0) #counter r
i = 0      #clear counter i
while (i < k):
    while (r < k):
        if (F[i] == F[r]):
            a+=1
        r+=1
    if (a > c):
        b = F[i]
        c = a
        d = 0
    elif (b == F[i]):
        d = 0
    elif (c == a):
        d = 1
    a=0
    r=0
    i+=1
if (d == 1):
    print("Non-maximum repetitions!!!")
elif (c == 0):
    print("Error")
else:
    print("Number ",b," is repeating ",c," times")

