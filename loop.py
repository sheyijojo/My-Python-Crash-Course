from typing import List


print('\n')
# for loops. When u want to do the same action with every item in a list, u can use python's for loop
print("****for loops for the same action ****")

# printing list of magicians' names in a magician list. printing Each name in the list.
# python says puu a name from te list magicians, and associate it with the variable magician.
# Then print the nme that has just been assigned to magician.
# python then repeats line 2 and 3 for each name in the list.
# for every magician in the list of magicians, print the magician's name.

magicians = ['adigun', 'aburo', 'boma']
for magician in magicians:
    print(magician)
    print(f"{magician.title()},that was a great learning trick")

print('.' * 20)
print('\n')

names = ['adigun', 'aburo', 'boma']
for name in names:
    print(f"{name.title()},sapa no go see usoooo")
    print(f"I can't wait for you to see my success, {name.title()}.\n")

print('.' * 20)  

# making numerical lists using range function. prints 1-4 not 1-5
print("****making numerical lists using range function ****")
for value in range(1, 5):
    print(value)
print('.' * 20) 

print("****passing only one value on class range ****")
for value in range(6):
    print(value)
print('.' * 20)  

# using range to make a list of numbers
print("****using range class to make a list of numbers with list class****")
numbers =list(range(1,10))
print(numbers)

# using range to make python skip number e.g print only even numbers or 3+4=5, 5+2=7
odd_numbers = list(range(3, 11, 2))
print(odd_numbers)
print('.' * 20)


# make a list of the first 10 square numbers
print("***make a list of the first 10 square numbers*****")
squares = []
for value in range(1, 11): 
    squares.append(value ** 2)
print(squares)

print('.' * 20)
print("\n")

# List comprehension allows you to generate this same list in just line of code.
squares = [value**2 for value in range(1, 11)]
print("****make a single line of code with list comprehension*****")
print(squares)


print('.' * 20)
# range is 0-2, iterate over 0+1, 0+1 * . = just one dot
# second iteration 1+1=2, 2 * . = two dots..
# third iteration 2+1= 3, 3 * . = three dots..
for number in range(3):
    print("Attempt", number + 1, (number + 1) * '.')
    print(f"Sheyi will age gracefully with age", number + 32, (number + 1) * ".", "in years to come")
print('.' * 20)

for value in range(1, 10, 2):
    print("Attempt", value , (value + 1) * ".")
print('.' * 20)

#looping through a slice
print("****Loopiing through a slice*****")
states = ['calabar', 'jos', 'lagos', 'ogun']
print("These are first two nice states to find good women: ")
for state in states[:2]:
    variable = (state.title())
    print(variable)


# using list comprehension
women = [state for state in states[:2]]
print(women)
    
