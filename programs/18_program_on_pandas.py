"""
Get data from
1) DB
2) xlsx
3) json

and produce
final_report.xlsx
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

print("Get data from xlsx")
print("-"*20)
# ------------

my_excel_df = pd.read_excel("db_dump_3.xlsx")
print(my_excel_df)

print("#"*40, end="\n\n")
#################################

print("Get data from json")
print("-"*20)
# ------------

my_json_df = pd.read_json("db_dump_4.json")
print(my_json_df)

print("#"*40, end="\n\n")
#################################

print("Merge all 3 files data")
print("-"*20)
# ------------

all_in_one_df = pd.concat([my_db_df, my_excel_df, my_json_df], axis=0)
print(all_in_one_df)

print("#"*40, end="\n\n")
#################################

print("1st 3 rows")
print("-"*20)
# ------------

print(all_in_one_df.head(3))

print("#"*40, end="\n\n")
#################################

print("All column names")
print("-"*20)
# ------------

print(all_in_one_df.columns)
# ['IP', 'PICS', 'Unnamed: 0']

print("#"*40, end="\n\n")
#################################


print("Remove 'Unnamed: 0' column")
print("-"*20)
# ------------

all_in_one_df.drop(["Unnamed: 0"], inplace=True, axis=1)
print(all_in_one_df)

print("#"*40, end="\n\n")
#################################

print("Remove duplicate rows")
print("-"*20)
# ------------

all_in_one_df.drop_duplicates(inplace=True)
print(all_in_one_df)

print("#"*40, end="\n\n")
#################################

print("replace 'No Image' with 'abc.jpg'")
print("-"*20)
# ------------

all_in_one_df.replace(['No Image'], 'abc.jpg', inplace=True)
print(all_in_one_df)

print("#"*40, end="\n\n")
#################################

print("Final Report")
print("-"*20)
# ------------

all_in_one_df.to_csv("final_report.csv", index=False)
print("Created final_report.csv ")

print("#"*40, end="\n\n")
#################################