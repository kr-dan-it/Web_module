import mysql.connector
import csv
import os

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "yb8u^2Y75#MkHy"
}

DB_NAME = "library_db"

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
    """Create db and 3 tables: books, authors and genres"""
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

def load_data_from_csv(conn, cursor):
    try:
        with open("data/genres.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f) # iterator
            next(reader) # skips column name
            for genre in reader:
                # genre => tuple(str, )
                genre_name = genre[0]
                try:
                    cursor.execute("insert into genres (name) values (%s)",
                                   (genre_name,))
                    # conn.commit()
                except mysql.connector.IntegrityError as e:
                    print(f"Genre {genre_name} already exists")

        with open("data/authors.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name, nationality = row
                try:
                    cursor.execute("insert into authors (name, nationality) values (%s, %s)", (name, nationality))
                except mysql.connector.IntegrityError:
                    print(f"Name {row[0]} already exists in table.")

        with open("data/books.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                title, name, genre = row  # Каменярі,Іван Франко,Поезія

                cursor.execute("select id from genres where name = %s", (genre,))
                genre_id = cursor.fetchone()[0]

                cursor.execute("select id from authors where name = %s", (name,))
                name_id = cursor.fetchone()[0]

                cursor.execute("insert into books (title, author_id, genre_id) values (%s, %s, %s)",
                               (title, name_id, genre_id))

        conn.commit()
        print("Data inserted successfully")
    except FileNotFoundError as e:
        print(f"File not found [{e.filename}]")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def query(cursor):
    cursor.execute("select * from books")
    print(cursor.fetchall())

def main():
    try:
        conn = connect_to_db(DB_CONFIG)
        if not conn:
            print("Connection unsuccessful (w/o db)")
            return
        cursor = conn.cursor()
        create_database_and_tables(cursor)
        query(cursor)
        conn.close()

        conn = connect_to_db(DB_CONFIG, DB_NAME)
        if not conn:
            print("Connection unsuccessful (w/ db)")
            return
        cursor = conn.cursor()
        load_data_from_csv(conn, cursor)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()