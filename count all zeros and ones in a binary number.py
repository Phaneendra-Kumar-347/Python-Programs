""" Write a program to count total zeros and ones in a binary number."""
num=int(input("enter a number"))
str1=bin(num)
str1=str1[2:]
print('no.of zero\'s in a binary letter {} is {}'.
      format(num,str1.count("0")))

print('no.of one\'s in a binary letter {} is {}'.
      format(num,str1.count("1")))


