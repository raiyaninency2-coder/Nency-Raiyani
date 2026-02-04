#no of alphabates and digits
s = input("Enter the string")
alpha = 0
digits = 0
i = 0
while i<len(s) :
    if s[i].isalpha():
        alpha+=1
    elif s[i].isdigit() :
        digits+=1
    i+=1
print("digits = ",digits)
print("alphabates = ",alpha)