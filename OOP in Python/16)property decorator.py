class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


s1 = Student(90, 80, 70)
print(s1.percentage)  # Output: 80.0%

s1.phy = 80
print(s1.percentage)
