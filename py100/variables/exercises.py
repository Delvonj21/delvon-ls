#1 Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.


# index            #idiomatic
# CatName          #non-idiomatic
# lazy_dog         #idiomatic
# quick_Fox        #non-idiomatic
# 1stCharacter     #illegal
# operand2         #idiomatic
# BIG_NUMBER       #non-idiomatic
# π                #non-idiomatic


#2 Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index             #idiomatic
# CatName           #non-idiomatic
# lazy_dog          #idiomatic
# quick_Fox         #non-idiomatic
# 1stCharacter      #illegal
# operand2          #idiomatic
# BIG_NUMBER        #non-idiomatic
# π                 #non-idiomatic

# 3Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index             #non-idiomatic
# CatName           #non-idiomatic
# snake_case        #non-idiomatic
# LAZY_DOG3         #idiomatic
# 1ST               #illegal
# operand2          #non-idiomatic
# BIG_NUMBER        #idiomatic
# Π                 #non-idiomatic

#4 Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index              non-idiomatic
# CatName            idiomatic
# Lazy_Dog           non-idiomatic
# 1ST                illegal
# operand2           non-idiomatic
# BigNumber3         idiomatic
# Πi                 non-idiomatic


#5 What happens when you run the following code? Why?

# NAME = 'Victor'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# NAME = 'Nina'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

#It will greet Victor and Nina, you should not use constants if you plan to change variables

#6 Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.

balance = (1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance)

#7 Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.

balance = 1000.00
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05

print(balance)


#8 Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

# obj = 'ABcd'          reassignment
# obj.upper()           neither
# obj = obj.lower()     reassignment
# print(len(obj))       neither
# obj = list(obj)       reassignment
# obj.pop()             mutation
# obj[2] = 'X'          mutation
# obj.sort()            mutation
# set(obj)              neither
# obj = tuple(obj)      reassignment