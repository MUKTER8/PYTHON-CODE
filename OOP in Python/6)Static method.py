class student:    
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    @staticmethod #decorator 
    def display():
        print("Adding new student in database..")


s1=student("Mukter",3.70)
print(s1.name,s1.cgpa)
s1.display()
