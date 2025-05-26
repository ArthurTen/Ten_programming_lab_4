a = 0
b = 1
c = 0
def fib():
    global a
    global b
    global c
    print (c)
    a = b
    b = c
    c = a+b
    
for i in range (20):
    fib()
    
    
    
    