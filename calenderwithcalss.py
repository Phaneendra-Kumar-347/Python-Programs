class findout_day():
    def __init__(self,date,month,year):
        self.date1=date
        self.month1=month
        self.year1=year
        #self.odddays=5 #for each 100 years
        self.leapodddays=2
        #self.nonleapodd=1
        self.findout_odddays()
    def findout_odddays(self):
         self.completedyear=self.year1-1
         self.totalcentury_odddays=self.completedyear%400//100*5
         self.totalnoncenturyyears=self.completedyear%100
         self.totalleapodddays=self.totalnoncenturyyears//4*self.leapodddays
         self.totalnonleapodddays=self.totalnoncenturyyears-(self.totalnoncenturyyears//4)
         self.findingyearodddays()
    def findingyearodddays(self):
        self.currentmonthodddays=self.date1%7
        if self.year1:
            if self.month1 ==1:
                self.currentyearodddays=self.currentmonthodddays
            
            if self.month1 ==2:
                self.currentyearodddays=self.currentmonthodddays+3
            
            if self.month1 ==3:
                self.currentyearodddays=self.currentmonthodddays+3+0
            if self.month1 ==4:
                self.currentyearodddays=self.currentmonthodddays+3+0+3
        
            if self.month1 ==5:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2
            
            if self.month1 ==6:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3
         
         
            if self.month1 ==7:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3+2
         
            if self.month1 ==8:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3+2+3
         
            if self.month1 ==9:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3+2+3+3

            if self.month1 ==10:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3+2+3+3+2
                
            if self.month1 ==11:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3+2+3+3+2+3   
                
                
            if self.month1 ==12:
                self.currentyearodddays=self.currentmonthodddays+3+0+3+2+3+2+3+3+2+3+2
        if((self.year1 % 4==0 and self.year1 % 100!=0 or self.year1 % 400==0) and self.month1 > 2):
            self.currentyearodddays= self.currentyearodddays+1
        
        self.totalodddays()
    
    def totalodddays(self):
          self.totalnoodddays=(self.currentyearodddays+ self.totalleapodddays+
                               self.totalnonleapodddays+self.totalcentury_odddays) % 7

findoutday1=findout_day(23,11,2019)
findoutday1=findout_day(1,1,2020)
findoutday1=findout_day(31,12,2021)
findoutday1=findout_day(1,1,2020)
findoutday1=findout_day(31,12,2020)
findoutday1=findout_day(1,1,2000)
findoutday1=findout_day(1,4,2100)



if findoutday1.totalnoodddays == 0:
    print("to day is sunday")
if findoutday1.totalnoodddays == 1:
    print("to day is monday")    
if findoutday1.totalnoodddays == 2:
    print("to day is tuesday")
if findoutday1.totalnoodddays == 3:
    print("to day is wednesday")
if findoutday1.totalnoodddays == 4:
    print("to day is thursday")
if findoutday1.totalnoodddays == 5:
    print("to day is friday")
if findoutday1.totalnoodddays == 6:
    print("to day is saturday") 
              
              

    