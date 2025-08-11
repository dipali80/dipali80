
feet = int(input('enter the value of feet'))
inches = int(input('enter the value of inches'))

total_inches  = (feet * 12 )+ inches

total_cm = total_inches * 2.54

total_meters = total_cm // 100
remaining_cm = total_cm % 100

print(f'{total_inches}{total_cm}{total_meters}{remaining_cm}')



