"""
David Clond
SDEV 220 M03
clond_M03_programming_assignment.py


This application solves the problems for the following 7.4, 7.5, 7.6, 7.7, 9.1, and 9.2
"""

# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# 7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
print(things[1].capitalize())      # this prints a capitalized "Cinderella"
print(things[1])                   # but this is not preserved

# 7.6 Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(things)

# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
things.remove("salmonella")
print(things)

# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

def get_odds(first=0, last=10, step=1):
    result = []
    for number in range(first, last, step):
        if number %2 == 1:
            result.append(number)
    return result

third_value = 3

for i in range(1, len(mylist := get_odds())):
    if i == third_value:
        print(mylist[i])
    elif i > third_value:
        break

