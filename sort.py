print('\n')
# sorting a list permanently with the sort() method
print("****sorting a list with the sort() method****")

cars = ['toyota', 'mercedes', 'camry', 'tesla', 'acura']
print(cars)
cars.sort()
print(cars)

print('\n')
# sorting a list alphabetically permanently in REVERSE with the sort() method
print("****sorting a list in REVERSE with the sort() method****")

motors = ['toyota', 'mercedes', 'camry', 'tesla', 'acura']
print(motors)
motors.sort(reverse=True)
print(motors)

print('\n')
# sorting a list temporarily with the sorted(variable) function, doesnt affect the original list
print("****sorting a list with the sorted(variable) function****")

nice_cars = ['toyota', 'mercedes', 'camry', 'tesla', 'acura']
print(nice_cars)
print(sorted(nice_cars))
print(nice_cars)

print('\n')
# printing a list in reverse order to change permanently but can change it back using the reverse() again
print("****printing a list in reverse order using reverse()methods ****")

nice = ['toyota', 'mercedes', 'camry', 'tesla', 'acura']
print(nice)
nice.reverse()
print(nice)
