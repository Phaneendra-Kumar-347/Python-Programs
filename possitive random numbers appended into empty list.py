from random import randint
rand_1=int(input("enter starting number"))
rand_2=int(input("enter ending number"))
list1=[]
len_list=int(input("enter excepting length of your list"))
while True:
    random_num=randint(rand_1,rand_2)
    if len(list1)<len_list:
        if random_num % 2 == 0:
            list1.append(random_num)
            continue
        else:
            continue
    else:
        print(list1)
        break
    
            
    
        
