# define a circle class to create a circle with radius r using the constructor.
# define an Area() method of the class which calculates the area of the circle.
# define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * (self.radius ** 2)

    def Perimeter(self):
        return 2*(22/7)*self.radius


r = int(input("Enter the radius of the circle: "))


c1 = Circle(r)
print("Area of the circle is: ", c1.Area())
print("Perimeter of the circle is: ", c1.Perimeter())
# Output:
