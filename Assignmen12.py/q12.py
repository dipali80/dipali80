
def lowercase(text):
    count = 0
    for i in text:
        if('a'<=i and i <='z'):
            count+=1
    return count
text = 'HAMBARDE DIpalii shankaraOOO Nanded Maharashtra'     
res = lowercase(text)    
print("number of lowercase are prasent in the sequence:" , res)
        