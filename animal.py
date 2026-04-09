# Parent Class
class Animal:
    def sound(self):
        print("Animal makes sound")

# Child Class (Inheritance)
class Dog(Animal):
    def sound(self):   # method override (Polymorphism)
        print("Dog barks")

class Cat(Animal):
    def sound(self):   # method override (Polymorphism)
        print("Cat meows")