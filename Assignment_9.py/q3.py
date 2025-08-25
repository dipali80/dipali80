
def revers_n(num , rev = 0):
    if(num == 0):
        return rev
    else:
         rev = rev*10 +(num%10)
         return revers_n(num// 10 , rev)
num = int(input("enter the number :"))
result =(revers_n(num)) 
print(result)       