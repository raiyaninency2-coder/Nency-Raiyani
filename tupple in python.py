#tupple in python 
#immutable
a = (92,98,97,36.50,"nency",36.50,"dev")
print(type(a))

#methods in tupple
no = a.count(36.50)
print(no)
n1 = a.index("dev")
print(n1)


print(len(a))


#convert tupple to list
n = list(a)
n.append(110)
a = tuple(n)
print(a)

d = (98,92,97)
print(max(d))
print(min(d))
print(sum(d))
