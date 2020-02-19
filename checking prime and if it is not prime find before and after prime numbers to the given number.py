""" find given number is prime or not"""
"""if given number is not prime then find next prime number"""

a=int(input("enter a number"))
while(a):
    for i in range(2,(a//2)+1):
        if (a%i==0):
            a=a+1
            break
    else:
        print(a,"is prime number")
        break
print("thank you")


"""count how much will add to get next prime number """
a=int(input("enter a number"))
count=0
while(True):
    for i in range(2,(a//2)+1):
        if (a%i==0):
            a=a+1
            count=count+1
            break
    else:
        print(a,"is prime number")
        break
print("thank you")
print(count)

"""find given number is prime or not and if it is not prime"""
"""find prime number it will come before the given number"""
a=int(input("enter a number"))
count=0
while(True):
    for i in range(2,(a//2)+1):
        if (a%i==0):
            a=a-1
            count=count-1
            break
    else:
        print(a,"is prime number")
        break
print("thank you")
print(count)