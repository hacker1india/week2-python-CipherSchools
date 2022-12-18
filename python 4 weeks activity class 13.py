#other than 3 type all the data types in python are immutable
a=[1,2,3,4]
print(a)
b=["Jatin",1,1.5,print]
print(b)
a=list()
k=[1,2,3,4]
k[0]=100
print(len("jatin"))
print('jatin'+'katyal')
print([1,2,3]+[4,5,6])
print([1]*4)
a = [1,2,3,4]
for x in a:
    print(x)
    
print("z" in "jatin")
print(1 in [1,2,3,4])

p=[1,2,3,4,5]
print(p[-1]) #inherantly
'''tuples,lists,dictionaries
list is optimized in such a way it can store n number of variables where n should be finite
obviously memory is limited but n will be the unknown'''
a=[1,2,3]
a.insert(1,100)
print(a)
a=[1,2,3,4]
a.append(5)
print(a)

a=[1,2,3,4,5]
a.pop()
print(a)
#dynamiclytyped languages
a=[1,2,3,4,5,6,7,8,9]

a.pop(2)
print(a)
a =["jatin","samarth","jatin","subham"]
a.remove("jatin")
print(a)
a=[3,2,1,4,5,6,7,8,9]
a.sort()#sort==putting the given list of data in ascending order
print(a)
b=[4,3,1,2,6]
sorted(b)
print(sorted(b))
print(b)
b=[1,2,3,4,5,4,3,2]
print(reversed(b))
print(list(reversed(b)))
print(b)
class Something:
    pass
for x in reversed(b):
    print(x)
'''lazy loading==when we fech things one by one(feaching in baches) and it is slow
vs eagar loading==feaching everything at once it is also fast but it will search everything at once
it wiil make us slow'''
#reversed(b)==lazy loading

for x in reversed(b):
    print(x)

a=[1,2,3,4,5]
[1,4,9,16]
for x in map(lambda x: x**2,a):
    print(x)

for i, x in enumerate(a):
        pass

def sqr(x):
    return x**2
for x in map(lambda x: x**2,a):
    print(x)
#delimmiter=/n
'''
1 2 3 4
'''
a=map(int, input().split())
a[0]
print(type(a[0]))
print(",".join(["jatin","smarth","molly"]))
