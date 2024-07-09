#1 To what values do the following expressions evaluate?

False or (True and False)         #False
True or (1 + 2)                   #True
(1 + 2) or True                   #3 
True and (1 + 2)                  #3
False and (1 + 2)                 #False
(1 + 2) and True                  #True
(32 * 4) >= 129                   #False
False != (not True)               #False
True == 4                         #False
False == (847 == '847')           #True


#2 Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer. 

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

#3 Refactor this statement to use a regular if statement instead.

# return ('bar' if foo() else qux())

if foo():
    return 'bar'
else: 
    return qux()


#4 Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def caps_string(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    

#5 Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')


