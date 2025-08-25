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
        email Text not null unique, 
        website_name Text,
        login_method Text
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS websites(
        website_name Text not null,
        login_method Text not null, 
        foreign key (user_id) references users(id) 
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
            cursor.execute("insert into users (username, password, email) "
                                "values(?, ?, ?)",
                                (self.username, self.password, self.email))
            connection.commit()
            print(f"User {self.username} successfully registered.")
        except sqlite3.IntegrityError as e:
            print(f"User {self.username} already exists.")
        finally:
            connection.close()

    def login_method(self, website, login_method):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("insert into users (username, password, email) "
                                "values(?, ?, ?)",
                                (self.username, self.password, self.email))
            connection.commit()
            print(f"User {self.username} successfully logged in using {self.login_method}.")


def login_through_website():
    website = input("Enter the website you want to log in on: ")
    login_method = input("Enter your login method: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")