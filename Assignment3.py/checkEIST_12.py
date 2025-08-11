
s1 = int(input("enter the sie 1:"))
s2 = int(input("enter the sie 2:"))
s3 = int(input("enter the sie 3:"))

if((s1 == s2) and (s2 == s3)):
    print("traingle is equilayteral" )
elif((s1 == s2) or(s2 == s3) or(s3 == s1)):#  at lest two angles of value same  exact needed
    print(" traingle is isoceles")
else:
    print("traingle is scalane")


