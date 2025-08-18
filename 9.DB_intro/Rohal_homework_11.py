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
        user_search = cursor.execute("select * from users where username = ? and password = ?", (username, password)).fetchone()
        if user_search is None:
            return False
        else:
            return True

def register_user():
    new_username = input("Enter your username: ")
    new_password = input("Enter your password: ")
    new_email = input("Enter your email: ")
    new_user = User(new_username, new_password, new_email)
    new_user.register()

def log_user_in():
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")
    user_to_log_in = User(login_username, login_password, " ")
    user_to_log_in.log_in(login_username, login_password)
    if user_to_log_in.log_in(login_username, login_password):
        print("Successfully logged in")
    else:
        print("Incorrect username or password")


def main_function():
    while True:
        print(" ")
        user_input = int(input("What would you like to do? Enter 1 (register), 2 (log in) or 3 (log out): "))
        if user_input in (1, 2, 3):
            if user_input == 1:
                register_user()
            if user_input == 2:
                log_user_in()
            if user_input == 3:
                print("Successfully logged out")
                break
        else:
            print ("No such command exists. Try again")


if __name__ == "__main__":
    set_up_database()

    main_function()
