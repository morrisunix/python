# parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# parent class
class Dog:

    # class attribute
    species = 'mammal'

    # initializer / instnace attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# child class (inherits from Dog class())
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# child class inherits from Dog class())
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# create instances of dogs
my_dogs = [
        Bulldog("Tom", 6),
        RussellTerrier("Fletcher", 7),
        Dog("Larry", 9)
]

# instantiate the Pets class
my_pets = Pets(my_dogs)

# output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))
