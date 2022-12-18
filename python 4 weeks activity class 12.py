#Data structures
#string  formating
a = 5
print("value of a is %d"% (a))  #python inheritedly dynamic init core it works on inherently
#dynamic
print("value of a is {}".format(a))

a,b,c,d = 1,2,3,4
"a={2},b={1},c={0}".format(c,b,a)


name="Jatin katya"
company = "shuttl"

"name={name} company={company}".format(name = name,company = company)
print(f"name = {name}")

"Hello I am {name} and I work at {company}".format(name = name, company = company)

"Hello {name} welcome to my Facebook".format(name = name, company = company)
print(f"name = {name}")
print(f"name = {10/3}")
len(r"a\nb")
for c in "a\nb":
    print(c)
for c in r"a\nb":
    print(c)

print("   jathin    ".strip())

print("1,2,3,4,5".split(","))

print("jatin katyal".replace("a","z"))

print("jatin katyal".count("a")) #try solve solution in single line readabe 


