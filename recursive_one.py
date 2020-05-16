'''def factorial_iterative(n):
    fact = 1
    for i in range(1, n):
        fact = fact * (i + 1)
    return fact


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print('enter the number')
y = int(input())
x = factorial_iterative(y)
z= factorial_recursive(y)
print(x)
print(z)'''
# fibonacci series


r = 1
u=2.5
f=r*u
l = 0.5
n =20
dx= l/n

tau = .2
d= tau/dx
aw = max(-f,(d-f/2),0)
print(aw)