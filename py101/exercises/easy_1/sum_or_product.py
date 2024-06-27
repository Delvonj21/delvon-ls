# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

def compute_sum(target_num):
    return sum(range(1, target_num + 1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num + 1):
        result *= num
    return result

number = int(input('Please enter an integer greater than 0: '))

operation = input('Enter "s" to compute sum, or "p" to compute the product. ')

if operation == 's':
    print(f'The sum of the integers between 1 and {number} is {compute_sum(number)}.')

elif operation == 'p':
    print(f'The product of the integers between 1 and {number} is {compute_product(number)}.')
else:
    print("Unknown operation")