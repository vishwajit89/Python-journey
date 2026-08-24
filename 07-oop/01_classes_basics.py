class Employee:
    language = "Py"  # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"  # This is an instance attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)
# Here name is instance attribute and salary and language are class attributes as they directly belong to the class


class Employee2:
    language = "Python"
    salary = 1200000

harry2 = Employee2()
harry2.language = "JavaScript"  # This creates an instance attribute, doesn't change the class attribute
print(harry2.language, harry2.salary)


class Employee3:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry3 = Employee3()
harry3.greet()
harry3.getInfo()


class Employee4:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language):  # dunder method, automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry4 = Employee4("Harry", 1300000, "JavaScript")
print(harry4.name, harry4.salary, harry4.language)

rohan4 = Employee4("Rohan", 900000, "Python")  # fixed: __init__ requires args once defined


class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 1200000, 245001)
print(r.name, r.salary, r.pin, r.company)


class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n ** 0.5}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()


class Demo:
    a = 4

o = Demo()
print(o.a)  # Prints the class attribute because instance attribute is not present
o.a = 0  # Instance attribute is set
print(o.a)  # Prints the instance attribute because instance attribute is present
print(Demo.a)  # Prints the class attribute