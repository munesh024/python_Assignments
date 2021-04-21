'''To find all the index of 0 in the given tuple below
tuple (0,1,2,3,0,1,3,0,23,0)'''



count=0
tup1 = (0,1,2,3,0,1,3,0,23,0)
for each in tup1:
    if each!=0:
        count=count+1
    
    else :
        print(tup1.index(each,count))
        count=count+1
        
        
