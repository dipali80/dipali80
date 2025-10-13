
try:
    num1 = int(input("enter th evalue of num1 :"))
    num2 = int(input("enter the value of num2 :"))
    while True :
        print('''plz select the choice from below:
              1. (+) addition.
              2. (-) substraction.
              3.(*) multiplication.
              4. (/) division.
              5. exit ..''')
        ch = input("enter your choice:")

        if(ch =='1'):
            print("addition of num1 and num2 :", num1 +num2)

        elif(ch == '2'):
            print("substraction of num1 and num2 :", num1 - num2)

        elif(ch == '3'):
            print("multiplication of 2 numbers :", num1 *num2)
        elif(ch == '4'):
            print("division of num1 and num2", num1 / num2)
        elif(ch == '5'):
            print("Exit!!")
        else:
            print("Invalid choice :")
            break
        

except ValueError as e:
    print("error is =", e)
except ZeroDivisionError as e:
    print("error is :", e)
except:
    print("invalid operator:")





        



            












# def calculator(num1, num2):
#     try:
#         num1 = int(input("enter the value of num1 :"))
#         num2 = int(input("enter th evalue of num2 :"))
#         while True:

#             print('''plz select the choice from below.
#                 1.+ addidtion
#                 2. - substraction.
#                 3.* multiplication.
#                 4./ division.
#                 5.exit''')
#             ch = input("enter the choice !!")

#             if(ch == '1'):
#                 print("addition of num1, num2", num1 +num2)

#             elif(ch == '2'):
#                 print("substraction of num1 and num2 :",num1 - num2)
            
#             elif(ch == '3'):
#                 print("multiplication of num1 and num2 ", num1 * num2)

#             elif(ch == '4'):
#                 print("division of num1  and num2", num1 / num2)

#             elif(ch == '5'):
#               print("Exit !!")
#             else:
#                 print("invlaid choice !!")

#     except ValueError as e:
#         print("eror", e)

#     except ZeroDivisionError as e:
#         print("error", e)

#     except:
#         print("invalid operator :")    
# calculator(num1, num2)    



            




