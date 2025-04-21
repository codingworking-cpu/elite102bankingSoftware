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
     print("account sucessfully created")
def delete_account():
  connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()

    username = input("input your username")
    password = ("confirm password")

    curson.execute("DELETE FROM accounts WHERE ")

def modify_password():
  connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()
    
    username = input("input old username")
    password = input("create a password")

    cursor.execute(f"UPDATE accounts {username} SET password {password}")

    print("password sucessfully changed")

   
                                                    


if __name__ == "__main__":
    main()