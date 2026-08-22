'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1
factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")


'''
sum(n) = sum(n-1) + n
'''

def total_sum(n):
    if n == 1:
        return 1
    return total_sum(n - 1) + n

print(total_sum(4))


def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

pattern(3)