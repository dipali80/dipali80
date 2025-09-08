
def alphanumaric(text):
    word_count = 0
    alpha_count = 0
    for i in text:
        if(i != " "):
            alpha_count+=1
        else:
            word_count+=1
    return word_count , alpha_count
text = 'dipali shankarao hambarde yamunabai highschool nanded maharashta mumbai sambhajinagar' 
print("before counting the nos and aplhabest :" , text)
res = alphanumaric(text)
print("number of words and no of characters are preseny in str is" , res)     
            