
li = [1 , 4, 3 , 2, 5, 6, 9, 8, 10 , 40 , 44, 33 ,22]
square =[]
cubes =[]
for i in range(len(li)):
    square.append(li[i]**2)
    cubes.append(li[i]**3)


print("orignal element of list:" , li)  
print("squares of list : " , square)
print("qubes of list :" , cubes)  
    