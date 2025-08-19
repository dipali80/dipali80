
def powersome(num):
    total = 0
    for i in range( 1 , num+1):
        total = total + (i**i)
    return total
num = int(input("enter the number :"))
result = powersome(num) 
print(f" the sum is : {result}")  
