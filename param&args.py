# Parameters and Arguments in Python
# defining and calling a function
print("Function 1:")

def get_milk1():
    print('1. Open door')
    print('2. Walk to the destination.')
    print('3. Buy milk.')
    print('4. Return home with milk. \n')
    
get_milk1()

# parameters and arguments
print("Function 2:")

def get_milk2(number, destination):
    print('1. Open door')
    print(f'2. Walk to the {destination}.')
    print(f'3. Buy {number} milk/s.')
    print('4. Return home with milk. \n')
get_milk2(20, 'Main Store') 

print("Function 3:")
def get_milk3(number, destination):
    print('1. Open door')
    print(f'2. Walk to the {destination}.')
    print(f'3. Buy {number} milk/s.')
    print('4. Return home with milk.\n')
    
# interchange the order by defining the variable
get_milk3(destination = 'Main Store', number= 10) 