s = input("Enter the string : ")
count = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
        count+=1
    #else:
       # print("not vowls in this string")
print(count)
