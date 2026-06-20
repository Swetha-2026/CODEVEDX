import random
import string
def generate_password(length, upper, lower, numbers, special):
    chars = ""
    if upper == "y":
        chars += string.ascii_uppercase
    if lower == "y":
        chars += string.ascii_lowercase
    if numbers == "y":
        chars += string.digits
    if special == "y":
        chars += string.punctuation
    if chars == "":
        return None
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password
def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
while True:
    print("\n===== PASSWORD GENERATOR & STRENGTH CHECKER =====")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            upper = input("Include Uppercase Letters? (y/n): ").lower()
            lower = input("Include Lowercase Letters? (y/n): ").lower()
            numbers = input("Include Numbers? (y/n): ").lower()
            special = input("Include Special Characters? (y/n): ").lower()
            password = generate_password(
                length,
                upper,
                lower,
                numbers,
                special
            )
            if password is None:
                print("Please select at least one character type.")
            else:
                print("\nGenerated Password:", password)
                print("Password Strength:", check_strength(password))
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        password = input("Enter password: ")
        print("Password Strength:", check_strength(password))
    elif choice == "3":
        print("Thank You")
        break
    else:
        print("Invalid Choice")