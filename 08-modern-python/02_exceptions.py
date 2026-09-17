a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")


try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("I am inside else")