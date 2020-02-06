#Write a program to swap two numbers using bitwise operator.
#In bitwise operator 1 is converted to binary form x=0001

x=int(input('Enter the value of x:'))
y=int(input('Enter the value of y:'))
print("Binary representation of x is ",bin(x))
print("Binary representation of y is ",bin(y))
print('Before swaping the value of x is {} and y is {}'.format(x,y))
x=x^y #in xor operation if both bits are same it will gives zero , 
y=x^y #otherwise gives 1
x=x^y
print('After swaping the value of x is {} and y is {}'.format(x,y))

