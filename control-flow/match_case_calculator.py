while True:
  try:
    num1 = float(input('Enter the first number: '))
    break
  except ValueError:
    print('Please enter a number.')

while True:
  try:
    num2 = float(input('Enter the second number: '))
    break
  except ValueError:
    print('Please enter a number.')

operation = input('Choose the operation (+, -, *, /): ')

while operation != '+' and operation != '-' and operation != '*' and operation != '/':
  operation = input('Please enter a valid operation sign: ')

match operation:
  case '+':
    print(f'The result is {num1 + num2}.')
  case '-':
    print(f'The result is {num1 - num2}.')
  case '*':
    print(f'The result is {num1 * num2}.')
  case '/':
    if num2 == 0:
      print('Cannot divide by zero.')
    else:
      print(f'The result is {num1 / num2}.')