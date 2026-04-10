import sqlite3

def get_user_by_username(username):
    # VULNERABLE: SQL Injection - directly concatenating user input
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {
            'id': result[0],
            'username': result[1],
            'email': result[2]
        }
    return None

def search_users(search_term):
    # VULNERABLE: SQL Injection via user input
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Directly concatenating user input into query
    query = "SELECT id, username, email FROM users WHERE email LIKE '%" + search_term + "%'"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    
    return results

if __name__ == "__main__":
    username = input("Enter username: ")
    user = get_user_by_username(username)
    if user:
        print(f"Found user: {user}")
    else:
        print("User not found")