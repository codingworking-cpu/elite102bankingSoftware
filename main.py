import sqlite3


def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the students table
    print("Fetching all rows from the students table...")
    results = cursor.execute('''
        SELECT * FROM students
    ''')

    print("Results:")
    for row in results:
        print(row)

    # Get all students with a GPA greater than 3.5
    print("Fetching students with GPA greater than 3.5...")
    results = cursor.execute('''
        SELECT * FROM students WHERE gpa > 3.5
    ''')
    print("Results:")
    for row in results:
        print(row)

    connection.close()



def check_balance():
  connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

def deposit_funds():
  connection = sqlite3.connect('balance.db')
    cursor = connection.cursor()

def wihdraw_funds():
  connection = sqlite3.connect('balance.db')
    cursor = connection.cursor()

def create_account():
  connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()

     username = input("create a username:")
     password = input("create a password")

     cursor.execute("INSERT INTO accounts (username, password) VALUES(?,?)",(username,password))
     connection.commit()
def delete_account():
  connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()

def modify_account():
  connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()
    
    username = input("create a username:")
    password = input("create a password")

   
                                                    


if __name__ == "__main__":
    main()