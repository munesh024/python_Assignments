'''Use find method and find the occurrences of given Sub String in the given String.
● String = "A new Apple Insider report has suggested that the Apple iPhone series that will
come out in 2022, likely the Apple iPhone 14 lineup,"
● Sub String "Apple" '''


st=""
n=1
count=0
str1 = "A new Apple Insider report has suggested that the Apple iPhone series that will\
come out in 2022, likely the Apple iPhone 14 lineup"
for each in str1:
    if each !=" " :
        st=st+each
        
    else :
        st=st+" "
        m=st.find("Apple",n)
        if m!= -1 :
            count=count+1
            n=n+m
            
        
    
        
print(f"the occurence  of the Apple string  is {count}")
        
