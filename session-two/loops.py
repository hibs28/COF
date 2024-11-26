# for loop
print("Before the loop\n")

for loop_number in range(5) :
    print(f"We are in loop no: {loop_number}")

print("\nAfter the loop")

# for loop on a string and a pattern
for i in "Hello":
    print(i)

# for loop on a list of items
for var in ["apples", "bananas", "cherries"] :
    print(var)

# ------------------------------------------------
print("\n--------------------\n")

# while loops
store_capacity = 5
while store_capacity > 0 :
    print("Please come in. Spaces available: " + str(store_capacity))
    store_capacity = store_capacity - 1 #comment this out and it will create an infinite loop

print("\nPlease wait for someone to exit the store.")

