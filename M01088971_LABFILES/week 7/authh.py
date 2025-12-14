
import bcrypt
import os




# REGISTER USER:
# Defining user file
User_data_file = 'users.txt'

# Hash a password
def hash_password(pwd):
    # Convert password to bytes, hash it, then convert back to string
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

# Verify a password
def verify_password(plain_text_password, hashed_password):
    # Encode both the plaintext password and stored hash to bytes
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    # This function checks if the entered password matches the stored hash
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)

# Check if username exists
def user_exists(name):
    try:
        with open(User_data_file, 'r') as f:
            # Check if any username in file matches the input
            return any(u.split(',')[0] == name for u in f)
    except FileNotFoundError:
        # File doesn't exist yet → no users
        return False
    



# Register a new user
def register_user(name, pwd):
    if user_exists(name):
        return False

    # Hash the password before storing
    hashed = hash_password(pwd)

    # this saves username and hashed password to file
    with open(User_data_file, 'a') as f:
        f.write(f"{name},{hashed}\n")

    return True




# LOGIN USER:
# Login a user
def login_user(name, pwd):
    try:
        with open(User_data_file, 'r') as f:
            for u in f:
                stored_name, stored_hash = u.strip().split(',')

                # Check if username matches
                if stored_name == name:
                    # Verify password
                    if verify_password(pwd, stored_hash):
                        print(f"Welcome, {name}!")
                        return True
                    else:
                        print("Incorrect password")
                        return False
    except FileNotFoundError:
        # No users registered yet
        print("No users registered yet")
        return False

    # Username not found
    print("Username not found")
    return False




# VALIDATE:
# Validate username
def validate_username(username):
    if not username or len(username) < 3:
        return False, "Username must be 3 character long"
    if not username.replace("_","").isalnum():
        return False, "must be letters, numbers, underscores only"
    return True, ""

# Validate password
def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    if not any(c.isdigit() for c in password):
        return False, "Password must have a num"
    if not any(c.isupper() for c in password):
        return False, "Password must have an uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must have a lowercase letter"
    return True, ""




# Implement the Main Menu:
def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()
            # Validate password
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # Register the user
            if register_user(username, password):
                print("User registered successfully!")
            else:
                print("Error: Username already exists.")

        elif choice == '2':
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
            else:
                print("\nLogin failed.")

            input("\nPress Enter to return to main menu...")

        elif choice == '3':
            # Exit
            print("\nThank you for using the authentication system. Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

import bcrypt
import os




# REGISTER USER:
# Defining user file
User_data_file = 'users.txt'

# Hash a password
def hash_password(pwd):
    # Convert password to bytes, hash it, then convert back to string
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

# Verify a password
def verify_password(plain_text_password, hashed_password):
    # Encode both the plaintext password and stored hash to bytes
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    # This function checks if the entered password matches the stored hash
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)

# Check if username exists
def user_exists(name):
    try:
        with open(User_data_file, 'r') as f:
            # Check if any username in file matches the input
            return any(u.split(',')[0] == name for u in f)
    except FileNotFoundError:
        # File doesn't exist yet → no users
        return False
    



# Register a new user
def register_user(name, pwd):
    if user_exists(name):
        return False

    # Hash the password before storing
    hashed = hash_password(pwd)

    # this saves username and hashed password to file
    with open(User_data_file, 'a') as f:
        f.write(f"{name},{hashed}\n")

    return True




# LOGIN USER:
# Login a user
def login_user(name, pwd):
    try:
        with open(User_data_file, 'r') as f:
            for u in f:
                stored_name, stored_hash = u.strip().split(',')

                # Check if username matches
                if stored_name == name:
                    # Verify password
                    if verify_password(pwd, stored_hash):
                        print(f"Welcome, {name}!")
                        return True
                    else:
                        print("Incorrect password")
                        return False
    except FileNotFoundError:
        # No users registered yet
        print("No users registered yet")
        return False

    # Username not found
    print("Username not found")
    return False




# VALIDATE:
# Validate username
def validate_username(username):
    if not username or len(username) < 3:
        return False, "Username must be 3 character long"
    if not username.replace("_","").isalnum():
        return False, "must be letters, numbers, underscores only"
    return True, ""

# Validate password
def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    if not any(c.isdigit() for c in password):
        return False, "Password must have a num"
    if not any(c.isupper() for c in password):
        return False, "Password must have an uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must have a lowercase letter"
    return True, ""




# Implement the Main Menu:
def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()
            # Validate password
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # Register the user
            if register_user(username, password):
                print("User registered successfully!")
            else:
                print("Error: Username already exists.")

        elif choice == '2':
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
            else:
                print("\nLogin failed.")

            input("\nPress Enter to return to main menu...")

        elif choice == '3':
            # Exit
            print("\nThank you for using the authentication system. Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

