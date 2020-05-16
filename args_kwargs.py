def funct(*k):
    for i in k:
        print(i)


funct('pramod', 'rahul', 'bhanu', 'mukul', 'mayank')


def fun(**p):
    for key, value in p.items():
        print(key, value)


# d={'name':'pramod'}
# fun(**d)
fun(name='pramod')