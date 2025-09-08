
li = [11 , 10 , 12 , 20 , 13, 30 , 20 , 17 , 15 , 19 , 17 , 80 , 44]
even = []
odd =[]
for i in range(len(li)):
    if(li[i] % 2 == 0):
        even.append(li[i])
    elif( li[i] %2!= 0):
        odd.append(li[i])
print("evn numbers of list :" , even) 
print("odd number of list :" , odd)           