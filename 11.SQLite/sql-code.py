import sqlite3

# create connection to db
connection = sqlite3.connect("my_database.db")

cursor = connection.cursor()

query_create_table = """
create table if not exists students(
    id integer primary key, 
    name text not null, 
    age integer, 
    grade text
);
"""

cursor.execute(query_create_table)
connection.commit()

# name = "Alice"
# age = 18
# grade = "A"
#
# cursor.execute("insert into students (name, age, grade) values (?, ?, ?)", (name, age, grade))
# connection.commit()

# student_data = [
#     ("Bob", 20, "C"),
#     ("Charlie", 19, "B"),
#     ("Diana", 20, "A")
# ]
#
# cursor.executemany("insert into students (name, age, grade) values (?, ?, ?)", student_data)
# connection.commit()

# drop_id = [(2,), (3,)]
#
# cursor.executemany("delete from students where id=(?)", drop_id)
# connection.commit()

# query = """
# select *
# from students;
# """
#
# cursor.execute(query)
# all_students = cursor.fetchall()
# print(all_students)

# student_data = [
#     ("Bob", 20, "C"),
#     ("Charlie", 19, "B"),
# ]
#
# cursor.executemany("insert into students (name, age, grade) values (?, ?, ?)", student_data)
# connection.commit()

# # select age above 19
# cursor.execute("""select * from students where age > 19;""")
# age_above_19 = cursor.fetchall()
# print(age_above_19)
#
# # select all named Bob
# cursor.execute("""select * from students where name=(?);""", ("Bob",))
# bob_data = cursor.fetchall()
# print(bob_data)

# student_name = "Bob"
# new_grade = "B"
#
# cursor.execute("Update students set grade = ? where name = ?", (new_grade, student_name))
# connection.commit()

# All students aged under 20 will have their age increased by 1
# Select all students with age < 20
cursor.execute("Select * from students;")
print(f"After update: {cursor.fetchall()}")

cursor.execute("Select id, age from students where age < 20;")
required_students = cursor.fetchall()
print(required_students)

for id_, age in required_students:
    new_age = age + 1
    cursor.execute("Update students set age = ? where id = ?", (new_age, id_))

connection.commit()

cursor.execute("Select * from students;")
print(f"After update: {cursor.fetchall()}")