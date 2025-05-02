import sqlite3
import os
import unittest

#runs script
def run_script(script_path):
   pass

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


 # functions for checking 
def check_balance():
  connection = sqlite3.connect('example.db')
  cursor = connection.cursor()
  print("fetching funds")
  Balance = cursor.execute("SELECT * FROM funds")

  print("Balance:")
  for row in results:
    print(row)

  # deposit and withdraw
def deposit_funds():
  connection = sqlite3.connect('balance.db')
  cursor = connection.cursor()
  #add to balance
  Money_calculator = cursor.execute("UPDATE funds SET balance")
def wihdraw_funds():
  connection = sqlite3.connect('balance.db')
  cursor = connection.cursor()
  #delete balance

def create_account():
  connection = sqlite3.connect('accounts.db')
  cursor = connection.cursor()

  username = input("create a username:")
  password = input("create a password")

  cursor.execute("INSERT INTO accounts (username, password) VALUES(?,?)",(username,password))
  connection.commit()
  print("account sucessfully created")  
  connection.close()

def delete_account():
  connection = sqlite3.connect('accounts.db')
  cursor = connection.cursor()

  username = input("input your username")
  password = ("confirm password")

  cursor.execute("DELETE FROM accounts WHERE ")

def modify_password():
  connection = sqlite3.connect('accounts.db')
  cursor = connection.cursor()
    
  username = input("input old username")
  password = input("create a password")

  cursor.execute(f"UPDATE accounts {username} SET password {password}")

  print("password sucessfully changed")

def mainMenu():
  #account setup
  create_account()
  #main menu features
  print("----Welcome to Elite 102 Banking---- \n Please select an option")
  print("1. withdraw funds")
  print("2. deposit funds")
  print("3.change password")
  print("4.exit")
  #menu navigation
  option_selected = input("make a selection:")
  if option_selected != "4":
    if option_selected = "1":
      wihdraw_funds()
    elif option_selected = "2":
      deposit_funds()
    elif option_selected = "3":
      modify_password()
  elif option_selected == "4":
    print("logging out....")
    time.sleep()
    #test to check if depositing works
class TestClass(unittest.TestCase)
 def test_valueTest(self):
  
   
mainMenu()                                            


if __name__ == "__main__":
    main()