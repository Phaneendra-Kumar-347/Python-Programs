""" classes """
class person():
    pass
p=person()
print(p)

class person():
     print("hello")
p=person()
print(p)

class person():
    def display(self):
        print("hello")
p=person()
p.display()

class person():
    @staticmethod
    def display():
        print("hello")
p=person()
p.display()

class person():
    def __init__(self,name):
        self.name1=name
        global name2
        name2="phani"
        self.name3="kumar"
    def display(self):
        print("hello",self.name1)
        print(name2)
        print(self.name3)
p=person("amul") # we can other way person("amul").display()
p.display()
print(name2)

""" instance and clss variables  """
class person():
    clg="sunflower"
    def __init__(self,name,rollnum):
        self.name1=name
        self.rollnum1=rollnum
    def display(self):
        print(self.name1)
        print(self.rollnum1)
        print(person.clg)
        person.clg="qis"
        print(person.clg)
        
student1=person("phani","abc123")
student1.display()
student2=person("amul","ac123")
student2.display()
print(student2.name1)
print(person.clg)
person.clg="sandy"
"""inheritance is getting methods from parent class to child class"""
class animal():
    def __init__(self,name):
        self.name1=name
        #print(self.colour1) # error becz it is in dog not in init
class dog(animal):
    def myname(self,colour):
        print(self.name1)
        self.name1="nani"
        print(self.name1)
        self.colour1=colour
        print(self.colour1)
d=dog("ammu")
d.myname("white")
d.name1
d.name1="mani"
d.name1
d.colour1
d.colour1="black"
d.colour1

"""mltilevel inheritance """
class grandfa():
    def heritage(self):
        print("will go to my child1")
class father2(grandfa):
    def heri(self):
        print("will go to my kid")
class son(father2):
    def he(self):
        print("will go to only myself")
son1=son()
son1.heritage()
son1.heri()
son1.he()
print(isinstance(son1, father2))
print(isinstance(son1, grandfa))
son1=father2()
son1.heri()
print(isinstance(son1, son))
print(isinstance(son1, grandfa))

"""multiple inheritance """
class father():
    def total(self):
        print("my child is good")
class mother():
    def full(self):
        print("my child is lovely")
class kid(father,mother):
    def myself(self):
        print("i love mom and dad")
son2=kid()
son2.full()
son2.myself()
son2.total()
"""method over riding """
class father1():
    def tota(self):
        print("my child is gooood")
class kid1(father1):
    def tota(self):
        print("i love my dad")
son3=kid1()
son3.tota()

""" encapsulation means hiding data """
""" method hiding """
class car():
    def __init__(self,name,roll,height):
        self.__update(name,roll)

    def black(self):
        print("black car")
    def __update(self,name,roll):
        print("update car")
        self.name1=name
        print(self.name1)
car1=car("audi","driver","8.5inch")
car1.black()
car1.__update()#error we use that private method but can not access.
     
""" variable hiding """
class bar():
    __speed=0
    __name=""
    def __init__(self):
        print(self.__speed)
        self.__speed=200
        self.__name="badi"
    def drive(self):
        print("iam a driver")
        print(self.__speed)
    def change(self,speed1):
        print(self.__speed)
        self.__speed=speed1
        print(self.__speed)
        self.__speed=100
        print(self.__speed)
bar1=bar()
bar1.drive()       
bar1.change(300)        
bar1.__speed ## error come becz we can not access outside      
bar1.__speed=1000 # no error
bar1.drive()      # but value not change inner becz we can not access
bar1.change(300) # but we can change inner by value as argument to parametre
                 # and that parametre assigned to private variable


""" ploymorphism means many forms same method perform different"""
"""in different classes """

class Dog():
    def sound(self):
        print("barking")
class Cat():
    def sound(self):
        print("meow meow")
def makesound(animaltype):
    animaltype.sound()
cat1=Cat()
dog1=Dog()
makesound(cat1)
makesound(dog1)

""" this is abstraction """
#from abc import ABC, abstractmethod
class Payment():
    def __init__(self,bill):
        self.bill1=bill
    def print_slip(self, amount):
        print('Purchase of amount- ', amount)
    #@abstractmethod
    def payment(self, amount):
        print("it is in payment class",amount)

class CreditCardPayment(Payment):
    def payment(self, amount):
        print("bill is",self.bill1)
        print('Credit card payment of- ', amount)

class MobileWalletPayment(Payment):
    def payment(self, amount):
        print("bill is",self.bill)
        print('Mobile wallet payment of- ', amount)

obj = CreditCardPayment(3000)
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment))
obj = MobileWalletPayment(2000)
obj.payment(200)
obj.print_slip(200)
print(isinstance(obj, Payment))
obj=Payment(1000)
obj.payment(300)
obj.print_slip(300)
obj.print_slip(500)
print(isinstance(obj, Payment)) # true
print(isinstance(obj, CreditCardPayment)) # false



