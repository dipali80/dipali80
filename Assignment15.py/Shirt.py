

class Shirt:
    def __init__(self, sid = 987, sname = "tiger", type = "full slues" , price = 450 , size = " x "):
        print("calling the cunstructior :")
        self.si = sid
        self.sn = sname
        self.ty = type
        self.p = price
        self.s = size

    def showData(self):
        print('sid :', self.si ) 
        print('sname :', self.sn )
        print('type:', self.ty )
        print('price:', self.p )
        print('size :', self.s ) 

    def __del__(self):
        print("destructore called :")      


obj1 = Shirt(1011 , "bubble shirt", "t-shirt", 300, "xl")
obj1.showData()

print("#########################################")

obj2 = Shirt()
obj2.showData()
         