
def demo(text):
    index = 9
    for i in text:
        if(i == 1):
            return text
        else:
            return text[:index]+text[index+1:]
text = 'dipalihambarde'
print("before removing the index in teh string" , text)
res = demo(text)
print("after removing 9th index from the string :" , res)        