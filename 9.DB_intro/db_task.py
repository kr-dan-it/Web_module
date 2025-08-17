from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Boolean
from sqlalchemy import and_
from sqlalchemy import join
import pandas as pd

engine = create_engine("sqlite:///european_database.sqlite")
conn = engine.connect()

metadata = MetaData()
division = Table("divisions", metadata, autoload_with=engine)
matches = Table("matchs", metadata, autoload_with=engine)

# query = matches.select()
# execution = conn.execute(query)
# print(execution.fetchmany(10))

# query1 = matches.select().where(and_(matches.columns.Div == "E0",
#                                      matches.columns.season == "2012"))
# execution1 = conn.execute(query1)
# # print(execution1.fetchmany(10))
#
# league_2012_dataframe = pd.DataFrame(execution1.fetchall())
# print(league_2012_dataframe.head(5))

query = division.select()
div_mat = join(division, matches, division.columns.division == matches.columns.Div)

print(conn.execute(div_mat.select([div_mat.columns.Div, div_mat.columns.Home])).fetchmany(10))