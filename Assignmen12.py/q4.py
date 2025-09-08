def exchangeele(text):
    if(len(text) <= 1):
        return text
    else:
        return text[-1]+text[1:-1]+text[0]
text = 'dipaa' 
res = exchangeele(text)
print("after exchanging 1st element to last:" , res )   
   
  
           

