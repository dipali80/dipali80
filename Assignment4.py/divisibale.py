
num = int(input("enter the number:"))
print(f'integer up to {num} that are not divisible by 2 or 3')

for i in range(1 , num+1):
    if(i %2 ! = 0 and i % 3 ! =0):
        print(i , end = " ")