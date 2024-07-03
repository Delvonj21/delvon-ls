#1 Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value. For example, if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.

print('Delvon' +' '+ 'Johnson' )

#3 What does the following code do? Why?

# print('5' + '10')
# It will print '510' because strings are concatenated together and returns a new string

#4 Refactor the code from the previous exercise to use coercion to print 15 instead.
print(int('5') + int('10'))


#5 Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:
foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error? 
# Yes, IndexError because the list index is out of range 

#6 To what value does the following expression evaluate?
'foo' == 'Foo'
# False because case matters when comparing strings

#7 What will the following code do? Why?
int('3.1415')
# ValueError the string value does not represent a valid integer.

#8 To what value does the following expression evaluate?
'12' < '9'
# True, strings are compared left to right character by character, '1' is less than '9'


