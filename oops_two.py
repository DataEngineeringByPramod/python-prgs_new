# class variable and instance variable
class Employee:
    no_of_leaves = 10  # class variable
    pass


harry = Employee()
rohan = Employee()
harry.name = 'HARRY'  # instance variable
harry.salary = 45612
harry.role = 'instructor'
rohan.name = 'ROHAN'
rohan.salary = 85612
rohan.role = 'instructor'
print(rohan.__dict__)# by using this we can access the instance variables of an object
rohan.no_of_leaves = 15
print(rohan.__dict__)
Employee.no_of_leaves = 12  # we can change the class variable by Employee.no_of_leaves
print(Employee.no_of_leaves)
print(rohan.name)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)

# we can not change thee class variable by instance variable
# class is a collection of objects or we can say class is template
# and after filling the template we get a object
