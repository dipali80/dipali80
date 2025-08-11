

# convert the time entered in hh, min and into second

hourse = int(input('enter the hourse'))
minitus =int(input('enter the minutes'))
second = int(input('enter the seconds'))

total_seconds = ((hourse *3600) + (minitus*60) +second)

print(f'total seconds {total_seconds}')