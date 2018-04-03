# day 7 code work
numlist = [1, 2, 3, 4, 5]

print(numlist)

numlist.reverse()

print(numlist)

mystring = 'christopher'
print(mystring)

print(list(mystring))
l = list(mystring)
print(l)
print(l[0])
print(l[5])

l.pop()
print(l)

l.insert(11, 'r')
print(l)

l[0] = 'x'
print(l)

del l[0]
print(l)

l.insert(0, 't')
print(l)

print(l.pop(0))
print(l)
print('-'*60)


mystring = 'christopher'
l = list(mystring)
t = tuple(mystring)

print(l)
print(t)

print('-'*60)
print('-'*60)

# dictionary
pybites = {'julian': 30, 'bob': [33, 40], 'mike': 33}

print(pybites)

people = {}

people['julian'] = 30
print(people)

people['bob'] = 103
print(people)

print(pybites.items())

for keys in pybites.keys():
    print(keys)

for values in pybites.values():
    print(values)

for keys, values in pybites.items():
    print('Name: {0} - Age: {1}'.format(keys, values))

for values in pybites['bob']:
    print(values)