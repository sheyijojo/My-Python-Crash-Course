print("-" * 20)
print("Modifying a List to a function")
#code that shows designs to be printed and after being printed are stored in seperate list.
#start with some designs that need to be printed
unprinted_designs = ['phone', 'tv', 'house', 'calender']
completed_models = [] # printed designs are moved here

#simulate printing each design, until none are left.
while unprinted_designs: # as long as designs remain in unprinted designs,
    current_design = unprinted_designs.pop() # remove design from the end of the list in unprinted and stores it.
    print(f"Printing model: {current_design}") # displays message, current design is being printed.
    completed_models.append(current_design) # adds design to the list of completed models


print("\nThe following models have been printed: ") # Display all completed models.
for completed_model in completed_models:
    print(completed_model)

# restructing the code by writing two functions.
# one will handle the printing the designs, 2nd will summarize d prints have been made
print("\n restructing the code by writing two functions. ")


def print_models(unprinted_designs, completed_models):
    """
    simulate printing each design, until none are left.
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        present_design = unprinted_designs.pop()
        print(f"Printing model: {present_design}")
        completed_models.append(present_design)

def show_completed_models(completed_models):
    """
    show all the models that were printed
    """
    print("\n The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["Bungalow", "Duplex", "Terrain", "Mansion"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# once you pop unprinted_designs, it becomes empty, to avoid this,
# pass the copy of the list to the function, just like this

print_models(unprinted_designs[:], completed_models)

# exercise
print("." * 30)
print("\n Try it yourself exercise")

def show_messages(short_text_messages, sent_messages):
    while short_text_messages:
        present_messages = short_text_messages.pop()
        print(f"message to be sent: {present_messages} ")
        sent_messages.append(present_messages)
  

def send_messages(sent_messages):
    print(f"\n These messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)


short_text_messages = ["Hi", "wats up", "Greetings", "Bawo ni"]
sent_messages = []

show_messages(short_text_messages[:], sent_messages)
send_messages(sent_messages)

#printing to check if the original list still exists.
print(short_text_messages)
print(sent_messages)

print("-" * 20)
print("Passing an Arbitary Numbers of Arguments")

# sometimes u won't know ahead of time how many arguments a function needs to accept.
# python allows a function to collect an arbitrary number of arguments from the calling statement.
#e.g consider a function that builds a pizza, accepts toppiings but u dont know the number of toppings wanted

def make_pizza(*toppings):
    """print the list of toppings dat av been requested   """
    print(f"\nMaking pizza with the follwowing toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperroni')
make_pizza('musrooms', 'buscuits', 'atarodo')


print("-" * 20)
print("Mixing Postional and arbitiary arguments")
# if u want a function to accept several diff kinds of argument. pkace the arbitary last in function defini
# you will see the generic parameter name *args, whc collects positional arguments like this.
def make_pizza(size, *toppings):
    print(f"\nMaking a fat {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(topping)


make_pizza(16, 'Otalenu')
make_pizza(12, 'mushrooms', 'medium extra', 'cheese party')


print('\n')
print(f"'-'" * 20)
# watch out for **kwargs used to collect non-specified keyword
print("Using arbitary keyword arguments")
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Buju', 'Benson', location = 'Nigeria', tribe = 'Igbo')

print(user_profile)

print('\n')
print(f"-" * 20)
# 
print("Storing your functions in modules")

