def show_loading():
    for _ in range(3):
        print("loading...")



a = 5
b = 7

print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()


'''def show_loading():
    for i in range(3):
        print("loading..." , ","*(i+1))'''


'''funtion can take parameters'''

def sheldon_knock():
    for _ in range(3):
        print("knock knock  knock penny" )

sheldon_knock()


'''def sheldon_knock():
    for _ in range(3):
        print("knock knock  knock " , name)

sheldon_knock("leonard")

def sheldon_knock(name, times = 3):
    for _ in range(times):
        print("knock knock knock", name)

sheldon_knock("leonard")'''


#return statement
def add(a,b):
    return a + b
a= add(1,2)
print(a)
