# user_input = int(input("Hello, what would you like to do? \n1 - Register \n2 - Log in \n3 - Log out \nEnter your number to continue: "))
#
# while user_input != 3:
#     if user_input == 1:
#         print("a")
#     elif user_input == 2:
#         print("b")
#     elif user_input == 3:
#         print("Logged out!")
#         break
#     else:
#         print("no")
#
# if user_input != range(1, 3):
#     while user_input != range(1, 3):
#         print("Your wrong, try again")
#         did_pass = input(f"Did Student {i} pass? (Passed/Failed) ").capitalize()
#     else:
#         passing.append(did_pass)
#         continue

# def player1():
#     while True:
#         user_input = int(input("Enter 1 (register), 2 (log in) or 3 (log out): "))
#         if user_input in (1, 2, 3):
#             if user_input == 1:
#                 print("Yeah")
#             if user_input == 2:
#                 print("Ok")
#             if user_input == 3:
#                 print("Bye")
#                 break
#         else:
#             print ("No such command is recognized. Try again")
#
# player1()

import sqlite3

def get_db_connection():
    return sqlite3.connect("users_database.db")
def set_up_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
        create table if not exists users(
        id integer primary key autoincrement, 
        username Text not null unique,
        password Text not null,
        email Text not null unique
        );
        """)
    except sqlite3.OperationalError as e:
        print(f"Помилка налаштування бази даних: {e}")
    finally:
        connection.close()

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.current_user = None

    def register(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("insert into users (username, password, email) values(?, ?, ?)", (self.username, self.password, self.email))
            connection.commit()
            print(f"User {self.username} successfully registered.")
        except sqlite3.IntegrityError as e:
            print(f"User {self.username} already exists.")
        finally:
            connection.close()

    def log_in(self, username, password):
        connection = get_db_connection()
        cursor = connection.cursor()
        user_search = cursor.execute("select * from users where username = ? and password = ?", (username, password))
        if user_search is None:
            return False
        else:
            return True

bob = User("Bob", "abcd123", " ")
print(bob.log_in("Bib", "acd123"))