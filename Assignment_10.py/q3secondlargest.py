
li = [20 , 40 , 50 , 8 ,90]
larg = li[0]
slarg = 0

for i in range( 0, len(li)):
    if(li[i] > larg):
        slarg = larg
        larg = li[i]

    elif(li[i]> slarg):
        slarg = li[i] 
print("second largest number :" , slarg)           