#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
user_inputed_base = float(input('What is your base? '))
user_inputed_exponent = float(input('What is your exponent? '))
result = 1

def user_inputted_numbers (base, exp):
    
    for i in range (int(user_inputed_exponent)):
        result = result*base
        

print(user_inputted_numbers(user_inputed_base,user_inputed_exponent))