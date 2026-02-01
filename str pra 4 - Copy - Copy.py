n = input("Enter the string : ")
print("First character :",n[0])
print("last character :",n[-1])
if len(n)%2!=0:
    mid = len(n)/2
    print("mid character",n[mid])