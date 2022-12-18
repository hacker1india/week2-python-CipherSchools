'''The_init_method
Dunders(magic methods)(event methods)'''
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
            print("Hello, my name is",self.name)
p = Person("Nikhil")
p.say_hi()
a = 1
print(a +1)
print(str(a))
'''for i in a:
    print(i)'''
del a
#Dunders==Dunders are those methods which implement these events.These are special
#case funcions
#Dunder representation __<name of dunder>__
class A:
    def __init__(self):
        print(self)
        print("initializer")

    def __del__(self):
        print(self)
        print("I am dying")
a = A()
a

a = 1
print(type(a))

print(a + 5)
print("jatin" * 2)
print("jatin".__mul__(2))

class A:
    a = 1
    b = 2

    def __add__(self,x):
        return self.a + self.b + x
a = A()
a + 3
