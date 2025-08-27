
li = [10 , 11 , 12 ,13 ,14 ,15 , 16 , 17 , 18 , 19 , 20 , 21 , 23]
even= []
odd =[]

for i in range( 0 , len(li)):
    if(i % 2 == 0):
        even.append(li[i])
    elif(i % 2 != 0 ):
        odd.append(li[i])

print("even no of list :" , even)
print("odd number of lis:" , odd)         