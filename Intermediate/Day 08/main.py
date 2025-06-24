# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 08

# Password Generator
import random
import string

def generate_password(length=12):
    """
    Generates a random password with a mix of letters, numbers, and symbols.
    """
    if length < 4:
        print("Password length should be at least 4")
        return None
        
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(characters))
        
    # Shuffle the password list to make it random
    random.shuffle(password)
    
    return "".join(password)

password_length = 16
new_password = generate_password(password_length)
if new_password:
    print(f"Generated password ({password_length} characters): {new_password}")

# Example Output (will be random):
# Generated password (16 characters): K!v6g$pS@wE7&jH2 