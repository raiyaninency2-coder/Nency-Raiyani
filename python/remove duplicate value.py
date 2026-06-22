lst = [25,50,25,75,75,48,48,96,89,89,96]
print("original list = ",lst)
lst2 = []
for i in lst:
    if i not in lst2 :
        lst2.append(i)
print(lst2)
