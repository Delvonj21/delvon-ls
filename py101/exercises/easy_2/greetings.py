# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

# Ask user for name
name = input('What is your name? ')
# greet the user
if name.endswith('!'):
    print(f'HELLO {name.upper()}! WHY ARE WE YELLING? ')
else:
    print(f'Hello {name} ')

