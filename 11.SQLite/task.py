import sqlite3
import datetime

current_user = None

def get_db_connection():
    return sqlite3.connect("store.db")
def set_up_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
        create table if not exists users(
        id integer primary key, 
        user_name Text not null unique,
        password Text not null
        );
        """)
        cursor.execute("""
        create table if not exists products(
        id integer primary key, 
        name Text not null unique,
        price real not null, 
        stock integer not null
        );
        """)
        cursor.execute("""
        create table if not exists orders(
        id integer primary key, 
        user_id integer,
        product_id integer, 
        quantity integer, 
        order_date Text, 
        foreign key (user_id) references users(id), 
        foreign key (product_id) references products(id)
        );
        """)
    except sqlite3.OperationalError as e:
        print(f"Помилка налаштування бази даних: {e}")
    finally:
        connection.close()

def register_user(user_name, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("insert into users (user_name, password) values(?, ?)", (user_name, password))
        connection.commit()
        print(f"User {user_name} successfully created")
    except sqlite3.IntegrityError as e:
        print(f"Користувач з іменем {user_name} вже існує.")
    finally:
        connection.close()

# register_user("admin", "admin")
# register_user("user", "12345")
# register_user("Bob", "qwerty")
# register_user("Bib", "asdfgh")

def login_user(user_name, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    global current_user

    wanted_user = "select id from users where user_name = ? and password = ?"
    cursor.execute(wanted_user, (user_name, password))
    user = cursor.fetchone()

    connection.close()

    if user:
        current_user = user[0]
        print(f"Welcome, {user_name}")
        return True
    else:
        print("Username or password is wrong")
        return False

# login_user("admin", "admin")

def add_product(name, price, stock):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("insert into products (name, price, stock) values (?, ?, ?);", (name, price, stock))
        connection.commit()
    except sqlite3.OperationalError as e:
        print(f"Add product failed: {e}")
    except sqlite3.IntegrityError:
        print(f"Add product failed, products {name} already exists")
    finally:
        connection.close()

def list_products():
    connection = get_db_connection()
    cursor = connection.cursor()
    products = cursor.execute("select * from products").fetchall()
    connection.commit()
    if products is None:
        print("No products found")
        return
    print("==================== Available products ====================")
    for product in products:
        print(f"ID: {product[0]:5>} | Product name: {product[1][:15]} | Price: {product[2]:4.2f} | Stock: ({product[3]:3>})")

def make_order(product_id, quantity):
    order_date = datetime.datetime.now().strftime("%Y.%m.%d, %H.%M.%S")
    if current_user is None:
        print("Увійдйть у систему.")
        return
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("select stock from products where id = ?", (product_id,))
    products_stock = cursor.fetchone()

    if products_stock and quantity <= products_stock[0]:
        try:
            new_stock = products_stock[0] - quantity
            cursor.execute("Update products set stock = ? where id = ?", (new_stock, product_id))
            # cursor.execute("Update students set age = ? where id = ?", (new_age, id_))
            cursor.execute("insert into orders (user_id, product_id, quantity, order_date) values (?, ?, ?, ?)", (current_user, product_id, quantity, order_date))
            connection.commit()
            print("Замовлення успішно створено.")
        except Exception as e:
            connection.rollback()
            print(f"Помилка при створенні замовлення: {e}")
        finally:
            connection.close()
    else:
        print("Недостатньо кількості товару на складі або невірний id продукту.")
        connection.close()

products_data = [ ("Клавіатура Razer BlackWidow", 129.99, 50),
                  ("Мишка Logitech MX Master 3", 99.50, 75),
                  ("Монітор Dell U2723QE", 650.00, 20),
                  ("Ноутбук MacBook Air M2", 1199.00, 15),
                  ("Смартфон Samsung Galaxy S23", 899.99, 30),
                  ("Навушники Sony WH-1000XM5", 349.00, 40),
                  ("Вебкамера Logitech C920", 75.00, 60),
                  ("Планшет Apple iPad Air", 599.00, 25),
                  ("Зовнішній диск Samsung T7", 89.99, 80),
                  ("Принтер Epson EcoTank L3250", 250.00, 10) ]

if __name__ == "__main__":
    # set_up_database()

    # register_user("admin", "admin")
    # register_user("user", "12345")
    # register_user("Bob", "qwerty")
    # register_user("Bib", "asdfgh")

    # login_user("Bob", "qwerty")
    login_user("Bib", "asdfgh")

    # add_product(*products_data[0])
    # [add_product(*item) for item in products_data]
    # list_products()

    # make_order(7, 20)
    # make_order(3, 2)
    make_order(10, 15)