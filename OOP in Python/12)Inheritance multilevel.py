# single inheritance
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type



car1 = ToyotaCar("diesel")
print(car1.start())
