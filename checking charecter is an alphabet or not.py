#program to check the given charecter is an alphabet or not
#using conditional operator only
charecter=input("enter one charecter")
if ord(charecter) >=65 and ord(charecter) <=90 or ord(charecter) >=97 and ord(charecter) <=122:
    print("the given input is an alphabet",charecter)
else:
    print("the given input is not an alphabet",charecter)


#without conditional operator
    
charecter=input("enter one charecter")
if charecter.isalpha():
    print("the given input is an alphabet",charecter)
else:
    print("the given input is not an alphabet",charecter)

