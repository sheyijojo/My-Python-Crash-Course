print("\n")
print("****knowing the posItion or an index of the item you want to remove from a list using 'del'****")
# Knowing the posItion or an index of the item you want to remove from a list using "del"
opor_list = ['Software', 'Security', 'General studies', 'Data Analyst', 'System Analyst']
print(opor_list)

print("\n")
print("****using delete when you know the index****")
#remove the third index
print(opor_list)
del opor_list[3]
print(opor_list)
print("\n")

#using pop method removes the last item in a list, but it lets you work
# with that item after removing it.
print("****printing using pop() method deletes the last itm****")
print(opor_list)
popped_list  = opor_list.pop()
print(opor_list)
print(popped_list)
print(f"I will be suspending the role of a {popped_list.upper()}. in 5 year's time")

#popping the index also
security = opor_list.pop(1)
print(f"The role of {security.upper()} also will be eliminated in due time")
print("\n")

# removing an item by values using REMOVE method.
print("****removing an item by values using REMOVE method****")
artists = ['Davido','Burna', 'Wizkid','Sheyi', 'Tuface']
artists.remove('Davido')
print(artists)