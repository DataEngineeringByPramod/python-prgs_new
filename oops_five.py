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

    @classmethod
    def from_str(cls, string):
        # params = string.split('-')  # returns a list
        # return cls(params[0], params[1], params[2])
          return cls(*string.split('-'))

# Employee.chaange_leaves(34)
# print(Employee.no_of_leaves)
# class methods are used to access the class variable
# and after making the class methods an object can also access the class methods and class variables

test = Employee('pramod', 84534, 'engineer')
karan = Employee.from_str('Karan-48074-student')
print(karan.salary)
print(karan.name)
print(test.name)
# print(test.name)
# test.chaange_leaves(34)
# print(test.no_of_leaves)
# print(test.__dict__)
# test2 = Employee()
