#write a program to find maximum number 
#with using conditional operator

first_num=int(input("enter a first number"))
second_num=int(input("enter a second number"))
if first_num >=second_num:
    print("the greatest number is",first_num)
else:
    print("the greatest number is",second_num)
    
    
    
#without using conditional operator

first_num=int(input("enter a first number"))
second_num=int(input("enter a second number"))
maximum_num=max(first_num,second_num)
print("the maximum number is ",maximum_num)

