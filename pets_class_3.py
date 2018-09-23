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
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # instance method
    def eat(self):
        self.is_hungry = False

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
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

my_dogs_are_humgry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        my_dogs_are_humgry = True

if my_dogs_are_humgry:
    print("My dogs are hungry")
else:
    print("My dogs are not hungry")
