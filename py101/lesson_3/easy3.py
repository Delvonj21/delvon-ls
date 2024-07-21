#1 Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

numbers.clear()

while numbers:
    numbers.pop()

#2 What will the following code output?
print([1, 2, 3] + [4, 5])

#[1, 2, 3, 4, 5]

#3 What will the following code output?
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

#hello there

#4 What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

[{"first": 42}, {"second": "value2"}, 3, 4, 5]

#5 The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ["blue", "green"]
    



