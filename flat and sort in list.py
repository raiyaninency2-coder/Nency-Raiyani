lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8]
lst1[2] = lst2
flat = []

for i in lst1 :
    if type(i)==list :
        for j in i:
            flat.append(j)
    else:
        flat.append(i)

print(flat)
flat.sort()
print(flat)


