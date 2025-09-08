

def anagram(text1 , text2):
    s_text1 = sorted(text1)
    s_text2 = sorted(text2)
    if(len(text1) == len(text2)):
        print("is anagram string")
    else:
        print("is not anagram string")
    if(s_text1 == s_text2) :
        print(" is a anagram string")
    else:
        print('is not anagram string') 

text1 = 'inch'
text2 = 'chin'
res = anagram(text1 , text2)
print(res)

        