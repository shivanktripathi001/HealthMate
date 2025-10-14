import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="healthmate_schema",
        cursorclass=pymysql.cursors.DictCursor  # Optional: returns results as dictionaries
    )

def create_user(username, password, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
    (username, password, email)
)
    conn.commit()
    conn.close()

# def create_user(username, password, email):
#     cursor = db.cursor()
#     cursor.execute(
#         "INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s)",
#         (username, password, email)
#     )
#     db.commit()

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )
    user = cursor.fetchone()
    conn.close()
    return user


def update_user_password(username, new_password):
    """Update user password in the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "UPDATE users SET password = %s WHERE username = %s",
            (new_password, username)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating password: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


        
