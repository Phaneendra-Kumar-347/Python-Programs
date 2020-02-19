""" in a list there are no.of tuples and every tuple contains peron name
   and their age and also weights are given.first sort with their age if
   the age is same then sort with their weights if the weights are also same
   then sort with their names if the names are also same they are duplicates 
   so print with duplicates first and rmove duplicates and print again."""
   
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
        