
from studant import Studant
from enggstudant import Enggstudant
from medicalstudant import Medicalstudant


class Collage:
    def __init__(self):
        self.studants_details = {}


    def addStudant(self):
      
        id = int(input("enter the studants id :"))
        name = input("enter the studants name :")
        age = int(input("enter the studants age :"))
        percentage  = int(input("enter the studants marks :"))

        ch = 0

        print('''plz select the choice from below:
                    1. anggenaring studant .
                    2.medical studant.
                    ''')
        ch = input("enter your choice ")

        if(ch == '1'):
                branch = input("enter the studants branch :")
                e1 = Enggstudant(id, name, age, percentage, branch)
                e1.calRank()
                edata = str(e1)

        elif(ch == '2'):
                specialization = input("enter the studants specialization :")
                internship_marks = int(input("enter the studants internship marks :"))
                m1 = Medicalstudant(id, name, age, percentage, specialization, internship_marks)
                edata = str(m1)
        else:
                    print("invalid choice :")
    
            
        self.studants_details[id] = edata
        print("studant added succesfully:")

        
    def getStudant(self):
        id = input("enter the  id :")
        if(id in self.studants_details.keys()):
            print(self.studants_details[id])
            print("gating the studant succesfully !!")


    def removeStudant(self):
        id = int(input("enter the studants id "))
        if(id in self.studants_details.keys()):
            del self.studants_details[id]
            print("stuant removed succsefully!!")

    def __str__(self):
        super().Medicalstudant()
        super().Enggstudant()

obj1 = Collage()
obj1.getStudant()                



