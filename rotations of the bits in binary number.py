"""Write a program to rotate bits of a given number."""
num=int(input("enter a number"))
list1=list(bin(num))
list1=list1[2:]
no_rotations=int(input("enter no.of rotations what you want"))
for i in range(no_rotations):
    x=list1.pop(0)
    list1.append(x)
list1="".join(list1)
print("after total rotations the binary value is {}".format(list1))




