#Write a program to check whether a number is even or odd 
#using bitwise operator.
#last bit(LSB) is 0 for all even numbers and 1 for all odd numbers.
#Example : 2 - 0000 0010, 8 - 0000 1000 and 5 - 0000 0101

num=int(input("Enter a number:"))
#print("Binary representation of num is:",bin(num))
if((num&1)==0):
    print("{} is Even Number".format(num))
else:
    print("{} is Odd Number ".format(num))



#using other way to find Even or Odd number

num=int(input("Enter a number:"))
a=list(bin(num))
#print(a)
if int(a[-1]) ==0:
    print("{} is Even Number".format(num))
else:
    print("{} is Odd Number".format(num))
    

#using other way to find Even or Odd number

num=int(input("Enter a number:"))
a=list(bin(num))
l=''.join(a)
#print(type(l))
if int(l[-1]) ==0:
    print("{} is Even Number".format(num))
else:
    print("{} is Odd Number".format(num))
    


#using other way to find Even or Odd number
    
num=int(input("Enter a number:"))
a=bin(num)
type(a[-1])
if int(a[-1]) ==0:
    print("{} is Even Number".format(num))
else:
    print("{} is Odd Number".format(num))
    

    
    
    