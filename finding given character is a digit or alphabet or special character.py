#finding given character is an alphabet or digit or special character
while True:
    ch = input("Please Enter Your Own Character : ")
    if len(ch) ==1:
        if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
            print("The Given Character ", ch, "is an Alphabet") 
        elif(ch >= '0' and ch <= '9'):
            print("The Given Character ", ch, "is a Digit")
        else:
            print("The Given Character ", ch, "is a Special Character")
        break
    else:
        print("the given input is more than one character please enter one character only")
        continue