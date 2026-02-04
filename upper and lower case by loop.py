s = input("Enter the string : ")
uppercase = ""
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        uppercase = ord(i) - 32
    else:
        uppercase = ord(i)    
    print(chr(uppercase),end="")  


n = input("Enter the string : ")  
for j in n :
    if 65 <= ord(j) <= 90:
        lowercase =  ord(j) + 32
    else :
        lowercase = ord(j)
    print(chr(lowercase),end="")   

