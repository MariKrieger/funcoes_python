Celsius = int(input('Digite a temperatura em Celsius: '))
Fahrenheit = int(input('Digite a temperatura em Fahrenheit: '))
Kelvin = int(input('Digite a temperatura em Kelvin: '))

Celsius1 = Celsius * 1.8 + 32
print("A temperatura de Celsius para Fahrenheit é de {:.2f} ".format(Celsius1))

Celsius2 = Celsius + 237
print("A temperatura de Celsius para Kelvin é de {:.2f}".format(Celsius2))

Fahrenheit1 = (Fahrenheit - 32) / 1.8
print("A temperatura de Fahrenheit para Celsius é de {:.2f}". format(Fahrenheit1))

Fahrenheit2 = (Fahrenheit - 32) * 5/9 + 273
print("A temperatura de Fahrenheit para Celsius é de {:.2f}".format(Fahrenheit2))

Kelvin1 = Kelvin - 273
print("A temperatura de Kelvin para Celsius é de {:.2f}".format(Kelvin1))

Kelvin2 = (Kelvin - 273) * 1.8 + 32
print("A temperatura de Kelvin para Fahrenheit é de {:.2f}". format(Kelvin2))