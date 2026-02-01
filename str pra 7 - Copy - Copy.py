s = input("Enter the string : ")
print("length = ",len(s))
count = 0
i = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
        count+=1
    else:
        i+=1
print("vowls = ",count)
print("consonants",i)
