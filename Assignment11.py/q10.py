
li = [11 , 20 , 40 , 13 , 17, 18 , 19 , 50 ]
for i in range(len(li)-1 , -1 , -1):
    if(li[i] %2 == 0):
        li.remove(li[i])
print("after removing even numbers from the list :" , li)        