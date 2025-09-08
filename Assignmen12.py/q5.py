
def demo(text):
    count = 0
    vowels = 'aeiouAEIOU'
    for i in text:
        if(i in vowels):
            count+=1
    return count
text = 'hello my name is dipali hambarde am from maharshtra'
res = demo(text)
print("total vowels is" , res)
        