amount = int(input('enter the amount:'))
temp = amount
two_thousand = temp // 2000
temp = temp % 2000
print(two_thousand)


five_hundred = temp // 500
temp = temp % 5000

two_hundred = temp // 200
temp = temp % 200

hundred = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twoenty = temp //20
temp = temp % 20

ten = temp // 10
temp = temp % 10

five = temp // 5
temp = temp % 5

total_notes = two_thousand + five_hundred + two_hundred + hundred + fifty

print(f' the 5 thousend amaount{ two_thousand} {five_hundred},{two_hundred}, {hundred},{fifty} {twoenty} {ten}{five}')