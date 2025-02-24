class student:    
    def __init__(self):#default constructor
        pass
        
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        print("Adding new student in database..")



s1=student("Mukter",3.70)
print(s1.name,s1.cgpa)

s2=student("Emon",3.80)
print(s2.name,s2.cgpa)