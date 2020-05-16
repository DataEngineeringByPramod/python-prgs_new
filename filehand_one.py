'''f = open('myfile.txt', 'w')
f.write('my name is pramod mittal')
f.close()'''

'''f = open('homework.txt', 'rt')
# f1 = open('rehx.txt','w')
st = f.read(3000)
for data in st:
    if data.isalpha():
        f1.write(data)
print('done')
x=st.count('Q')
print(x)
f.close()
# f1.close()'''
# for line by line reading and writing of of file
f = open('homework.txt','r')
f1=open('reass.txt','w')
for line in f:
    f1.write(line)
f.close()










