# faulty calculator
print('welcome to the faulty calculator')
print('enter first number')
x = int(input())
print('enter second number')
y = int(input())
print('enter the operation which u want to perform(+,-,*,/)')
op = input()
if op == '+':
    if x == 56 and y == 9:
        print('56+9 = 77')
    else:
        z = x + y
        print('sum of x y =', z)
if op == '-':
    if x == 56 and y == 9:
        print('56-9 = 77')
    else:
        z = x - y
        print('sub of %d-%d =', z)
if op == '*':
    if x == 45 and y == 3:
        print('45*3 = 555')
    else:
        z = x * y
        print('mul of %d*%d =', z)
if op == '/':
    if x == 56 and y == 6:
        print('56/6 = 4')
    else:
        z = x / y
        print('div of %d/%d =', z)
