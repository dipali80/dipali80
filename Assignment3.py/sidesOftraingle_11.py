
s1 = int(input("enter the side 1:"))
s2 = int(input("enter the side 2:"))
s3 = int(input("enter the side 3:"))

if((s1 + s2 >s3)and(s2 +s3 >s1)and (s1 +s3 >s2)):
    print(f'traingle is valid')
else:
    print(f' traingle is invalid')



