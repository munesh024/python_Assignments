import random 
def password_gen(): 
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "abcdefghijklmnopqrstuvwxyz"
    str3 = "0123456789"
    str4="~!@#$%^&*"
    list1 = random.sample( str1,4) 
    list2 = random.sample( str2,4) 
    list3 = random.sample( str3,4)
    list4 = random.sample( str4,4)
    list1. extend( list2)
    list1. extend( list3)
    list1.extend(list4)
    random.shuffle( list1) 
    otp = "". join( list1) 
    print(otp)
    
password_gen()
