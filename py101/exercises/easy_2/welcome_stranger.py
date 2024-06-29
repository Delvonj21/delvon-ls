# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

# Create a function that takes 2 arguments a list and dictionary
def greetings(name, job):
    return(f'Hello, {' '.join(name)}! Nice to have a '
           f'{job['title']} {job['occupation']}'
          ' around.')

greeting = greetings(
    ["Delvon", "D", "Johnson"],
    {"title": "Master", "occupation": "Chef"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.