import mysql.connector
import csv
import os

with open("pwd.txt", "r") as file:
    PWD = file.read()

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": PWD
}

DB_NAME = "users_db"

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

def create_database_and_tables(cursor):
    try:
        cursor.execute(f"Create database if not exists {DB_NAME};")
        cursor.execute(f'use {DB_NAME};')
        cursor.execute("""
        create table if not exists users (
        id int auto_increment primary key,
        username varchar(30) not null unique,
        password varchar(50) not null unique,
        email varchar(50) not null unique
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS login_info (
        id integer auto_increment primary key,
        site_name varchar(70) not null,
        username varchar(30) not null unique,
        password varchar(50) not null unique,
        login_method varchar(30) not null,
        user_id integer,
        foreign key (user_id) references users(id)
        );
        """)

        print("Database and tables created.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def register(conn, cursor, username, email, password):
        try:
            cursor.execute("insert into users (username, email, password) values (%s, %s, %s)", (username, email, password))
            print("User registered successfully")
        except mysql.connector.IntegrityError:
            print(f"User {username} already exists.")
        conn.commit()

# def websites(conn, cursor, site_name, username, password, login_method):


def query(cursor):
    cursor.execute("select * from users")
    print(cursor.fetchall())

def main():
    try:
        conn = connect_to_db(DB_CONFIG, DB_NAME)
        if not conn:
            print("Connection unsuccessful (w/ db)")
            return
        cursor = conn.cursor()
        register(conn, cursor, "JohnDoe", "john@doe.com", "qwerty")
        register(conn, cursor, "JaneDoe", "jane@doe.com", "asdfgh")
        query(cursor)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()