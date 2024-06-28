# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

def multisum(max_value):
    total_sum = 0
    for number in range(1, max_value + 1):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number
    return total_sum
    
# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)