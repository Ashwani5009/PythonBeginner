class Animal:
    def walk(self):
        print("walking")

# inheritence between Dog and Animal


class Dog(Animal):
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woosh!")


Dog1 = Dog("roger", 8)

print(Dog1.name)
print(Dog1.age)
Dog1.bark()
Dog1.walk()
