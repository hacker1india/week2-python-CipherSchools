print(1,2,3,4,5,6,7,8,9,sep=",")

#sep="," ==== key worded
def func(a,b,c,d):
    print(a)
    print(b)
    print(c)  #formal arguments the arguments which are in  def of funtion are called formal arguments
func(b=1,c=2,a=3,d=4) #actual arguments  the areguments that are  given to the funtion when it is  exicuted are called actual arguments

'''def func(a):
    print("Hello")

def fun(a):
    print(a)

func()
func(1)'''


def hello():                #a fancy statement assigns a funtion to a identifier 
    print("Hello World!")
    return 1

hello()

hello

a = 1  #assigns right side vslue to left side

a = hello

hello()

a() #In python funtions is also a object

hello = 2

print(hello)
a()


#every thing that contains a value  in python is object

#def func(a,b=10,c):
'''
*args **kwargs  == just an identificaition function
'''

print(1,2,3,4,5,6)
#func(1,c=5)
'''Arguments in other languages
-Requried arguments 'func(a)'
-Defualt arguments'func(b=1)'

Arguments in python
-Rquried arguments
-Defualted arguments
-Optional positional only arguments
-Resquired keyworded only  arguments
-Defualt keword only  arguments 
-Optional keyworded only arguments
'''
def func(a,b):
    print(a,b)
func(1,2)

def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(3,4)

def func( *a):  #*a=all the positional arguments given to this funtion will be combined
               #and stored inside the variable
    print(a)
func()
def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,d=8)

#In formal arguments form memory is not alocateddef func(a,b,*c,d):
''' the memory of this alocated to set instruction set of formula  in
def func(a,b,*c,d):print(a)
    print(b)
    print(c)
    print(d)'''
def func(a,b,*c,d,e="jathin"):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,d="something",e="asdf")

def func(**k): #**pack all the key worded arguments inside the variable
    print(k)   #def fun(a,b,*c,d,e="",**k)
    func(name = "jathin") #*c=dynamic arguments
    '''def func(a,b=1,*c,d,e="",**k):
print(k)
func(name = "jathin") it's a statement that creates a funtion with the name of func'''
l=1
t=3
c=print(l+t)
print(c)
c=None

sorted([1,2,3,4])

#onelined funtion#Anonymous funtion,lambda 
k=lambda a,b:  a+b  #lambda a,b:  a+b this expression  returns a funtion
k(1,2)

