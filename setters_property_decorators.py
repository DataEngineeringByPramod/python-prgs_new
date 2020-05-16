#  setters and property decorators
class Employee:
    def __init__(self, fnames, lnames):
        self.fname = fnames
        self.lname = lnames
        # self.email = f'{self.fname}.{self.lname}@gmail.com'

    def explain(self):
        return f'this employee is{self.fname} {self.lname}'

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'
    @email.setter
    def email(self,string):
        print('i am runnig......')
        names=string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    # @email.deleter
    #  def email(self):
    #     self.fname =

Hindustani_supporter = Employee('Hindustani', 'supporter')
# Pramod_mittal = Employee()
print(Hindustani_supporter.explain())
# Hindustani_supporter.fname = 'US'
print(Hindustani_supporter.email)
Hindustani_supporter.fname = 'US'
print(Hindustani_supporter.email)
# print(Hindustani_supporter.email)
# print(Hindustani_supporter.__dict__)
Hindustani_supporter.email = 'this.that@gmail.com'
print(Hindustani_supporter.fname)
print(Hindustani_supporter.lname)
print(Hindustani_supporter.email)