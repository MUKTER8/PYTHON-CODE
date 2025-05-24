class Person:
    name = "anonymous"
    print(name)  # Output: anonymous

    def changeName(self, name):
        self.name = name
        print(self.name)  # Output: name passed to changeName method


p1 = Person()
p1.changeName("Jane Doe")
print(p1.name)  # Output: Jane Doe
