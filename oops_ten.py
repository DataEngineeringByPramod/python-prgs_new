# PUBLIC -->ALL PUBLUC-->GHAR K BAHAR
# PRIVATE-->GHAR WALE-->GHAR K ANDAR
# PROTECTED-->ONLY ME-->KAMRE K ANDAR
class Employee:
    no_of_leaves = 10
    _protected = 9  # only derived class can use the protected variables
    __private = 11  #private variable


emp = Employee()
print(emp._protected)
print(emp._Employee__private)  # name mangling
