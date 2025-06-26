import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure the password contains at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the characters
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"\n🔐 Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the password generator
main()

