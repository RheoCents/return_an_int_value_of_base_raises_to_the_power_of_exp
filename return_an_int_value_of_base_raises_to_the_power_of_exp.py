#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
user_inputed_base = float(input('What is your base? '))
user_inputed_exponent = float(input('What is your exponent? '))


def user_inputted_numbers (base, exp):
    result = 1
    for i in range (int(user_inputed_exponent)):
        result = result*base
    print(result)    

user_inputted_numbers(user_inputed_base,user_inputed_exponent)