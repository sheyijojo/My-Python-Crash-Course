"""
Exersice

You have been asked to make a special book categorization program, which assigns each book a special 
code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters
 (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12


"""
"""

file = open("/usercode/files/books.txt", "r")

#your code goes here
books = file.readlines()
for line in books: 
    a =line[0]
    b = len((line.strip())) #strip removes \n that is at the back of the tittle for readlines method.
    print(f"{a}{b}")           # except the last one.

file.close()"""

print("Workiing with dictionaries")
print("*" * 20)
squares = {1:1, 2:4, 3: "error", 4:16,}
squares[8] = 64
squares[3] = 9
print(squares)

print("*" * 20)
print("Mad Exercise")
primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[4])
print(primes[7])
print(primes[primes[4]])



print("*" * 20)
#get method
print("Get method")

pairs = {1: "apple",
        "orange" : [2,3,4],
        None: "True",
        True: False,
}

print("*" * 20)
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(1234, "Not in dictionary"))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0)) 
print(fib.get(7, 5))


print("*" * 20)
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

print("*" * 20)
print("List comprehension")
cubes = [i*3 for i in range(5)]
print(cubes)
cubes = [i**3 for i in range(5)]
print(cubes)


a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)


"""def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count"""


"""filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))"""


nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))