lst = ["nency","dev","niyati","vraj"]
for i in lst:
    s = ""
    for j in i :
        if 'a'<=j<='z':
           s = s + chr(ord(j) - 32)
        else:
            s = s + j
        lst[i] = s

print(lst)
    
