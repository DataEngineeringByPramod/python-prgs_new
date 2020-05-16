class Employee:
    no_of_leaves = 10
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f' Name is {self.name}  and salary is {self.salary}  and role is {self.role}'


harry = Employee('PRAMOD',852963,'ENGINEER')
# rohan = Employee()
# harry.name = 'HARRY'  # instance variable
# harry.salary = 45612
# harry.role = 'instructor'
# rohan.name = 'ROHAN'
# rohan.salary = 85612
# rohan.role = 'instructor'
# print(rohan.printdetails())
# # after caalling the function one argument means object name for which we want to access the function from class
# # goes automatically in self keyword as a argument
# print(harry.printdetails())
#print(harry.name)

#print(harry.salary)
#print(harry.role)
print(harry.printdetails())
