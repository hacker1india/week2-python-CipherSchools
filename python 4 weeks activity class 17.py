'''Abstraction = hidding the unwanted data (need to know basis)
Encapsulation = grouping of data
Polymorphism = maltiforms(multiple forms)
Inheritence = having some same properties'''
#oops is a paradyne
#example of encapsulation
student1 = {
    "name": "Jatin Katyal",
    "marks": 50
}
student2 = {
    "name": "Samarth",
    "marks":50
}
'''Python object can have multiple traits
callable(e.g. functions and classes)
iterable(e.g. list,string,generator)
contextable(e.g. files)'''
class Person():
    pass
p = Person()
print(p)
hex(id(p))

a = 1
'''def square(a):
    print(a**2)
with a:
    square()
a.sq'''
class Person:
    name = "Jatin"
    def say_hi(self):
        print(f"Hello Everyone ! I am {self.name}")
p = Person()
p.say_hi()
Person.say_hi(p)

class Person:
    name = "Jatin"
    def say_hi(this):
        print(f"Hello Everyone ! I am {this.name}")
p = Person()
p.say_hi()#method call
Person.say_hi(p)#function call

