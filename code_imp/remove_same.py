l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)

for i in l2:
    print(i, ":", l1.index(i))