import time

initial = time.time()
for i in range(45):
    print('my name is pramod mittal')
print('time taken by the for loop', time.time() - initial)
initial2 = time.time()
k = 0
while k < 46:
    print('my name is pramod mittal')
    k = k + 1
print('time taken by the the while loop',time.time()-initial2)