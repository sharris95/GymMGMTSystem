#Gym Database Management Assignment

import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='FitnessCenter',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def add_member(id, name, age):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
        connection.commit()
        print(f"Member {name} added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def add_workout_session(member_id, session_date, session_time, activity):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)", (member_id, session_date, session_time, activity))
        connection.commit()
        print(f"Workout session for member {member_id} added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def update_member_age(member_id, new_age):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        if cursor.fetchone() is None:
            print(f"Member ID {member_id} does not exist.")
        else:
            cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))
            connection.commit()
            print(f"Member ID {member_id} age updated to {new_age}.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_workout_session(session_id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        connection.commit()
        print(f"Workout session ID {session_id} deleted successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Example function calls to test the functionality
add_member(1, 'Jane Doe', 28)
add_workout_session(1, '2024-07-27', '18:00', 'Yoga')
update_member_age(1, 29)
delete_workout_session(1)

def get_members_in_age_range(start_age, end_age):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Members WHERE age BETWEEN %s AND %s", (start_age, end_age))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Example function call to test the functionality
get_members_in_age_range(25, 30)

# Verification steps
print("Members data:")
get_members_in_age_range(0, 100)

print("\nWorkout sessions for member ID 1:")
connection = create_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM WorkoutSessions WHERE member_id = 1")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()

print("\nMembers data (after deletion):")
connection = create_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM Members WHERE name = 'John Smith'")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("SELECT * FROM WorkoutSessions WHERE member_id = 2")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()
