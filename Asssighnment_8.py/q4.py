def sumodd(num):

    total = 0
    for i in range(1 , num+1):
        if(i % 2 != 0):
            total += i
    return total
num = int(input("enter the number:"))
result = sumodd(num)
print(f" the  sum of odd numbers from 1 to {num} is : {result}")
             