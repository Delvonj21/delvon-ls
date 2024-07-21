# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)  #2  The global keyword tells the function to assume that a refers to the global variable 'a'