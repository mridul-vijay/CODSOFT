import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_special=True):
    characters = list(string.ascii_lowercase)
    if use_upper:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_special:
        characters.extend(string.punctuation)
    if length < 1:
        return "Password length must be at least 1."
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (e.g., @#$!) (y/n): ").lower() == 'y'
    password = generate_password(length, use_upper, use_digits, use_special)
    print(f"\nGenerated Password: {password}")

main()
