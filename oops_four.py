# class methods
class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def chaange_leaves(cls, leaves):
        cls.no_of_leaves = leaves


# Employee.chaange_leaves(34)
# print(Employee.no_of_leaves)
# class methods are used to access the class variable
# and after making the class methods an object can also access the class methods
#by using the class methods we can change the class variable with the help of an object

test = Employee('pramod', 84534, 'engineer')
print(test.name)
test.chaange_leaves(34)
print(test.no_of_leaves)
print(test.__dict__)
print(Employee.no_of_leaves)
#test2 = Employee()
