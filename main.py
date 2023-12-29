import random

random_int = random.randint(1, 10)
print('random integer: ', random_int)

random_float = random.random()
print('random float: ', round(random_float * 10, 2))

love_score = random.randint(1, 100)
print(f'your love score is: {love_score}')

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(states_of_america[0])
print(states_of_america[-3])
print(states_of_america[:3])
print(states_of_america[47:])

extended_states = states_of_america[:]
extended_states.extend(["Freedomland", "Sugarland"])
print(extended_states[47:])
appended_states = extended_states[:]
appended_states.append("Lastland")
print(appended_states[47:])

print(f"there are {len(states_of_america)} states in america")

# Example of keeping list values in place
original_list = [1, 2, 3]

# Assigning a new value to an element in original_list modifies the original list
original_list[0] = 99

# Creating a new list using a slice and modifying it does not affect the original list
new_list = original_list[:]
new_list[1] = 88
print("Original List:", original_list)
print("New List:", new_list)

# Nested lists
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
               "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches",
          "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen_nested = [fruits, vegetables]
print(dirty_dozen_nested[0])
print(dirty_dozen_nested[1])

fruits = ["Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
