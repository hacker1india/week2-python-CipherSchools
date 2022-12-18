a = [1,2,3]
a[0] = 100
a[2] = 200
print(a)

a=(1,2,3,4)
print(type(a)) #tuples have different data types
#tuples are used when you don't want to change the data in it.
def func(*args):
    print(type(args))
func(1,2,3,4)
a = 5
b = 9
a,b=b,a
c=a,b
print(type(c))
def sum_diff(a,b):
    s = a+b
    d = a-b

    return s,d
c = sum_diff(10,5)
print(type(c))
print(c)
a = 1,2,3,4
print(type(a))

s,d = sum_diff(10,5)
print(s,d)
#List to tuple and tuple to list
a =(1,2,3,4)
print(list(a))
print(type(a))
print(list(range(5)))
print(tuple(range(5)))

a = (1,2,3,4,5)
a = [1,2,3,4]
a.append(5)
print(a)
a.append(7)     
print(a)
'''List py
[1,2,3,4,5,6]
 Dictionaries
 a= dict()
 a["name"]
 a[1]
a[(1,2)]
'''
a ={
    "name": "Jatin Katyal",
    1: "something",
    (1,2): "tuple key wat?"
    }
print(a["name"])
print(a[1])
'''print(a[(1,2)])
a= {
     [1,2]: "something"
     }'''
#three data types are mutable possible list,dictionary,set
a={
    "name": "Jatin Katyal"
    }
a["name"] = "Gourav"

print(a)
a = {

    "name": "Jatin",
    "company": "shuttl",
    "collage": "LPU"
    }
print(a["name"])
print(a["company"])
print(a["collage"])
#print(a["marks"])

key ="marks"
if key in a:
    print(a[key])
else:
    print("key doesn't exit")
key = "marks"
print(a.get(key))

key = "marks"
print(a.get(key, "key doesn't exit"))

print(a.keys())
print(a.values())

for x in a.items():
    print(x)

for key, value in a.items():
    print(key, "->",value)

print(a)
for x in a:
    print(x)
#every dictionary is a sequence
print(list(a))


