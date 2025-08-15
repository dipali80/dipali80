
id = "dipaa"
password = 12345
check = 0
user_id = input("enter the user id :")
user_password = int(input("enter the password :"))
while( check < 3):
    if(user_id == id and user_password == password):
        print("loging succesful:")
else:
        print("to many checks :")
        check+=1


