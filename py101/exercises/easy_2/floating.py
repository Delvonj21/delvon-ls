# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

print(f'{first_number} + {second_number} = '
      f'{first_number + second_number}')

print(f'{first_number} - {second_number} = '
      f'{first_number - second_number}')

print(f'{first_number} * {second_number} = '
      f'{first_number * second_number}')

print(f'{first_number} / {second_number} = '
      f'{first_number / second_number}')

print(f'{first_number} // {second_number} = '
      f'{first_number // second_number}')

print(f'{first_number} % {second_number} = '
      f'{first_number % second_number}')

print(f'{first_number} ** {second_number} = '
      f'{first_number ** second_number}')

