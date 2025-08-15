
num = int(input("enter the number of studants"))
s1 = int(input("enter the marks of subject 1"))
s2 = int(input("enter the marks of subject 2"))
s3 = int(input("enter the marks of subject 3"))
s4 = int(input("enter the marks of subject 4"))
s5 = int(input("enter the marks of sbject 5"))

percentage  = s1 + s2 + s3 + s4 + s5 / 500 *100
print(f"{percentage} percentage of 5 subjects marks")

avg_percentage = percentage / 5
print(f"{ avg_percentage} avrage percentage of 5 subject marks")