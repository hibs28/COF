# creating and calling function
def hello():
    name = input("Name? ")
    print("Hello, " + name)

hello()

# defining an argument
def hello_two(name_two):
    print(f"Hello, {name_two}")

hello_two("Hibah")

# returning a value
def sum_of(x,y):
    return  str(x+y)

total = sum_of(20,30)
print("The total sum is " + total)
