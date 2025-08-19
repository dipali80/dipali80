
def reversnum(num):
    revers = 0
    while(num > 0):
        digit = num % 10
        revers = revers * 10 + digit
        num //= 10
    return revers

num = int(input("enter the number:"))
result = reversnum(num)
print(f"the revers number of {num} is : {result}")    