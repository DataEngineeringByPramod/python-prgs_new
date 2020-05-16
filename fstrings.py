me = 'pramod'
a = 'this is %s' % me
print(a)

x = 6
y = 10
a = 'this is {} {}'
b = a.format(x, y)
print(b)

z = f'this is {x + 20 + 50} {y * 20 + 20}'
print(z)
