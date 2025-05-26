import random

my_list = [random.randint(0, 100) for _ in range(20)]

print(my_list)

a = 0
b = 2
pair = []

def sort():
    global a, b, pair
    if a < len(my_list) - 1:
        pair = my_list[a : b]
        if my_list[a] > my_list[b-1]:
            my_list[a], my_list[b-1] = my_list[b-1], my_list[a]
        
        #print(my_list)
        a += 1
        b += 1
        sort()

sorted = False
while not sorted:
    a = 0
    b = 2
    old_list = my_list.copy()
    sort()
    sorted = my_list == old_list

print(my_list)

 
    
