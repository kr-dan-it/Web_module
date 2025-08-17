# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base
#
# Making an orm object manually
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#
#     def __repr__(self):
#         return f"<User(id={self.id}, username={self.username}, email={self.email})>"

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Boolean

# engine = create_engine("sqlite:///european_database.sqlite")
# conn = engine.connect()
#
# metadata = MetaData()
# division = Table("divisions", metadata, autoload_with=engine)
#
# # print(repr(metadata.tables["divisions"]))
# #
# # print(division.columns.keys())
#
# query = division.select()
# print(query)
#
# execution = conn.execute(query)
# print(execution.fetchone())
# print(execution.fetchall())

engine = create_engine("sqlite:///datacamp.sqlite")
conn = engine.connect()
metadata = MetaData()
Student = Table("Student", metadata,
          Column('Id', Integer(), primary_key=True),
                Column('Name', String(255), nullable=False),
                Column('Major', String(255), default="Math"),
                Column('Pass', Boolean(), default=True)
                )

metadata.create_all(engine)

from sqlalchemy import insert
# query = insert(Student).values(Id=1, Name="Matthew", Major="English", Pass=True)
# print(query)

# execution = conn.execute(query)
# conn.commit()
#
query1 = Student.select()
execution1 = conn.execute(query1)
print(execution1.fetchone())

# values_list = [
#     {'Id':'2', 'Name':'Nisha', 'Major':"Science", 'Pass':False},
#     {'Id':'3', 'Name':'Natasha', 'Major':"Math", 'Pass':True},
#     {'Id':'4', 'Name':'Ben', 'Major':"English", 'Pass':False}
# ]
#
# query = insert(Student).values(values_list)
# execution = conn.execute(query)
# conn.commit()
#
# from sqlalchemy import and_
# query = Student.select().where(and_(Student.columns.Major == "English",
#                                     Student.columns.Pass == True))
#
# print(conn.execute(query).fetchall())