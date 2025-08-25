
def count_d(n):
    if(n == 0):
        return 0
    else:
        return 1 + count_d (n // 10)

def armstrong(n , power):
    if(n == 0):
        return 0
    else:
        return (n% 10)** power + armstrong (n // 10 , power)

num = int(input("enter the number :"))
power = count_d(num)

if(armstrong(num , power ) == num):
    print(f"{num} is armstrong number :")
else:
    print(f"{num} is not armstrong number :")
















# def armstrong(num , power):
#     if(num == 0):
#         return 0
#     else:
#         digit =(num % 10)
#         return((digit ** power) + armstrong(num // 10 , power))
    
# num = int(input("enter the number to check armstrong or not :"))
# power = len(str(num))
# result = armstrong(num , power)
# print( result)

# if( result == num):
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not a armstrong number")    