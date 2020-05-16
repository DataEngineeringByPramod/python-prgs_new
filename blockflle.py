with open('homework.txt') as f:
    a = f.readlines(150)
    print(a)
f = open('homework.txt', 'r+')
f.write('my name is pramod mittal')
st = f.readlines()
print(st)
