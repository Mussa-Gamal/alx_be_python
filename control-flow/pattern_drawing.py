while True:
  try:
    num = int(input('Enter the size of the pattern: '))
    if num < 0:
      print('Please enter a Positive Integer')
    else:
      break
  except ValueError:
    print('Please enter a Positive Integer')

for row in range(1, num + 1):
  print('*' * num)