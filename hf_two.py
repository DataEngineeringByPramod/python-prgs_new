# x=int(input('enter first number'))
# y=int(input('enter second number'))
# op = input('enter the operation which u want to perform on these two nu:')
# if op=='+':
#     if x==5 and y==10:
#         print(x+y+10)
#     else:
#         print(x+y)
#
# elif op=='-':
#     print(x-y)
# elif op=='*':
#     print(x*y)
# elif '/':
#     print(x/y)
# else:
#     print('not a valid op')

lst =[10,20,30,40,50,70,'pramod']
for i in lst:
    if str(i).isnumeric():
        print(i)
    else:
        print()
