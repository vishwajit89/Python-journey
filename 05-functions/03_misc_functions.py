def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > b and c > a:
        return c
    else:
        return "Two or more numbers are tied for greatest"

a = 1
b = 23
c = 3
print(greatest(a, b, c))


def f_to_c(f):
    return 5 * (f - 32) / 9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")


print("a")
print("b")
print("c", end="")
print("d", end="")


def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")


def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item)
    return n

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))


def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multiply(5)