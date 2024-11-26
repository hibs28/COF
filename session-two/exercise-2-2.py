"""
Exercise 2.2
----------------
You have friends at your house for dinner, and you've accidentally burnt the lasagne. Time to order pizza.
"""
num_of_guests = input("How many guests are at the dinner? ")
pizza_per_person = input("How many people can 1 pizza feed? ")

total_of_pizzas = int(num_of_guests) * 1/int(pizza_per_person)

print(f"The total number of pizzas you need is {total_of_pizzas}")
