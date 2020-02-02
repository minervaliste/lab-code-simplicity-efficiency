'''
Create a function to request the input. It will allow us to launch the questions as many times as needed
without repeating code. It works for a better UX, as if the user enters wrong values they can re-enter them 
without launching the program again.
'''
def request_code():
    a = input('Please choose your first number (0 to 5): ')
    b = input('What do you want to do? (+, -): ')
    c = input('Please choose your second number (0 to 5): ')
    return a, b, c

'''
Create a function to check the input. As in the previous case, it can be reused as many times as the
user enters an incorrect input. Moreover, it shortens the check by grouping the conditions (instead of stating
all of them like in the previous code)
'''    
def check_operation(a, b, c):
    number_list = ['0', '1', '2', '3', '4', '5']
    operation_list = ['+' , '-']
    return a in number_list and b in operation_list and c in number_list 

'''
Create a function that controls all the initial dialogue with the user
'''

def start_calculator():
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')
    valid_input = False
    while valid_input == False:
        a, b, c = request_code()
        valid_input = check_operation(a, b, c)
        if valid_input == False:
            print('I am not able to answer this question. Check your input.')
    return a, b, c

'''
Create a function to do the mathematical operation, instead of creating conditions for all possible options.
By asking the numbers in numbers we can easily cast them into int and operate with them. 
'''    
def addition(a, b, c):
    if b == '-':
        result = int(a) - int(c)
    else:
        result = int(a) + int(c)
    return result


if __name__ == '__main__':
     
    a, b, c = start_calculator()
    result = addition(a, b, c)
    print(a, b, c, '=', result)
    print("Thanks for using this calculator, goodbye :)")
