'''Sorting the ip address depending on the last number '''


ip = ["192.168.0.09", "192.168.0.8","192.168.0.10", "192.168.0.15"]

def fun(x):
    m = x.split(".")[3]
    return int(m)
    
ip.sort(key=fun)
print (ip)
