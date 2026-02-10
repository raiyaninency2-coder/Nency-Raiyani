lst1 = [92,97,98,88,85,36.50,37.75,35.50]
lst2 = [36.50,37.75,35.50]
lst3 = []
for i in lst1 :
    if  i not in lst2:
        lst3.append(i)
print(lst3)

