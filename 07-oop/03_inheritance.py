class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()
print(a.company, b.company)


class Employee2:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer2(Employee2, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a2 = Employee2()
b2 = Programmer2()
b2.show()
b2.printLanguages()
b2.showLanguage()


class Employee3:
    a = 1

class Programmer3(Employee3):
    b = 2

class Manager(Programmer3):
    c = 3

o = Employee3()
print(o.a)  # Prints the a attribute
# print(o.b)  # Would error - no b attribute in Employee3 class

o = Programmer3()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)