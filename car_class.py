print("*" * 20)
print("Working with classes and Instances")
print("*" * 20)
print("\n")
class Car:
    def __init__(self, make, model, year):
        """Initialize attibutes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model} {self.year}"
        return long_name.title()
    
my_new_car = Car('Mercedes', 'G-class', 2022)
print(f"Na baba God do this {my_new_car.make} for me ooo and see the make below: ")
print(my_new_car.get_descriptive_name())


print("*" * 20)
print("Setting a default value for an attribute")
# when an instance is created, attributes can be defined without being passed in as parameters
# attribues can be defined in the __init__() method.
