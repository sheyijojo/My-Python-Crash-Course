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

# Returning a dictionary
print("*" * 20)
print("Returning a dictionary")
def build_person(first_name, last_name, age = None):
    """ Return a dictionary of information about a person """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
    
musician = build_person('Buju', 'Banson', age=27)
print(musician)

# using a function with a while loop
print("-" * 20)
print("using a function with a while loop")

def def_formatted(first_name, second_name):
    full_name = f"Your king's name is: {first_name} {second_name}"
    return full_name  

formatted_names = def_formatted('Olusheyi', 'Gaji')
print(formatted_names)


print("-" * 20)
print("Always put break in your while loop to prevent infinite loops")
# always put break in your while loop to prevent infinite loops

def new_roles(first_job, second_job):
    """return your kind of jobs"""
    two_jobs = f"{first_job} and {second_job}!."
    return two_jobs

#ise = new_roles('DevOps Cloud', 'Business Intelligence Developer')

#print(ise)"""

while True:
    print("(enter 'end' at any time to quit)")
    f_job = input("enter your First Job: ") 
    if f_job == 'end':
        break

    print("(enter 'q' at any time to quit)")
    s_job = input("enter your Second Job: ") 
    if s_job == 'q':
        break

    work = new_roles(f_job, s_job)
    print(f"\n congrats for your new job as {work}")

print("\n")
print("-" * 20)
print("Passing a List to a function")
# Passing a list to  function

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

users = ["Drake", "Karty", "Obama"]
greet_users(users)

print("-" * 20)
print("Modifying a List to a function")
#code that shows designs to be printed and after being printed are stored in seperate list.
#start with some designs that need to be printed
unprinted_designs = ['phone', 'tv', 'house', 'calender']
completed_models = []

#simulate printing each design, until none are left.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
