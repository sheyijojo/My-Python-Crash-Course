# Functions are named blocks of code designed to do one specific job

#from this import d
#from turtle import title


def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user() # calling the func tells python to execute the code in the function.

#print hello is actually the only code in body of the function.
# docstring is those triple quotes """" which describes what d function does.
#def is a keyword telling python u are defining a function.

print("*" * 30)

#passing an information to a function
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('Olusheyi') # Olusheyi is an argument pased from a func call to a func!

"""
Entering the greet_user('olusheyi') calls the greet_user() and gives the function
the info it needs to execute the print() call.

"""
print("\n")
print("Positional Arguments and calling fucntion multiple times is great ! ")
print("*" * 30)

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

describe_pet("dog", "Harry Buoy")
describe_pet("dog", "Pepe")

print("\n")
print("Keyword Argument in function! is a name-value pair that u pass to a function, frees from positional wahala ")
print("^" * 30)

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

describe_pet(pet_name="Harry Buoy", animal_type="dog", )

print("\n")
print("Default values for paramenter in the function ")
#argument is defiined as for a paramenter, u can exclude argumen in the function call"
# this simplifies the function calls
#notice i changed the order of the parameter, because the only arument match up 1st parameter
# if u notice most of the func calls to func describe_pet() are being used to descibe dog.

print("^" * 30)
def describe_pet(pet_name, animal_type = 'dog'):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

describe_pet('Thopmson')




print("\n")
print("^" * 30)
# u no fit dey display outfit all the time, u need data and then return some set of values
print("Return value: you dont print output all the time: You hear sheyi ")


def get_formatted_name(first_name, last_name):
    """ Return a full name, neatly formatted """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

makanaki = get_formatted_name('Olusheyi', 'Gaji')
print(makanaki)



print("^" * 30)
print("Making an argument optional")
# for example when you want to add middle name, add it to the lat

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
       full_name = f"{first_name} {last_name} {middle_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('Timi', 'Badboy')
print(musician)

musician = get_formatted_name('Davido', 'Agbaya', 'Sureboy')
print(musician)
   
        
"""if middle_name:
        full_name = f"{first_name} {last_name} {middle_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Timi', 'Loading')
print(musician)

musician = get_formatted_name('John', 'hooker', 'lee')
print(musician)
"""
