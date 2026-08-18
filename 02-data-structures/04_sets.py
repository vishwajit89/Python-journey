s = {1, 5, 32, 54, 5, 5, 5, "Harry"}
print(s, type(s))
s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))

e = set()  # Don't use s = {} — that creates an empty dictionary, not a set
s = {1, 5, 32, 54, 5, 5, 5}
print(s)

s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}
print(s1.union(s2))
print(s1.intersection(s2))