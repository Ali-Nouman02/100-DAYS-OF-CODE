#calculator
#fucntions that do certain operations & return a value
#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1/n2

#storing the operatiors and their functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#storing user input in a variable
def calculator():
    num1 = float(input("what is the first number ?: "))
    #printing symbols for users to pick
    for symbols in operations:
        print(symbols)
    """"IMPORTANT: Here we go inside operation dictionary then operator
    user picked becomes key to acces the function. which gets saved in 
    a new variable."""
    notend = True
    while notend:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what is the next number ?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a  new calculation.: ") == 'y':
         num1 = answer
        else:
         notend = False
         calculator()

calculator()


