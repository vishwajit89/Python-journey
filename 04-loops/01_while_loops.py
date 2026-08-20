l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]
i = 0
while i < len(l):
    print(l[i])
    i += 1


for i in range(645):
    pass  # does nothing 645 times - placeholder loop

i = 0
while i < 45:
    print(i)
    i += 1


n = int(input("Enter the number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(total)