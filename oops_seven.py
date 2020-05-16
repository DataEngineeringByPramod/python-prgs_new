# abstraction:break into layer
# encapsulation:collection of all layer in a frame or hiding the details of implementation
# inheritence
class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return print(f'{self.name}  {self.salary}  {self.role}')


class Programmer(Employee):  # single level inheritence
    no_of_holidays = 50
    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

    def printprog(self):
        return print(f'{self.name}  {self.salary}  {self.role}  {self.language}')


harry = Employee('pramod', 741852, 'engineer')
rohan = Employee('rohan', 852741, 'developer')
subham = Programmer('shubham', 963852, 'front-end developer', ['python', 'java'])
karan = Programmer('karan', 987654, 'back-end', ['python', 'kotlin'])
print(karan.printprog())
print(karan.no_of_holidays)
print(Employee.no_of_leaves)
print(karan.printdetails())

