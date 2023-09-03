import random
import string

def password_generator(length,complexity):
    if complexity == "low":
        char = string.ascii_letters
    
    elif complexity == "medium":
        char = string.ascii_letters + string.digits
    
    elif complexity == "high":
        char = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid Complexity level")
    
    password = ''
    
    for i in range(length):
        password += random.choice(char)
    
    return password

print("{}\nPassword Generator!\n{}".format("-"*19,"-"*19))

try:
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter complexity level (low,medium,high): ").lower()
    
    if complexity not in ['high','medium','low']:
        print("please enter a proper complexity level")
    elif length <= 0:
        print("Please enter positive integer number")
    else:
        output = password_generator(length,complexity)
        print("Generated Password: {}".format(output))
        
except ValueError:
    print("Provide the valid input")