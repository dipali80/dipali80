def larger_text(text1, text2):
    count1 = 0
    count2 =0
    for i in text1:
        count1+=1
        for j in text2:
            count2+=1
            if(text1 > text2):
                return text1
            elif( text2 > text1):
                return text2
            else:
                return -1
text1 = 'dipali'
text2 = 'hambarde'
res = larger_text(text1 , text2)
print("the largest string is : ", res)
        

     