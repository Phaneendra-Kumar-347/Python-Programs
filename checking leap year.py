#write a program if the year is leap year or not 
#by using only conditional operator
year=int(input("enter a year"))
if (year % 4 == 0 and year % 100 !=0 or year % 400 ==0):
    print("it is a leap year",year)
else:
    print("it is not a leap year",year)