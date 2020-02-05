#write a program to find maximum among three numbers
#using only conditional operator

first_num=int(input("enter first number"))
second_num=int(input("enter second number"))
third_num=int(input("enter third number"))
if (first_num >= second_num) and (first_num >= third_num):
    print("the greatest number is ",first_num)
elif (second_num >= third_num):
    print("the greatest number is ",second_num)
else:
    print("the greatest number is ",third_num)