# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

temp = float(input('Enter temperature in Celsius '))
kelvin = temp + 273.15
fahr = ((9 / 5) * temp ) + 32
print(f'Kelvin: {kelvin} K, Fahrenheit: {fahr} °F')