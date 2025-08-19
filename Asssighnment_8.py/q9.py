
def palindrom(num):
    orignal = num
    revers = 0
    while(num > 0):
        digit = num % 10
        revers = revers * 10 +digit
        num //= 10
    return orignal == revers

num = int(input("enter the number :"))
if(palindrom(num)):
    print(f"{num} is palindrom number :")
else:
    print(f"{num} is not palindrom number : ")    