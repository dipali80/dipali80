
from studant import Studant

class Medicalstudant(Studant):
    def __init__(self, id, name, age, percentage, specialization, internship_marks):
        super().__init__(id, name, age, percentage)
        self.specil = specialization
        self.internship = internship_marks

    def accept(self):
        super().accept()  
        self.specil = input("enter the specialization in:")
        self.internship = int(input("enter the internship marks :"))  

    def calRank(self):
         super().calRank() 

    def __str__(self):
        super().__str__()
        f"{self.specil}, specialization of studant {self.internship}, marks of internship"


# M1 = Medicalstudant(104, "soham", 18, 70, "mbbs", 50)        
# M1.accept()
# M1.calRank()
# M1.s_Details()


    