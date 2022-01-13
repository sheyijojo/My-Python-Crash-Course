# A list is a collection of items in a particular order.
# square brackets in python represents a list[], individual elements are seperated ny cooma.

courses = ['Software', 'Security', 'General studies']
print(courses)

# Acceessing the Index(Position) of a list
print('.' * 20)
opor_list =  ['Software', 'Security', 'General studies']
print(opor_list[0])
print(opor_list[0].title())
print(opor_list[-1])


print('.' * 20)
print("**using individual values from a list\n")

opor_list = ['Software', 'Security', 'General studies']
print(f"My first likeable course is: {opor_list[0].title()}.")

#changing the item in the list
opor_list = ['Software', 'Security', 'General studies']
print (opor_list)
opor_list[1] = 'Data Analysis'
print(opor_list)
print('.' * 20)
# Adding item to the end of a list
opor_list.append('Business Analyst')
print(opor_list)

# Buildiing a list from an empty list using append
print("***Buildiing a list from an empty list using append")
print('.' * 20)

empty_list = []
empty_list.append('Glory')
empty_list.append('Honor')
empty_list.append('Faith')
print(empty_list)

#printing a specific index
print("***printing a specific index")
print(empty_list[2])

# Inserting into a  list using insert
print('.' * 20)
print("***Inserting into a  list using insert")
print(opor_list)
opor_list.insert(2,'System Analyst')
print(opor_list)