class A:
    def met(self):
        print('this is a method from class a')

class B(A):
    def met(self):
        print('this is a method from class B')

class C(A):
    def met(self):
        print('this is a method from class C')

class D(C,B):#sequence of inherited class is dependent
    def met(self):
        print('this is a method from class D')



a=A()
b=B()
c=C()
d=D()
print(d.met())