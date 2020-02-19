""" csv files """
path="//Users/colors//csvfiles.csv"
for line in open(path):
    print(line,end="")
    #break
#or other ways
lines=[line for line in open(path)]
print(lines)
for i in lines:
    print(i,end="")
    #break

with open(path) as f1: # check with this with files it is in files.
    #print(f1.read())
    #for i in f1:
     #   print(i,end="")
    text=f1.read()
    print(text)
for i in text:
    print(i)
    break
    

# different operatios
lines=[line for line in open(path)]
print(lines)
for i in lines:
    print(i[0],end="")
    #break

lines=[line for line in open(path)]
print(lines)
for i in lines:
    print(lines[0],end="")
    #break

lines=[line for line in open(path)]
print(lines)
for i in range(len(lines)):
    print(lines[i],end="")
    #break
lines=[line for line in open(path)]
print(lines[0])
print(lines[1])

# very important
path="//Users/colors//csvfiles.csv" 
dataset=[line.strip().split(",") for line in open(path)]  
print(dataset) # remove strip and see once    
print(dataset[0])
for i in dataset:
    print(i)
#    break
#operation on above program
for i in dataset:
    print(i[0])
    print(type(i[0]))
    
for i in range(len(dataset)):
    print(dataset[0])

for i in range(len(dataset)):
    print(dataset[i])
    
""" with csv module """
import csv
path="//Users/colors//csvfiles.csv" 
file=open(path,newline="")
#print(file)
print(file.read())
file.seek(0)
for i in file:
    print(i,end="")
reader1=csv.reader(file)
print(reader1)# only address print


path="//Users/colors//csvfiles.csv" 
file=open(path,newline="")
reader1=csv.reader(file)
for i in reader1:
    print(i)


path="//Users/colors//csvfiles.csv" 
file=open(path,newline="")
reader1=csv.reader(file)
for i in reader1:
    print(i[0]) 


path="//Users/colors//csvfiles.csv" 
file=open(path,newline="")
reader1=csv.reader(file)
next(reader1) # see here it is like generator so once print next do not print.
for i in reader1:
    print(i[0])
    
path="//Users/colors//csvfiles.csv" 
file=open(path,newline="")
reader1=csv.reader(file)  # these operations not possible in csv
for i in reader1:
    print(reader1[0])    

    

path="//Users/colors//csvfiles.csv" 
file=open(path,newline="")
reader1=csv.reader(file)
header=next(reader1)
data=[row for row in reader1]
print(header)
print(data)
print(data[0])
for i in data:
    print(i)
for i in data:
    print(i[0])
for i in range(len(data)):
    print(data[0])
for i in range(len(data)):
    print(data[i])
    