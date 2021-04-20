'''Sorting the ip address depending on the last number '''


ip = ["192.168.0.09", "192.168.0.08","192.168.0.10", "192.168.0.15"]

def fun(x):
    m = x.split(".")[3]
    print(m)
    return m
    
ip.sort(key=fun)
print (ip)
