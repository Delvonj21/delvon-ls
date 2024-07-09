# Write a function that takes a short line of text and prints it within a box.

def print_in_box(message):
    horizontal = f'+-{"-" * len(message)}-+'
    vertical = f'| {" " * len(message)} |'

    print(horizontal)
    print(vertical)
    print(f'| {message} |')
    print(vertical)
    print(horizontal)


print(print_in_box('To boldly go where no one has gone before'))