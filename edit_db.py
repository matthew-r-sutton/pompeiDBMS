import mysql.connector as mysql
import configparser
import pandas as pd

# read-in data need for sql connection
config = configparser.ConfigParser()
config.read('./config.ini')

db = mysql.connect(
    host=config['mysql']['host'],
    user=config['mysql']['user'],
    passwd=config['mysql']['pass'],
    database="test_2"
)

cursor = db.cursor(buffered=True)

def edit():
    action = input("Would you like to EDIT or DELETE an existing record, or ADD a new one.")
