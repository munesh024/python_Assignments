#program to check wheather the given number is primem or not 


m=int(input("enter the number"))   
count=0
for i in range(1,m+1):  
    if m%i==0 :              #dividing given number from starting from 1 to n+1  
        count=count+1        #if m is divided by i then increase count by 1
        
if count==2 :                #since prime number is divided by one and the number itself  ,if count is 2  
    print("prime number")    #it prints the number is prime or else not a prime
else :
    print("not a prime number")
