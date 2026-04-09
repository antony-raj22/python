from animal import Dog, Cat

# Polymorphism function
def make_sound(animal):
    animal.sound()

# Objects
dog = Dog()
cat = Cat()

# Call function
make_sound(dog)
make_sound(cat)