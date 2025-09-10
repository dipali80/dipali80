

class Book:
    def  __init__(self, bid = 101, bname = "bhagavat", price = 500, author = "premanand"):
        print("calling the cunstrocture")
        self.bi = bid
        self.bn = bname
        self.p = price
        self.a = author

    def ShowData(self):
        print("showing the data")
        print("book id", self.bi)
        print("bookname", self.bn)
        print("price", self.p)
        print(" author", self.a)

    def __del__(self):
        print("destructer called :") 

obj1 = Book(123, "bhagvat puran ", 250 , "babaji")
obj1.ShowData( )
print("###############################################")
obj2 = Book()
obj2.ShowData()


     