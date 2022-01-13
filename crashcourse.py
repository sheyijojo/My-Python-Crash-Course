print("Hello world")
message = "United Airlines"
print(message)

first_name = "Sheyi"
last_name = "Gaji"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")

simple_name = "Omo Ologo"


# eliminating extra space in python. Althoug this gives the same result, maybe cost of piplint
favorite_lang = 'Python '
print(favorite_lang)
favorite_lang1 = 'Python'
print(favorite_lang1)
favorite_lang = favorite_lang.rstrip()
favorite_lang
print(favorite_lang)


# explanation on methods
name = "sheyi jojo"
print(name.title())
# the title method appears after the variable in the print() call.
# method is an action that python can perform on a piece of data. The dot after name tells
# python to make the tille() method act on the variable name. 
# Every method is followed by parentheses, bcos most times they need addiitonal info. But can be empty


# Generating new line and tab(sapce)
print("." * 20)
print("Languages: \nPython\nC++\nJavascript")