
age1 = int(input('enter the age of person 1:'))
ticket_amt = int(input("enter the ticket amount"))

if(age1< 12):
    dis_amt = ticket_amt * 0.3
    amt1 = ticket_amt - dis_amt
elif( age1 >59):
    dis_amt = ticket_amt * 0.5
    amt2 = ticket_amt - dis_amt
