#calculator
import art

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add, 
    '-' : subtract, 
    '*' : multiply, 
    '/' : divide
    }
# should_continue = True
# while should_continue:
#     num1 = int(input('What is the first number? '))
#     num2 = int(input('What is the second number? '))
#     for symbol in operations:
#         print(symbol)

#     operation_symbol = input('Pick an operation from the line above: ')

#     calculation_function = operations[operation_symbol]
#     first_answer = calculation_function(num1, num2)
#     print(f'{num1} {operation_symbol} {num2} = {first_answer}')
#     should_continue = input(f'Type "y" to continue calculating with {first_answer}, or type "n" to start a new calculation: ')
#     if should_continue == 'y':
#         num3 = int(input('What is the next number? '))
#         operation_symbol = input('Pick an operation: ')
#         calculation_function = operations[operation_symbol]
#         second_answer = calculation_function(first_answer, num3)
#         print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')
#     else:
#         should_continue = True
print(art.logo)

def calculator():
    num1 = float(input('What is the first number? '))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input('Pick an operation from the line above: ')
        num2 = float(input('What is the next number? '))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        if input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ') == 'y':
            num1 = answer
        else:
            should_continue = False


calculator()
