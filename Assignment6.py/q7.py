
for i in range( 65 , 74):
    for j in range(74-i):
        print(" " , end=" ")
    for j in range( 74 , i-1):
        print(" ", end=" ")
    for k in range( 65 , i+1):
        a = chr(k)
        print(a , end=" ")
    print()    
         