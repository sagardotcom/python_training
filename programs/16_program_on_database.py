"""
Get data from web_server.log

then

extract
IP
PICS

then

send extracted data to database
"""

"""
How to communicate with database in python?

python-program  <-- Communicate using Library  -->  Any Databases (SQL/No-SQL)

Example:
python-program  <-- Communicate using Library (cx-oracle)  -->  Oracle Databases
python-program  <-- Communicate using Library (mysql.connector)  -->  MySQL Databases
python-program  <-- Communicate using Library (sqlite3)  -->  SQLite Databases
"""

"""
We need ONE database.
- We can use SQLite database
    (serverless)
"""

"""
How to install/create SQLite database?

2 OPTIONS
OPTION-1: Use SQLite software
OPTION-2: Without Using SQLite software, Using python library sqlite3
   we can create/communicate with sqlite database
"""

print("Create database and table")
print("-"*20)
# ------------

import sqlite3

print("Create/connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Done\n")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Create table if not present")

my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
PICS VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")

print("#"*40, end="\n\n")
#################################

print("Get data from web_server.log")
print("-"*20)
# ------------

my_log_file_handle = open("../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
#################################

print("Extract Info and write to database")
print("-"*20)
# ------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST)\s+/(pics/(\w+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        img = match_result.group(4)
        if img is None:
            img = "No Image"
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{img}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records are inserted\n")

print("#"*40, end="\n\n")
#################################

print("Get data from database")
print("-"*20)
# ------------

my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
print(my_db_result)
my_db_connection.close()

print("#"*40, end="\n\n")
#################################