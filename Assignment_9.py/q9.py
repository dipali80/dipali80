
def power(m , n):
    if(m == 0 and n == 0):
        return 1
    else:
         return m**n


# m = 2
# n = 3
m = int(input("enter the value of m :"))
n = int(input("enter the value of n :"))
result = (power(m , n))
print(result)