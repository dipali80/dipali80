
def prime(num):
    for i in range(2 , num):
      if(num %i == 0):
         return False
      else:
         return True
      
num = int(input("enter the number :")) 
result = (prime(num))
print(result)     
         
   
    