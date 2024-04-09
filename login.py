import psycopg2
from psycopg2 import sql
from psycopg2 import Error

DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = ""

def connectDb():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = connection.cursor()
        print("Connected to database successfully")
    except Error as e:
        print(f"Error while connecting to PostgreSQL: {e}")
        exit()


# Login options
def create_account():
    pass

def member_login():
    print("You chose option 1")

def trainer_login():
    print("You chose option 2")

def admin_login():
    print("You chose option 3")


# Menu options
def member_menu():
    pass

def trainer_login():
    pass

def admin_login():
    pass
