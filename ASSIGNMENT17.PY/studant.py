
class Studant:
    def __init__(self, id, name, age, percentage ):
        self.sid = id
        self.sname = name
        self.sage = age
        self.sper = percentage

    def accept(self):
        self.id = int(input("enter stuadnts id "))
        self.sname = input("enter studants name ")   
        self.sage = int(input("enter stuadnts age :"))
        self.sper = int(input("enter studants marks :"))

    def s_Details(self):
        print("STUDANTS Id = ", self.sid)
        print("STUDANTS NAME =", self.sname) 
        print("STUDANTS AGE = ", self.sage) 
        print("STUDANTS PERCENTAGE = ", self.sper) 

    def __str__(self):
        return f"{self.sid}, studant is {self.sname}, studant name, {self.sage}, studant age {self.sper}, stuadnat percentage "
    
    def calRank(self):
        if(self.sper > 90):
            print("1st class:")
        elif(self.sper > 80):
            print("2nd class")
        elif(self.sper >70):
            print("3rd class")
        elif(self.sper > 60):
            print("4th class")
        elif(self.sper > 50):
            print("5th class")
        elif(self.sper > 40):
            print(" studant pass.")
        else:
            print(" studant faile!!")

# s1 = Studant(101, "dipaa", 21, 60)
# s1.calRank()
# s1.s_Details()


         
