#program to check the given character is an alphabet or not
#using conditional operator only
while True:
    character=input("enter one character")
    if len(character) ==1:
        if ord(character) >=65 and ord(character) <=90 or ord(character) >=97 and ord(character) <=122:
            print("the given input is an alphabet",character)
        else:
            print("the given input is not an alphabet",character)
        break
    else:
        print("the given input is more than one character please enter one character only")
        continue


#without conditional operator
    
character=input("enter one character")
if character.isalpha():
    print("the given input is an alphabet",character)
else:
    print("the given input is not an alphabet",character)

