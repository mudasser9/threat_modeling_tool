
# Additional database functions as needed
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost:8080',
        user='root',
        password='',
        database='threat_modeling.sql'
    )
