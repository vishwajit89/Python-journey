l = [3, 513, 53, 535]

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")


myList = [1, 2, 9, 5, 3, 5]
squaredList = [i * i for i in myList]
print(squaredList)


def myFunc():
    print("Hello world!")

if __name__ == "__main__":
    # If this code is directly executed by running the file it's present in
    print("We are directly running this code")
    myFunc()
    print(__name__)