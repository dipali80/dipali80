
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))

square_root = ((b**2)- (4*a*c))**0.5

result1 = (-b+ square_root) / 2*a
result2 = (-b-square_root) / 2*a
print(f'{result1}, result1 {result2} result2')