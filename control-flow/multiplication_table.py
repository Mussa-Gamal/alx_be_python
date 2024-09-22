while True:
  try:
    number = int(input('Enter a number to see its multiplication table: '))
    break
  except ValueError:
    print('Please enter an Integer.')

for table in range(1, 11):
  print(f'{number} * {table} = {number * table}')