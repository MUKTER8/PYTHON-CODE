class student:    
    university="PCIU" #class attr
    def __init__(self,name,cgpa): #constructor
        self.name=name #obj attr
        self.cgpa=cgpa
    def hello(self): #Method
        print("Welcome",self.name)
    def get_cgpa(self):
        return self.cgpa



s1=student("Mukter",3.70) #object
s1.hello()
print(s1.get_cgpa())#call method