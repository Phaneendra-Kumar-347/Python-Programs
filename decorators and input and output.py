""" use input and outputs """
print("my name is %s "%"phani")
print("my name is %s and my mom name is %s"%("phani","lakshmi"))

""" decorators are used to give extra featurs at present program without modify its structurs"""
def welcomee():
    print("welcomee")
#welcomee()

def function_call(calling_function):  
    return calling_function
function_call(welcomee())

def welcomee():
    print("welcomee")
#welcomee()

def function_call(calling_function):
    print("iam ok in functioncall")   
    return calling_function     # see the out puts and below fixed it
function_call(welcomee())


def welcomee():
    print("welcomee")
#welcomee()

def function_call(calling_function): # one way of fixing
    print("iam ok in functioncall")   
    return calling_function()
function_call(welcomee)


def welcomee():
    print("welcomee")
#welcomee()

def function_call(calling_function):# otherway of fixing
    print("iam ok in functioncall")   
    return calling_function
fun=function_call(welcomee)
fun()


def welcome():
    print("welcome")
def function_call(calling_function):
    return calling_function()
function_call(welcome)


def sqr(num):
    return num**2
def cube(num):
    return num**3
def function(sqr_,cube_,innum):
    return(cube_(innum)-sqr_(innum))
function(sqr,cube,3)


def sqr(num):
    return num**2
def cube(num):
    return num**3
def function(sqr_,cube_):
    return(cube_-sqr_)
function(sqr(3),cube(3))



def plus_one(number):
    return number + 1
add_one = plus_one
add_one(5)


def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)


def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

""" once see below outputs"""
def plus_one():
    def add_one():
        print("aaaaa")

                      
    
    return add_one
aaa=plus_one()
aaa()


def plus_one():
    def add_one():
        print("aaaaa")


    
    return add_one()
aaa=plus_one()

def plus_one():
    def add_one():
        print("aaaaa")


    
    return add_one
aaa=plus_one()  # not print ofcourse aaa also not print if aaa()print

def plus_one():
    def add_one():
        print("aaaaa")


    result=add_one()
    return result
aaa1=plus_one()

def plus_one():
    def add_one():
        print("aaaaa")


    result=add_one
    return result()
aaa1=plus_one()
print(aaa1)  #no value already printed


def plus_one():
    def add_one():
        print("aaaaa")
        return "aaaaaaaaaaa"

    result=add_one()
    return result
aaa1=plus_one()

""" with simple see first program"""
@function_call
def welcomee1():
    print("welcome and hii")
welcomee1()

""" generator functions with fibonacci example """
def genfib(num):
    a,b=0,1
    print(a)
    print(b)
    while True:
        c=a+b
        if c<num:
            yield c
            a=b
            b=c
        else:
            break
genfib(10)  
next(genfib(10)) # only one time iterate so 1 come every time
generator=genfib(10) 
next(generator)

""" other way """
def genfib1(num):
    a,b=0,1
    print(a)
    print(b)
    i=0
    while i in range(0,num+1):
        c=a+b
        yield c
        a=b
        b=c
generat=genfib1(10)       
next(generat)


