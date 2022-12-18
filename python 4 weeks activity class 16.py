#comprehension
a = []
for i in range(5):
    a.append(i)
print(a)
[i  for i in range(5)] #list comprehension

print(list(map(lambda x: x**2, range(5))))

a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)
'''a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a) is a 2d array'''
[ [ j for j in range(5) for i in range(5) ] ]
''' [<value to append> <for statement> <for statement>......<if statement>...]'''
a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)
'''a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a) nested if of 1d array'''
print([j for i in range(5) for j in range(5)])

print([i for i in range(5)])
n = 5
print([ [ max(i+1 , j+1 , n-i, n-j)for j in range(n)] for i in range(n) ])
[[(i,j) for j in range(2) ]for i in range(2) ]
#dict comprehension
a={
    2: 4,
    3: 9,
    4: 16,
    }
print(type(a))
print({
    2: 4,
    3: 9,
    4: 16,
    })
print({ i: i**2 for i in range(5) })
#Set comprehension
a={ i for i in range(5)}
print(type(a))
a = (i for i in range(5))
print(type(a))
''' all comprehensions are egar loading'''
it = iter(a)
next(it)

for x in a:
    print(x)
