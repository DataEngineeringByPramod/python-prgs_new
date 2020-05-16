# dunders method
# mapping operators to functions  python documentation
# operatoor overloading
class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):  # way of representing a object
        return f'Employee ({self.name} {self.salary} {self.role})'

    def __str__(self):
        return f' ({self.name} {self.salary} {self.role})'


a = Employee('pramod', 741123, 'programmer')
b = Employee('qwerty', 963852, 'eng')
print(a + b)
print(a / b)
print(repr(a))  # priority is given to str method
# repr jab chalega tab ham use call kare
