import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",       # Replace with your MySQL server's hostname
        user="root",            # Replace with your MySQL username
        password="your_password" # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Creating the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Print success message
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:  # Catching MySQL specific errors
    # Print error message if connection fails or any MySQL error occurs
    print(f"Error connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()       # Close cursor
        connection.close()    # Close connection
        print("MySQL connection is closed.")
