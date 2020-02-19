weekday=0
totaldays=0

def findout_day(date,month,year):
    #date=int(input("enter your date"))
    #month=int(input("enter your month in numericals"))
    #year=int(input("enter year"))
    
    total_days=int(((year-1)*365)+((year-1)//4))
    
    for century_nonleap_year in range((year-1)//100*100,1,-100):
       if(century_nonleap_year % 400 != 0):
            total_days=total_days-1
    """ or other way for century non leap years """
    #for century_nonleap_year in range(1,(year-1)//100+1):
     #   if(century_nonleap_year % 4 != 0):
      #      total_days=total_days-1
        
   
    
    
    def january():
        global totalno_days
        totalno_days=total_days+date
        
    def february():
        global totalno_days
        totalno_days=total_days+date+31
    def march():
        global totalno_days
        totalno_days=total_days+date+31+28
    def april():
        global totalno_days
        totalno_days=total_days+date+31+28+31
    def may():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30
    def jun():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31
    def july():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31+30
    def august():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31+30+31
    def september():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31+30+31+31
    def october():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31+30+31+31+30
    def november():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31+30+31+31+30+31
    def december():
        global totalno_days
        totalno_days=total_days+date+31+28+31+30+31+30+31+31+30+31+30
        
    dictionary={
        1:january,
        2:february,
        3:march,
        4:april,
        5:may,
        6:jun,
        7:july,
        8:august,
        9:september,
        10:october,
        11:november,
        12:december}
    
    dictionary.get(month)()
    global totaldays
    totaldays=totalno_days
    if((year%4==0 and year%100!=0 or year%400==0) and month>2):
        totaldays=totalno_days+1
    #global totaldays
    return totaldays
    
#totaldays=0
#findout_day(31,12,1)
#findout_day(31,12,2019)
#findout_day(20,11,2019)
#findout_day(21,11,2019)
#findout_day(1,1,2000)
#findout_day(31,12,2000)   # we can give input like this or
#findout_day(1,1,2004)
#findout_day(31,12,2004)
#findout_day(1,3,2000)
#findout_day(31,12,2000)
#findout_day(15,2,2020)
#findout_day(1,1,2020)
#findout_day(31,12,2020)
#findout_day(1,1,2021)
#findout_day(31,12,2003)
    
date=int(input("enter the date"))
month=int(input("enter the month"))
year=int(input("enter the year"))

findout_day(date,month,year)


#print(totaldays)
weekday=totaldays%7
if(weekday==0):
    print("to day is sunday")
if(weekday==1):
    print("to day is monday")
if(weekday==2):
    print("to day is tuesday")
if(weekday==3):
    print("to day is wednesday")
if(weekday==4):
    print("to day is thursday")
if(weekday==5):
    print("to day is friday")
if(weekday==6):
    print("to day is saturday")

