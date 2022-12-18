'''List -> ordered and can be indexed using positions
Dicts > unordered and can be indexed using keys
Sets -> unordered and can't be indexed set can be iterable'''
a={1,2,3,4,5,6,7,8,9} #to define in a function we use curly braces
print(type(a))
a = {"name": "jatin"}
print(type(a))
a={1,2,3,4,5,6,7,8,9}
print(type(a))
print(list(a))
a.add(89)
a.remove(1)
a.add(69)
for i in a:
    print(i)
a = {1,2,3,4}
b = {3,4,5,6}
print(a - b) 
print(a.union(b))
print(a.intersection(b))
'''a=[91,2,3,4,5,6,7,89]
print(a.add(1))
print(a.remove(4))'''

'''a = [
    ['','',''],
    ['','',''],
    ['','',''],
    ]'''
a = [
    ['']*3
    ]*3
print(a)
a[1][1] = 'x'
print(a)
print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1]))
a=[1,2,3,4,5,6,7,8,9]
print(id(1))
a[0] = 100
a = 1
print(id(a))
#001011100011100011010
class Student:
    name ="Toney"
    marks = 60
a = 255
b = 255
print(a == b)
print(a is b)

print(id(a) == id(b))
'''definitive value
None
False
True'''
print(id(259))
''''jatin' -> "asdfghjklmnbvcx" -> "jatin" #encryption function 
'jatin' -> "erftghbnm" #hashing function used in digesting values
'jatin' -> "erftghbnm" # by defaulthashing can be done with only in immutable functions'''

a="{1,2,3,4,5,6,77,8,9,}"
print(hash(a))

a="{jatin}"
print(hash(a))
