# Multi-level inheritence

class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isdance(self):
        return f' yes i dance {self.dance} no of times'


class Grandson(Son):
    dance = 6

    def isdance(self):
        #overiding of method of son class
        return f' yes i dance  very awesomely {self.dance} no of times'
carry = Dad()
larry = Son()
harry = Grandson()
print(harry.isdance())
print(harry.basketball)# all the properties of dad and son came in grandson
# there is one rule that first of all the object search the method and class variable
# in his own class if not found then move to parent class
print(larry.basketball)


# quiz
# electronic device
# pocket  gadget
# mobile phone

#class Electronic_device:
