
num = int(input("enter the number:"))
lenght = len(str(num))

temp = num 
sum = 0
while(temp > 0):
    digit = temp % 10
    sum += digit ** lenght
    temp = temp // 10 
    print(f"{num} , {sum}")
  
if(sum == num):
        print(" armstrong number :")
else:
        ("not armstrong number :")



 