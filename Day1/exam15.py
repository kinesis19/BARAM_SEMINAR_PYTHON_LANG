a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)

a = [1, 2, 3]
b = [1, 2, 3]
c = [3, 2, 1]

print(a == b)
print(a != c)