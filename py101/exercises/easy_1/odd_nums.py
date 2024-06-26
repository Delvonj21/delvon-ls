# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.


print("What is your starting number? ")
starting_number = int(input())

print("What is your ending number? ")
ending_number = int(input())

for number in range(starting_number, ending_number):
    if number % 2 != 0:
        print(number)