# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# Ask user for bill amount
bill_amount = float(input("What is the bill? "))

# Ask user for tip rate
tip_rate = float(input("What is the tip percentage? "))

# compute the tip
tip = (tip_rate / 100) * bill_amount

total = tip + bill_amount 

# print tip and total amount of the bill
print(f'The tip is ${tip: .2f}')
print(f'The total is ${total: .2f}')