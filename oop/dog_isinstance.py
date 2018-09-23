# Parent class
class Dog:

    # class attribute
    species = 'mammal'

    # initializer / Instance attibutes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)


# child class (inherits from Dog() class)
class RusellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# child classes inherit attributes and
# behaviors from the import parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# child classes have specific attribites
# and behaviors as well
print(jim.run("slowly"))

# is jim an instance of Dog()?
print(isinstance(jim, Dog))

# is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# is johnny walker an instance of Bulldog()?
johnnywalker = RusellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# is julie an instance of jim?
print(isinstance(julie, jim))
