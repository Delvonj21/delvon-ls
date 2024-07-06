#1 Consider this code:

# def multiply_numbers(num1, num2, num3):
#     result = num1 * num2 * num3
#     return result

# product = multiply_numbers(2, 3, 4)
# Identify the following items in that code:

# function name                  multiply_numbers
# function arguments             (2, 3, 4)
# function definition            multiply_numbers(num1, num2, num3):
#                           
# function body                  result = num1 * num2 * num3
#                                 return result  
# function parameters            (num1, num2, num3)
# function invocation            multiply_numbers(2, 3, 4)
# function return value          24
# all identifiers                multiply_numbers, num1, num2, num3, result, product 

#2 Identify all of the identifiers on each line of the following code.

# def multiply(left, right):   
#     return left * right

# def get_num(prompt):              
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')         
# second_number = get_num('Enter the second number: ')       
# product = multiply(first_number, second_number)           
# print(f'{first_number} * {second_number} = {product}')   
# 
multiply	1, 9
left	1, 2
right	1, 2
first_number	7, 9, 10
second_number	8, 9, 10
get_num	4, 7, 8
prompt	4, 5
float	5
input	5
product	9, 10
print	10  

#3 Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

Global	multiply, get_num, first_number, second_number, product
Local	left, right, prompt
Built-in	float, input, print


#4 In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

Function names:
multiply: defined on line 1, used on line 9.
get_num: defined on line 4, used on lines 7 and 8.
float: built-in function used on line 5.
input: built-in function used on line 5.
print: built-in function used on line 10.
Parameters:
left and right are defined on line 1 and then used on line 2.
prompt is defined on line 4 and then used on line 5.

#5 Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?


# def say(message):
#     print(f'==> {message}')

# string1 = input()
# string2 = input()

# say(max(string1.upper(), string2.lower()))

Function Names:	
say	

Built-in Function Names:	
print
input
max

Method Names:
upper	
lower	

#6 The following function returns a list of the remainders of dividing the numbers in numbers by 3:

# def remainders_3(numbers):
#     return [number % 3 for number in numbers]
# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]    #print(any(remainders_3(numbers_1)))
numbers_2 = [1, 2, 4, 5]             #print(any(remainders_3(numbers_2)))
numbers_3 = [0, 3, 6]                #print(any(remainders_3(numbers_3)))
numbers_4 = []                       #print(any(remainders_3(numbers_4)))


#7 The following function returns a list of the remainders of dividing the numbers in numbers by 5:

# def remainders_5(numbers):
#     return [number % 5 for number in numbers]
# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:


numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         #print(all(remainders_5(numbers_1)))
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]                   #print(all(remainders_5(numbers_2)))
numbers_3 = [0, 5, 10]                                 #print(all(remainders_5(numbers_3)))
numbers_4 = []                                         #print(all(remainders_5(numbers_4)))
