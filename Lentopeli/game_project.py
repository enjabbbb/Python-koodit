import mysql.connector
import random

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='game_project',
    user='aleksandra',
    password='H6nckrxfRMz',
    autocommit=True
)
