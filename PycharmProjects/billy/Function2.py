# Functions
# Functions are blocks of codes that executes certain tasks.

#z and y are parameters
def save_record(z,y):
    name = input("Enter Your Name")
    age = int(input("Enter Your Age"))
    salary = int(input("Enter Your Salary"))
    tax = float(input("Enter Your Tax"))
    if salary < z:
        return "You Get 2000Kes Bonus"
    elif tax < 2.5:
        return "You Get 4000 Points"
    else:
        return "OK"


# invoke/call/trigger/use
#save_record()


# Create a function that prompts for three numbers
# Find the Maximum number
# Functions can return values


def max_min():
    list = [123, 64, 75]
    return max(list)

# functions can accept parameters








