
def sumofdic( citycodes):
    sum= 0
    for key , value  in citycodes.items():
        sum+= value
    return sum
citycodes = { 'nanded' : 26 , 'pune': 27 , 'nashik' : 80  ,'hussa' : 12}     
res = sumofdic(citycodes)
print("the sum of items is : ", res)