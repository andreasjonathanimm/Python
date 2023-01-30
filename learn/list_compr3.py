a = ['a', 4, 'c', 12, 'e', 3, 'd']
b = [e for e in a if type(e) == int]
c = [e for e in a if type(e) == str]
print(b, c)