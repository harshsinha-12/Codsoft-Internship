# Password Generator

import random
import string

# The generate_password function creates a password by combining 
# characters from string.ascii_letters (letters), string.digits (numbers), 
# and string.punctuation (special characters). 


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# The main function handles user input and displays the generated password.


def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()