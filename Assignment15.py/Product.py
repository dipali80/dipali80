

class Product:
    def __init__(self , pid = 111, pname = "headset", price = 3000, quality = "say to handle"):
        print("cunstructore called : ")
        self.pi = pid
        self.pn = pname
        self.p = price
        self.q = quality

    def showProduct(self):
        print("show the product data")
        print("product id :", self.pi) 
        print("product name :", self.pn) 
        print("price :", self.p) 
        print("quality :", self.q)

    def __del__(self):
        print("calling the destructor :")  

obj1 = Product(103 , "earburds", 2000 , "it provides wireless connection , easy to handle")
obj1.showProduct()

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
obj2 = Product()
obj2.showProduct()           

  





        