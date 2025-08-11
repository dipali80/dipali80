
# calculate the salary of employee according to da(10%), ta(12%),hra (15%) of basic salary


salary = int(input("enter the total salary of employee"))

da = (salary * 10)/100 
ta= (salary * 12)/100
hra = (salary * 15)/100

total_salary = da + ta + hra + salary

print(f"total salary, {total_salary}")