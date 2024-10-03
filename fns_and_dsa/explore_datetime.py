from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

  def calculate_future_date():
    nonlocal current_date
    days = int(input('Enter the number of days to add to the current date: '))
    tdelta = timedelta(days=days)
    future_date = current_date + tdelta
    print(f'Future date: {future_date.date()}')

  calculate_future_date()
display_current_datetime()