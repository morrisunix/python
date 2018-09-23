class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))


# Comparation
if philo.age > mikey.age:
    print("The oldest dog is {0} it is {1} years old".format(philo.name, philo.age))
else:
    print("The oldest dog is {0} it is {1} years old".format(mikey.name, mikey.age))
