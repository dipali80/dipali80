
class Product:
     discount = 100
     def __init__(self, id = 101 , name = "bhagvat gita ", price = 100 , quantity = 15):
          print("cunstrucytore called")
          self.pid = id
          self.pname = name 
          self.price = price
          self.quantity = quantity

     def Showproduct(self):
          print("PRODUCT ID = ", self.pid)
          print("PRODUCT name = ", self.pname) 
          print("PRODUCT price = ", self.price) 
          print("PRODUCT quantity = ", self.quantity) 
        #   print("DISCOUNT = ", Product.discount)
          final_price = self.price - (self.price * Product.discount)
          print("final price = ", final_price)
        #   print("final price of product = ", final_price)

     @staticmethod
     def  calculateDescount():
         print("final price = ", Product.discount)

p1 = Product(11, "ppoja", 1100, 18)
p1.Showproduct() 
p1.calculateDescount()
          
          
        



        