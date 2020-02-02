import random
import string
'''
Create a function that controls all the initial dialogue with the user. The control of the correct input
is integrated in this function too, to avoid a "Try again" message that makes the user launch the program
again every time.
'''
def request_code():
    a = int(input('Enter minimum string length: '))
    b = int(input('Enter maximum string length: '))
    while b < a:
        print('Maximum string length should be higher than minimum string length')
        b = int(input('Enter maximum string length: '))
    n = int(input('How many random strings to generate? '))
    return a, b, n

'''
Create a function that generates as many codes as requested. Since the values are already correct,
no validation is included here. Moreover, randint is used independently of a and b values (if equal, the
same number is passed to 'generate_random_string' function all the time) 
'''
def create_codes(a=8, b=12, n=1):
    r = []
    for i in range(n):
        c = random.randint(a, b)
        r.append(generate_random_string(c))
    return r
'''
Define a function that generates a random string of lowercase letters and digits for a given length. The
string library is used to avoid creating a list with all the possilble vallues.
'''
def generate_random_string(length=12):
    possible_values = string.ascii_lowercase + string.digits
    return ''.join(random.choice(possible_values) for i in range(length))

if __name__ == '__main__':

    a, b, n = request_code()
    print('Here you are!', create_codes(a, b, n))
