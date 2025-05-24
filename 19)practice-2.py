# define a employee class with attributes role department & salary.This class also has showDetails() method.
# create an engineer class that inherits properties from employee attributes:name & age
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        return f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}"


class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def showDetails(self):
        return f"Name: {self.name}, Age: {self.age}, " + super().showDetails()


e1 = Engineer("Alice", 30, "Software Engineer", "IT", 80000)
# Output: Name: Alice, Age: 30, Role: Software Engineer, Department: IT, Salary: 80000
print(e1.showDetails())
e2 = Engineer("Bob", 28, "Civil Engineer", "Construction", 70000)
# Output: Name: Bob, Age: 28, Role: Civil Engineer, Department: Construction, Salary: 70000
print(e2.showDetails())
