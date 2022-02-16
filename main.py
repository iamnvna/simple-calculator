print("Simple calculator.")

# Operations
def addition(a, b):
    ans = a + b
    return ans

def subtraction(a, b):
    ans = a - b
    return ans

def multiply(a, b):
    ans = a * b
    return ans

def division(a, b):
    ans = a / b
    return ans

# Select operation
print("\nOperations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Validate user input
def user_input():
    global a, b
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input.")
            continue
        return a, b

# Calculator loop
while True:
    operation = input("\nSelect operation (1/2/3/4): ")

    global a, b
    if operation in ('1', '2', '3', '4'):
        if operation == '1':
            user_input()
            print(f"{a} + {b} = {addition(a, b)}")
        elif operation == '2':
            user_input()
            print(f"{a} - {b} = {subtraction(a, b)}")
        elif operation == '3':
            user_input()
            print(f"{a} * {b} = {multiply(a, b)}")
        elif operation == '4':
            user_input()
            print(f"{a} / {b} = {division(a, b)}")
        else:
            break
        
        again = input("Do you want to make another calculation? (Y/N): ").lower()
        if again == 'y':
            continue
        else:
            quit()
    
    else:
        print("You entered an invalid input."
              "\nTry again.")
        continue

# Commentary
'''
Line 1:
    Line 1 is a simple print statement that welcomes the users to the function of the
    program.

Line 4-18:
    These blocks of codes are functions that accept two parameters and perform an
    operation on them. The answer is returned anytime either function is called.

Line 28-37:
    This block of code  evaluates the user input for the operands to be sure they are numbers.
    It does so using the 'try except' statements.
    
Line 40-69:
    This block of code uses the while loop to iterate through the program when necessary.
    The while loop contains a series of if/elif/else statements that compare user input
    from line 31, evaluates it to the appropriate operator, then runs the appropriate block
    of code in the if/elif/else statements. Where the user input doesn't match any input
    from line 31, the user is prompted to enter a valid input (Line 57-60). After each
    successful operation, the user is asked if they want to perform another operation (Line 51-
    55). This allows the user to perform a new operation altogether or use the output from the
    previous operations in further operations.
'''