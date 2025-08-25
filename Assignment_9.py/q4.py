def sum(num):
    if(num == 0):
        return 0
    else:
        return num+sum(num-1)
    
num = int(input("enter the number:"))
result = sum(num)
print(result)    