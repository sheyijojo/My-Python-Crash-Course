import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)


"""
Modules

There are three main types of modules in Python, those you write yourself, 
those you install from external sources, and those that are preinstalled with Python.
The last type is called the standard library, and contains many useful modules. 
Some of the standard library's useful modules include string, re, datetime, math, random, os, 
multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

Tasks that can be done by the standard library include string parsing, data serialization, 
testing, debugging and manipulating dates, emails, command line arguments, and much more!

"""

"""

Many third-party Python modules are stored on the Python Package Index (PyPI).
The best way to install these is using a program called pip. This comes installed by default 
with modern distributions of Python. If you don't have it, it is easy to install online. Once you have it,
 installing libraries from PyPI is easy. Look up the name of the library you want to install,
  go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name. Once you've done this, import the library and use it in your code.

Using pip is the standard way of installing libraries on most operating systems, 
but some libraries have prebuilt binaries for Windows. These are normal executable files that let you install libraries with a GUI the same way you would install other programs

"""


"""

Exception Handling


To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
The try block contains code that might throw an exception.
 If that exception occurs, the code in the try block stops being executed, 
 and the code in the except block is run. If no error occurs, the code in the except block doesn't run.

"""


try:
    variable = 10
    print(variable +"Hello")
    print(variable/2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occured")


"""
Exception Handling

An except statement without any exception specified will catch all errors. 
These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
For example:

"""
print("\n")
print("." * 20)
try:
    word = "spam"
    print(word/0)

except:
    print("an error has occured")

print("\n")
print("." * 20)
print(" 'Finally' is used after try and except")
print("." * 20)
"""
finally

To ensure some code runs no matter what errors occur, you can use a finally statement. 
The finally statement is placed at the bottom of a try/except statement.
 Code within a finally statement always runs after execution of the code in the try,
  and possibly in the except, blocks.

"""
try:
    print("Hello will print, but the value doesnt print")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero is an error to avoid")
finally:
    print("This code will run no matter what because of 'finally'")
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

#class exercise, check exercise
try:
	#your code goes here
	print(coffee[choice])
	
except:
	#and here
	print("Invalid number")
finally:
	#and finally here
	print("Have a good day")

"""
Assertions


An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.

Programmers often place assertions at the start of a function to check for valid input, 
and after a function call to check for valid output.
"""
print("\n")
print("." * 20)
print(" Assertions are statement that assert or state fact in ur prog. boolean operations")
def avg(marks):
    assert len(marks) != 0
    return sum (marks)/len(marks)

mark1 = []
print("Average mark of mark1: ", avg(mark1))

#print(1)
#assert 2 + 2 == 4
#print(2)
#assert 1 + 1 == 3
#print(3) 

# read more on asser "https://www.programiz.com/python-programming/assert-statements"

"""
Let's take an example, where we have a function that will calculate 
the average of the values passed by the user and the value should not be an empty list.
 We will use assert statement to check the parameter and 
if the length is of the passed list is zero, the program halts.

""" 
