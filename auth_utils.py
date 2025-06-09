
import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.hash import pbkdf2_sha256
import json
import os
import psycopg2



# Load environment variables from .env file
# Database connection
def get_db_connection():
    """Create a connection to the PostgreSQL database"""
    # Try to get from environment variable first
    database_url = os.environ.get('DATABASE_URL')
    
    # If not available, use hardcoded local configuration
    if not database_url:
        database_url = "postgresql://postgres:1324@localhost:5432/hackseek_db"
    
    conn = psycopg2.connect(database_url)
    return conn

# User authentication functions
def register_user(username, email, password):
    """
    Register a new user with hashed password
    
    Args:
        username (str): User's username
        email (str): User's email
        password (str): User's password (will be hashed)
        
    Returns:
        bool: True if registration was successful, False otherwise
        str: Error message if registration failed
    """
    # Hash the password
    password_hash = pbkdf2_sha256.hash(password)
    
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Check if username or email already exists
        cur.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
        if cur.fetchone():
            return False, "Username or email already exists"
        
        # Insert the new user
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s) RETURNING id",
            (username, email, password_hash)
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        return True, user_id
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        cur.close()
        conn.close()

def authenticate_user(username, password):
    """
    Authenticate a user
    
    Args:
        username (str): User's username
        password (str): User's password
        
    Returns:
        bool: True if authentication successful, False otherwise
        dict or str: User data if successful, error message if failed
    """
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        # Get user data
        cur.execute("SELECT id, username, email, password_hash FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        
        if not user:
            return False, "User not found"
        
        # Verify password
        if pbkdf2_sha256.verify(password, user['password_hash']):
            # Remove password hash before returning
            user.pop('password_hash', None)
            return True, user
        else:
            return False, "Incorrect password"
    except Exception as e:
        return False, str(e)
    finally:
        cur.close()
        conn.close()

# User searches and solutions history
def save_user_search(user_id, problem_statement):
    """
    Save a user's search/problem statement
    
    Args:
        user_id (int): User's ID
        problem_statement (str): The problem statement
        
    Returns:
        int or None: ID of the saved search, or None if failed
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "INSERT INTO searches (user_id, problem_statement) VALUES (%s, %s) RETURNING id",
            (user_id, problem_statement)
        )
        search_id = cur.fetchone()[0]
        conn.commit()
        return search_id
    except Exception as e:
        conn.rollback()
        print(f"Error saving search: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def save_user_solution(user_id, search_id, solution_data):
    """
    Save a user's solution
    
    Args:
        user_id (int): User's ID
        search_id (int): Search ID this solution belongs to
        solution_data (dict): The solution data to save
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Convert dict to JSON
        solution_json = json.dumps(solution_data)
        
        cur.execute(
            "INSERT INTO saved_solutions (user_id, search_id, solution_data) VALUES (%s, %s, %s)",
            (user_id, search_id, solution_json)
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error saving solution: {e}")
        return False
    finally:
        cur.close()
        conn.close()

def get_user_search_history(user_id):
    """
    Get a user's search history
    
    Args:
        user_id (int): User's ID
        
    Returns:
        list: List of user's searches
    """
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cur.execute(
            """
            SELECT s.id, s.problem_statement, s.created_at::timestamp,
                (SELECT COUNT(*) FROM saved_solutions WHERE search_id = s.id) AS solution_count
            FROM searches s
            WHERE s.user_id = %s
            ORDER BY s.created_at DESC
            """,
            (user_id,)
        )
        searches = cur.fetchall()
        return searches
    except Exception as e:
        print(f"Error getting search history: {e}")
        return []
    finally:
        cur.close()
        conn.close()

def get_user_saved_solutions(search_id):
    """
    Get a user's saved solutions for a specific search
    
    Args:
        search_id (int): Search ID
        
    Returns:
        list: List of user's saved solutions
    """
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cur.execute(
            "SELECT id, solution_data, created_at::timestamp FROM saved_solutions WHERE search_id = %s ORDER BY created_at DESC",
            (search_id,)
        )
        solutions = cur.fetchall()
        
        # Parse JSON data
        for solution in solutions:
            solution['solution_data'] = json.loads(solution['solution_data'])
        
        return solutions
    except Exception as e:
        print(f"Error getting saved solutions: {e}")
        return []
    finally:
        cur.close()
        conn.close()

def get_user_profile(user_id):
    """
    Get a user's profile information
    
    Args:
        user_id (int): User's ID
        
    Returns:
        dict: User profile data
    """
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cur.execute(
            "SELECT id, username, email, date_of_birth, gender, profile_pic_url, theme FROM users WHERE id = %s",
            (user_id,)
        )
        user_profile = cur.fetchone()
        return user_profile
    except Exception as e:
        print(f"Error getting user profile: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def update_user_profile(user_id, profile_data):
    """
    Update a user's profile information
    
    Args:
        user_id (int): User's ID
        profile_data (dict): Dictionary containing profile fields to update
        
    Returns:
        bool: True if update was successful, False otherwise
    """
    # Fields allowed to be updated
    allowed_fields = ['email', 'date_of_birth', 'gender', 'profile_pic_url', 'theme']
    
    # Filter out only allowed fields
    update_fields = {k: v for k, v in profile_data.items() if k in allowed_fields}
    
    if not update_fields:
        return False, "No valid fields to update"
    
    # Construct query
    set_clause = ", ".join([f"{field} = %s" for field in update_fields.keys()])
    values = list(update_fields.values())
    values.append(user_id)  # Add user_id for WHERE clause
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            f"UPDATE users SET {set_clause} WHERE id = %s",
            values
        )
        conn.commit()
        return True, "Profile updated successfully"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        cur.close()
        conn.close()

def update_user_password(user_id, current_password, new_password):
    """
    Update a user's password
    
    Args:
        user_id (int): User's ID
        current_password (str): Current password for verification
        new_password (str): New password to set
        
    Returns:
        bool: True if update was successful, False otherwise
        str: Success or error message
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Verify current password
        cur.execute("SELECT password_hash FROM users WHERE id = %s", (user_id,))
        result = cur.fetchone()
        
        if not result:
            return False, "User not found"
        
        current_hash = result[0]
        
        if not pbkdf2_sha256.verify(current_password, current_hash):
            return False, "Current password is incorrect"
        
        # Hash and update the new password
        new_hash = pbkdf2_sha256.hash(new_password)
        
        cur.execute(
            "UPDATE users SET password_hash = %s WHERE id = %s",
            (new_hash, user_id)
        )
        conn.commit()
        return True, "Password updated successfully"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        cur.close()
        conn.close()

def reset_user_password(username, email, new_password):
    """
    Reset a user's password using their username and email
    
    Args:
        username (str): User's username
        email (str): User's email address
        new_password (str): New password to set
        
    Returns:
        bool: True if reset was successful, False otherwise
        str: Success or error message
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Verify the username and email match a user
        cur.execute(
            "SELECT id FROM users WHERE username = %s AND email = %s",
            (username, email)
        )
        result = cur.fetchone()
        
        if not result:
            return False, "No user found with the provided username and email combination."
        
        user_id = result[0]
        
        # Hash the new password
        new_password_hash = pbkdf2_sha256.hash(new_password)
        
        # Update the password
        cur.execute(
            "UPDATE users SET password_hash = %s WHERE id = %s",
            (new_password_hash, user_id)
        )
        conn.commit()
        
        return True, "Password reset successfully."
    except Exception as e:
        conn.rollback()
        print(f"Error resetting user password: {e}")
        return False, f"Error: {str(e)}"
    finally:
        cur.close()
        conn.close()
        
def delete_user_account(user_id, password):
    """
    Delete a user account and all associated data
    
    Args:
        user_id (int): User's ID
        password (str): User's password for verification
        
    Returns:
        bool: True if deletion was successful, False otherwise
        str: Success or error message
    """
    conn = None
    cur = None
    
    try:
        # First verify the password in a separate connection
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Verify the user's password
        cur.execute("SELECT password_hash FROM users WHERE id = %s", (user_id,))
        result = cur.fetchone()
        
        if not result:
            return False, "User not found."
        
        current_hash = result[0]
        
        if not pbkdf2_sha256.verify(password, current_hash):
            return False, "Password is incorrect. For security reasons, we cannot delete your account without password verification."
        
        # Close the first connection after verification
        cur.close()
        conn.close()
        
        # Open a new connection for deletion operations
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Delete user's saved solutions
        cur.execute(
            """
            DELETE FROM saved_solutions 
            WHERE user_id = %s OR 
                  search_id IN (SELECT id FROM searches WHERE user_id = %s)
            """,
            (user_id, user_id)
        )
        conn.commit()
        
        # Delete user's searches in a separate query
        cur.execute("DELETE FROM searches WHERE user_id = %s", (user_id,))
        conn.commit()
        
        # Finally, delete the user
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        
        return True, "Your account has been successfully deleted."
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error deleting user account: {e}")
        return False, f"Error: {str(e)}"
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()