# you write classes that represent real-world things and situations
# Writing a class, u define d general behavior that a whole category of objects can have.
print("-" * 20)
print("Creating a Dog class")

class Dog:  #class is defined. No parenthesis, we are creating this class from scratch
    """ A simple attempt to model a dog. """

# each instances created from d dog class will store a name and an age and we will give each
# dog the ability to sit() and roll().

    def __init__(self, name, age): # a function that is part of a class is called a method.
     """initialize name and age attributes"""
     self.name = name # attribues 
     self.age= age # every variable prefixed by self is available to every method in the class

# The __init__() method is a special method that python runs automically whenever we create a new instance based
# on the Dog class. it helps prevent python's default method names from conflicting with ur method names.
# the method is defined with 3 parameters.

#when we call the method, python passes self, we can pass Dog() a name and an age arguments, self is passed automically
# any variable prefixed with  self is available to every method in the class. 

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitiing")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


print("\n")
# think of a class as a set of instructions for how to make an instance.
# the class Dog is a set of iinstructions that tells python how to make individual isntance rep specific dogs


print("Making an instance from a class")
my_dog = Dog('Wille', 10)

 # telliing python to create a dog name is 'Willie' and age is 6
# when python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6.
# name and age are attrbutes

# use dot to access the attributes an instance e,g my_dog.name

print(f"My dog's name is {my_dog.name}.") # accessing the attributes of an instance
print(f"My dog is {my_dog.age} years old.")

print("." * 20)
print("Accessing the methods under Dog class")
my_dog.sit()
my_dog.roll_over()

# creating multiple instances
your_dog = Dog('Mucy', 5)
print(f"This your dog, {your_dog.name} is {your_dog.age} years old! chai!")
your_dog.sit()