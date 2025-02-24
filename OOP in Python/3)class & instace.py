class student:    
    university="PCIU"   
    name="anonymous"
    def __init__(self,name,cgpa):
        self.name=name #obj attr>class attr
        self.cgpa=cgpa
        print("Adding new student in database..")



s1=student("Mukter",3.70)
print(s1.name,s1.cgpa,s1.university)

s2=student("Emon",3.80)
print(s2.name,s2.cgpa,s2.university)