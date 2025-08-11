
# WAP  without using 3rd ( tric1 x,y = y,x)

x = int(input('enter the value of x:'))
y = int(input('enter the value of y:'))

x = x + y
y = x - y 
x = x - y

print(f' after swaping x: {x} y: {y}')

# using trick

x = int(input('enter the value of x:'))
y = int(input('enter the value of y:'))

x , y  = y , x
print(f' after swaping x: {x} y: {y}')