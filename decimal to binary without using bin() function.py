# conversion of decimal number to binary number without using "bin()" function.

num=int(input("enter a number"))
str1=""
while True:
    if num > 0:
        x=num%2
        num=num//2
        str1=str1+str(x)
    else:
        break
str1=str1[::-1]
print("The number {} from decimal to binary is".format(str1))



