friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends[0])
friends[0] = "Grapes"  # Unlike Strings, lists are mutable
print(friends[0])
print(friends[1:4])

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34, 62, 2, 6, 11]
value = l1.pop(3)
print(value)
print(l1)

l = [3, 3, 5, 1]
print(sum(l))