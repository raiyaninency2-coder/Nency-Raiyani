#factorial using function
def fact(n):
    n = int(input("Enter the num : "))
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    print(factorial)
    return factorial
fact(1)