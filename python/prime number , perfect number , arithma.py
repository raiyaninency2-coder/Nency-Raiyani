#prime number , perfect number , armstrong , palindrome , automorphic

#s = int(input("enter the num : "))
#for i in range(2,s) :
 #   if s%i==0 :
  #      print("number is not prime ")
   #     break
#else:
 #   print("number is prime")

s1 = int(input("enter the num : "))
sum = 0
for i in range(1,s1) :
    if s1%i==0 :
        sum= sum + i
if sum == s1 :
    print("number is perfect")
else:
    print("number is not perfect")


s2 = int(input("Enter the string : "))
temp = s2
sum = 0
while(temp>0):
    t = temp%10
    sum = sum + t*t*t
    temp = temp//10
if sum==s2 :
    print("num is armstrong ")
else:
    print("num is not armstrong ")


s3 = int(input("Enter the num : "))
a = s3
sum = 0
while a>0 :
    v = a%10
    sum = (sum*10)+v
    a = a//10
if sum == s3 :
    print("number is palindrome ")
else:
    print("not palindrome")



s4 = int(input("Enter the num : "))
d = s4*s4
h = s4
flage = True
while h>0 :
    if h%10 != d%10 :
        print("number is not automorphic")
        flage = False
        break
    h = h // 10
    d = d // 10
if flage == True :
    print("Automorphic number ")

    









