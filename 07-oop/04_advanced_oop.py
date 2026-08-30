class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Manager()
print(o.a, o.b, o.c)


class Employee2:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee2()
e.a = 45
e.show()  # still prints 1 - cls.a refers to the class attribute, not the instance attribute e.a


class Employee3:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e3 = Employee3()
e3.a = 45
e3.name = "Harry Khan"
print(e3.fname, e3.lname)
e3.show()


class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)
print(n + m)


class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()


class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()


class Employee4:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100

e4 = Employee4()
e4.salaryAfterIncrement = 280.8
print(e4.increment)