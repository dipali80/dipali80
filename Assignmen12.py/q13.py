
def numberlater(text):
    d_count = 0
    l_count = 0
    for i in text:
        if('0' <= i and i<= '9'):
            d_count +=1
        elif('a'<=i and i<='z' or 'A'<= i and i<= 'Z'):
            l_count +=1
    return d_count , l_count
text = 'dipali1134hambarde7075nanded'   
d_count , l_count = numberlater(text)
print("number of digit present inside the sequnce is :", d_count)  
print("numbers of laters prasent inside the sequence is ", l_count)   