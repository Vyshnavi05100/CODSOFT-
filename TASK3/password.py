import random
import string

# Function to generate a random password
def generate_password(length):
    # Defining the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Using random.choices to pick characters from the list
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

# Main function to run the program
def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length < 6:
                print("Please enter a length of 6 or more for a secure password.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("\nYour generated password is:", password)

# Run the program
if __name__ == "__main__":
    main()
