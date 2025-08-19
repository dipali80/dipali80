
def factsum(num):

    fact_sum = 0
    fact = 1
    for i in range( 1 , num +1):
        fact_sum += fact

num = int(input("enter the number :"))
result = factsum(num) 
print(f"the susm {num} is: {result}")       