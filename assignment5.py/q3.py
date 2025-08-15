
passanger = int(input("enter the no of passangers:"))
ticket_price = int(input("enter the price of ticket"))
age = int(input("enter theh age of passanger"))
total_price = passanger * ticket_price
for i in range(total_price):
  if(age<12):
    disc1 = ticket_price / 0.3
    print(f"{disc1} 30 percent descount")
  elif(age>59):
    disc2 = ticket_price / 0.5
    print(f"{disc2} 50 percent descount")
  else:
    print("others need to pay full")