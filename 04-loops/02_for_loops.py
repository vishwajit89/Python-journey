## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)


for i in range(100):
    if i == 34:
        break  # Exit the loop right now
    print(i)

for i in range(100):
    if i == 34:
        continue  # Skip this iteration
    print(i)


n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")


n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")