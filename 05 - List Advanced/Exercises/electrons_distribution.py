number_of_electrons = int(input())

electron_layers = []
current_layer = 0

while number_of_electrons:

    current_layer += 1
    formula = 2 * current_layer ** 2

    if number_of_electrons > formula:
        electron_layers.append(formula)
        number_of_electrons -= formula

    else:
        electron_layers.append(number_of_electrons)
        number_of_electrons = 0

print(electron_layers)
