#  generators and iterators and iterable and iteration
#  itearble-->__iter__() or __getitem__()
#  iterator-->__next__()
#  iteration
# generator --> iterate one time  range is a generator
def gen(n):
    for i in range(n):
        yield i
g=gen(74)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())




