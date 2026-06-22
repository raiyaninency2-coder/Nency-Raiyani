#fibonakki series :
n = int(input("enter the num : "))
a = 0
b = 1
for i in range(0,n+1):
    print(a,end=" ")
    a = b
    c = a+b
    a = c


