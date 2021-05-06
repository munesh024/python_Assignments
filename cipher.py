#To Write the Caesar cipher program i.e. if we enter A then we have to get the 3rd element starting/ from A that is D.

n=0
str = input("enter the string")

for each in str.upper():
    if each=="X" :
        n=1
        m =ord("@")+n
        m=chr(m)
        print(m,end="")
            
        
    elif each=="Y" :
        n=2
        m =ord("@")+n
        m=chr(m)
        print(m,end="")
            
            
    elif each=="Z":
        n=3
        m =ord("@")+n
        m=chr(m)
        print(m,end="")
        
    elif each==" ":
        print(each,end="")
        continue
            
    else:
        m=ord(each)+3
        m=chr(m)
        print(m,end="")

