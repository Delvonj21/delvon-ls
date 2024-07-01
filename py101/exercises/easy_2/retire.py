# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime


age = int(input('What is your age? '))
years_to_retire = int(input('At what age would you like to retire? '))

years = years_to_retire - age
now = datetime.now()
current_year = now.year

print(f"It's {current_year}. You will retire in {current_year + years} ")
print(f"You have only {years} years of work to go!")
      
