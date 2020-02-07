"Write a program to flip bits of a binary number "
"using bitwise operator."
import math 
num=int(input("enter a number"))
def invertBits(num):  
    x = int(math.log2(num)) + 1
    print(x)
    for i in range(x):  
        num = (num ^ (1 << i))  
    print(num) 
    print(bin(num))
  
invertBits(num)  

