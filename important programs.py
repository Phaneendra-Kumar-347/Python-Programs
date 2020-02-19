""" how to perform in nested lists """
list1=[[1,2,3],
       [1,3,4]]
list2=[]
for i in list1:
    list2.append(i)
print(list2)
for j in list2:
  print(list2[0],list2[1])
  print(j[0],j[2])
  #break 

""" string operations """
str1="ki"
str2="hi"
a=str1+" "+str2
b=str1+str2
print(b)
print(a)

""" split operations split gives directly a list """
"""and it give return so we can store any where but value of main variable not change"""
a="abc"
a.split(" ")

""" better examples of split """

li=["1",  "2",  "3","k","h",   "kii"]
a=("".join(li))
type(a)
print(a)
li[5]
li[5][0]    
li.pop(5)


li=["1",  "2",  "3","k","h",    "kii"]
a=(" ".join(li))
type(a)
print(a)


li=["1",  "2",  "3","k","h","kii"]
a=(",".join(li))
type(a)
print(a)


li=["1"  "2"  "3" "k" "h"     "kii"]
a=(" ".join(li)) #a=(",".join(li)) a=("".join(li)) # output is same
type(a)
print(a)


""" splitting operations imp"""

str1="abc 2k1    23love you 1i4"
print(str1)
list1=str1.split(" ")
print(list1)
str1=""
str2=""
list1[0][0]
for i in list1:
    #print(i)
    for j in i:
        if j.isalpha():
            str1=str1+j
        elif j.isnumeric():
            str2=str2+j
        else:
            pass
print("str1 is {},numerical str2 is {}".format(str1,str2))

""" splitting and join operations """

str1="g     e   e         k"
list1=str1.split(" ")
print(list1) 
print("".join(list1))

str1="g e e k"
list1=str1.split(" ")
print(list1) 
print("".join(list1)) 

str1="g   e   e     k"
list1=str1.split(" ")
print(list1)
str1=""
for i in list1:
    if i.isalpha():
       str1=str1+i
print(str1)


str1="g e e     k"
list1=str1.split(" ")
print(list1)
str1=""
for i in list1:
    str1=str1+i
print(str1)


str1="g e e    k"
str2=""
for i in str1:
    if i.isalpha():
       str2=str2+i
print(str2)
str2[::-1] 

str1="g  e  e  k"
str2=" "
for i in str1:
    if i == " ":
        pass
    else:
        str2=str2+i
print(str2)



input1="hello,poer,hii,jii,hii"
a=input1.split(",")
print(a)
a=list(dict.fromkeys(a)) #dict.fromkeys(a) dictionary will come 
a.sort()                 #with none values
print(a)
print(",".join(a)) # print(" ".join(a))


input1="hello poer hii jii hii"
a=input1.split(" ")
print(a)
a=list(dict.fromkeys(a))
a.sort()
print(a)
print(" ".join(a)) # print("".join(a))


"""inportant program """
abc="rama krishna akupati"
li=[]
for i in abc:
    if i not in li:
        print(abc.count(i),i)
        li.append(i)
li.sort()
print(li)

""" palindrome number """
a=121
b=""
d=a
while a:
    c=a%10
    b=b+str(c)
    a=a//10
print(b)
type(b)
type(d)
if int(b)==d:
    print(b)
    
""" other way of palindrome number """
a=121
str(a)
type(a)
a=str(a)
type(a)
print(a)
b=a[::-1]
if a==b:
    b=int(b)
    print(b)
type(b)

""" removing duplicate values """

a=[1,2,3,4,4,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

""" finding second highest values in a dictionary """

a={"bb":50,"kk":70,"id":75,"di":45,"cc":70}
b=sorted(a.values())
b=b[-2]
print(b)
car={}
for i,j in a.items():
    if j == b:
        print(i,j)
        car.update({i:j})
print(car)

""" creating dictionaries """

d = dict([("age", 25),("b","c")])
print(d)
b=dict(a="h")
print(b)

""" dictionaries operations """
dict1={1:5,2:4}
for i in dict1.values():
    print(i)
for i in dict1.keys():
    print(i)


a=[4,2,3,1,4]
b=(dict.fromkeys(a,1))
print(b)

a=[4,2,3,1,4]
b=list(dict.fromkeys(a))
print(b)




""" in dictionaries none will come if key is not present"""
dict1={1:4,5:7}
print(dict1.get(8))


""" important programs about common elements in two lists """
import random
l1=list(range(1,100))
random.shuffle(l1)

l2=list(range(1,50))
random.shuffle(l2)
count=0
for i in l2:
    for j in l1:
        if i==j:
            print(i)
        count=count+1
print(count)



l1=list(range(1,100))
random.shuffle(l1)
l1=set(l1)

l2=list(range(1,50))
random.shuffle(l2)
l2=set(l2)

l3=l1.union(l2)
print(list(l3)) # or other way

l4=l1|l2
print(list(l4)) #union or | return values



import random
l1=list(range(1,100))
random.shuffle(l1)
l1=set(l1)

l2=list(range(1,50))
random.shuffle(l2)
l2=set(l2)
print(list(l1 & l2)) #or
print(list(l1.intersection(l2)))



import random
l1=list(range(1,100))
random.shuffle(l1)

l2=list(range(1,50))
random.shuffle(l2)
count=0
dict1=dict.fromkeys(l1,1)
for i in l2:
    if dict1.get(i)!= None:
        print(i)
    count=count+1
print(count)


import random
l1=list(range(1,100))
random.shuffle(l1)

l2=list(range(1,50))
random.shuffle(l2)
count=0
for i in l2:
     if i in l1:
         print(i)
     count=count+1
print(count)


import random
l1=list(range(1,100))
random.shuffle(l1)

l2=list(range(1,50))
random.shuffle(l2)
count=0
for i in l2:
    if l1.count(i) != 0:
        print(i)
    count=count+1
print(count)

""" possitive random numbers appended to empty list """
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
            #continue
        else:
            continue
    else:
        print(list1)
        break
    
""" very very important """
list1=[("hari",22,54),("madu",23,55),("madu",22,51),("anil",20,54),("hari",23,55),("bunny",20,54),("anil",20,54),("anil",20,51)]
list2=[]
list3=[]
list4=[]
for i in list1:
    list2.append(i[1])
    list3.append(i[2])
    list4.append(i[0])
list2=set(list2)
list3=set(list3)
list4=set(list4)
list2=list(list2)
list3=list(list3)
list4=list(list4)
list4.sort()
list2.sort()
list3.sort()
for x in list2:
    for j in list3:
        for k in list4:
             for i in list1:
                 if x==i[1] and j==i[2] and k==i[0]:
                     print(i)
                     #break # duplicates will remove if u put break here.
                     #for y in list4:   # we can find out by this also.
                      #   if y==i[0]:
                       #     print(i)
                        #    break
        
""" wrong but see the code where wrong """           
for x in list2:
    for j in list3:
        for i in list1:
            if x==i[1] and j==i[2]:
                for y in list4:
                    if y==i[0]:
                        print(i)
                        break




        






