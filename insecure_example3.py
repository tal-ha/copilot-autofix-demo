import hashlib

# VULNERABLE: Hardcoded credentials exposed in code
DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "Admin@12345"
API_KEY = "sk-1234567890abcdefghijklmnop"

def hash_password(password):
    # VULNERABLE: MD5 is cryptographically broken and should not be used for password hashing
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(username, password):
    # VULNERABLE: Hardcoded credentials and weak password comparison
    # This is a simplified example simulating database check
    stored_username = "admin"
    stored_password_hash = hash_password("password123")
    
    input_hash = hash_password(password)
    
    # VULNERABLE: No protection against timing attacks
    if username == stored_username and input_hash == stored_password_hash:
        return True
    return False

def login(username, password):
    if verify_password(username, password):
        print("Login successful!")
        return True
    else:
        print("Login failed!")
        return False

if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    login(user, pwd)
