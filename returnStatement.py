# RETURN STATEMENTS
# Create a function called times
# Have this function take two inputs
# Multiply these inputs together
# Provide the results as an output
# Call your function and multiply, 3 by 5
# store value in a variable called answer
# print answer on the console

def times(num1, num2):
    # answer = num1 * num2
    return num1 * num2

result = times(3,5)
print(result)

# With user input
def timesWithUserInput(num1, num2):
    return num1 * num2

x = input('Enter num1: ')
y = input('Enter num2: ')

# Convert input values to integers
x = int(x)
y = int(y)

result = timesWithUserInput(x, y)
print(result)
