#sorting of number

dict1={"hari":29,"mani":30,"siva":29}
b=list(sorted(dict1.values()))
#print(b)
c=set(b)
print(c)
b=list(c)
print(b)
b.sort()
print(b)
dict2={}
for k in b:
    for i,j in dict1.items():
        if j==k:
            dict2.update({i:j})
            #print(i,j)
print(dict2)
            
 #remove duplicate of word #           
str1="mani kumqar phani banu love moni mani"
a=str1.split(" ") #it spllits and converts the string in to direct list
print(str1)
print(a)
b=set(a)
print(b)
b=list(b)
print(b)
type(b)
b.sort()
print(b)
print(" ".join(b))


#print the 2nd grade of the students
list5=[["hari",40],["banu",70],["bavani",40],["sachin",80]]
list6=[]
print(list5)
for i in list5:
    list6.append(i[1])
print(list6)
list6=set(list6)
print(list6)
list6=list(list6)
print(list6)
list6.sort()
print(list6)
list6=list6[-3]
print(list6)
for i in list5:
    if i[1]==list6:
        print(i)
        
        
        
  #clock wise      
n=[1,2,3,4,5]
l=int(input("enter the no of rotations :"))
for i in range(1,l+1):
    a=n.pop(0)
    n.append(a)
    print("num of rotations is",i)
    print(n)

#anti clock wise
n=[1,2,3,4,5]
l=int(input("enter the no of rotations :"))
for i in range(1,l+1):
    a=n.pop()
    n.insert(0,a)
    print(i,"st rotation is: ")
    print(n)
    
    
#duplicate remove using lists;
l=[1,2,1,4,3,4,5]
m=[]
for i in l:
    if i not in m: 
        m.append(i)
            
            
#remove duplicate by dictionaries            
mylist = ["hello", 2 ,"hello", 3, 4,6,5,5, 5]
mylist = list(dict.fromkeys(mylist))
print(mylist)

#remove duplicate by for loop
listofElements=[1,2,3,4,5,6,1,1,1] 
uniqueList=[]       
for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
            
           
b=[1,2,3,1]
del b[0] #it will not return anything
a=b.sort() # it wont give return so a value is none
print(a)   # none
print(b)
c=sorted(b) #it will return the result into the variable
print(c)
d=b.remove(2) #it will also does not give 
              #return anything,it will directly change in the variable
print(d)      #none coming
b.append(5) #it can store as well as changes the variablec yes
