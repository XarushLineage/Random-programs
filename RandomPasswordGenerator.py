import random
import string

def generate_password(length, include_numbers=True, include_special_chars=True, include_uppercase=True):
    """
    Generate a random password with the given options.

    Args:
        length (int): Length of the password.
        include_numbers (bool): Whether to include numbers.
        include_special_chars (bool): Whether to include special characters.
        include_uppercase (bool): Whether to include uppercase letters.

    Returns:
        str: A random password meeting the given requirements.
    """


    # Define the character sets to use in the password
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    # Initialize the character set for the password
    password_chars = lowercase_chars

    # Add uppercase characters if requested
    if include_uppercase:
        password_chars += uppercase_chars

    # Add numbers if requested
    if include_numbers:
        password_chars += numbers

    # Add special characters if requested
    if include_special_chars:
        password_chars += special_chars

    # Generate the password by randomly choosing characters from the set
    password = "".join(random.choice(password_chars) for i in range(length))

    return password

def main():
    # Ask the user for options
    length = int(input("Enter the length of the password: "))
    
    # Validate input
    if length < 7:
        print("Password length should be at least 8 characters.")
        main()
    
    # Get input for including numbers
    while True:
        include_numbers = input("Include numbers? (y/n): ").lower()
        if include_numbers == "y" or include_numbers == "n":
            include_numbers = include_numbers == "y"
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Get input for including special characters
    while True:
        include_special_chars = input("Include special characters? (y/n): ").lower()
        if include_special_chars == "y" or include_special_chars == "n":
            include_special_chars = include_special_chars == "y"
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Get input for including uppercase letters
    while True:
        include_uppercase = input("Include uppercase letters? (y/n): ").lower()
        if include_uppercase == "y" or include_uppercase == "n":
            include_uppercase = include_uppercase == "y"
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Get input for the number of passwords to generate
    while True:
        try:
            num_passwords = int(input("How many passwords do you want to generate?: "))
            if num_passwords < 1:
                print("Number of passwords should be at least 1.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate the passwords
    for i in range(num_passwords):
        password = generate_password(length, include_numbers, include_special_chars, include_uppercase)
        print("Password {}: {}".format(i+1, password))

if __name__ == "__main__":
    main()
