
def sumdigit(num):
    total = 0
    while(num> 0):
        digit = num % 10
        total += digit
        num //= 10
    return total
num = int(input("enter the number :"))
result = sumdigit(num)
print(f" the sum of digit of {num} is: {result}")
