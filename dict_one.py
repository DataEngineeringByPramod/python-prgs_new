'''d1 = {'name': 'pramod', 'rno': 1700804, 'add': 'agra'}
print(d1['rno'])
print(d1['name'])
print(d1['add'])
d1['name2'] = 'ayush'
d1['rishabh']= {'gf': 'as', 'city': 'aligarh'}
d1['bhanu'] = 'gpampp'
print(d1['rishabh']['gf'])
del d1['bhanu']
d1['rno'] = 1800804
d2 = d1.copy()
print(d2)
del d2['add']
print(d2)
print(d1)
print(d2.items())'''
#assignment
apni = {'mutable':'that can change',
        'immutable':'that can no change',
        'set':'collection of well defined objects',
        'quarantine':'self isolation for 14 day'}

x = input('search the word')
print(apni[x])
print(apni.items())

