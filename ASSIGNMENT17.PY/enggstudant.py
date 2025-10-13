
from studant import Studant


class Enggstudant(Studant):
    def __init__(self, id, name, age, percentage, branch , internal_marks):
        super().__init__(id, name, age, percentage)
        self.branch = branch
        self.inter = internal_marks

    def accept(self):
        super().accept()  
        self.branch = input("enter the studants branch :")
        self.inter = int(input("enter the studants internal marks :"))

    def s_Details(self):
         super().s_Details()  
         print("BRANCH OF STUDANT = ", self.branch) 
         print("INTERNAL MARKS OF STUDANTS = ", self.inter) 

    def __str__(self):
        super().__str__() 
        return f"{self.branch} branch of studant, {self.inter}, internal marks of studant "

    def calRank(self):
        super().calRank() 

# E1 = Enggstudant(102, "pooja", 22, 70, "engginearing", 60) 
# E1.accept()
# print("###########")

# E1.calRank()  
# E1.s_Details()     
# print(E1)


