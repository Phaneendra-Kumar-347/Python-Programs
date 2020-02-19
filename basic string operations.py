""" string methods in python """
a="  hello   world  "
print(a.strip())
def remove(string): 
    return string.replace(" " , "") 
      
string = ' g e e k '
print(remove(string)) 

def remove(string): 
    return "".join(string.split()) 
string = ' g e e k '
print(remove(string))

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J")) 

a = "Hello, World!, phani"
print(a.split(","))
a = "Hello \n World!"
print(a.split("\n"))
a = "Hello World!"
print(a.split(" "))
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print("My name is John, and I am {}".format(age))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello, And WElcome To My World!"
x = txt.casefold()
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x ,"is my favorite")

""" tuples changing """
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

txt = "Mi casa, su casa."
x = txt.rfind("a")
print(x)
x = txt.find("a")

""" list comprehension """
squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

squares=[i*i for i in range(1,10)]
print(squares)

movies=["kaani","raani","mani","ramya","ravali"]
mov=[]
for i in movies:
    if i.startswith("r"):
        mov.append(i)
print(mov)       

movi=[t for t in movies if t.startswith("r")]
print(movi)
""" dictionaries """
dict1={}
dict1["hari"]="samsung"
dict1["nari"]="apple"
print(dict1)
d = dict([("age", 25),("b","c")])
b=dict(a="h")
print(b)
dict1={1:"a",2:"v"}
dict2={1:"e"}
dict1.update(dict2)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference(y) 
x-y
y-x




