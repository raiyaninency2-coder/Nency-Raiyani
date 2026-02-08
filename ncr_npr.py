# ncr and npr :
n = int(input("Enter the num : "))
r = int(input("Enter the num : "))
nfactorial = 1
rfactorial = 1
k = n-r
kfactorial = 1
if n<r or n<0 or r<0 :
    print("invalid syntax")
else :
    for i in range(1,n+1):
        nfactorial= nfactorial*i
    for j in range(1,r+1):
        rfactorial = rfactorial*j
    for k in range(1,k+1):
        kfactorial = kfactorial*k
    
    npr = nfactorial // kfactorial
    ncr = nfactorial // (rfactorial*kfactorial)
    print("ncr = ",ncr)
    print("npr = ",npr)

    