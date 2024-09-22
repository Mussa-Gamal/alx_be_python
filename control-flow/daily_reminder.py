task = input('Enter your task: ')

priority = input('Priority (high/medium/low): ').lower()
while priority not in ['high', 'medium', 'low']:
  priority = input('Please enter a priority within (high/medium/low): ').lower()

time_bound = input('Is it time-bound? (yes/no): ').lower()
while time_bound not in ['yes', 'no']:
  time_bound = input('Please enter a time-bound within (yes/no): ').lower()

if priority in ['high', 'medium', 'low']:
  if time_bound == 'yes':
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
  else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")