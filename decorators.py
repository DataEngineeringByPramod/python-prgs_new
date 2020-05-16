'''def func1():
    print('my name is pramod mittal')
func2 = func1
func2()
del func1
print('deleted')
func2()'''


# def funcret(num):
#     if num ==0:
#         return print
#     if num==1:
#         return int
# a=funcret(1)
# print(a)
#
# def executer(func):
#     func('this')
#
#
# executer(print)
def dec(func1):
    def nowexec():
        print('executing now')
        func1()
        print('executed')

    return nowexec


@dec
def who_is_pramod():
    print('pramod is a good boy')


# decorators means adjusting a function into another function
# who_is_pramod = dec(who_is_pramod)
who_is_pramod()
