
num = int(input("enter the number"))

sum_divisor = 0
for i in range(1, num):
    if(num % 1 == 0):
        sum_divisor +=i
if(sum_divisor == num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not perfect number")        