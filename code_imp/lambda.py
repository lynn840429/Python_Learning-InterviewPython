a = [1, 2, 3, 4, 5, 6, 7]

b = filter(lambda x: x%2==0, a)
print(list(b))

# c = filter(lambda x: x**2, a)
# print(list(c))

d = map(lambda x: x**2, a)
print(list(d))

e = map(lambda x: x%2==0, a)
print(list(e))
