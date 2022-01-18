def make_pizza(size, *toppings):
    print(f"\nMaking a fat {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(topping)


make_pizza(16, 'Otalenu')
make_pizza(12, 'mushrooms', 'medium extra', 'cheese party')