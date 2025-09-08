def bubblesort(li):
    for i in range(1 , len(li)):
        for j in range( 0 , len(li)-i):
            if(li[j] > li[j+1]):
                li[j] , li[j+1] = li[j+1] , li[j]
    return li
li = [ 50 , 40 , 30 , 20 ,10 , 5, 2]     
res = bubblesort(li)
print(res)  

print(li[-2])
