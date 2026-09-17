# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")  # Output: List is too long (5 elements, expected <= 3)


from typing import List, Union, Tuple

n: int = 5
name: str = "Harry"

def add(a: int, b: int) -> int:
    return a + b


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(5007))