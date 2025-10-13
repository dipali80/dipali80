

class Shirt:
    size_price = 100
    def __init__(self, sid = 222, sname = "", stype = "kurta" , price = 1100, size = "medium"):
        print("cunstructore called :")
        self.id = sid
        self.name = sname
        self.type = stype
        self.price = price
        self.size = size

    def showData(self):
        print("SHIRT ID = ", self.id) 
        print("SHIRT NAME = ", self.name) 
        print("SHIRT TYPE = ", self.type)
        print("SHIRT PRICE = ", self.price)
        print("shirt size = ", self.size)
        # print("size price = ", Shirt.size_price)
        


    @staticmethod

    def price_per_size(size):
        if(size == "small"):
            return 1000
        elif(size == "medium"):
            return 1100
        elif(size == "large"):
            return 1200
        elif(size == "xlarge"):
            return 1300
        else:
            print("invalid choice :")

obj1 = Shirt("sk570", "sangram shirt", "denim shirt", 1000, "small")
obj1.price_per_size("small")
obj1.showData()            
      

    


      



        