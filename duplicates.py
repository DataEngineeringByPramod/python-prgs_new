# write a program to find the occurences of each item in the given list
my_list = [1,2,3,4,1,2,3,4,4,5,5,8,9]
occ_dict = {}

for i in my_list:
    if i in occ_dict:
        occ_dict[i] = occ_dict[i] + 1
    else:
        occ_dict[i] = 1
print(occ_dict)
