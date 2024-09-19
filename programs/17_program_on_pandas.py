"""
Get data from database
and
write to
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
"""

print("Get data from database")
print("-"*20)
# ------------

import sqlite3
my_db_connection = sqlite3.connect('my_database.sqlite3')

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)

print(my_db_df)

print("#"*40, end="\n\n")
#################################

print("Write to files")
print("-"*20)
# ------------

# db_dump_1.txt
my_db_df.to_csv("db_dump_1.txt", sep="\t")

# db_dump_2.csv
my_db_df.to_csv("db_dump_2.csv") # default sep=","

# db_dump_3.xlsx
my_db_df.to_excel("db_dump_3.xlsx")

# db_dump_4.json
my_db_df.to_json("db_dump_4.json")

# db_dump_5.xml
my_db_df.to_xml("db_dump_5.xml")

print("""
Created below files,
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
Please check
""")

print("#"*40, end="\n\n")
#################################