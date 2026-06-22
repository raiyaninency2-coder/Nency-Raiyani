# sinx expansion
x_deg = int(input("Enter the angle in degree : "))
n = int(input("Enter the num : "))
x = x_deg*3.14/180
sinx = 0
sign = 1
for i in range(1,2*n,2):
    fact = 1
    for j in range(1,i+1):
        fact = fact*j
    sinx = sinx + sign * (x**i)/fact
    sign = sign*(-1)


print(sinx)
