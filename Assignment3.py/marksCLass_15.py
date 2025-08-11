
marks1 = int(input('enter the marks of subject 1:'))
marks2 = int(input('enter the marks of subject 2:'))
marks3 = int(input('enter the marks of subject 3:'))
marks4 = int(input('enter the marks of subject 4:'))
marks5 = int(input('enter the marks of subject 5:'))

if(marks1>= 90):
    print('first claas grade ')
elif(marks2>=80 and marks2 <=90):
    print(" second class grade")
elif(marks3>= 70 and marks3<=80):
    print('third class grade')
elif(marks4>= 60 and marks4<=70):
    print('forth class grade')
elif(marks5>= 50 and marks5<= 70):
    print('fifth class grade')
else:
    print('fail')
