


def demo(data):
    count1 = 0
    count2 = 0
   
    for key ,  values in data.items():
        if(key in data):

         count1 += 1 
        for key , values in data.items():
            if(values in data):
             count2 += 1
    return  count1 , count2 
data = {'dipaa' : 'hambarde' , 'soham' :'hambarde' , 'sangita': 'hambarde' }    
res = demo(data)
print(res)   