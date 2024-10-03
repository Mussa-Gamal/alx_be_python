FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  ctemp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f'{fahrenheit}°F is {ctemp}°C')

def convert_to_fahrenheit(celsius):
  ftemp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  print(f'{celsius}°C is {ftemp}°F')

while True:
  try:
    temp = float(input('Enter the temperature to convert: '))
    break
  except ValueError:
    print('Invalid temperature. Please enter a numeric value.')

degree = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()

while degree != 'c' and degree != 'f':
  degree = input('Please enter a valid degree: ')

if degree == 'c':
  convert_to_celsius(temp)
elif degree == 'f':
  convert_to_fahrenheit(temp)