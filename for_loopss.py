list = ['harry', 'carry', 'marry', 'sarry']
for item in list:
    print(item)
# unpacking of list
list2 = [['harry', 1], ['carry', 2], ['marry', 3], ['sarry', 4], ]
for item, sno in list2:
    print(item, sno)
dict1 = dict(list2)
print(dict1)
# for item,sno in dict1:
# print(item,sno)
# error because dict can not iterate like this we have to use.item function
for item, sno in dict1.items():
    print(item, sno)
#if we want to print only keys in from dictionary
for item in dict1:
    print(item)