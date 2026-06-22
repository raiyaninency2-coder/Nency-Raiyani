lst = [10,20,-5,-6,-8,-96,-665,30,45,-89,85,73]
lst1 = []
lst2 = []
for i in lst:
    if i < 0 :
        lst2.append(i)
    else :
        lst1.append(i)

print("positive list = ",lst1)
print("nagative list = ",lst2)
