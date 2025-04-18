import sqlite3

DB_NAME = 'example.db'

MANAGE_FUNDS = 'balance.db'

ACCOUNT_INFO = 'accounts.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students
            (id integer primary key, 
            name text, 
            age integer, 
            grade text, 
            gpa real)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO students (name, age,grade, gpa) VALUES
        ('Alice', 16, '10th', 3.5),
        ('Bob', 17, '11th', 3.8),
        ('Charlie', 15, '9th', 3.2)
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


   connection = sqlite3.connect(MANAGE_FUNDS)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")

     cursor.execute('''
        CREATE TABLE IF NOT EXISTS students
            (transaction type,
            previous balance, 
            current balance)
            
    ''')
 # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO funds (transaction type, previous balance, current balance) VALUES
        ('deposit', 1000. 1100),
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()
    print("Table created.")

    
   connection = sqlite3.connect(ACCOUNT_INFO)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")

     cursor.execute('''
        CREATE TABLE IF NOT EXISTS students
            (username,
            password)
            
    ''')
 # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO accounts (username, password) VALUES
        (admin, admin)
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()
    print("Table created.")


initialize_database()