a = (1, 45, 342, 3424, False, "Rohan", "Shivam")
print(a)
print(type(a))

a = (1, 45, 342, 3424, False, 45, "Rohan", "Shivam")
print(a)
no = a.count(45)
print(no)
i = a.index(3424)
print(i)
print(len(a))

a = (34, 234, "Harry")
# a[2] = "Larry"  # TypeError: tuples are immutable, can't reassign items

a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)