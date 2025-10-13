

class Telivison:
    def __init__(self, model_no, screen_size, price):
        self.model = model_no
        self.sc = screen_size
        self.price = price

    def member(self):
        try:
            self.model = input("enter the model number:")
            self.sc = int(input("enter the screen size:"))
            self.price = int(input("enter the screen price:"))

            if(len(self.model) > 4 ):
        
                raise ValueError
            
            if(self.sc < 12 or self.sc > 70):
                raise ValueError
            
            elif(self.price > 5000):
                raise ValueError
            else:
                print("all details are valid :")

        except Exception as e:
            print("error", e)

    def showDetails(self):
        print("model number = ", self.model) 
        print("screen number =", self.sc)  
        print("price = ", self.price)     

obj1 = Telivison(1234, 56,3000)
obj1.member()  
obj1.showDetails() 


      


            
            










            