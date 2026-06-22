lst1 = [88,92,97,98,73,51,36.50,37.75,35.25,85]

n = float(input("Enter the num : "))
for i in range(0,len(lst1)):
    if n == lst1[i]:
        print(f"{n} is found at ",i)
        break
else :
    print("not found")    


