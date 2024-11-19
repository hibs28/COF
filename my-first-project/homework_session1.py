"""
Question 1
I am building some very high quality chairs and need exactly four nails for each chair. I've written a
program to calculate how many nails I need to buy to build these chairs.
chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))
When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. Is
my program calculating the total number of nails correctly? What is the problem? How do I fix it?
"""
# Because chairs and nails are two different data types (string and integer).
# You will need to remove the brackets and change it to  chairs = 15

"""
Question 2
I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix
the program?
my_name = Penelope
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)
"""
# Penelope is not defined. It needs to be in quotation marks "" to be a string

"""
Question 3

I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
make. Write a program to calculate this.
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
able to easily change these values if I want.
"""

eggs_in_a_box = 6
eggs_for_omelette = 4

total_num_of_boxes = eggs_in_a_box / eggs_for_omelette
print(f"You will need {total_num_of_boxes} for {eggs_for_omelette} omelettes")