class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped.")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortunes")
car2=ToyotaCar("prius")
print(car1.color)
print(car1.name)
print(car1.start())
