def sod(num):
    # sum = 0
    if(num == 0):
        return 0
    else:
        return (num % 10)+sod(num // 10)
num = int(input("enter the digit :")) 
result = (sod(num))
print(result)   
