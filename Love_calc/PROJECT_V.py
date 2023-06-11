#This was one of my earliest projects.Looking back there were easier methods to do this.


#Valentine Project
#Completed
#Self-project
#Natural method
#Ongoing updates
#Bugs fixed : 2


#Input names

name_1=str(input("Enter your name: ")).replace(" ","")
name_2=str(input("Enter your crush's name: ")).replace(" ","")

#Converting into string

def lists(string1,string2):
    global list1,list2
    list1=[]
    list2=[]
    list1[:0]=string1
    list2[:0]=string2
    return

lists(name_1,name_2)

#Creating LOVE

list3=["L","O","V","E"]

#Collection of common elements and classification

thelist=list1+list2+list3
lengthoflist=len(thelist)
n=lengthoflist-1
list4=[]
for x in range(0,n):
    a=thelist[x]
    b=thelist.count(a)
    list4.append(b)

#Using functions for upcoming loops

#Addition of corner elemnts with limit being absolute half of the list

def sum():  
  global list5 
  list5=[]
  i=0
  m=len(list4)-1
  p=int(len(list4)/2)
  for r in range(0,p):   
   
     a=list4[i]
     b=list4[m]
     c=a+b
     i=i+1
     m=m-1
     list5.append(c)
     
#when list is odd limit must be changed and middle element must be added

def odd():
    o=len(list4)-1
    t=int(o/2)
    w=list4[t]
    global list5
    list5.append(w)

#loop continous addition until only 2 elements are left 

while len(list4)!=2:
    
   sum()
   if len(list4)%2!=0:
      odd()
   list4=list5 


#Conversion to integer and problem solving when individual element length go above 2

if len(list4)==2:
    a=str(list4[0])
    b=str(list4[1])
    c=a+b
    f=str(0)
    while len(f)!=2: 
     if len(c)==3:
         e=int(c[0])+int(c[2])
         f=str(e)+str(c[1])
         c=f
     if len(c)==4:  
         e=int(c[0])+int(c[3])
         g=int(c[1])+int(c[2])
         f=str(e)+str(g) 
         c=f

print(f,"%")
  
if int(f)>=80:
    print("You are in a path to success")
elif int(f)>=50 and int(f)<80:
    print("You have a chance")
elif int(f)>=20 and int(f)<50:
    print("Its risky,drop it")
else:
    print("It will end in failure")    
