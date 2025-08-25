import mysql.connector
import os

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "yb8u^2Y75#MkHy"
}

DB_NAME = "users_db"

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

def connect_to_db(config, db_name=None):
    """Create and return database connection"""
    try:
        if db_name:
            config["database"] = db_name
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

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

def create_database_and_tables(cursor):
    try:
        cursor.execute(f"Create database if not exists {DB_NAME};")
        cursor.execute(f'use {DB_NAME};')
        cursor.execute("""
        create table if not exists authors (
        id int auto_increment primary key,
        name varchar(30) not null,
        nationality varchar(30)
        );
        """)

        cursor.execute("""
        create table if not exists genres (
        id int auto_increment primary key,
        name varchar(30) not null unique 
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
        id integer auto_increment primary key,
        title varchar(128) not null unique,
        author_id integer, 
        genre_id integer,
        foreign key (author_id) references authors(id),
        foreign key (genre_id) references genres(id)
        );
        """)

        print("Database and tables created.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")