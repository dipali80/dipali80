
def largest_word(text):
    word = ""
    larger = ""
    max_length = 0

    for i in text + " ":  
        if i!= " ":
            word += i
        else:
         
            length = 0
            for  j in word:
                length += 1
            if length > max_length:
                max_length = length
                larger = word
            word = ""  
    return larger


text = "hi my name i dipali hambarde"
res = largest_word(text)
print(res)