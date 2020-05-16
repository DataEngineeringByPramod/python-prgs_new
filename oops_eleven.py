# polymorphism-->ability to take various forms
print(5 + 6)
print('5' + '6')


# super keyword and overiding
class A:
    classvar1 = 'i am a class variable inside class A'

    def __init__(self):
        self.var1 = 'i am inside class A"s constructor'
        self.classvar1 = 'instance variable in class A'
        self.special = 'special'


class B(A):
    classvar1 = 'i am a class variable inside class B'

    def __init__(self):  # here constructor overides if anu constructor overides then previous constructor will not run
        # super().__init__()
        self.var1 = 'i am inside class B"s constructor'
        self.classvar1 = 'instance variable in class B'
        super().__init__()
        print(super().classvar1)


# if we want to use both the constructors then we have to use super keyword


a = A()
b = B()
print(b.classvar1)
print(b.special)
print(b.var1)
