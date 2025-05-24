class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(n1, n2):
        return Complex(n1.real + n2.real, n1.img + n2.img)

    def __sub__(n1, n2):
        return Complex(n1.real - n2.real, n1.img - n2.img)


n1 = Complex(2, 3)
n1.showNumber()  # Output: 2 i + 3 j
n2 = Complex(4, 5)
n2.showNumber()  # Output: 4 i + 5 j

n3 = n1 + n2  # Using the __add__ method)
n3.showNumber()  # Output: 6 i + 8 j
n4 = n1 - n2  # Using the __sub__ method
n4.showNumber()  # Output: -2 i + -2 j
