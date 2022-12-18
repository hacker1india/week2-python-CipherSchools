###Lambda expression
lambda a,b: a+b
print("Hello world")
show = print
show("something")
def func():
    return 1+4
a = func
a()
names=["jathin","subhan","samath"]
for name in names:
    print(name)
for name in enumerate(names):#enumerate will create index to it
    print(name) #examples of itterations are arrays,strings,dictionaries,some range
names=["jathin","subhan","samath"]
for a in enumerate(names):
    print(a[0],a[1])
a=5
b=9
a=a+b
b=a-b
a=a-b
print(a,b)

k=4
l=0
k,l=l,k
print(a,b)
a=[1,2]
b,c=a
print(b,c)
for i,name in enumerate(names): #works on touples and unpacking
    print(i,"-",name)

#parallel arays
names=["jathin","subhan","samath"]
scores=[50,80,90,70]
for i,name in enumerate(names):
    score = scores[i]
    print(name,"-",score)
names=["jathin","subhan","samath"]
scores=[50,80,90,70]
for a in zip(names, scores):
    print(name,"-",score)

