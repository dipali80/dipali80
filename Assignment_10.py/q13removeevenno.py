
li =[ 10 , 11, 2 , 20 , 23 , 33, 37 , 60 ,90 , 80 , 22]
for i in range( len(li)-1 , -1 , -1):
    if(li[i] % 2 == 0):
        li.remove(li[i])

print("list after removing evwn numbwers :", li)        
