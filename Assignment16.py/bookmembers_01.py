

class Book:
    count = 0
    def __init__(self, bid = 111, bname = "BHAGVAT GITA", price = 250, author = "SWAMI NARAYAN"):
        Book.count += 1
        print("instructure called :")
        self.id = bid
        self.name = bname
        self.price = price
        self.author = author

    def showData(self):
        print("BOOK ID = ", self.id) 
        print("BOOK NAME = ", self.name)
        print("BOOK PRICE = ", self.price)   
        print("BOOK AUTHOR = ", self.author)
        # print("count = ", Book.count)

    @staticmethod

    def countobjects():
        print("numbers of object created :",Book.count)

    def __del__(self):
        print("destructure called :")    

book1 = Book()  
book1.showData()
book1.countobjects() 

book2 = Book(100, "bhagvatam", 1000, "surat muni")
book2.showData()
book2.countobjects()

     

   

     




      
    
    