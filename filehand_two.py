# f = open('homework.txt', 'r')
'''print(f.readline())  # reads the single line only
print(f.readline())  # for printing the next line from a line
print(f.readline())
print(f.readline())
print(f.readlines()) ''' # read the full file and creates a list
f = open('homework.txt', 'a')
f.write('external examination paper prepared bty prabindra singh bhan\n')
print('done')
f.close()

