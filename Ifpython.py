#if statements
print("****samples of if*****")

tech_comp = ['fb', 'google', 'twitter', 'ibm', 'meta']

for tech in tech_comp:
    if tech == 'google':
        print(tech.upper())
    else:
        print(tech.title())