#sets in python
s = {}#type = dict
s1 = set()#empty set
s2 = {92,98,97,36.50}
s3 = {5,5,7,7,8,8,9,9}
print(type(s1))
print(s3)#elements are not repeat



#methods of sets
s2.add(97.56)
s2.update({7,8,9})

s2.remove(36.50) #error if no found
s2.discard(100 )#no error if no found
s2.pop() #remove random elements

print(s2)

#operation in sets
n = {97,92,95,93}
d = {97,78,89,93}
print(n.union(d))
print(n.intersection(d))
print(n.difference(d))
print(n.symmetric_difference(d))


print({97,93}.issubset(n))
print(n.issuperset({97,92}))
