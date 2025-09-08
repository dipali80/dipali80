
def multdict(grocery):
    mult = 1
    for key , values in grocery.items():
        mult *= values
    return mult
grocery = { 'chips': 10 , 'caritos': 20 , 'milk' : 12} 
res = multdict(grocery) 
print("thhe multiplication of items is : " , res)  
