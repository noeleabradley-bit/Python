import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1amSpirit!",
  database="testdb"
)

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load key-value pairs from the local .env file into system environment variables
load_dotenv()

# Define top-of-file constants pulled securely from environment
DB_HOST = os.getenv("DB_HOST", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME_TEST", "")

mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD,
  database=DB_NAME

)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM transactions")

for x in mycursor:
  print(x)